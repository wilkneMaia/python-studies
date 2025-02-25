import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# Título do aplicativo
st.title("📊 Dashboard de Geração de Energia")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

@st.cache_data
def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
    return df

if uploaded_file:
    # Carregar os dados
    df = load_data(uploaded_file)

    # Seleção de intervalo de datas
    st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
    min_date = df["Date"].min().date()
    max_date = df["Date"].max().date()
    date_range = st.sidebar.date_input(
        "Selecione a data ou intervalo", [min_date, max_date],
        min_value=min_date, max_value=max_date, key="date_selector"
    )

    # Ajustar seleção única de data para um intervalo válido
    if isinstance(date_range, tuple) or isinstance(date_range, list):
        start_date, end_date = date_range[0], date_range[-1]
    else:
        start_date, end_date = date_range, date_range

    # Seleção de Microinversor
    st.sidebar.subheader("🔌 Selecione Microinversor(es)")
    microinversores = df["Microinversor"].unique()
    selected_microinversores = st.sidebar.multiselect(
        "Escolha os microinversores", microinversores, default=microinversores
    )

    # Filtrando os dados com base na seleção
    df_filtered = df[
        (df["Date"].dt.date >= start_date) &
        (df["Date"].dt.date <= end_date) &
        (df["Microinversor"].isin(selected_microinversores))
    ]

    # Calcular energia gerada neste mês, neste ano e total
    current_month = pd.Timestamp.now().month
    current_year = pd.Timestamp.now().year

    energia_mes = df_filtered[df_filtered["Date"].dt.month == current_month]["Energy (kWh)"].sum()
    energia_ano = df_filtered[df_filtered["Date"].dt.year == current_year]["Energy (kWh)"].sum()
    energia_total = df_filtered["Energy (kWh)"].sum()

    # Exibir painel de visão geral
    st.markdown(
        f"""
        <div style="display: flex; justify-content: space-around; padding: 20px; background-color: #f0f2f6; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
            <div style="text-align: center;">
                <h3 style="color: #333;">Energia este mês</h3>
                <h2 style="color: #007BFF;">{energia_mes:.2f} kWh</h2>
            </div>
            <div style="text-align: center;">
                <h3 style="color: #333;">Energia este ano</h3>
                <h2 style="color: #007BFF;">{energia_ano / 1000:.2f} MWh</h2>
            </div>
            <div style="text-align: center;">
                <h3 style="color: #333;">Energia total</h3>
                <h2 style="color: #007BFF;">{energia_total / 1000:.2f} MWh</h2>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Agrupar dados por Microinversor, somando a energia total
    df_grouped = df_filtered.groupby("Microinversor")["Energy (kWh)"].sum().reset_index()

    # Definir a altura máxima com base no maior valor da lista selecionada
    max_value = df_grouped["Energy (kWh)"].max()
    if max_value == 0:
        max_value = 1  # Evita problemas no eixo Y

    # Criando visualização estilo cards
    if not df_filtered.empty:
        st.subheader("⚡ Geração de Energia")

        # Filtrar os dados para os microinversores selecionados
        df_selected = df_filtered[df_filtered['Microinversor'].isin(selected_microinversores)]

        # Agrupar por microinversor e somar a energia gerada
        df_totals = df_selected.groupby('Microinversor')['Energy (kWh)'].sum().reset_index()

        cols = st.columns(min(20, len(df_totals)))  # Ajusta dinamicamente o número de colunas

        for i, (index, row) in enumerate(df_totals.iterrows()):
            with cols[i % len(cols)]:
                st.markdown(
                    f"""
                    <div style="padding: 10px; border-radius: 10px; background-color: #f0f2f6; text-align: center; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
                        <h4 style="color: #333;">{row['Microinversor']}</h4>
                        <h2 style="color: #007BFF;">{row['Energy (kWh)']} kWh</h2>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # Criar gráfico de barras customizado
    st.subheader("🔍 Energia Total por Microinversor")
    fig = go.Figure()

    for _, row in df_grouped.iterrows():
        fill_color = "#008CFF" if row["Energy (kWh)"] > 0 else "#444444"  # Azul se houver energia, cinza se for 0
        text_color = "white" if row["Energy (kWh)"] > 0 else "#BBBBBB"
        fig.add_trace(go.Bar(
            x=[row["Microinversor"]],
            y=[max_value],
            marker=dict(color="black"),
            opacity=0.3,
            showlegend=False
        ))
        fig.add_trace(go.Bar(
            x=[row["Microinversor"]],
            y=[row["Energy (kWh)"]],
            text=f"{row['Energy (kWh)']:.2f} kWh",
            textposition="auto",
            marker=dict(color=fill_color),
            name=row["Microinversor"],
            textfont=dict(color=text_color)
        ))

    # Adicionar linhas horizontais nos intervalos das barras
    for i in range(1, 11):  # 10 intervalos
        fig.add_shape(
            go.layout.Shape(
                type="line",
                x0=-0.5, x1=len(df_grouped["Microinversor"]) - 0.5,
                y0=(max_value / 10) * i, y1=(max_value / 10) * i,
                line=dict(color="white", width=1, dash="dot")
            )
        )

    fig.update_layout(
        barmode="overlay",
        plot_bgcolor="#222",
        paper_bgcolor="#222",
        font=dict(color="white"),
        yaxis=dict(title="Energia Gerada (kWh)", range=[0, max_value * 1.1], showgrid=False),
        xaxis=dict(title="Microinversor", showgrid=False),
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 Evolução da Geração de Energia")
    df_time_series = df_filtered.groupby(["Date", "Microinversor"])["Energy (kWh)"].sum().reset_index()

    fig_line = go.Figure()
    for micro in selected_microinversores:
        df_micro = df_time_series[df_time_series["Microinversor"] == micro]
        fig_line.add_trace(go.Scatter(
            x=df_micro["Date"], y=df_micro["Energy (kWh)"],
            mode="lines+markers", name=micro
        ))

    fig_line.update_layout(
        plot_bgcolor="#222", paper_bgcolor="#222", font=dict(color="white"),
        xaxis_title="Data", yaxis_title="Energia Gerada (kWh)"
    )
    st.plotly_chart(fig_line, use_container_width=True)

    st.subheader("📊 Distribuição da Geração por Microinversor")
    fig_pie = go.Figure(data=[go.Pie(
        labels=df_grouped["Microinversor"], values=df_grouped["Energy (kWh)"],
        hole=0.4, textinfo="percent+label"
    )])

    fig_pie.update_layout(plot_bgcolor="#222", paper_bgcolor="#222", font=dict(color="white"))
    st.plotly_chart(fig_pie, use_container_width=True)

    st.subheader("📊 Energia Gerada Acumulada ao Longo do Tempo")
    df_cumulative = df_time_series.copy()
    df_cumulative["Cumulative Energy"] = df_cumulative.groupby("Microinversor")["Energy (kWh)"].cumsum()

    fig_area = px.area(
        df_cumulative, x="Date", y="Cumulative Energy", color="Microinversor",
        labels={"Cumulative Energy": "Energia Acumulada (kWh)"}
    )

    fig_area.update_layout(plot_bgcolor="#222", paper_bgcolor="#222", font=dict(color="white"))
    st.plotly_chart(fig_area, use_container_width=True)
