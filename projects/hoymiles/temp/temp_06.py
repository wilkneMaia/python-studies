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
#     df["Month_Year"] = df["Date"].dt.strftime('%Y-%m')  # Adiciona a coluna Ano-Mês
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

#         # Filtrar os dados para o ano selecionado
#         yearly_data = df[df["Year"] == selected_year]

#         if not yearly_data.empty:
#             daily_data = yearly_data.groupby("Day")["Energy"].sum().reset_index()
#             st.write(f"📈 Dados de geração de energia para {selected_year}")

#             # Gráfico de barras
#             fig_bar = px.bar(daily_data, x="Day", y="Energy", title="Geração de Energia por Dia",
#                              labels={"Day": "Dia", "Energy": "Geração de Energia (kWh)"},
#                              template="plotly_dark")
#             fig_bar.update_xaxes(type='category', tickmode='linear', dtick=1)  # Mostrar todos os dias
#             st.plotly_chart(fig_bar)

#             # Criar gráfico de quadrantes com ano/mês no eixo vertical e dias no eixo horizontal
#             quadrante_data = yearly_data.pivot_table(index="Month_Year", columns="Day", values="Energy", aggfunc="sum", fill_value=0)
#             fig_quadrante = go.Figure()
#             for month in quadrante_data.index:
#                 fig_quadrante.add_trace(go.Scatter(x=quadrante_data.columns, y=[str(month)]*len(quadrante_data.columns),
#                                                    mode='markers',
#                                                    marker=dict(size=10, color=quadrante_data.loc[month].values, colorscale='teal', showscale=True),
#                                                    text=quadrante_data.loc[month].values,
#                                                    hoverinfo="text",
#                                                    name=str(month)))
#             fig_quadrante.update_layout(title=f"Quadrante de Produção de Energia ({selected_year})",
#                                         xaxis_title="Dia",
#                                         yaxis_title="Ano-Mês",
#                                         template="plotly_dark",
#                                         xaxis=dict(tickmode='linear', dtick=1),
#                                         yaxis=dict(type='category'))  # Garantir que os valores do eixo Y sejam categóricos
#             st.plotly_chart(fig_quadrante)
#         else:
#             st.warning("⚠️ Nenhum dado disponível para este período.")

# if uploaded_file:
#     df = load_data(uploaded_file)
#     display_tabs(df)


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from numpy import polyfit

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
#     df["Month"] = df["Date"].dt.month  # Adiciona a coluna do mês
#     df["Month_Year"] = df["Date"].dt.strftime('%Y-%m')  # Adiciona a coluna Ano-Mês
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

#         # Filtrar os dados para o mês e ano selecionado
#         filtered_data = df[(df["Year"] == selected_year) & (df["Month"] == selected_month)]

#         if not filtered_data.empty:
#             daily_data = filtered_data.groupby("Day")["Energy"].sum().reset_index()
#             st.write(f"📈 Dados de geração de energia para {selected_year}-{selected_month:02d}")

#             # Calcular linha de tendência (regressão linear)
#             x = daily_data["Day"]
#             y = daily_data["Energy"]
#             slope, intercept = polyfit(x, y, 1)  # Regressão linear

#             # Plotando gráfico de barras e linha de tendência
#             fig_bar = px.bar(daily_data, x="Day", y="Energy", title="Geração de Energia por Dia",
#                             labels={"Day": "Dia", "Energy": "Geração de Energia (kWh)"},
#                             template="plotly_dark", color="Energy", color_continuous_scale="Blues")  # Usando uma paleta suave

#             # Ajustando o gráfico de barras para visual mais clean
#             fig_bar.update_traces(marker=dict(line=dict(width=0.5, color="black")), opacity=0.8)  # Borda nas barras e leve transparência

#             # Adicionando a linha de tendência
#             fig_bar.add_trace(go.Scatter(x=x, y=slope * x + intercept, mode='lines', name='Tendência',
#                                         line=dict(color='#ff5722', width=3, dash='solid')))  # Linha de tendência laranja

