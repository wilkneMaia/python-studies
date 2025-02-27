# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
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

# def plot_line_chart(df_micro, micro):
#     fig = px.line(df_micro, x="Date", y="Energy (kWh)", markers=True,
#                   title=f"Evolução da Geração - {micro}")
#     st.plotly_chart(fig, use_container_width=True)

# def plot_pie_chart(df_grouped):
#     st.subheader("📊 Distribuição da Geração por Microinversor")
#     fig = px.pie(df_grouped, names="Microinversor", values="Energy (kWh)", hole=0.4)
#     st.plotly_chart(fig, use_container_width=True)

# def plot_cumulative_energy(df_time_series):
#     st.subheader("📊 Energia Gerada Acumulada")
#     df_time_series["Cumulative Energy"] = df_time_series.groupby("Microinversor")["Energy (kWh)"].cumsum()
#     fig = px.area(df_time_series, x="Date", y="Cumulative Energy", color="Microinversor")
#     st.plotly_chart(fig, use_container_width=True)

# if uploaded_file:
#     df = load_data(uploaded_file)

#     # Filtros no sidebar
#     st.sidebar.subheader("📅 Selecione um intervalo de datas")
#     min_date, max_date = df["Date"].min().date(), df["Date"].max().date()
#     date_range = st.sidebar.date_input("Data", [min_date, max_date], min_value=min_date, max_value=max_date)

#     # Ajuste para garantir que a data selecionada seja uma tupla, caso contrário, trata-se como intervalo único
#     if isinstance(date_range, tuple):
#         start_date, end_date = date_range
#     else:
#         start_date = end_date = date_range  # Se for uma única data, usa a mesma para o intervalo

#     # Seleção de microinversores
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect("🔌 Escolha os Microinversores", microinversores, default=microinversores)

#     # Filtrando os dados corretamente
#     df_filtered = df[
#         (df["Date"].dt.date >= start_date) &  # Garantindo que as datas estão corretas
#         (df["Date"].dt.date <= end_date) &
#         (df["Microinversor"].isin(selected_microinversores))
#     ]

#     # Cálculo de energia gerada
#     current_month, current_year = pd.Timestamp.now().month, pd.Timestamp.now().year
#     energia_mes = df_filtered[df_filtered["Date"].dt.month == current_month]["Energy (kWh)"].sum()
#     energia_ano = df_filtered[df_filtered["Date"].dt.year == current_year]["Energy (kWh)"].sum()
#     energia_total = df_filtered["Energy (kWh)"].sum()

#     # Exibir métricas principais
#     col1, col2, col3 = st.columns(3)
#     col1.metric("⚡ Energia este mês", f"{energia_mes:.2f} kWh")
#     col2.metric("🌍 Energia este ano", f"{energia_ano / 1000:.2f} MWh")
#     col3.metric("🔋 Energia total", f"{energia_total / 1000:.2f} MWh")

#     # Agrupar por microinversor para gerar gráficos
#     df_grouped = df_filtered.groupby("Microinversor")["Energy (kWh)"].sum().reset_index()

#     plot_pie_chart(df_grouped)

#     st.subheader("📈 Evolução da Geração de Energia")
#     df_time_series = df_filtered.groupby(["Date", "Microinversor"])["Energy (kWh)"].sum().reset_index()
#     for micro in selected_microinversores:
#         df_micro = df_time_series[df_time_series["Microinversor"] == micro]
#         plot_line_chart(df_micro, micro)

#     plot_cumulative_energy(df_time_series)

#     # Gráfico de barras de energia por microinversor
#     st.subheader("🔍 Energia Total por Microinversor")
#     fig = px.bar(df_grouped, x="Microinversor", y="Energy (kWh)", text_auto=True)
#     st.plotly_chart(fig, use_container_width=True)


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

#     # Sidebar com opções de filtragem
#     st.sidebar.subheader("📅 Selecione o período de análise")
#     period_option = st.sidebar.radio("Período", ["Dia", "Semana", "Mês", "Ano", "Total"], horizontal=True)

#     # Ajuste do intervalo de datas
#     max_date = df["Date"].max().date()
#     min_date = df["Date"].min().date()
#     selected_date = st.sidebar.date_input("Selecione a data", max_date, min_value=min_date, max_value=max_date)

