import streamlit as st
import pandas as pd
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

if uploaded_file:
    df = load_data(uploaded_file)
    df["Date"] = pd.to_datetime(df["Date"])  # Garantir que seja datetime

    # Sidebar com opções de filtragem
    st.sidebar.subheader("📅 Selecione o período de análise")
    period_option = st.sidebar.radio("Período", ["Dia", "Semana", "Mês", "Ano", "Total"], horizontal=True)

    # Ajuste do intervalo de datas
    max_date = df["Date"].max().date()
    min_date = df["Date"].min().date()
    selected_date = st.sidebar.date_input("Selecione a data", max_date, min_value=min_date, max_value=max_date)

    # Converter para datetime.date antes de fazer comparações
    if period_option == "Dia":
        start_date = selected_date
        end_date = selected_date
    elif period_option == "Semana":
        start_date = (selected_date - pd.DateOffset(days=6)).date()
        end_date = selected_date
    elif period_option == "Mês":
        start_date = selected_date.replace(day=1)
        end_date = (start_date + pd.DateOffset(months=1) - pd.DateOffset(days=1)).date()
    elif period_option == "Ano":
        start_date = selected_date.replace(month=1, day=1)
        end_date = (start_date + pd.DateOffset(years=1) - pd.DateOffset(days=1)).date()
    else:
        start_date, end_date = min_date, max_date  # "Total"

    # Filtrando os dados corretamente (garantindo que start_date e end_date são do tipo datetime.date)
    df_filtered = df[
        (df["Date"].dt.date >= start_date) &
        (df["Date"].dt.date <= end_date)
    ]

    # Criar gráfico interativo de histórico de geração
    st.subheader("📈 Histórico de Geração de Energia")
    fig = px.area(df_filtered, x="Date", y="Energy (kWh)", title=f"Produção - {period_option}", labels={"Energy (kWh)": "Potência (kW)"})
    st.plotly_chart(fig, use_container_width=True)

# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("📤 Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para datetime
#     return df

# if uploaded_file:
#     df = load_data(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Garantir que seja datetime

#     # Criar layout com tabs para seleção de período
#     st.subheader("📅 Histórico de Dados")
#     tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dia", "Semana", "Mês", "Ano", "Total"])

#     with tab1:
#         period_option = "Dia"
#     with tab2:
#         period_option = "Semana"
#     with tab3:
#         period_option = "Mês"
#     with tab4:
#         period_option = "Ano"
#     with tab5:
#         period_option = "Total"

#     st.write(f"🔹 Período selecionado: **{period_option}**")


import streamlit as st
import pandas as pd
import datetime

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

if uploaded_file:
    df = load_data(uploaded_file)
    df["Date"] = pd.to_datetime(df["Date"])  # Garantir que seja datetime

    # Criar layout com tabs para seleção de período
    st.subheader("📅 Histórico de Dados")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dia", "Semana", "Mês", "Ano", "Total"])

    with tab1:
        period_option = "Dia"
    with tab2:
        period_option = "Semana"
    with tab3:
        period_option = "Mês"
        # Seleção de mês e ano usando selectbox
        selected_month = st.selectbox("Selecione o mês", range(1, 13), format_func=lambda x: f"{x:02d}")
        selected_year = st.selectbox("Selecione o ano", range(2023, 2025))
        st.write(f"Mês selecionado: {selected_month:02d}/{selected_year}")
    with tab4:
        period_option = "Ano"
    with tab5:
        period_option = "Total"

    st.write(f"🔹 Período selecionado: **{period_option}**")
