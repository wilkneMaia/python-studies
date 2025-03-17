import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import streamlit as st
from indicators import display_performance_indicators
import pandas as pd

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
    fig = create_bar_chart(daily_data, "Day", "Energy", "Geração de Energia por Dia", "Dia", "Geração de Energia (kWh)")
    fig.add_trace(go.Scatter(x=x, y=slope * x + intercept, mode='lines', name='Tendência', line=dict(color='#ff5722', width=3, dash='solid')))
    fig.update_layout(
        title=dict(text="Geração de Energia por Dia", x=0.5, xanchor='center', font=dict(size=16, color="white")),
        xaxis=dict(title="Dia", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Geração de Energia (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig)

# Função para exibir gráfico de geração acumulada de energia
def plot_cumulative_energy_graph(daily_data):
    fig_line = px.line(
        daily_data, x="Day", y="Energy",
        title="Geração Acumulada de Energia por Dia",
        labels={"Day": "Dia", "Energy": "Geração Acumulada (kWh)"},
        template="plotly_dark"
    )
    fig_line.update_traces(mode='lines+markers', line=dict(color="#00bcd4", width=2), marker=dict(size=6, color="#ff5722", line=dict(width=1, color="white")))
    fig_line.update_layout(
        title=dict(text="Geração Acumulada de Energia por Dia", x=0.5, xanchor='center', font=dict(size=16, color="#ffffff")),
        xaxis=dict(title="Dia", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Geração Acumulada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
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
        plot_cumulative_energy_graph(daily_data)
        plot_heatmap_by_week(df, selected_date)
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