#     # Converter para datetime.date antes de fazer comparações
#     if period_option == "Dia":
#         start_date = selected_date
#         end_date = selected_date
#     elif period_option == "Semana":
#         start_date = (selected_date - pd.DateOffset(days=6)).date()
#         end_date = selected_date
#     elif period_option == "Mês":
#         start_date = selected_date.replace(day=1)
#         end_date = (start_date + pd.DateOffset(months=1) - pd.DateOffset(days=1)).date()
#     elif period_option == "Ano":
#         start_date = selected_date.replace(month=1, day=1)
#         end_date = (start_date + pd.DateOffset(years=1) - pd.DateOffset(days=1)).date()
#     else:
#         start_date, end_date = min_date, max_date  # "Total"

#     # Filtrando os dados corretamente (garantindo que start_date e end_date são do tipo datetime.date)
#     df_filtered = df[
#         (df["Date"].dt.date >= start_date) &
#         (df["Date"].dt.date <= end_date)
#     ]

#     # Criar gráfico interativo de histórico de geração
#     st.subheader("📈 Histórico de Geração de Energia")
#     fig = px.area(df_filtered, x="Date", y="Energy (kWh)", title=f"Produção - {period_option}", labels={"Energy (kWh)": "Potência (kW)"})
#     st.plotly_chart(fig, use_container_width=True)

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


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import datetime
# import calendar

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
#         # Seleção de mês e ano
#         selected_month = st.selectbox("Selecione o mês", range(1, 13), format_func=lambda x: f"{x:02d}")
#         selected_year = st.selectbox("Selecione o ano", range(2000, 2101))
#         st.write(f"Mês selecionado: {selected_month:02d}/{selected_year}")
#     with tab4:
#         period_option = "Ano"
#     with tab5:
#         period_option = "Total"

#     st.write(f"🔹 Período selecionado: **{period_option}**")


# import streamlit as st
# import pandas as pd
# import datetime

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
#         # Seleção de mês e ano usando selectbox
#         selected_month = st.selectbox("Selecione o mês", range(1, 13), format_func=lambda x: f"{x:02d}")
#         selected_year = st.selectbox("Selecione o ano", range(2023, 2026))
#         st.write(f"Mês selecionado: {selected_month:02d}/{selected_year}")
#     with tab4:
#         period_option = "Ano"
#     with tab5:
#         period_option = "Total"

#     st.write(f"🔹 Período selecionado: **{period_option}**")


# import streamlit as st
# import pandas as pd
# import datetime

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

# def display_tabs(df):
#     # Criar layout com tabs para seleção de período
#     st.subheader("📅 Histórico de Dados")
#     tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dia", "Semana", "Mês", "Ano", "Total"])

#     with tab1:
#         period_option = "Dia"
#     with tab2:
#         period_option = "Semana"
#     with tab3:
#         period_option = "Mês"
#         # Seleção de mês e ano usando selectbox lado a lado
#         col1, col2 = st.columns(2)
#         with col1:
#             selected_month = st.selectbox("Selecione o mês", range(1, 13), format_func=lambda x: f"{x:02d}")
#         with col2:
#             selected_year = st.selectbox("Selecione o ano", range(2023, 2026))
#         st.write(f"Mês selecionado: {selected_month:02d}/{selected_year}")
#     with tab4:
#         period_option = "Ano"
#     with tab5:
#         period_option = "Total"

#     st.write(f"🔹 Período selecionado: **{period_option}**")

# if uploaded_file:
#     df = load_data(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Garantir que seja datetime
#     display_tabs(df)


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
#     df.columns = df.columns.str.strip()  # Remove espaços extras nos nomes das colunas
#     df.rename(columns={"Energy (kWh)": "Energy"}, inplace=True)  # Renomeia a coluna
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para datetime
#     df["Day"] = df["Date"].dt.day  # Adiciona a coluna de dias do mês
#     return df

# def display_tabs(df):
#     st.subheader("📅 Histórico de Dados")
#     tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dia", "Semana", "Mês", "Ano", "Total"])

#     with tab3:
#         col1, col2 = st.columns(2)
#         with col1:
#             selected_month = st.selectbox("Selecione o mês", range(1, 13), format_func=lambda x: f"{x:02d}")
#         with col2:
#             selected_year = st.selectbox("Selecione o ano", range(2023, 2026))

