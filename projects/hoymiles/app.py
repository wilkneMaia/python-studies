from data_loader import load_data
from visualizations import plot_area_stack_by_year, plot_candlestick_by_month, plot_comparative_months_by_year_line, plot_scatter_by_year, plot_weekly_data_by_date, plot_energy_by_week, plot_cumulative_energy_by_week_2, plot_energy_bar_chart, plot_cumulative_energy_graph, plot_quadrant_graph, plot_total_by_year, plot_heatmap_by_week, plot_heatmap_by_day_and_month, plot_energy_bar_chart_by_month, plot_energy_bar_chart_by_month, plot_comparative_months_by_year_line_filtered, plot_trendline_by_day, plot_heatmap_by_hour_and_day, plot_stacked_bar_chart_by_hour, plot_boxplot_by_day, display_total_performance_indicators, display_revenue_summary, display_environmental_benefits, display_total_performance_indicators_3, display_revenue_summary_3, display_environmental_benefits_3
from indicators import display_weekly_performance_indicators, display_performance_indicators

import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from numpy import polyfit


# Configuração da página
st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# Barra lateral para seleção do arquivo
uploaded_file = st.sidebar.file_uploader("📤 Faça upload do arquivo CSV", type=["csv"])

def display_tabs(df):
    """Exibe os gráficos com base no filtro de Mês, Semana, Ano ou Total"""
    # st.subheader("📅 Histórico de Dados")
    filter_option = st.sidebar.radio("Selecione a visualização", ["Dia", "Semana", "Mês", "Ano", "Total"], key="filter_option")

    if filter_option == "Semana":
        selected_date = st.sidebar.date_input("Selecione uma data para ver a semana correspondente", value=pd.to_datetime("2025-01-01"), key="selected_date")
        selected_year = selected_date.year
        filtered_data = df[df["Year"] == selected_year]
        selected_week = selected_date.isocalendar().week

        if not filtered_data.empty:
            plot_weekly_data_by_date(df, selected_date)
            plot_cumulative_energy_by_week_2(df, selected_year, selected_week)
        else:
            st.warning("⚠️ Nenhum dado disponível para este período.")

    elif filter_option == "Mês":
        col1, col2 = st.sidebar.columns(2)
        with col1:
            selected_month = st.selectbox("Selecione o mês", range(1, 13), format_func=lambda x: f"{x:02d}", key="selected_month")
        with col2:
            selected_year = st.selectbox(
                "Selecione o ano",
                range(2021, 2026),
                index=4,  # Define o índice do valor padrão (2025 é o 5º item, índice 4)
                key="selected_year_month",
                format_func=lambda x: f"{x:02d}"
            )
        filtered_data = df[(df["Year"] == selected_year) & (df["Month"] == selected_month)]
        if not filtered_data.empty:
            daily_data = filtered_data.groupby("Day")["Energy"].sum().reset_index()
            st.markdown(f"<h3>📈 Dados de geração de energia para {selected_year}-{selected_month:02d}</h3>", unsafe_allow_html=True)
            x = daily_data["Day"]
            y = daily_data["Energy"]
            slope, intercept = np.polyfit(x, y, 1)
            display_performance_indicators(daily_data)
            plot_energy_bar_chart(daily_data, x, slope, intercept)
            plot_cumulative_energy_graph(daily_data, selected_year, selected_month)
            plot_trendline_by_day(daily_data, selected_year, selected_month)
        else:
            st.warning("⚠️ Nenhum dado disponível para este período.")

    elif filter_option == "Ano":
        current_year = pd.Timestamp.now().year
        year_range = list(range(2021, 2026))
        default_index = year_range.index(current_year) if current_year in year_range else 0

        selected_year = st.sidebar.selectbox(
            "Selecione o ano",
            year_range,
            key="selected_year",
            index=default_index  # Define o índice do ano atual como padrão
        )
        filtered_data = df[df["Year"] == selected_year]

        if not filtered_data.empty:
            daily_data = filtered_data.groupby("Day")["Energy"].sum().reset_index()
            st.markdown(f"<h3>📈 Dados de geração de energia para o ano {selected_year}", unsafe_allow_html=True)
            x = daily_data["Day"]
            y = daily_data["Energy"]
            slope, intercept = np.polyfit(x, y, 1)
            display_performance_indicators(daily_data)
            plot_energy_bar_chart_by_month(df, selected_year)
            plot_comparative_months_by_year_line_filtered(df, selected_year)
            plot_heatmap_by_day_and_month(df, selected_year)
        else:
            st.warning("⚠️ Nenhum dado disponível para este período.")

    elif filter_option == "Total":
        st.markdown("<h3>📊 Resumo Total</h3>", unsafe_allow_html=True)

    # Criar colunas para exibir os displays lado a lado
    col1, col2, col3 = st.columns(3)

    with col1:
        display_total_performance_indicators_3(df)  # Exibe o resumo total de energia
    with col2:
        display_revenue_summary_3(df)  # Exibe a receita da usina
    with col3:
        display_environmental_benefits_3(df)  # Exibe os benefícios ambientais


        # display_total_performance_indicators_3(df)
        # display_revenue_summary_3(df)
        # display_environmental_benefits_3(df)
        # # display_total_performance_indicators(df)
        # # display_revenue_summary(df)
        # # display_environmental_benefits(df)
    plot_total_by_year(df)
    plot_comparative_months_by_year_line(df)
    plot_area_stack_by_year(df)
    plot_scatter_by_year(df)
    plot_candlestick_by_month(df)

if uploaded_file:
    df = load_data(uploaded_file)
    display_tabs(df)