#             # Melhorando a visualização do eixo X e Y
#             fig_bar.update_layout(
#                 title=dict(
#                     text="Geração de Energia por Dia",  # Título mais direto
#                     x=0.5,  # Centralizar o título
#                     font=dict(size=18, color="#ffffff"),  # Tamanho e cor do título
#                 ),
#                 xaxis=dict(
#                     title="Dia",  # Título do eixo X
#                     showgrid=False,  # Retirar a grid para um visual mais clean
#                     tickmode='linear',
#                     ticks="outside",  # Ticks fora do gráfico para um visual mais limpo
#                     tickwidth=2,  # Largura dos ticks
#                     tickangle=45,  # Angulação dos ticks para melhor leitura
#                     tickfont=dict(color="#ffffff"),  # Cor dos ticks
#                 ),
#                 yaxis=dict(
#                     title="Geração de Energia (kWh)",  # Título do eixo Y
#                     showgrid=True,  # Manter a grid no eixo Y para referência
#                     zeroline=True,  # Linha no zero
#                     zerolinewidth=1,
#                     zerolinecolor="gray",
#                     tickfont=dict(color="#ffffff"),  # Cor dos ticks no eixo Y
#                 ),
#                 plot_bgcolor="#181818",  # Cor do fundo do gráfico igual ao dashboard
#                 paper_bgcolor="#181818",  # Fundo do gráfico e do papel (área fora do gráfico)
#                 margin=dict(l=40, r=40, t=40, b=40),  # Reduzir as margens para dar mais destaque ao gráfico
#             )

#             # Exibindo o gráfico
#             st.plotly_chart(fig_bar)

#             # Criar gráfico de quadrantes com ano/mês no eixo vertical e dias no eixo horizontal
#             quadrante_data = filtered_data.pivot_table(index="Month_Year", columns="Day", values="Energy", aggfunc="sum", fill_value=0)
#             fig_quadrante = go.Figure()

#             # Adicionar os pontos de quadrante
#             for month in quadrante_data.index:
#                 fig_quadrante.add_trace(go.Scatter(
#                     x=quadrante_data.columns,
#                     y=[str(month)] * len(quadrante_data.columns),
#                     mode='markers',
#                     marker=dict(
#                         size=10,
#                         color=quadrante_data.loc[month].values,
#                         colorscale='teal',  # Mudando para uma paleta mais moderna
#                         showscale=True,  # Para mostrar a escala de cores
#                         colorbar=dict(title="Energia (kWh)", tickvals=[0, 10, 20, 30], ticktext=["0", "10", "20", "30"])  # Ajuste da barra de cores
#                     ),
#                     text=quadrante_data.loc[month].values,
#                     hoverinfo="text",
#                     name=str(month),
#                 ))

#             # Ajustar layout para um estilo clean e moderno
#             fig_quadrante.update_layout(
#                 title=f"Quadrante de Produção de Energia ({selected_year})",
#                 title_font=dict(size=18, color="#ffffff"),  # Cor do título
#                 xaxis=dict(
#                     title="Dia",
#                     title_font=dict(size=14, color="#ffffff"),
#                     showgrid=False,  # Retirar grid para um visual mais limpo
#                     tickmode='linear',
#                     ticks="outside",
#                     tickwidth=2,
#                     tickangle=45,  # Melhor legibilidade dos ticks
#                     tickfont=dict(color="#ffffff"),  # Cor dos ticks
#                 ),
#                 yaxis=dict(
#                     title="Ano-Mês",
#                     title_font=dict(size=14, color="#ffffff"),
#                     showgrid=False,  # Retirar grid no eixo Y
#                     tickfont=dict(color="#ffffff"),
#                     type='category',  # Garantir que o eixo Y seja categórico
#                 ),
#                 plot_bgcolor="#181818",  # Fundo escuro, mantendo o tema
#                 paper_bgcolor="#181818",  # Cor do fundo geral
#                 margin=dict(l=40, r=40, t=40, b=40),  # Reduzir as margens para dar mais destaque
#                 colorway=["#007bff"],  # Cor única para os pontos, se necessário
#             )