#         # Filtrar os dados para o mês e ano selecionados
#         filtered_df = df[(df["Date"].dt.month == selected_month) & (df["Date"].dt.year == selected_year)]

#         if not filtered_df.empty:
#             daily_data = filtered_df.groupby("Day")["Energy"].sum().reset_index()
#             st.write(f"📈 Dados de geração de energia para {selected_month:02d}/{selected_year}")
#             fig = px.bar(daily_data, x="Day", y="Energy", title="Geração de Energia por Dia",
#                          labels={"Day": "Dia", "Energy": "Geração de Energia (kWh)"},
#                          template="plotly_dark")
#             fig.update_xaxes(type='category', tickmode='linear', dtick=1)  # Mostrar todos os dias
#             st.plotly_chart(fig)
#         else:
#             st.warning("⚠️ Nenhum dado disponível para este período.")

# if uploaded_file:
#     df = load_data(uploaded_file)
#     display_tabs(df)


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
#     df.columns = df.columns.str.strip()  # Remove espaços extras nos nomes das colunas
#     df.rename(columns={"Energy (kWh)": "Energy"}, inplace=True)  # Renomeia a coluna
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para datetime
#     df["Day"] = df["Date"].dt.day  # Adiciona a coluna de dias do mês
#     df["Month"] = df["Date"].dt.month  # Adiciona a coluna de mês
#     df["Year"] = df["Date"].dt.year  # Adiciona a coluna do ano
#     return df

# def display_tabs(df):
#     st.subheader("📅 Histórico de Dados")
#     tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dia", "Semana", "Mês", "Ano", "Total"])

#     with tab3:
#         col1, col2 = st.columns(2)
#         with col1:
#             selected_month = st.selectbox("Selecione o mês", range(1, 13), format_func=lambda x: f"{x:02d}", key="month_selectbox")
#         with col2:
#             selected_year = st.selectbox("Selecione o ano", range(2023, 2026), key="year_selectbox")

#         # Filtrar os dados para o mês e ano selecionados
#         filtered_df = df[(df["Date"].dt.month == selected_month) & (df["Date"].dt.year == selected_year)]

#         if not filtered_df.empty:
#             daily_data = filtered_df.groupby("Day")["Energy"].sum().reset_index()
#             st.write(f"📈 Dados de geração de energia para {selected_month:02d}/{selected_year}")

#             # Gráfico de barras
#             fig_bar = px.bar(daily_data, x="Day", y="Energy", title="Geração de Energia por Dia",
#                              labels={"Day": "Dia", "Energy": "Geração de Energia (kWh)"},
#                              template="plotly_dark")
#             fig_bar.update_xaxes(type='category', tickmode='linear', dtick=1)  # Mostrar todos os dias
#             st.plotly_chart(fig_bar)

#             # Seleção de ano para o gráfico de calor
#             selected_year_heatmap = st.selectbox("Selecione o ano para o gráfico de calor", range(2023, 2026), key="year_heatmap_selectbox")

#             # Filtrar os dados para o ano selecionado
#             df_filtered = df[df["Date"].dt.year == selected_year_heatmap]

#             # Adicionar colunas de mês e dia
#             df_filtered["Month"] = df_filtered["Date"].dt.month
#             df_filtered["Day"] = df_filtered["Date"].dt.day

#             # Criar tabela dinâmica para o heatmap
#             heatmap_data = df_filtered.pivot_table(index="Month", columns="Day", values="Energy", aggfunc="sum", fill_value=0)

#             # Ajustar os rótulos do eixo y para mostrar o ano e o mês
#             heatmap_data.index = [f"{selected_year_heatmap}-{month}" for month in heatmap_data.index]

#             # Criar o gráfico de calor
#             fig_heatmap = px.imshow(
#                 heatmap_data,
#                 labels=dict(x="Dia", y="Mês", color="Geração de Energia (kWh)"),
#                 x=heatmap_data.columns,
#                 y=heatmap_data.index,
#                 title=f"Comparação de Produção Diária por Mês ({selected_year_heatmap})",
#                 color_continuous_scale="teal"
#             )

#             # Exibir o gráfico no Streamlit
#             st.plotly_chart(fig_heatmap)
#         else:
#             st.warning("⚠️ Nenhum dado disponível para este período.")

