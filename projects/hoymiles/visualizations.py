import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import streamlit as st
from indicators import display_performance_indicators
import pandas as pd
import locale

# Configurar o locale para o padrão brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Função para criar gráficos de barras
def create_bar_chart(data, x, y, title, xlabel, ylabel):
    fig = px.bar(data, x=x, y=y, title=title, labels={x: xlabel, y: ylabel}, template="plotly_dark")
    fig.update_layout(
        title=dict(text=title, x=0.5, font=dict(size=16, color="white")),
        xaxis=dict(title=xlabel, showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title=ylabel, showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )
    return fig

# Função para exibir gráficos de barras
def plot_energy_bar_chart(daily_data, x, slope, intercept):
    fig_bar = px.bar(daily_data, x="Day", y="Energy", title="Geração de Energia por Dia",
                     labels={"Day": "Dia", "Energy": "Geração de Energia (kWh)"},
                     template="plotly_dark", color="Energy", color_continuous_scale="Blues")

    # Personalizando o gráfico
    fig_bar.update_traces(marker=dict(line=dict(width=0.5, color="black")), opacity=0.8)
    fig_bar.add_trace(go.Scatter(x=x, y=slope * x + intercept, mode='lines', name='Tendência',
                                line=dict(color='#ff5722', width=3, dash='solid')))

    # Ajustando layout
    fig_bar.update_layout(
        title=dict(text="Geração de Energia por Dia", x=0.5, font=dict(size=22, color="white")),
        xaxis=dict(title="Dia", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2,
                   tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Geração de Energia (kWh)", showgrid=True, zeroline=True, zerolinewidth=1,
                   zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )

    st.plotly_chart(fig_bar)

# Função para exibir gráfico de geração acumulada de energia
def plot_cumulative_energy_graph(daily_data, selected_year, selected_month):
    """Exibe um gráfico de linha acumulada de energia por dia, corrigindo os dias exibidos no eixo x"""
    # Gerar os dias corretos para o mês e ano selecionados
    start_date = pd.Timestamp(year=selected_year, month=selected_month, day=1)
    end_date = start_date + pd.offsets.MonthEnd(0)
    valid_days = pd.date_range(start=start_date, end=end_date).day

    # Filtrar os dados para incluir apenas os dias válidos
    daily_data = daily_data[daily_data["Day"].isin(valid_days)]

    # Criar o gráfico de linha
    fig_line = px.line(
        daily_data, x="Day", y="Energy",
        title="Geração Acumulada de Energia por Dia",
        labels={"Day": "Dia", "Energy": "Geração Acumulada (kWh)"},
        template="plotly_dark"
    )

    # Personalizar o gráfico
    fig_line.update_traces(
        mode='lines+markers',
        line=dict(color="#00bcd4", width=2),
        marker=dict(size=6, color="#ff5722", line=dict(width=1, color="white"))
    )

    # Ajustar o layout com espaço no início e no fim, sem exibir valores fora do intervalo
    fig_line.update_layout(
        title=dict(text="Geração Acumulada de Energia por Dia", x=0.5, xanchor='center', font=dict(size=16, color="#ffffff")),
        xaxis=dict(
            title="Dia", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2,
            tickangle=45, tickfont=dict(color="#ffffff"),
            range=[valid_days.min() - 0.5, valid_days.max() + 0.5]  # Adiciona espaço visual sem incluir valores fora do intervalo
        ),
        yaxis=dict(
            title="Geração Acumulada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1,
            zerolinecolor="gray", tickfont=dict(color="#ffffff")
        ),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )

    st.plotly_chart(fig_line)

# Função para exibir gráfico de energia gerada por semana
def plot_energy_by_week(df, selected_year):
    weekly_data = df[df["Year"] == selected_year].groupby("Week")["Energy"].sum().reset_index()
    x = weekly_data["Week"]
    y = weekly_data["Energy"]
    slope, intercept = np.polyfit(x, y, 1)
    fig = px.bar(weekly_data, x="Week", y="Energy", title=f"Energia Gerada por Semana ({selected_year})", labels={"Week": "Semana", "Energy": "Energia Gerada (kWh)"}, template="plotly_dark")
    fig.add_trace(go.Scatter(x=x, y=slope * x + intercept, mode='lines', name='Tendência', line=dict(color='#ff5722', width=3, dash='solid')))
    fig.update_layout(
        title=dict(text=f"Energia Gerada por Semana ({selected_year})", x=0.5, font=dict(size=16, color="white")),
        xaxis=dict(title="Semana", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig)

# Função para exibir gráfico de geração acumulada de energia por semana
def plot_cumulative_energy_by_week(df, selected_year):
    weekly_data = df[df["Year"] == selected_year].groupby("Week")["Energy"].sum().reset_index()
    fig_line = px.line(weekly_data, x="Week", y="Energy", title=f"Geração Acumulada de Energia por Semana ({selected_year})",
                       labels={"Week": "Semana", "Energy": "Geração Acumulada (kWh)"}, template="plotly_dark")
    fig_line.update_traces(mode='lines+markers', line=dict(color="#00bcd4", width=2), marker=dict(size=6, color="#ff5722", line=dict(width=1, color="white")))
    fig_line.update_layout(
        title=dict(text=f"Geração Acumulada de Energia por Semana ({selected_year})", x=0.5, font=dict(size=16, color="#ffffff")),
        xaxis=dict(title="Semana", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Geração Acumulada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig_line)

# Função para exibir gráfico de geração de energia por semana
def plot_weekly_data_by_date(df, selected_date):
    selected_date = pd.to_datetime(selected_date)
    selected_week = selected_date.isocalendar().week
    selected_year = selected_date.year
    weekly_data = df[(df["Year"] == selected_year) & (df["Week"] == selected_week)]
    if not weekly_data.empty:
        daily_data = weekly_data.groupby("Day")["Energy"].sum().reset_index()
        st.markdown(f"<h3>📈 Dados de geração de energia para a semana {selected_week} do ano {selected_year}</h3>", unsafe_allow_html=True)
        x = daily_data["Day"]
        y = daily_data["Energy"]
        slope, intercept = np.polyfit(x, y, 1)
        display_performance_indicators(daily_data)
        plot_energy_bar_chart(daily_data, x, slope, intercept)
        # plot_cumulative_energy_graph(daily_data)
        # plot_heatmap_by_week(df, selected_date)
    else:
        st.warning("⚠️ Nenhum dado disponível para esta semana.")

# Função para exibir gráfico de quadrantes
def plot_quadrant_graph(filtered_data, selected_year):
    """Exibe um gráfico de quadrantes comparativo dos meses por ano"""
    # Criação da tabela pivot para os dados
    quadrante_data = filtered_data.pivot_table(index="Month_Year", columns="Day", values="Energy", aggfunc="sum", fill_value=0)

    # Inicializando o gráfico de quadrantes
    fig_quadrante = go.Figure()

    # Adicionando os pontos de quadrante para cada mês
    for month in quadrante_data.index:
        fig_quadrante.add_trace(go.Scatter(
            x=quadrante_data.columns,
            y=[str(month)] * len(quadrante_data.columns),
            mode='markers',
            marker=dict(size=10, color=quadrante_data.loc[month].values, colorscale='teal', showscale=True,
                        colorbar=dict(title="Energia (kWh)", tickvals=[0, 10, 20, 30], ticktext=["0", "10", "20", "30"])),
            text=quadrante_data.loc[month].values,
            hoverinfo="text",
            name=str(month),
        ))

    # Ajustando o layout
    fig_quadrante.update_layout(
        title=f"Quadrante de Produção de Energia ({selected_year})",
        title_font=dict(size=18, color="#ffffff"),
        xaxis=dict(title="Dia", title_font=dict(size=14, color="#ffffff"),
                   showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Ano-Mês", title_font=dict(size=14, color="#ffffff"),
                   showgrid=False, tickfont=dict(color="#ffffff"), type='category'),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40),
        colorway=["#007bff"]
    )

# Função para gráfico de total de energia gerada por ano (barra)
def plot_total_by_year(df):
    """Exibe o total de energia gerada por ano"""
    total_data = df.groupby("Year")["Energy"].sum().reset_index()
    fig = create_bar_chart(total_data, "Year", "Energy", "Total de Energia Gerada por Ano", "Ano", "Total de Energia Gerada (kWh)")
    st.plotly_chart(fig)

# Função para gráfico de comparativo de meses por ano com linhas
def plot_comparative_months_by_year_line(df):
    """Exibe um gráfico de linhas comparativo dos meses por ano"""
    monthly_comparison = df.groupby(["Year", "Month"])["Energy"].sum().reset_index()
    fig = px.line(monthly_comparison, x="Month", y="Energy", color="Year",
                  title="Comparativo de Energia Gerada por Mês e Ano",
                  labels={"Month": "Mês", "Energy": "Energia Gerada (kWh)", "Year": "Ano"},
                  template="plotly_dark", markers=True)
    fig.update_layout(
        title=dict(text="Comparativo de Energia Gerada por Mês e Ano", x=0.5, font=dict(size=16, color="white")),
        xaxis=dict(title="Mês", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig)

# Função para exibir gráfico de área empilhada
def plot_area_stack_by_year(df):
    """Exibe um gráfico de área empilhada comparativo dos meses por ano"""
    monthly_comparison = df.groupby(["Year", "Month"])["Energy"].sum().reset_index()
    fig = px.area(monthly_comparison, x="Month", y="Energy", color="Year", title="Comparativo de Energia Gerada por Mês e Ano (Área Empilhada)", labels={"Month": "Mês", "Energy": "Energia Gerada (kWh)", "Year": "Ano"}, template="plotly_dark")
    fig.update_layout(title=dict(text="Comparativo de Energia Gerada por Mês e Ano", x=0.5, font=dict(size=16, color="white")),
                      xaxis=dict(title="Mês", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
                      yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
                      plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40))
    st.plotly_chart(fig)

# Função para exibir gráfico de dispersão
def plot_scatter_by_year(df):
    """Exibe um gráfico de dispersão comparativo dos meses por ano"""
    monthly_comparison = df.groupby(["Year", "Month"])["Energy"].sum().reset_index()
    fig = px.scatter(monthly_comparison, x="Month", y="Energy", color="Year", title="Comparativo de Energia Gerada por Mês e Ano (Dispersão)", labels={"Month": "Mês", "Energy": "Energia Gerada (kWh)", "Year": "Ano"}, template="plotly_dark")
    fig.update_layout(title=dict(text="Comparativo de Energia Gerada por Mês e Ano", x=0.5, font=dict(size=16, color="white")),
                      xaxis=dict(title="Mês", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
                      yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
                      plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40))
    st.plotly_chart(fig)

# Função para exibir gráfico Candlestick
def plot_candlestick_by_month(df):
    """Exibe um gráfico Candlestick comparativo dos meses por ano"""
    monthly_comparison = df.groupby(["Year", "Month"])["Energy"].sum().reset_index()
    fig_data = []
    for year in monthly_comparison["Year"].unique():
        year_data = monthly_comparison[monthly_comparison["Year"] == year]
        fig_data.append(go.Candlestick(
            x=year_data["Month"],
            open=[year_data["Energy"].iloc[0]] * len(year_data),  # Energia do primeiro mês do ano repetida para todos os meses
            high=[year_data["Energy"].max()] * len(year_data),    # Energia máxima repetida para todos os meses
            low=[year_data["Energy"].min()] * len(year_data),     # Energia mínima repetida para todos os meses
            close=[year_data["Energy"].iloc[-1]] * len(year_data),# Energia do último mês repetida para todos os meses
            name=str(year)
        ))

    fig = go.Figure(fig_data)
    fig.update_layout(
        title=dict(text="Comparativo de Energia Gerada por Mês e Ano (Candlestick)", x=0.5, font=dict(size=16, color="white")),
        xaxis=dict(title="Mês", tickmode='linear', tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], ticktext=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                   showgrid=False, ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig)

# Função para exibir gráfico de calor
def plot_heatmap_by_week(df, selected_date):
    """Exibe um gráfico de calor (heatmap) da energia gerada ao longo dos dias da semana"""
    selected_date = pd.to_datetime(selected_date)
    selected_week = selected_date.isocalendar().week
    selected_year = selected_date.year

    # Filtrar os dados para a semana e ano selecionados
    weekly_data = df[(df["Year"] == selected_year) & (df["Week"] == selected_week)]

    # Criar uma tabela pivot para os dados
    heatmap_data = weekly_data.pivot_table(index="Week", columns="Date", values="Energy", aggfunc="sum", fill_value=0)

    # Criar o gráfico de calor
    fig = px.imshow(heatmap_data, labels=dict(x="Dia", y="Semana", color="Energia Gerada (kWh)"),
                    x=heatmap_data.columns.strftime('%Y-%m-%d'), y=heatmap_data.index, color_continuous_scale="Blues")

    fig.update_layout(
        title=dict(
            xanchor='center',
            text=f"Distribuição de Energia Gerada por Dia da Semana ({selected_year})",
            x=0.5, font=dict(size=16, color="white"
        )),
        xaxis=dict(title="Dia", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Semana", showgrid=False, tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40),
        coloraxis_colorbar=dict(title="Energia Gerada (kWh)", tickvals=[0, 10, 20, 30], ticktext=["0", "10", "20", "30"])
    )

    st.plotly_chart(fig)

# Função para exibir gráfico de calor
def plot_heatmap_by_day_and_month(df, selected_year):
    """Exibe um gráfico de calor (heatmap) da energia gerada ao longo dos dias e meses"""
    # Filtrar os dados para o ano selecionado
    yearly_data = df[df["Year"] == selected_year]

    # Adicionar uma coluna "Month_Year" para exibir "Ano-Mês"
    yearly_data["Month_Year"] = yearly_data["Date"].dt.strftime('%Y-%m')

    # Criar uma tabela pivot para os dados
    heatmap_data = yearly_data.pivot_table(index="Month_Year", columns="Day", values="Energy", aggfunc="sum", fill_value=0)

    # Criar o gráfico de calor
    fig = px.imshow(heatmap_data, labels=dict(x="Dia", y="Mês-Ano", color="Energia Gerada (kWh)"),
                    x=heatmap_data.columns, y=heatmap_data.index, color_continuous_scale="Blues")

    fig.update_layout(
        title=dict(text=f"Distribuição de Energia Gerada por Dia e Mês ({selected_year})", x=0.5, xanchor='center', font=dict(size=16, color="white")),
        xaxis=dict(title="Dia", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Mês-Ano", showgrid=False, tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40),
        coloraxis_colorbar=dict(title="Energia Gerada (kWh)", tickvals=[0, 10, 20, 30], ticktext=["0", "10", "20", "30"])
    )

    st.plotly_chart(fig)


# TODO: Enviar o grafico ao selecionar o mes e ano
def plot_energy_bar_chart_by_month(df):
    """Exibe um gráfico de barras com a energia gerada por mês"""
    # Criar uma coluna "Month_Year" no formato MM-YYYY
    df["Month_Year"] = df["Date"].dt.strftime('%m-%Y')

    # Agrupar os dados por "Month_Year" e calcular a soma da energia gerada
    monthly_data = df.groupby("Month_Year")["Energy"].sum().reset_index()

    # Criar o gráfico de barras
    fig_bar = px.bar(
        monthly_data, x="Month_Year", y="Energy",
        title="Geração de Energia por Mês",
        labels={"Month_Year": "Mês-Ano", "Energy": "Geração de Energia (kWh)"},
        template="plotly_dark", color="Energy", color_continuous_scale="Blues"
    )

    # Personalizar o gráfico
    fig_bar.update_traces(marker=dict(line=dict(width=0.5, color="black")), opacity=0.8)

    # Ajustar o layout
    fig_bar.update_layout(
        title=dict(text="Geração de Energia por Mês", x=0.5, xanchor='center', font=dict(size=22, color="white")),
        xaxis=dict(title="Mês-Ano", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Geração de Energia (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )

    st.plotly_chart(fig_bar)


def plot_energy_bar_chart_by_month(df, selected_year):
    """Exibe um gráfico de barras com a energia gerada por mês para o ano selecionado"""
    # Filtrar os dados para o ano selecionado
    yearly_data = df[df["Year"] == selected_year]

    # Criar uma coluna "Month_Year" no formato MM-YYYY
    yearly_data["Month_Year"] = yearly_data["Date"].dt.strftime('%m-%Y')

    # Agrupar os dados por "Month_Year" e calcular a soma da energia gerada
    monthly_data = yearly_data.groupby("Month_Year")["Energy"].sum().reset_index()

    # Criar o gráfico de barras
    fig_bar = px.bar(
        monthly_data, x="Month_Year", y="Energy",
        title=f"Geração de Energia por Mês ({selected_year})",
        labels={"Month_Year": "Mês-Ano", "Energy": "Geração de Energia (kWh)"},
        template="plotly_dark", color="Energy", color_continuous_scale="Blues"
    )

    # Personalizar o gráfico
    fig_bar.update_traces(marker=dict(line=dict(width=0.5, color="black")), opacity=0.8)

    # Ajustar o layout
    fig_bar.update_layout(
        title=dict(text=f"Geração de Energia por Mês ({selected_year})", x=0.5, xanchor='center', font=dict(size=22, color="white")),
        xaxis=dict(title="Mês-Ano", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Geração de Energia (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )

    st.plotly_chart(fig_bar)


def plot_comparative_months_by_year_line_filtered(df, selected_year):
    """Exibe um gráfico de linhas comparativo dos meses para o ano selecionado"""
    # Filtrar os dados para o ano selecionado
    yearly_data = df[df["Year"] == selected_year]

    # Criar uma coluna "Month_Year" no formato MM-YYYY
    yearly_data["Month_Year"] = yearly_data["Date"].dt.strftime('%m-%Y')

    # Agrupar os dados por "Month_Year" e calcular a soma da energia gerada
    monthly_data = yearly_data.groupby("Month_Year")["Energy"].sum().reset_index()

    # Criar o gráfico de linhas
    fig = px.line(
        monthly_data, x="Month_Year", y="Energy",
        title=f"Comparativo de Energia Gerada por Mês ({selected_year})",
        labels={"Month_Year": "Mês-Ano", "Energy": "Energia Gerada (kWh)"},
        template="plotly_dark", markers=True
    )

    # Ajustar o layout
    fig.update_layout(
        title=dict(text=f"Comparativo de Energia Gerada por Mês ({selected_year})", x=0.5, font=dict(size=16, color="white")),
        xaxis=dict(title="Mês-Ano", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )

    st.plotly_chart(fig)


def plot_boxplot_by_day(daily_data, selected_year, selected_month):
    """Exibe um boxplot da energia gerada por dia no mês selecionado"""
    fig_box = px.box(
        daily_data,
        x="Day",
        y="Energy",
        title=f"Distribuição de Energia Gerada por Dia ({selected_year}-{selected_month:02d})",
        template="plotly_dark"
    )
    fig_box.update_layout(
        title=dict(text=f"Distribuição de Energia Gerada por Dia ({selected_year}-{selected_month:02d})", x=0.5, font=dict(size=16, color="white")),
        xaxis=dict(title="Dia", tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Energia Gerada (kWh)", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818"
    )
    st.plotly_chart(fig_box)


def plot_stacked_bar_chart_by_hour(df, selected_year, selected_month):
    """Exibe um gráfico de barras empilhadas com a energia gerada por hora ao longo dos dias"""
    # Filtrar os dados para o mês e ano selecionados
    monthly_data = df[(df["Year"] == selected_year) & (df["Month"] == selected_month)]

    # Agrupar os dados por dia e hora
    hourly_data = monthly_data.groupby(["Day", "Hour"])["Energy"].sum().reset_index()

    # Criar o gráfico de barras empilhadas
    fig_bar = px.bar(
        hourly_data,
        x="Day",
        y="Energy",
        color="Hour",
        title=f"Energia Gerada por Hora ao Longo dos Dias ({selected_year}-{selected_month:02d})",
        labels={"Day": "Dia", "Energy": "Energia Gerada (kWh)", "Hour": "Hora"},
        template="plotly_dark"
    )
    fig_bar.update_layout(
        title=dict(text=f"Energia Gerada por Hora ao Longo dos Dias ({selected_year}-{selected_month:02d})", x=0.5, font=dict(size=16, color="white")),
        xaxis=dict(title="Dia", tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Energia Gerada (kWh)", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818"
    )
    st.plotly_chart(fig_bar)


def plot_heatmap_by_hour_and_day(df, selected_year, selected_month):
    """Exibe um heatmap da energia gerada por hora ao longo dos dias do mês selecionado"""
    # Filtrar os dados para o mês e ano selecionados
    monthly_data = df[(df["Year"] == selected_year) & (df["Month"] == selected_month)]

    # Criar uma tabela pivot para os dados
    heatmap_data = monthly_data.pivot_table(index="Hour", columns="Day", values="Energy", aggfunc="sum", fill_value=0)

    # Criar o gráfico de calor
    fig_heatmap = px.imshow(
        heatmap_data,
        labels=dict(x="Dia", y="Hora", color="Energia Gerada (kWh)"),
        title=f"Mapa de Calor: Energia Gerada por Hora e Dia ({selected_year}-{selected_month:02d})",
        template="plotly_dark", color_continuous_scale="Blues"
    )
    fig_heatmap.update_layout(
        title=dict(text=f"Mapa de Calor: Energia Gerada por Hora e Dia ({selected_year}-{selected_month:02d})", x=0.5, font=dict(size=16, color="white")),
        xaxis=dict(title="Dia", tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Hora", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818"
    )
    st.plotly_chart(fig_heatmap)


def plot_trendline_by_day(daily_data, selected_year, selected_month):
    """Exibe um gráfico de linha com a tendência da energia gerada por dia no mês selecionado"""
    start_date = pd.Timestamp(year=selected_year, month=selected_month, day=1)
    end_date = start_date + pd.offsets.MonthEnd(0)
    valid_days = pd.date_range(start=start_date, end=end_date).day
    fig_trend = px.scatter(
        daily_data,
        x="Day",
        y="Energy",
        trendline="ols",
        title=f"Tendência de Energia Gerada por Dia ({selected_year}-{selected_month:02d})",
        labels={"Day": "Dia", "Energy": "Energia Gerada (kWh)"},
        template="plotly_dark"
    )

    # Ajustar o layout para exibir todos os dias no eixo x
    fig_trend.update_layout(
        title=dict(text=f"Tendência de Energia Gerada por Dia ({selected_year}-{selected_month:02d})", x=0.5, font=dict(size=16, color="white")),
        xaxis=dict(
            title="Dia",
            showgrid=False, # Remove as linhas de grade
            tickmode="linear",  # Exibe os ticks de forma linear
            ticks="outside",    # Exibe os ticks fora do gráfico
            tickwidth=2,        # Espessura dos ticks
            tickfont=dict(color="#ffffff"), # Cor dos ticks
            range=[valid_days.min() - 0.5, valid_days.max() + 0.5],  # Adiciona espaço visual sem incluir valores fora do intervalo
            tick0=1,            # Começa no dia 1
            dtick=1,            # Intervalo de 1 dia entre os ticks
            tickangle=45,       # Rotaciona os ticks em 45 graus

        ),
        yaxis=dict(
            title="Energia Gerada (kWh)",
            tickfont=dict(color="#ffffff")
        ),
        plot_bgcolor="#181818",
        paper_bgcolor="#181818"
    )
    st.plotly_chart(fig_trend)


def plot_cumulative_energy_by_week_2(df, selected_year, selected_week):
    """Exibe um gráfico de linha acumulada de energia por dia na semana selecionada"""
    # Filtrar os dados para o ano e semana selecionados
    weekly_data = df[(df["Year"] == selected_year) & (df["Week"] == selected_week)]

    # Verificar se há dados disponíveis
    if weekly_data.empty:
        st.warning(f"⚠️ Nenhum dado disponível para a semana {selected_week} do ano {selected_year}.")
        return

    # Agrupar os dados por dia e calcular a soma da energia gerada
    daily_data = weekly_data.groupby("Day")["Energy"].sum().reset_index()

    # Criar o gráfico de linha acumulada
    fig_line = px.line(
        daily_data, x="Day", y="Energy",
        title=f"Geração Acumulada de Energia por Dia na Semana {selected_week} ({selected_year})",
        labels={"Day": "Dia", "Energy": "Geração Acumulada (kWh)"},
        template="plotly_dark"
    )

    # Personalizar o gráfico
    fig_line.update_traces(
        mode='lines+markers',
        line=dict(color="#00bcd4", width=2),
        marker=dict(size=6, color="#ff5722", line=dict(width=1, color="white"))
    )

    # Ajustar o layout com espaço no início e no fim
    fig_line.update_layout(
        title=dict(text=f"Geração Acumulada de Energia por Dia na Semana {selected_week} ({selected_year})", x=0.5, xanchor='center', font=dict(size=16, color="#ffffff")),
        xaxis=dict(
            title="Dia", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2,
            tickangle=45, tickfont=dict(color="#ffffff"),
            range=[daily_data["Day"].min() - 0.5, daily_data["Day"].max() + 0.5]  # Adiciona espaço visual sem incluir valores fora do intervalo
        ),
        yaxis=dict(
            title="Geração Acumulada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1,
            zerolinecolor="gray", tickfont=dict(color="#ffffff")
        ),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )

    st.plotly_chart(fig_line)

def display_revenue_summary(total_data):
    """Exibe um resumo da receita da usina, incluindo economia no mês atual e no total"""
    # Preço da unidade da eletricidade (R$/kWh)
    electricity_price_per_kwh = 1.00

    # Calcular o total de energia gerada (kWh)
    total_energy_kwh = total_data["Energy"].sum()

    # Calcular o total de energia gerada no mês atual
    current_year = pd.Timestamp.now().year
    current_month = pd.Timestamp.now().month
    current_month_data = total_data[(total_data["Year"] == current_year) & (total_data["Month"] == current_month)]
    current_month_energy_kwh = current_month_data["Energy"].sum()

    # Calcular a receita total e a receita do mês atual
    total_revenue = total_energy_kwh * electricity_price_per_kwh  # Receita total (R$)
    current_month_revenue = current_month_energy_kwh * electricity_price_per_kwh  # Receita do mês atual (R$)

    # Dividir em colunas para exibir as métricas
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="💰 Economia no Mês Atual",
            value=f"R$ {locale.format_string('%.2f', current_month_revenue, grouping=True)}",
            delta=None,
            help=f"Energia gerada no mês atual ({current_month:02d}/{current_year}) convertida em economia (R$)"
        )
    with col2:
        st.metric(
            label="💰 Economia Total",
            value=f"R$ {locale.format_string('%.2f', total_revenue, grouping=True)}",
            delta=None,
            help="Energia total gerada convertida em economia (R$)"
        )

def display_total_performance_indicators(total_data):
    """Exibe um resumo total dos dados de energia"""
    # Capacidade máxima do sistema (em kW)
    system_capacity_kw = 4.4

    # Calcular o total de energia gerada (kWh e MWh)
    total_energy_kwh = total_data["Energy"].sum()
    total_energy_mwh = total_energy_kwh / 1000

    # Calcular o total de energia gerada no mês atual
    current_year = pd.Timestamp.now().year
    current_month = pd.Timestamp.now().month
    current_month_data = total_data[(total_data["Year"] == current_year) & (total_data["Month"] == current_month)]
    current_month_energy_kwh = current_month_data["Energy"].sum()
    current_month_energy_mwh = current_month_energy_kwh / 1000

    # Calcular a eficiência com base na capacidade máxima do sistema
    total_hours = len(total_data) * 24  # Número total de horas no período (aproximado)
    max_possible_energy_kwh = system_capacity_kw * total_hours
    efficiency = (total_energy_kwh / max_possible_energy_kwh) * 100 if max_possible_energy_kwh > 0 else 0

    # Calcular o total de energia gerada no ano atual
    current_year_data = total_data[total_data["Year"] == current_year]
    current_year_energy_kwh = current_year_data["Energy"].sum()
    current_year_energy_mwh = current_year_energy_kwh / 1000  # Conversão de kWh para MWh


    # Outras métricas
    std_dev_energy = total_data["Energy"].std()

    # Dividir em colunas para exibir as métricas
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric(
            label="📅 Energia Gerada Este Mês",
            value=f"{locale.format_string('%.2f', current_month_energy_mwh, grouping=True)} MWh",
            delta=None,
            help=f"Total de energia gerada no mês atual ({current_month:02d}/{current_year}) em MWh"
        )
    with col2:
        st.metric(
            label="🔋 Energia Gerada Este Ano",
            value=f"{locale.format_string('%.2f', current_year_energy_mwh, grouping=True)} MWh",
            delta=None,
            help=f"Total de energia gerada no ano atual ({current_year}) em MWh"
        )
    with col3:
        st.metric(
            label="🔋 Total de Energia Gerada",
            value=f"{locale.format_string('%.2f', total_energy_mwh, grouping=True)} MWh",
            delta=None,
            help="Energia total gerada no período completo (em MWh)"
        )
    with col4:
        st.metric(
            label="📊 Desvio Padrão",
            value=f"{locale.format_string('%.2f', std_dev_energy, grouping=True)} kWh",
            delta=None,
            help="Desvio padrão da energia gerada no período completo"
        )
    with col5:
        st.metric(
            label="💡 Eficiência (%)",
            value=f"{locale.format_string('%.2f', efficiency, grouping=True)} kWh",
            delta=None,
            help="Eficiência da geração de energia em relação à capacidade máxima do sistema"
        )

def display_environmental_benefits(total_data):
    """Exibe os benefícios ambientais com base na energia gerada"""
    # Fatores de conversão ajustados para os valores fornecidos
    co2_emission_factor = 1.0  # kg de CO2 evitados por kWh (ajustado para os valores fornecidos)
    carbon_absorption_per_tree = 18.32  # kg de CO2 absorvidos por árvore por ano (ajustado para os valores fornecidos)

    # Calcular o total de energia gerada (kWh)
    total_energy_kwh = total_data["Energy"].sum()

    # Calcular a redução de emissão de CO2 (em toneladas)
    total_co2_reduction_kg = total_energy_kwh * co2_emission_factor
    total_co2_reduction_ton = total_co2_reduction_kg / 1000  # Conversão para toneladas

    # Calcular a neutralização de carbono (número de árvores)
    total_trees = total_co2_reduction_kg / carbon_absorption_per_tree

    # Dividir em colunas para exibir as métricas
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="🌍 Redução da Emissão de CO2",
            value=f"{locale.format_string('%.2f', total_co2_reduction_ton, grouping=True)} Tonelada(s)",
            delta=None,
            help="Quantidade de CO2 evitada com base na energia gerada (em toneladas)"
        )
    with col2:
        st.metric(
            label="🌳 Neutralização de Carbono",
            value=f"{locale.format_string('%.0f', total_trees, grouping=True)} Árvore(s)",
            delta=None,
            help="Quantidade de árvores necessárias para neutralizar o CO2 evitado"
        )


def display_total_performance_indicators_3(total_data):
    """Exibe um resumo total dos dados de energia em um card estilizado com texto e valores alinhados"""
    # Calcular os dados
    total_energy_kwh = total_data["Energy"].sum()
    total_energy_mwh = total_energy_kwh / 1000
    avg_energy = total_data["Energy"].mean()
    max_energy = total_data["Energy"].max()
    min_energy = total_data["Energy"].min()
    std_dev_energy = total_data["Energy"].std()

    # Estilo do card
    card_style = """
        <style>
        .card {
            background-color: #1e1e1e;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
            overflow: hidden; /* Garante que o conteúdo não ultrapasse as bordas arredondadas */
        }
        .card-header {
            padding: 15px;
            text-align: center;
        }
        .card-header h3 {
            color: #ffffff;
            margin: 0;
        }
        .card-header hr {
            border: 0;
            height: 1px;
            background: #444444; /* Cor da linha abaixo do título */
            margin: 10px 0 0 0; /* Margem apenas acima da linha */
        }
        .card-content {
            padding: 20px; /* Espaçamento interno para o conteúdo */
        }
        .card-content .row {
            display: flex; /* Garante que os itens fiquem lado a lado */
            justify-content: space-between; /* Espaço entre o texto e o valor */
            align-items: center; /* Alinha os itens verticalmente */
            margin: 5px 0;
            padding-bottom: 10px;
            border-bottom: 1px solid #444444; /* Linha separadora */
        }
        .card-content .row .label {
            color: #ffffff;
            font-weight: normal;
            text-align: left;
            flex: 1; /* O texto ocupa o espaço à esquerda */
        }
        .card-content .row .value {
            color: #00ff00; /* Cor verde para os valores */
            font-weight: bold;
            text-align: right;
            flex: 0; /* O valor ocupa o espaço à direita */
        }

        .title {
            color: grey;
            font-size: 12px; /* Ajuste o tamanho da fonte */
            margin-left: 5px; /* Adiciona um pequeno espaçamento à esquerda */
            vertical-align: middle; /* Alinha verticalmente com o valor */
        }
        </style>
    """

    # Adicionar o estilo ao Streamlit
    st.markdown(card_style, unsafe_allow_html=True)

    # Conteúdo do card com texto e valores alinhados
    card_content = f"""
    <div class="card">
        <div class="card-header">
            <h3>🔋 Resumo Total de Energia</h3>
            <hr>
        </div>
        <div class="card-content">
            <div class="row">
                <span class="label"><strong>Total de Energia Gerada:</strong></span>
                <span class="value">{total_energy_mwh:,.2f}</span><span class="title">MWh</span>
            </div>
            <div class="row">
                <span class="label"><strong>Média de Energia:</strong></span>
                <span class="value">{avg_energy:,.2f}</span><span class="title">kWh</span>
            </div>
            <div class="row">
                <span class="label"><strong>Máxima de Energia:</strong></span>
                <span class="value">{max_energy:,.2f}</span><span class="title">kWh</span>
            </div>
            <div class="row">
                <span class="label"><strong>Mínima de Energia:</strong></span>
                <span class="value">{min_energy:,.2f}</span><span class="title">kWh</span>
            </div>
            <div class="row">
                <span class="label"><strong>Desvio Padrão:</strong></span>
                <span class="value">{std_dev_energy:,.2f}</span><span class="title">kWh</span>
            </div>
        </div>
    </div>
    """

    # Exibir o card no Streamlit
    st.markdown(card_content, unsafe_allow_html=True)


def display_revenue_summary_3(total_data):
    """Exibe a receita da usina em um card estilizado"""
    # Preço da unidade da eletricidade (R$/kWh)
    electricity_price_per_kwh = 1.00

    # Calcular o total de energia gerada (kWh)
    total_energy_kwh = total_data["Energy"].sum()

    # Calcular o total de energia gerada no mês atual
    current_year = pd.Timestamp.now().year
    current_month = pd.Timestamp.now().month
    current_month_data = total_data[(total_data["Year"] == current_year) & (total_data["Month"] == current_month)]
    current_month_energy_kwh = current_month_data["Energy"].sum()

    # Calcular a receita total e a receita do mês atual
    total_revenue = total_energy_kwh * electricity_price_per_kwh  # Receita total (R$)
    current_month_revenue = current_month_energy_kwh * electricity_price_per_kwh  # Receita do mês atual (R$)

    # Estilo do card
    card_style = """
        <style>
        .card {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        .card h3 {
            color: #ffffff;
            margin-bottom: 10px;
        }
        .card p {
            color: #ffffff;
            margin: 5px 0;
        }
        </style>
    """

    # Adicionar o estilo ao Streamlit
    st.markdown(card_style, unsafe_allow_html=True)

    # Conteúdo do card
    card_content = f"""
    <div class="card">
        <h3>💰 Receita da Usina</h3>
        <p><strong>Economia no Mês Atual:</strong> R$ {current_month_revenue:,.2f}</p>
        <p><strong>Economia Total:</strong> R$ {total_revenue:,.2f}</p>
    </div>
    """

    # Exibir o card no Streamlit
    st.markdown(card_content, unsafe_allow_html=True)

def display_environmental_benefits_3(total_data):
    """Exibe os benefícios ambientais em um card estilizado"""
    # Fatores de conversão
    co2_emission_factor = 0.053  # kg de CO2 evitados por kWh
    carbon_absorption_per_tree = 21  # kg de CO2 absorvidos por árvore por ano

    # Calcular o total de energia gerada (kWh)
    total_energy_kwh = total_data["Energy"].sum()

    # Calcular a redução de emissão de CO2 (em toneladas)
    total_co2_reduction_kg = total_energy_kwh * co2_emission_factor
    total_co2_reduction_ton = total_co2_reduction_kg / 1000  # Conversão para toneladas

    # Calcular a neutralização de carbono (número de árvores)
    total_trees = total_co2_reduction_kg / carbon_absorption_per_tree

    # Estilo do card
    card_style = """
        <style>
        .card {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        .card h3 {
            color: #ffffff;
            margin-bottom: 10px;
        }
        .card p {
            color: #ffffff;
            margin: 5px 0;
        }
        </style>
    """

    # Adicionar o estilo ao Streamlit
    st.markdown(card_style, unsafe_allow_html=True)

    # Conteúdo do card
    card_content = f"""
    <div class="card">
        <h3>🌱 Benefícios Ambientais</h3>
        <p><strong>Redução da Emissão de CO2:</strong> {total_co2_reduction_ton:,.2f} Tonelada(s)</p>
        <p><strong>Neutralização de Carbono:</strong> {total_trees:,.0f} Árvore(s)</p>
    </div>
    """

    # Exibir o card no Streamlit
    st.markdown(card_content, unsafe_allow_html=True)