#             st.plotly_chart(fig_quadrante)

#             # Gráfico de Linhas - Geração Acumulada de Energia
#             fig_line = px.line(daily_data, x="Day", y="Energy", title="Geração Acumulada de Energia por Dia",
#                             labels={"Day": "Dia", "Energy": "Geração Acumulada (kWh)"},
#                             template="plotly_dark")  # Usando o template dark para o fundo escuro

#             # Personalizando o gráfico para um aspecto mais moderno e limpo
#             fig_line.update_traces(
#                 mode='lines+markers',  # Mantém as linhas e os marcadores
#                 line=dict(color="#00bcd4", width=2),  # Cor da linha (azul claro)
#                 marker=dict(size=6, color="#ff5722", line=dict(width=1, color="white"))  # Cor dos marcadores e borda
#             )

#             # Ajustando o layout para ser mais clean
#             fig_line.update_layout(
#                 title=dict(
#                     text="Geração Acumulada de Energia por Dia",  # Título mais direto
#                     x=0.5,  # Centralizar o título
#                     font=dict(size=16, color="#ffffff"),  # Cor branca para o título
#                 ),
#                 xaxis=dict(
#                     title="Dia",  # Título do eixo X
#                     showgrid=False,  # Retirar a grade para um visual mais clean
#                     tickmode='linear',
#                     ticks="outside",  # Ticks fora do gráfico para um visual mais limpo
#                     tickwidth=2,  # Largura dos ticks
#                     tickangle=45,  # Angulação dos ticks para melhor leitura
#                     tickfont=dict(color="#ffffff"),  # Cor dos ticks
#                 ),
#                 yaxis=dict(
#                     title="Geração Acumulada (kWh)",  # Título do eixo Y
#                     showgrid=True,  # Manter a grid no eixo Y para referência
#                     zeroline=True,  # Linha no zero
#                     zerolinewidth=1,
#                     zerolinecolor="gray",
#                     tickfont=dict(color="#ffffff"),  # Cor dos ticks no eixo Y
#                 ),
#                 plot_bgcolor="#181818",  # Cor do fundo do gráfico igual ao dashboard
#                 paper_bgcolor="#181818",  # Fundo do gráfico e do papel (área fora do gráfico)
#                 margin=dict(l=40, r=40, t=40, b=40),  # Reduzir as margens para dar mais destaque ao gráfico
#             )

#             st.plotly_chart(fig_line)

#         else:
#             st.warning("⚠️ Nenhum dado disponível para este período.")

# if uploaded_file:
#     df = load_data(uploaded_file)
#     display_tabs(df)


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from numpy import polyfit

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Barra lateral para seleção do arquivo
# uploaded_file = st.sidebar.file_uploader("📤 Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     """Carrega e processa os dados do arquivo CSV"""
#     df = pd.read_csv(uploaded_file)
#     df.columns = df.columns.str.strip()  # Remove espaços extras nos nomes das colunas
#     df.rename(columns={"Energy (kWh)": "Energy"}, inplace=True)  # Renomeia a coluna
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para datetime
#     df["Day"] = df["Date"].dt.day  # Adiciona a coluna de dias do mês
#     df["Month"] = df["Date"].dt.month  # Adiciona a coluna do mês
#     df["Month_Year"] = df["Date"].dt.strftime('%Y-%m')  # Adiciona a coluna Ano-Mês
#     df["Year"] = df["Date"].dt.year  # Adiciona a coluna do ano
#     return df

# def display_tabs(df):
#     """Exibe as abas com gráficos baseados no filtro de mês e ano"""
#     st.subheader("📅 Histórico de Dados")
#     tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dia", "Semana", "Mês", "Ano", "Total"])

#     with tab3:
#         # Barra lateral para selecionar o mês e ano
#         with st.sidebar:
#             selected_month = st.selectbox("Selecione o mês", range(1, 13), format_func=lambda x: f"{x:02d}")
#             selected_year = st.selectbox("Selecione o ano", range(2023, 2026))

#         # Filtrar os dados para o mês e ano selecionado
#         filtered_data = df[(df["Year"] == selected_year) & (df["Month"] == selected_month)]