# if uploaded_file:
#     df = load_data(uploaded_file)
#     display_tabs(df)


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
#     df.columns = df.columns.str.strip()  # Remove espaços extras nos nomes das colunas
#     df.rename(columns={"Energy (kWh)": "Energy"}, inplace=True)  # Renomeia a coluna
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para datetime
#     df["Day"] = df["Date"].dt.day  # Adiciona a coluna de dias do mês
#     df["Month"] = df["Date"].dt.strftime('%Y-%m')  # Adiciona a coluna de mês-ano
#     df["Year"] = df["Date"].dt.year  # Adiciona a coluna do ano
#     return df

# def display_tabs(df):
#     st.subheader("📅 Histórico de Dados")
#     tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dia", "Semana", "Mês", "Ano", "Total"])

#     with tab3:
#         col1, col2 = st.columns(2)
#         with col1:
#             selected_month = st.selectbox("Selecione o mês", range(1, 13), format_func=lambda x: f"{x:02d}")
#         with col2:
#             selected_year = st.selectbox("Selecione o ano", range(2023, 2026))

#         # Filtrar os dados para o mês e ano selecionados
#         filtered_df = df[(df["Date"].dt.month == selected_month) & (df["Date"].dt.year == selected_year)]

#         if not filtered_df.empty:
#             daily_data = filtered_df.groupby("Day")["Energy"].sum().reset_index()
#             st.write(f"📈 Dados de geração de energia para {selected_month:02d}/{selected_year}")

#             # Gráfico de barras
#             fig_bar = px.bar(daily_data, x="Day", y="Energy", title="Geração de Energia por Dia",
#                              labels={"Day": "Dia", "Energy": "Geração de Energia (kWh)"},
#                              template="plotly_dark")
#             fig_bar.update_xaxes(type='category', tickmode='linear', dtick=1)  # Mostrar todos os dias
#             st.plotly_chart(fig_bar)

#             # Criar heatmap de produção diária ao longo dos meses do ano selecionado
#             heatmap_data = df[df["Year"] == selected_year].pivot_table(index="Month", columns="Day", values="Energy", aggfunc="sum", fill_value=0)
#             fig_heatmap = px.imshow(heatmap_data,
#                                     labels=dict(x="Dia", y="Mês", color="Geração de Energia (kWh)"),
#                                     x=heatmap_data.columns, y=heatmap_data.index,
#                                     title=f"Comparação de Produção Diária por Mês ({selected_year})",
#                                     color_continuous_scale="teal")
#             st.plotly_chart(fig_heatmap)
#         else:
#             st.warning("⚠️ Nenhum dado disponível para este período.")

