import streamlit as st
import pandas as pd

def display_performance_indicators(daily_data):
    total_energy = daily_data["Energy"].sum()
    avg_energy = daily_data["Energy"].mean()
    max_energy = daily_data["Energy"].max()
    min_energy = daily_data["Energy"].min()
    std_dev_energy = daily_data["Energy"].std()
    ideal_energy = total_energy * 0.9
    efficiency = (total_energy / ideal_energy) * 100 if ideal_energy > 0 else 0
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1: st.metric(label="🔋 Total de Energia Gerada", value=f"{total_energy:,.2f} kWh", delta=f"+{total_energy - avg_energy:,.2f} kWh", delta_color="inverse")
    with col2: st.metric(label="📊 Média de Energia Diária", value=f"{avg_energy:,.2f} kWh")
    with col3: st.metric(label="⚡ Máxima de Energia Diária", value=f"{max_energy:,.2f} kWh")
    with col4: st.metric(label="📉 Mínima de Energia Diária", value=f"{min_energy:,.2f} kWh")
    with col5: st.metric(label="📊 Desvio Padrão", value=f"{std_dev_energy:,.2f} kWh")
    with col6: st.metric(label="💡 Eficiência (%)", value=f"{efficiency:,.2f}%")

def display_weekly_performance_indicators(weekly_data):
    total_energy = weekly_data["Energy"].sum()
    avg_energy = weekly_data["Energy"].mean()
    max_energy = weekly_data["Energy"].max()
    min_energy = weekly_data["Energy"].min()
    std_dev_energy = weekly_data["Energy"].std()
    ideal_energy = total_energy * 0.9
    efficiency = (total_energy / ideal_energy) * 100 if ideal_energy > 0 else 0
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1: st.metric(label="🔋 Total de Energia Gerada", value=f"{total_energy:,.2f} kWh", delta=f"+{total_energy - avg_energy:,.2f} kWh", delta_color="inverse")
    with col2: st.metric(label="📊 Média de Energia Semanal", value=f"{avg_energy:,.2f} kWh")
    with col3: st.metric(label="⚡ Máxima de Energia Semanal", value=f"{max_energy:,.2f} kWh")
    with col4: st.metric(label="📉 Mínima de Energia Semanal", value=f"{min_energy:,.2f} kWh")
    with col5: st.metric(label="📊 Desvio Padrão", value=f"{std_dev_energy:,.2f} kWh")
    with col6: st.metric(label="💡 Eficiência (%)", value=f"{efficiency:,.2f}%")