#         if not filtered_data.empty:
#             daily_data = filtered_data.groupby("Day")["Energy"].sum().reset_index()
#             st.write(f"📈 Dados de geração de energia para {selected_year}-{selected_month:02d}")

#             # Cálculo da linha de tendência (regressão linear)
#             x = daily_data["Day"]
#             y = daily_data["Energy"]
#             slope, intercept = polyfit(x, y, 1)  # Regressão linear

#             # Gráfico de barras com linha de tendência
#             fig_bar = px.bar(daily_data, x="Day", y="Energy", title="Geração de Energia por Dia",
#                              labels={"Day": "Dia", "Energy": "Geração de Energia (kWh)"},
#                              template="plotly_dark", color="Energy", color_continuous_scale="Blues")

#             # Personalizando o gráfico
#             fig_bar.update_traces(marker=dict(line=dict(width=0.5, color="black")), opacity=0.8)
#             fig_bar.add_trace(go.Scatter(x=x, y=slope * x + intercept, mode='lines', name='Tendência',
#                                         line=dict(color='#ff5722', width=3, dash='solid')))

#             # Ajustando layout
#             fig_bar.update_layout(
#                 title=dict(text="Geração de Energia por Dia", x=0.5, font=dict(size=22, color="white")),
#                 xaxis=dict(title="Dia", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2,
#                            tickangle=45, tickfont=dict(color="#ffffff")),
#                 yaxis=dict(title="Geração de Energia (kWh)", showgrid=True, zeroline=True, zerolinewidth=1,
#                            zerolinecolor="gray", tickfont=dict(color="#ffffff")),
#                 plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
#             )

#             # Exibindo o gráfico
#             st.plotly_chart(fig_bar)


#             # Criando gráfico de quadrantes com ano/mês no eixo vertical e dias no eixo horizontal
#             quadrante_data = filtered_data.pivot_table(index="Month_Year", columns="Day", values="Energy", aggfunc="sum", fill_value=0)
#             fig_quadrante = go.Figure()

#             for month in quadrante_data.index:
#                 fig_quadrante.add_trace(go.Scatter(
#                     x=quadrante_data.columns,
#                     y=[str(month)] * len(quadrante_data.columns),
#                     mode='markers',
#                     marker=dict(size=10, color=quadrante_data.loc[month].values, colorscale='teal', showscale=True,
#                                 colorbar=dict(title="Energia (kWh)", tickvals=[0, 10, 20, 30], ticktext=["0", "10", "20", "30"])),
#                     text=quadrante_data.loc[month].values,
#                     hoverinfo="text",
#                     name=str(month),
#                 ))

#             fig_quadrante.update_layout(
#                 title=f"Quadrante de Produção de Energia ({selected_year})",
#                 title_font=dict(size=18, color="#ffffff"),
#                 title_x=0.5,  # Centraliza horizontalmente
#                 title_y=0.95,  # Ajuste vertical se necessário (valor 0.95 está próximo do topo)
#                 xaxis=dict(title="Dia", title_font=dict(size=14, color="#ffffff"), showgrid=False, tickmode='linear',
#                         ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
#                 yaxis=dict(title="Ano-Mês", title_font=dict(size=14, color="#ffffff"), showgrid=False, tickfont=dict(color="#ffffff"),
#                         type='category'),
#                 plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40),
#                 colorway=["#007bff"]
#             )

#             st.plotly_chart(fig_quadrante)


#             # Gráfico de linhas de geração acumulada de energia
#             fig_line = px.line(daily_data, x="Day", y="Energy", title="Geração Acumulada de Energia por Dia",
#                                labels={"Day": "Dia", "Energy": "Geração Acumulada (kWh)"}, template="plotly_dark")

#             fig_line.update_traces(mode='lines+markers', line=dict(color="#00bcd4", width=2),
#                                    marker=dict(size=6, color="#ff5722", line=dict(width=1, color="white")))