# if uploaded_file:
#     df = load_data(uploaded_file)
#     display_tabs(df)


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("📤 Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df.columns = df.columns.str.strip()  # Remove espaços extras nos nomes das colunas
#     df.rename(columns={"Energy (kWh)": "Energy"}, inplace=True)  # Renomeia a coluna
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para datetime
#     df["Day"] = df["Date"].dt.day  # Adiciona a coluna de dias do mês
#     df["Month"] = df["Date"].dt.strftime('%Y-%m')  # Adiciona a coluna de mês-ano
#     df["Year"] = df["Date"].dt.year  # Adiciona a coluna do ano
#     return df

# def display_tabs(df):
#     st.subheader("📅 Histórico de Dados")
#     tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dia", "Semana", "Mês", "Ano", "Total"])

#     with tab3:
#         col1, col2 = st.columns(2)
#         with col1:
#             selected_month = st.selectbox("Selecione o mês", range(1, 13), format_func=lambda x: f"{x:02d}")
#         with col2:
#             selected_year = st.selectbox("Selecione o ano", range(2023, 2026))

#         # Filtrar os dados para o mês e ano selecionados
#         filtered_df = df[(df["Date"].dt.month == selected_month) & (df["Date"].dt.year == selected_year)]

#         if not filtered_df.empty:
#             daily_data = filtered_df.groupby("Day")["Energy"].sum().reset_index()
#             st.write(f"📈 Dados de geração de energia para {selected_month:02d}/{selected_year}")

#             # Gráfico de barras
#             fig_bar = px.bar(daily_data, x="Day", y="Energy", title="Geração de Energia por Dia",
#                              labels={"Day": "Dia", "Energy": "Geração de Energia (kWh)"},
#                              template="plotly_dark")
#             fig_bar.update_xaxes(type='category', tickmode='linear', dtick=1)  # Mostrar todos os dias
#             st.plotly_chart(fig_bar)

#             # Criar gráfico de quadrantes com ano/mês no eixo vertical e dias no eixo horizontal
#             quadrante_data = df[df["Year"] == selected_year].pivot_table(index="Month", columns="Day", values="Energy", aggfunc="sum", fill_value=0)
#             fig_quadrante = go.Figure()
#             for month in quadrante_data.index:
#                 fig_quadrante.add_trace(go.Scatter(x=quadrante_data.columns, y=[month]*len(quadrante_data.columns),
#                                                    mode='markers', marker=dict(size=quadrante_data.loc[month].values, color=quadrante_data.loc[month].values, colorscale='teal', showscale=True),
#                                                    name=month))
#             fig_quadrante.update_layout(title=f"Quadrante de Produção de Energia ({selected_year})",
#                                         xaxis_title="Dia",
#                                         yaxis_title="Mês",
#                                         template="plotly_dark",
#                                         xaxis=dict(tickmode='linear', dtick=1))  # Mostrar todos os valores no eixo X
#             st.plotly_chart(fig_quadrante)
#         else:
#             st.warning("⚠️ Nenhum dado disponível para este período.")

# if uploaded_file:
#     df = load_data(uploaded_file)
#     display_tabs(df)


import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# Título do aplicativo
st.title("📊 Dashboard de Geração de Energia")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("📤 Faça upload do arquivo CSV", type=["csv"])

@st.cache_data
def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()  # Remove espaços extras nos nomes das colunas
    df.rename(columns={"Energy (kWh)": "Energy"}, inplace=True)  # Renomeia a coluna
    df["Date"] = pd.to_datetime(df["Date"])  # Converter para datetime
    df["Day"] = df["Date"].dt.day  # Adiciona a coluna de dias do mês
    df["Month_Year"] = df["Date"].dt.strftime('%Y-%m')  # Adiciona a coluna Ano-Mês
    df["Year"] = df["Date"].dt.year  # Adiciona a coluna do ano
    return df

def display_tabs(df):
    st.subheader("📅 Histórico de Dados")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dia", "Semana", "Mês", "Ano", "Total"])

    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            selected_month = st.selectbox("Selecione o mês", range(1, 13), format_func=lambda x: f"{x:02d}")
        with col2:
            selected_year = st.selectbox("Selecione o ano", range(2023, 2026))

        # Filtrar os dados para o ano selecionado
        yearly_data = df[df["Year"] == selected_year]

        if not yearly_data.empty:
            daily_data = yearly_data.groupby("Day")["Energy"].sum().reset_index()
            st.write(f"📈 Dados de geração de energia para {selected_year}")

            # Gráfico de barras
            fig_bar = px.bar(daily_data, x="Day", y="Energy", title="Geração de Energia por Dia",
                             labels={"Day": "Dia", "Energy": "Geração de Energia (kWh)"},
                             template="plotly_dark")
            fig_bar.update_xaxes(type='category', tickmode='linear', dtick=1)  # Mostrar todos os dias
            st.plotly_chart(fig_bar)

            # Criar gráfico de quadrantes com ano/mês no eixo vertical e dias no eixo horizontal
            quadrante_data = yearly_data.pivot_table(index="Month_Year", columns="Day", values="Energy", aggfunc="sum", fill_value=0)
            fig_quadrante = go.Figure()
            for month in quadrante_data.index:
                fig_quadrante.add_trace(go.Scatter(x=quadrante_data.columns, y=[str(month)]*len(quadrante_data.columns),
                                                   mode='markers',
                                                   marker=dict(size=10, color=quadrante_data.loc[month].values, colorscale='teal', showscale=True),
                                                   text=quadrante_data.loc[month].values,
                                                   hoverinfo="text",
                                                   name=str(month)))
            fig_quadrante.update_layout(title=f"Quadrante de Produção de Energia ({selected_year})",
                                        xaxis_title="Dia",
                                        yaxis_title="Ano-Mês",
                                        template="plotly_dark",
                                        xaxis=dict(tickmode='linear', dtick=1),
                                        yaxis=dict(type='category'))  # Garantir que os valores do eixo Y sejam categóricos
            st.plotly_chart(fig_quadrante)
        else:
            st.warning("⚠️ Nenhum dado disponível para este período.")

if uploaded_file:
    df = load_data(uploaded_file)
    display_tabs(df)
