import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# Título do aplicativo
st.title("📊 Dashboard de Geração de Energia")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("📤 Faça upload do arquivo CSV", type=["csv"])

@st.cache_data
def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    df["Date"] = pd.to_datetime(df["Date"])  # Converter para datetime
    return df

def plot_line_chart(df_micro, micro):
    fig = px.line(df_micro, x="Date", y="Energy (kWh)", markers=True,
                  title=f"Evolução da Geração - {micro}")
    st.plotly_chart(fig, use_container_width=True)

def plot_pie_chart(df_grouped):
    st.subheader("📊 Distribuição da Geração por Microinversor")
    fig = px.pie(df_grouped, names="Microinversor", values="Energy (kWh)", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

def plot_cumulative_energy(df_time_series):
    st.subheader("📊 Energia Gerada Acumulada")
    df_time_series["Cumulative Energy"] = df_time_series.groupby("Microinversor")["Energy (kWh)"].cumsum()
    fig = px.area(df_time_series, x="Date", y="Cumulative Energy", color="Microinversor")
    st.plotly_chart(fig, use_container_width=True)

if uploaded_file:
    df = load_data(uploaded_file)

    # Filtros no sidebar
    st.sidebar.subheader("📅 Selecione um intervalo de datas")
    min_date, max_date = df["Date"].min().date(), df["Date"].max().date()
    date_range = st.sidebar.date_input("Data", [min_date, max_date], min_value=min_date, max_value=max_date)

    # Ajuste para garantir que a data selecionada seja uma tupla, caso contrário, trata-se como intervalo único
    if isinstance(date_range, tuple):
        start_date, end_date = date_range
    else:
        start_date = end_date = date_range  # Se for uma única data, usa a mesma para o intervalo

    # Seleção de microinversores
    microinversores = df["Microinversor"].unique()
    selected_microinversores = st.sidebar.multiselect("🔌 Escolha os Microinversores", microinversores, default=microinversores)

    # Filtrando os dados corretamente
    df_filtered = df[
        (df["Date"].dt.date >= start_date) &  # Garantindo que as datas estão corretas
        (df["Date"].dt.date <= end_date) &
        (df["Microinversor"].isin(selected_microinversores))
    ]

    # Cálculo de energia gerada
    current_month, current_year = pd.Timestamp.now().month, pd.Timestamp.now().year
    energia_mes = df_filtered[df_filtered["Date"].dt.month == current_month]["Energy (kWh)"].sum()
    energia_ano = df_filtered[df_filtered["Date"].dt.year == current_year]["Energy (kWh)"].sum()
    energia_total = df_filtered["Energy (kWh)"].sum()

    # Exibir métricas principais
    col1, col2, col3 = st.columns(3)
    col1.metric("⚡ Energia este mês", f"{energia_mes:.2f} kWh")
    col2.metric("🌍 Energia este ano", f"{energia_ano / 1000:.2f} MWh")
    col3.metric("🔋 Energia total", f"{energia_total / 1000:.2f} MWh")

    # Agrupar por microinversor para gerar gráficos
    df_grouped = df_filtered.groupby("Microinversor")["Energy (kWh)"].sum().reset_index()

    plot_pie_chart(df_grouped)

    st.subheader("📈 Evolução da Geração de Energia")
    df_time_series = df_filtered.groupby(["Date", "Microinversor"])["Energy (kWh)"].sum().reset_index()
    for micro in selected_microinversores:
        df_micro = df_time_series[df_time_series["Microinversor"] == micro]
        plot_line_chart(df_micro, micro)

    plot_cumulative_energy(df_time_series)

    # Gráfico de barras de energia por microinversor
    st.subheader("🔍 Energia Total por Microinversor")
    fig = px.bar(df_grouped, x="Microinversor", y="Energy (kWh)", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)