#             fig_line.update_layout(
#                 title=dict(text="Geração Acumulada de Energia por Dia", x=0.5, font=dict(size=16, color="#ffffff")),
#                 xaxis=dict(title="Dia", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2,
#                            tickangle=45, tickfont=dict(color="#ffffff")),
#                 yaxis=dict(title="Geração Acumulada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1,
#                            zerolinecolor="gray", tickfont=dict(color="#ffffff")),
#                 plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
#             )

#             st.plotly_chart(fig_line)


#             # Indicadores de Performance com ícones e cores
#             total_energy = daily_data["Energy"].sum()
#             avg_energy = daily_data["Energy"].mean()
#             max_energy = daily_data["Energy"].max()
#             min_energy = daily_data["Energy"].min()
#             std_dev_energy = daily_data["Energy"].std()

#             # Supondo que a eficiência ideal de geração seja 90% da capacidade máxima (você pode ajustar essa lógica conforme necessário)
#             ideal_energy = total_energy * 0.9
#             efficiency = (total_energy / ideal_energy) * 100 if ideal_energy > 0 else 0

#             # Exibindo indicadores com ícones e cores em colunas menores
#             col1, col2, col3, col4, col5, col6 = st.columns(6)

#             with col1:
#                 st.metric(
#                     label="🔋 Total de Energia Gerada",
#                     value=f"{total_energy:,.2f} kWh",  # Formatação para números com vírgula e 2 casas decimais
#                     delta=f"+{total_energy - avg_energy:,.2f} kWh",  # Diferença em relação à média
#                     delta_color="inverse",  # Inverte a cor do delta (positivo em verde, negativo em vermelho)
#                     help="Energia total gerada no período selecionado"
#                 )

#             with col2:
#                 st.metric(
#                     label="📊 Média de Energia Diária",
#                     value=f"{avg_energy:,.2f} kWh",  # Formatação para números com vírgula e 2 casas decimais
#                     delta=None,  # Nenhuma diferença a ser mostrada
#                     help="Média diária de energia gerada no período selecionado"
#                 )

#             with col3:
#                 st.metric(
#                     label="⚡ Máxima de Energia Diária",
#                     value=f"{max_energy:,.2f} kWh",  # Máxima energia gerada em um único dia
#                     delta=None,
#                     help="Maior valor de energia gerada em um único dia no período"
#                 )

#             with col4:
#                 st.metric(
#                     label="📉 Mínima de Energia Diária",
#                     value=f"{min_energy:,.2f} kWh",  # Mínima energia gerada em um único dia
#                     delta=None,
#                     help="Menor valor de energia gerada em um único dia no período"
#                 )

#             with col5:
#                 st.metric(
#                     label="📊 Desvio Padrão",
#                     value=f"{std_dev_energy:,.2f} kWh",  # Desvio padrão da geração de energia
#                     delta=None,
#                     help="Mede a variabilidade da geração de energia no período"
#                 )

#             with col6:
#                 st.metric(
#                     label="💡 Eficiência (%)",
#                     value=f"{efficiency:,.2f}%",  # Eficiência percentual em relação à meta ideal
#                     delta=None,
#                     help="Eficiência da geração de energia em relação à meta ideal de 90%"
#                 )



#         else:
#             st.warning("⚠️ Nenhum dado disponível para este período.")

# if uploaded_file:
#     df = load_data(uploaded_file)
#     display_tabs(df)


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from numpy import polyfit

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Barra lateral para seleção do arquivo
# uploaded_file = st.sidebar.file_uploader("📤 Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     """Carrega e processa os dados do arquivo CSV"""
#     df = pd.read_csv(uploaded_file)
#     df.columns = df.columns.str.strip()  # Remove espaços extras nos nomes das colunas
#     df.rename(columns={"Energy (kWh)": "Energy"}, inplace=True)  # Renomeia a coluna
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para datetime
#     df["Day"] = df["Date"].dt.day  # Adiciona a coluna de dias do mês
#     df["Month"] = df["Date"].dt.month  # Adiciona a coluna do mês
#     df["Month_Year"] = df["Date"].dt.strftime('%Y-%m')  # Adiciona a coluna Ano-Mês
#     df["Year"] = df["Date"].dt.year  # Adiciona a coluna do ano
#     return df

# # Função para exibir gráfico de barras com linha de tendência
# def plot_energy_bar_chart(daily_data, x, slope, intercept):
#     fig_bar = px.bar(daily_data, x="Day", y="Energy", title="Geração de Energia por Dia",
#                      labels={"Day": "Dia", "Energy": "Geração de Energia (kWh)"},
#                      template="plotly_dark", color="Energy", color_continuous_scale="Blues")

#     # Personalizando o gráfico
#     fig_bar.update_traces(marker=dict(line=dict(width=0.5, color="black")), opacity=0.8)
#     fig_bar.add_trace(go.Scatter(x=x, y=slope * x + intercept, mode='lines', name='Tendência',
#                                 line=dict(color='#ff5722', width=3, dash='solid')))

#     # Ajustando layout
#     fig_bar.update_layout(
#         title=dict(text="Geração de Energia por Dia", x=0.5, font=dict(size=22, color="white")),
#         xaxis=dict(title="Dia", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2,
#                    tickangle=45, tickfont=dict(color="#ffffff")),
#         yaxis=dict(title="Geração de Energia (kWh)", showgrid=True, zeroline=True, zerolinewidth=1,
#                    zerolinecolor="gray", tickfont=dict(color="#ffffff")),
#         plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
#     )

#     st.plotly_chart(fig_bar)

# # Função para exibir gráfico de quadrantes
# def plot_quadrant_graph(filtered_data, selected_year):
#     quadrante_data = filtered_data.pivot_table(index="Month_Year", columns="Day", values="Energy", aggfunc="sum", fill_value=0)
#     fig_quadrante = go.Figure()

#     for month in quadrante_data.index:
#         fig_quadrante.add_trace(go.Scatter(
#             x=quadrante_data.columns,
#             y=[str(month)] * len(quadrante_data.columns),
#             mode='markers',
#             marker=dict(size=10, color=quadrante_data.loc[month].values, colorscale='teal', showscale=True,
#                         colorbar=dict(title="Energia (kWh)", tickvals=[0, 10, 20, 30], ticktext=["0", "10", "20", "30"])),
#             text=quadrante_data.loc[month].values,
#             hoverinfo="text",
#             name=str(month),
#         ))

#     fig_quadrante.update_layout(
#         title=f"Quadrante de Produção de Energia ({selected_year})",
#         title_font=dict(size=18, color="#ffffff"),
#         title_x=0.5,  # Centraliza horizontalmente
#         title_y=0.95,  # Ajuste vertical se necessário
#         xaxis=dict(title="Dia", title_font=dict(size=14, color="#ffffff"), showgrid=False, tickmode='linear',
#                    ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
#         yaxis=dict(title="Ano-Mês", title_font=dict(size=14, color="#ffffff"), showgrid=False, tickfont=dict(color="#ffffff"),
#                    type='category'),
#         plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40),
#         colorway=["#007bff"]
#     )

#     st.plotly_chart(fig_quadrante)

# # Função para exibir gráfico de linha acumulada
# def plot_cumulative_energy_graph(daily_data):
#     fig_line = px.line(daily_data, x="Day", y="Energy", title="Geração Acumulada de Energia por Dia",
#                        labels={"Day": "Dia", "Energy": "Geração Acumulada (kWh)"}, template="plotly_dark")

#     fig_line.update_traces(mode='lines+markers', line=dict(color="#00bcd4", width=2),
#                            marker=dict(size=6, color="#ff5722", line=dict(width=1, color="white")))

#     fig_line.update_layout(
#         title=dict(text="Geração Acumulada de Energia por Dia", x=0.5, font=dict(size=16, color="#ffffff")),
#         xaxis=dict(title="Dia", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2,
#                    tickangle=45, tickfont=dict(color="#ffffff")),
#         yaxis=dict(title="Geração Acumulada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1,
#                    zerolinecolor="gray", tickfont=dict(color="#ffffff")),
#         plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
#     )

#     st.plotly_chart(fig_line)

# # Função para exibir indicadores de performance
# def display_performance_indicators(daily_data):
#     total_energy = daily_data["Energy"].sum()
#     avg_energy = daily_data["Energy"].mean()
#     max_energy = daily_data["Energy"].max()
#     min_energy = daily_data["Energy"].min()
#     std_dev_energy = daily_data["Energy"].std()

#     # Supondo que a eficiência ideal de geração seja 90% da capacidade máxima (você pode ajustar essa lógica conforme necessário)
#     ideal_energy = total_energy * 0.9
#     efficiency = (total_energy / ideal_energy) * 100 if ideal_energy > 0 else 0

#     # Exibindo indicadores com ícones e cores em colunas menores
#     col1, col2, col3, col4, col5, col6 = st.columns(6)

#     with col1:
#         st.metric(
#             label="🔋 Total de Energia Gerada",
#             value=f"{total_energy:,.2f} kWh",
#             delta=f"+{total_energy - avg_energy:,.2f} kWh",
#             delta_color="inverse",
#             help="Energia total gerada no período selecionado"
#         )

#     with col2:
#         st.metric(
#             label="📊 Média de Energia Diária",
#             value=f"{avg_energy:,.2f} kWh",
#             delta=None,
#             help="Média diária de energia gerada no período selecionado"
#         )

#     with col3:
#         st.metric(
#             label="⚡ Máxima de Energia Diária",
#             value=f"{max_energy:,.2f} kWh",
#             delta=None,
#             help="Maior valor de energia gerada em um único dia no período"
#         )

#     with col4:
#         st.metric(
#             label="📉 Mínima de Energia Diária",
#             value=f"{min_energy:,.2f} kWh",
#             delta=None,
#             help="Menor valor de energia gerada em um único dia no período"
#         )

#     with col5:
#         st.metric(
#             label="📊 Desvio Padrão",
#             value=f"{std_dev_energy:,.2f} kWh",
#             delta=None,
#             help="Mede a variabilidade da geração de energia no período"
#         )

#     with col6:
#         st.metric(
#             label="💡 Eficiência (%)",
#             value=f"{efficiency:,.2f}%",
#             delta=None,
#             help="Eficiência da geração de energia em relação à meta ideal de 90%"
#         )

# # Função principal para exibir os gráficos
# def display_tabs(df):
#     """Exibe as abas com gráficos baseados no filtro de mês e ano"""
#     st.subheader("📅 Histórico de Dados")

#     # Filtros na barra lateral para selecionar o período
#     filter_option = st.sidebar.radio("Selecione a visualização", ["Dia", "Semana", "Mês", "Ano", "Total"])

#     # Barra lateral para selecionar o mês e ano (se for Mês)
#     if filter_option == "Mês":
#         # Organizando mês e ano na mesma linha com st.columns()
#         col1, col2 = st.sidebar.columns(2)

#         with col1:
#             selected_month = st.selectbox("Selecione o mês", range(1, 13), format_func=lambda x: f"{x:02d}")
#         with col2:
#             selected_year = st.selectbox("Selecione o ano", range(2023, 2026))

#         filtered_data = df[(df["Year"] == selected_year) & (df["Month"] == selected_month)]

#         if not filtered_data.empty:
#             daily_data = filtered_data.groupby("Day")["Energy"].sum().reset_index()
#             st.write(f"📈 Dados de geração de energia para {selected_year}-{selected_month:02d}")

#             # Exibindo gráficos
#             x = daily_data["Day"]
#             y = daily_data["Energy"]
#             slope, intercept = polyfit(x, y, 1)

#             plot_energy_bar_chart(daily_data, x, slope, intercept)
#             plot_quadrant_graph(filtered_data, selected_year)
#             plot_cumulative_energy_graph(daily_data)
#             display_performance_indicators(daily_data)

#         else:
#             st.warning("⚠️ Nenhum dado disponível para este período.")

# # Função para carregar os dados e exibir gráficos
# if uploaded_file:
#     df = load_data(uploaded_file)
#     display_tabs(df)
