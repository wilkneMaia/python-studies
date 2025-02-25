# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data

#     # Seleção de intervalo de datas
#     st.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date, key="date_selector")

#     df_filtered = df.copy()

#     # Print para depuração
#     st.write("### Dados filtrados:")
#     st.write(df_filtered.head())


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date, key="date_selector")

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect("Escolha os microinversores", microinversores, default=microinversores)

#     df_filtered = df.copy()

#     # Print para depuração
#     st.write("### Dados filtrados:")
#     st.write(df_filtered.head())


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date, key="date_selector")

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect("Escolha os microinversores", microinversores, default=microinversores)

#     # Filtrando os dados com base na seleção
#     df_filtered = df[(df["Date"].dt.date >= date_range[0]) & (df["Date"].dt.date <= date_range[1]) & (df["Microinversor"].isin(selected_microinversores))]

#     # Print para depuração
#     st.write("### Dados filtrados:")
#     st.write(df_filtered.head())

#     # Criando o gráfico de geração de energia por Microinversor ao longo do tempo
#     if not df_filtered.empty:
#         st.subheader("📊 Geração de Energia ao longo do tempo")
#         fig = px.line(
#             df_filtered,
#             x="Date",
#             y="Energy (kWh)",
#             color="Microinversor",
#             title="Geração de Energia por Microinversor",
#             labels={"Energy (kWh)": "Energia (kWh)", "Date": "Data"},
#             markers=True
#         )
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.warning("Nenhum dado disponível para os filtros selecionados.")


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date, key="date_selector")

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect("Escolha os microinversores", microinversores, default=microinversores)

#     # Filtrando os dados com base na seleção
#     df_filtered = df[(df["Date"].dt.date >= date_range[0]) & (df["Date"].dt.date <= date_range[1]) & (df["Microinversor"].isin(selected_microinversores))]

#     # Print para depuração
#     st.write("### Dados filtrados:")
#     st.write(df_filtered.head())

#     # Criando visualização estilo cards
#     if not df_filtered.empty:
#         st.subheader(f"⚡ Geração de Energia - {date_range}")
#         cols = st.columns(min(20, len(df_filtered)))  # Ajusta dinamicamente o número de colunas

#         for i, (index, row) in enumerate(df_filtered.iterrows()):
#             with cols[i % len(cols)]:
#                 fig = go.Figure(go.Indicator(
#                     mode="number",
#                     value=row["Energy (kWh)"],
#                     title={"text": f"{row['Microinversor']}<br><span style='font-size:0.8em;color:gray;'>{row['SN']} - {row['Port']}</span>"},
#                     number={"suffix": " W"}
#                 ))
#                 st.plotly_chart(fig, use_container_width=True, key=f"chart_{index}")

#     # Criando o gráfico de geração de energia por Microinversor ao longo do tempo
#     if not df_filtered.empty:
#         st.subheader("📊 Geração de Energia ao longo do tempo")
#         fig = px.line(
#             df_filtered,
#             x="Date",
#             y="Energy (kWh)",
#             color="Microinversor",
#             title="Geração de Energia por Microinversor",
#             labels={"Energy (kWh)": "Energia (kWh)", "Date": "Data"},
#             markers=True
#         )
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.warning("Nenhum dado disponível para os filtros selecionados.")


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date, key="date_selector")

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect("Escolha os microinversores", microinversores, default=microinversores)

#     # Filtrando os dados com base na seleção
#     df_filtered = df[(df["Date"].dt.date >= date_range[0]) & (df["Date"].dt.date <= date_range[1]) & (df["Microinversor"].isin(selected_microinversores))]

#     # Print para depuração
#     st.write("### Dados filtrados:")
#     st.write(df_filtered.head())

#     # Criando visualização estilo cards mais limpos e mostrando apenas os 3 primeiros por Microinversor
#     if not df_filtered.empty:
#         st.subheader(f"⚡ Geração de Energia - {date_range}")
#         df_grouped = df_filtered.groupby("Microinversor").head(3)  # Seleciona apenas 3 entradas por microinversor
#         cols = st.columns(3)  # Apenas 3 colunas para os cards

#         for i, (index, row) in enumerate(df_grouped.iterrows()):
#             with cols[i % 3]:
#                 st.metric(label=f"{row['Microinversor']} - Port {row['Port']}", value=f"{row['Energy (kWh)']} kWh")

#     # Criando o gráfico de geração de energia por Microinversor ao longo do tempo
#     if not df_filtered.empty:
#         st.subheader("📊 Geração de Energia ao longo do tempo")
#         fig = px.line(
#             df_filtered,
#             x="Date",
#             y="Energy (kWh)",
#             color="Microinversor",
#             title="Geração de Energia por Microinversor",
#             labels={"Energy (kWh)": "Energia (kWh)", "Date": "Data"},
#             markers=True
#         )
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.warning("Nenhum dado disponível para os filtros selecionados.")


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date, key="date_selector")

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect("Escolha os microinversores", microinversores, default=microinversores)

#     # Filtrando os dados com base na seleção
#     df_filtered = df[(df["Date"].dt.date >= date_range[0]) & (df["Date"].dt.date <= date_range[1]) & (df["Microinversor"].isin(selected_microinversores))]

#     # Print para depuração
#     st.write("### Dados filtrados:")
#     st.write(df_filtered.head())

#     # Criando visualização estilo cards mais estilizados e mostrando apenas os 3 primeiros por Microinversor
#     if not df_filtered.empty:
#         st.subheader(f"⚡ Geração de Energia - {date_range}")
#         df_grouped = df_filtered.groupby("Microinversor").head(3)  # Seleciona apenas 3 entradas por microinversor
#         cols = st.columns(3)  # Apenas 3 colunas para os cards

#         for i, (index, row) in enumerate(df_grouped.iterrows()):
#             with cols[i % 3]:
#                 st.markdown(
#                     f"""
#                     <div style="padding: 10px; border-radius: 10px; background-color: #f0f2f6; text-align: center; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
#                         <h4 style="color: #333;">{row['Microinversor']}</h4>
#                         <p style="font-size: 18px; color: #666;">Port {row['Port']}</p>
#                         <h2 style="color: #007BFF;">{row['Energy (kWh)']} kWh</h2>
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )

#     # Criando o gráfico de geração de energia por Microinversor ao longo do tempo
#     if not df_filtered.empty:
#         st.subheader("📊 Geração de Energia ao longo do tempo")
#         fig = px.line(
#             df_filtered,
#             x="Date",
#             y="Energy (kWh)",
#             color="Microinversor",
#             title="Geração de Energia por Microinversor",
#             labels={"Energy (kWh)": "Energia (kWh)", "Date": "Data"},
#             markers=True
#         )
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.warning("Nenhum dado disponível para os filtros selecionados.")


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date, key="date_selector")

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect("Escolha os microinversores", microinversores, default=microinversores)

#     # Filtrando os dados com base na seleção
#     df_filtered = df[(df["Date"].dt.date >= date_range[0]) & (df["Date"].dt.date <= date_range[1]) & (df["Microinversor"].isin(selected_microinversores))]


#     # Criando o gráfico de geração de energia por Microinversor ao longo do tempo
#     if not df_filtered.empty:
#         st.subheader("📊 Geração de Energia ao longo do tempo")
#         fig = px.line(
#             df_filtered,
#             x="Date",
#             y="Energy (kWh)",
#             color="Microinversor",
#             title="Geração de Energia por Microinversor",
#             labels={"Energy (kWh)": "Energia (kWh)", "Date": "Data"},
#             markers=True
#         )
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.warning("Nenhum dado disponível para os filtros selecionados.")


# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input(
#         "Selecione a data ou intervalo", [min_date, max_date],
#         min_value=min_date, max_value=max_date, key="date_selector"
#     )

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect(
#         "Escolha os microinversores", microinversores, default=microinversores
#     )

#     # Filtrando os dados com base na seleção
#     df_filtered = df[
#         (df["Date"].dt.date >= date_range[0]) &
#         (df["Date"].dt.date <= date_range[1]) &
#         (df["Microinversor"].isin(selected_microinversores))
#     ]

#     # Criar gráficos por Microinversor
#     st.subheader("🔍 Geração de Energia por Microinversor")
#     for micro in selected_microinversores:
#         df_micro = df_filtered[df_filtered["Microinversor"] == micro]
#         if not df_micro.empty:
#             fig = px.bar(
#                 df_micro, x="Date", y="Energy (kWh)", title=f"Microinversor {micro}",
#                 labels={"Energy (kWh)": "Energia Gerada (kWh)", "Date": "Data"}
#             )
#             st.plotly_chart(fig, use_container_width=True)


# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input(
#         "Selecione a data ou intervalo", [min_date, max_date],
#         min_value=min_date, max_value=max_date, key="date_selector"
#     )

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect(
#         "Escolha os microinversores", microinversores, default=microinversores
#     )

#     # Filtrando os dados com base na seleção
#     df_filtered = df[
#         (df["Date"].dt.date >= date_range[0]) &
#         (df["Date"].dt.date <= date_range[1]) &
#         (df["Microinversor"].isin(selected_microinversores))
#     ]

#     # Agrupar dados por Microinversor e Data, somando a energia por Port
#     df_grouped = df_filtered.groupby(["Date", "Microinversor"])['Energy (kWh)'].sum().reset_index()

#     # Criar gráfico de barras empilhadas por Microinversor
#     st.subheader("🔍 Geração de Energia por Microinversor (Soma dos Ports)")
#     fig = px.bar(
#         df_grouped, x="Date", y="Energy (kWh)", color="Microinversor",
#         title="Energia Gerada por Microinversor ao Longo do Tempo",
#         labels={"Energy (kWh)": "Energia Gerada (kWh)", "Date": "Data"},
#         barmode='stack'
#     )
#     st.plotly_chart(fig, use_container_width=True)


# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input(
#         "Selecione a data ou intervalo", [min_date, max_date],
#         min_value=min_date, max_value=max_date, key="date_selector"
#     )

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect(
#         "Escolha os microinversores", microinversores, default=microinversores
#     )

#     # Filtrando os dados com base na seleção
#     df_filtered = df[
#         (df["Date"].dt.date >= date_range[0]) &
#         (df["Date"].dt.date <= date_range[1]) &
#         (df["Microinversor"].isin(selected_microinversores))
#     ]

#     # Agrupar dados por Microinversor, somando a energia total
#     df_grouped = df_filtered.groupby("Microinversor")["Energy (kWh)"].sum().reset_index()

#     # Criar gráfico de barras onde cada barra representa um inversor com a soma da energia
#     st.subheader("🔍 Energia Total por Microinversor")
#     fig = px.bar(
#         df_grouped, x="Microinversor", y="Energy (kWh)", color="Microinversor",
#         title="Energia Gerada por Microinversor",
#         labels={"Energy (kWh)": "Energia Gerada (kWh)", "Microinversor": "Microinversor"},
#     )
#     st.plotly_chart(fig, use_container_width=True)


# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input(
#         "Selecione a data ou intervalo", [min_date, max_date],
#         min_value=min_date, max_value=max_date, key="date_selector"
#     )

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect(
#         "Escolha os microinversores", microinversores, default=microinversores
#     )

#     # Filtrando os dados com base na seleção
#     df_filtered = df[
#         (df["Date"].dt.date >= date_range[0]) &
#         (df["Date"].dt.date <= date_range[1]) &
#         (df["Microinversor"].isin(selected_microinversores))
#     ]

#     # Agrupar dados por Microinversor, somando a energia total
#     df_grouped = df_filtered.groupby("Microinversor")["Energy (kWh)"].sum().reset_index()

#     # Criar gráfico de barras personalizado
#     st.subheader("🔍 Energia Total por Microinversor")
#     fig = px.bar(
#         df_grouped, x="Microinversor", y="Energy (kWh)", color="Microinversor",
#         title="Energia Gerada por Microinversor",
#         labels={"Energy (kWh)": "Energia Gerada (kWh)", "Microinversor": "Microinversor"},
#         text_auto=True  # Exibir valores dentro das barras
#     )
#     fig.update_traces(marker=dict(line=dict(width=2, color='black')))
#     fig.update_layout(
#         plot_bgcolor="#222",  # Fundo escuro
#         paper_bgcolor="#222",  # Fundo escuro
#         font=dict(color="white"),
#         bargap=0.1,  # Ajustar espaçamento entre barras
#         uniformtext_minsize=12,  # Tamanho mínimo do texto
#         uniformtext_mode='hide'  # Ocultar texto se ficar muito pequeno
#     )
#     st.plotly_chart(fig, use_container_width=True)


# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input(
#         "Selecione a data ou intervalo", [min_date, max_date],
#         min_value=min_date, max_value=max_date, key="date_selector"
#     )

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect(
#         "Escolha os microinversores", microinversores, default=microinversores
#     )

#     # Filtrando os dados com base na seleção
#     df_filtered = df[
#         (df["Date"].dt.date >= date_range[0]) &
#         (df["Date"].dt.date <= date_range[1]) &
#         (df["Microinversor"].isin(selected_microinversores))
#     ]

#     # Agrupar dados por Microinversor, somando a energia total
#     df_grouped = df_filtered.groupby("Microinversor")["Energy (kWh)"].sum().reset_index()

#     # Calcular percentual em relação ao maior valor
#     max_value = df_grouped["Energy (kWh)"].max()
#     df_grouped["Percentage"] = (df_grouped["Energy (kWh)"] / max_value) * 100 if max_value > 0 else 0

#     # Criar gráfico de barras customizado
#     st.subheader("🔍 Energia Total por Microinversor")
#     fig = go.Figure()

#     for _, row in df_grouped.iterrows():
#         fill_color = "#008CFF" if row["Energy (kWh)"] > 0 else "rgba(255, 255, 255, 0)"  # Azul se houver energia, transparente se for 0
#         fig.add_trace(go.Bar(
#             x=[row["Microinversor"]],
#             y=[100],
#             marker=dict(color="black"),
#             opacity=0.3,
#             showlegend=False
#         ))
#         fig.add_trace(go.Bar(
#             x=[row["Microinversor"]],
#             y=[row["Percentage"]],
#             text=f"{row['Energy (kWh)']:.2f} kWh" if row["Energy (kWh)"] > 0 else "0 kWh",
#             textposition="inside",
#             marker=dict(color=fill_color),
#             name=row["Microinversor"]
#         ))

#     fig.update_layout(
#         barmode="overlay",
#         plot_bgcolor="#222",
#         paper_bgcolor="#222",
#         font=dict(color="white"),
#         yaxis=dict(title="% da Energia Máxima", range=[0, 110], showgrid=False),
#         xaxis=dict(title="Microinversor", showgrid=False),
#     )

#     st.plotly_chart(fig, use_container_width=True)


# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input(
#         "Selecione a data ou intervalo", [min_date, max_date],
#         min_value=min_date, max_value=max_date, key="date_selector"
#     )

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect(
#         "Escolha os microinversores", microinversores, default=microinversores
#     )

#     # Filtrando os dados com base na seleção
#     df_filtered = df[
#         (df["Date"].dt.date >= date_range[0]) &
#         (df["Date"].dt.date <= date_range[1]) &
#         (df["Microinversor"].isin(selected_microinversores))
#     ]

#     # Agrupar dados por Microinversor, somando a energia total
#     df_grouped = df_filtered.groupby("Microinversor")["Energy (kWh)"].sum().reset_index()

#     # Definir a altura máxima com base no maior valor da lista selecionada
#     max_value = df_grouped["Energy (kWh)"].max()

#     # Criar gráfico de barras customizado
#     st.subheader("🔍 Energia Total por Microinversor")
#     fig = go.Figure()

#     for _, row in df_grouped.iterrows():
#         fill_color = "#008CFF" if row["Energy (kWh)"] > 0 else "rgba(255, 255, 255, 0)"  # Azul se houver energia, transparente se for 0
#         fig.add_trace(go.Bar(
#             x=[row["Microinversor"]],
#             y=[max_value],
#             marker=dict(color="black"),
#             opacity=0.3,
#             showlegend=False
#         ))
#         fig.add_trace(go.Bar(
#             x=[row["Microinversor"]],
#             y=[row["Energy (kWh)"]],
#             text=f"{row['Energy (kWh)']:.2f} kWh" if row["Energy (kWh)"] > 0 else "0 kWh",
#             textposition="inside",
#             marker=dict(color=fill_color),
#             name=row["Microinversor"]
#         ))

#     fig.update_layout(
#         barmode="overlay",
#         plot_bgcolor="#222",
#         paper_bgcolor="#222",
#         font=dict(color="white"),
#         yaxis=dict(title="Energia Gerada (kWh)", range=[0, max_value * 1.1], showgrid=False),
#         xaxis=dict(title="Microinversor", showgrid=False),
#     )

#     st.plotly_chart(fig, use_container_width=True)


# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input(
#         "Selecione a data ou intervalo", [min_date, max_date],
#         min_value=min_date, max_value=max_date, key="date_selector"
#     )

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect(
#         "Escolha os microinversores", microinversores, default=microinversores
#     )

#     # Filtrando os dados com base na seleção
#     df_filtered = df[
#         (df["Date"].dt.date >= date_range[0]) &
#         (df["Date"].dt.date <= date_range[1]) &
#         (df["Microinversor"].isin(selected_microinversores))
#     ]

#     # Agrupar dados por Microinversor, somando a energia total
#     df_grouped = df_filtered.groupby("Microinversor")["Energy (kWh)"].sum().reset_index()

#     # Definir a altura máxima com base no maior valor da lista selecionada
#     max_value = df_grouped["Energy (kWh)"].max()
#     if max_value == 0:
#         max_value = 1  # Evita problemas no eixo Y

#     # Criar gráfico de barras customizado
#     st.subheader("🔍 Energia Total por Microinversor")
#     fig = go.Figure()

#     for _, row in df_grouped.iterrows():
#         fill_color = "#008CFF" if row["Energy (kWh)"] > 0 else "#444444"  # Azul se houver energia, cinza se for 0
#         text_color = "white" if row["Energy (kWh)"] > 0 else "#BBBBBB"
#         fig.add_trace(go.Bar(
#             x=[row["Microinversor"]],
#             y=[max_value],
#             marker=dict(color="black"),
#             opacity=0.3,
#             showlegend=False
#         ))
#         fig.add_trace(go.Bar(
#             x=[row["Microinversor"]],
#             y=[row["Energy (kWh)"]],
#             text=f"{row['Energy (kWh)']:.2f} kWh",
#             textposition="auto",
#             marker=dict(color=fill_color),
#             name=row["Microinversor"],
#             textfont=dict(color=text_color)
#         ))

#     # Adicionar linhas horizontais nos intervalos das barras
#     for i in range(1, 11):  # 10 intervalos
#         fig.add_shape(
#             go.layout.Shape(
#                 type="line",
#                 x0=-0.5, x1=len(df_grouped["Microinversor"]) - 0.5,
#                 y0=(max_value / 10) * i, y1=(max_value / 10) * i,
#                 line=dict(color="white", width=1, dash="dot")
#             )
#         )

#     fig.update_layout(
#         barmode="overlay",
#         plot_bgcolor="#222",
#         paper_bgcolor="#222",
#         font=dict(color="white"),
#         yaxis=dict(title="Energia Gerada (kWh)", range=[0, max_value * 1.1], showgrid=False),
#         xaxis=dict(title="Microinversor", showgrid=False),
#     )

#     st.plotly_chart(fig, use_container_width=True)


# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input(
#         "Selecione a data ou intervalo", [min_date, max_date],
#         min_value=min_date, max_value=max_date, key="date_selector"
#     )

#     # Ajustar seleção única de data para um intervalo válido
#     if isinstance(date_range, tuple) or isinstance(date_range, list):
#         start_date, end_date = date_range[0], date_range[-1]
#     else:
#         start_date, end_date = date_range, date_range

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect(
#         "Escolha os microinversores", microinversores, default=microinversores
#     )

#     # Filtrando os dados com base na seleção
#     df_filtered = df[
#         (df["Date"].dt.date >= start_date) &
#         (df["Date"].dt.date <= end_date) &
#         (df["Microinversor"].isin(selected_microinversores))
#     ]

#     # Agrupar dados por Microinversor, somando a energia total
#     df_grouped = df_filtered.groupby("Microinversor")["Energy (kWh)"].sum().reset_index()

#     # Definir a altura máxima com base no maior valor da lista selecionada
#     max_value = df_grouped["Energy (kWh)"].max()
#     if max_value == 0:
#         max_value = 1  # Evita problemas no eixo Y

#     # Criar gráfico de barras customizado
#     st.subheader("🔍 Energia Total por Microinversor")
#     fig = go.Figure()

#     for _, row in df_grouped.iterrows():
#         fill_color = "#008CFF" if row["Energy (kWh)"] > 0 else "#444444"  # Azul se houver energia, cinza se for 0
#         text_color = "white" if row["Energy (kWh)"] > 0 else "#BBBBBB"
#         fig.add_trace(go.Bar(
#             x=[row["Microinversor"]],
#             y=[max_value],
#             marker=dict(color="black"),
#             opacity=0.3,
#             showlegend=False
#         ))
#         fig.add_trace(go.Bar(
#             x=[row["Microinversor"]],
#             y=[row["Energy (kWh)"]],
#             text=f"{row['Energy (kWh)']:.2f} kWh",
#             textposition="auto",
#             marker=dict(color=fill_color),
#             name=row["Microinversor"],
#             textfont=dict(color=text_color)
#         ))

#     # Adicionar linhas horizontais nos intervalos das barras
#     for i in range(1, 11):  # 10 intervalos
#         fig.add_shape(
#             go.layout.Shape(
#                 type="line",
#                 x0=-0.5, x1=len(df_grouped["Microinversor"]) - 0.5,
#                 y0=(max_value / 10) * i, y1=(max_value / 10) * i,
#                 line=dict(color="white", width=1, dash="dot")
#             )
#         )

#     fig.update_layout(
#         barmode="overlay",
#         plot_bgcolor="#222",
#         paper_bgcolor="#222",
#         font=dict(color="white"),
#         yaxis=dict(title="Energia Gerada (kWh)", range=[0, max_value * 1.1], showgrid=False),
#         xaxis=dict(title="Microinversor", showgrid=False),
#     )

#     st.plotly_chart(fig, use_container_width=True)


# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input(
#         "Selecione a data ou intervalo", [min_date, max_date],
#         min_value=min_date, max_value=max_date, key="date_selector"
#     )

#     # Ajustar seleção única de data para um intervalo válido
#     if isinstance(date_range, tuple) or isinstance(date_range, list):
#         start_date, end_date = date_range[0], date_range[-1]
#     else:
#         start_date, end_date = date_range, date_range

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect(
#         "Escolha os microinversores", microinversores, default=microinversores
#     )

#     # Filtrando os dados com base na seleção
#     df_filtered = df[
#         (df["Date"].dt.date >= start_date) &
#         (df["Date"].dt.date <= end_date) &
#         (df["Microinversor"].isin(selected_microinversores))
#     ]

#     # Agrupar dados por Microinversor, somando a energia total
#     df_grouped = df_filtered.groupby("Microinversor")["Energy (kWh)"].sum().reset_index()

#     # Definir a altura máxima com base no maior valor da lista selecionada
#     max_value = df_grouped["Energy (kWh)"].max()
#     if max_value == 0:
#         max_value = 1  # Evita problemas no eixo Y

#     # Criar gráfico de barras customizado
#     st.subheader("🔍 Energia Total por Microinversor")
#     fig = go.Figure()

#     for _, row in df_grouped.iterrows():
#         fill_color = "#008CFF" if row["Energy (kWh)"] > 0 else "#444444"  # Azul se houver energia, cinza se for 0
#         text_color = "white" if row["Energy (kWh)"] > 0 else "#BBBBBB"
#         fig.add_trace(go.Bar(
#             x=[row["Microinversor"]],
#             y=[max_value],
#             marker=dict(color="black"),
#             opacity=0.3,
#             showlegend=False
#         ))
#         fig.add_trace(go.Bar(
#             x=[row["Microinversor"]],
#             y=[row["Energy (kWh)"] + 0.3],
#             text=f"{row['Energy (kWh)']:.2f} kWh",
#             textposition="auto",
#             marker=dict(color=fill_color),
#             name=row["Microinversor"],
#             textfont=dict(color=text_color)
#         ))

#     # Adicionar linhas horizontais nos intervalos das barras
#     for i in range(1, 11):  # 10 intervalos
#         fig.add_shape(
#             go.layout.Shape(
#                 type="line",
#                 x0=-0.5, x1=len(df_grouped["Microinversor"]) - 0.5,
#                 y0=(max_value / 10) * i, y1=(max_value / 10) * i,
#                 line=dict(color="white", width=1, dash="dot")
#             )
#         )

#     fig.update_layout(
#         barmode="overlay",
#         plot_bgcolor="#222",
#         paper_bgcolor="#222",
#         font=dict(color="white"),
#         yaxis=dict(title="Energia Gerada (kWh)", range=[0, max_value * 1.1], showgrid=False),
#         xaxis=dict(title="Microinversor", showgrid=False),
#     )

#     st.plotly_chart(fig, use_container_width=True)

#     st.subheader("📈 Evolução da Geração de Energia")
#     df_time_series = df_filtered.groupby(["Date", "Microinversor"])["Energy (kWh)"].sum().reset_index()

#     fig_line = go.Figure()
#     for micro in selected_microinversores:
#         df_micro = df_time_series[df_time_series["Microinversor"] == micro]
#         fig_line.add_trace(go.Scatter(
#             x=df_micro["Date"], y=df_micro["Energy (kWh)"],
#             mode="lines+markers", name=micro
#         ))

#     fig_line.update_layout(
#         plot_bgcolor="#222", paper_bgcolor="#222", font=dict(color="white"),
#         xaxis_title="Data", yaxis_title="Energia Gerada (kWh)"
#     )
#     st.plotly_chart(fig_line, use_container_width=True)

#     st.subheader("📊 Distribuição da Geração por Microinversor")
#     fig_pie = go.Figure(data=[go.Pie(
#         labels=df_grouped["Microinversor"], values=df_grouped["Energy (kWh)"],
#         hole=0.4, textinfo="percent+label"
#     )])

#     fig_pie.update_layout(plot_bgcolor="#222", paper_bgcolor="#222", font=dict(color="white"))
#     st.plotly_chart(fig_pie, use_container_width=True)


#     st.subheader("📊 Energia Gerada Acumulada ao Longo do Tempo")
#     df_cumulative = df_time_series.copy()
#     df_cumulative["Cumulative Energy"] = df_cumulative.groupby("Microinversor")["Energy (kWh)"].cumsum()

#     fig_area = px.area(
#         df_cumulative, x="Date", y="Cumulative Energy", color="Microinversor",
#         labels={"Cumulative Energy": "Energia Acumulada (kWh)"}
#     )

#     fig_area.update_layout(plot_bgcolor="#222", paper_bgcolor="#222", font=dict(color="white"))
#     st.plotly_chart(fig_area, use_container_width=True)

#      # Criando visualização estilo cards
#     if not df_filtered.empty:
#         st.subheader(f"⚡ Geração de Energia - {date_range}")

#         # Filtrar os dados para os microinversores selecionados
#         df_selected = df_filtered[df_filtered['Microinversor'].isin(selected_microinversores)]

#         # Agrupar por microinversor e somar a energia gerada
#         df_totals = df_selected.groupby('Microinversor')['Energy (kWh)'].sum().reset_index()

#         cols = st.columns(min(20, len(df_totals)))  # Ajusta dinamicamente o número de colunas

#         for i, (index, row) in enumerate(df_totals.iterrows()):
#             fig = go.Figure(go.Indicator(
#                 mode="number",
#                 value=row["Energy (kWh)"],
#                 title={"text": f"{row['Microinversor']}<br><span style='font-size:0.8em;color:gray;'>Total</span>"},
#                 number={"suffix": " kWh"}
#             ))
#             st.plotly_chart(fig, use_container_width=True, key=f"chart_{index}")


# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# import plotly.express as px

# # Configuração da página
# st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # Título do aplicativo
# st.title("📊 Dashboard de Geração de Energia")

# # Upload do arquivo CSV
# uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = load_data(uploaded_file)

#     # Seleção de intervalo de datas
#     st.sidebar.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.sidebar.date_input(
#         "Selecione a data ou intervalo", [min_date, max_date],
#         min_value=min_date, max_value=max_date, key="date_selector"
#     )

#     # Ajustar seleção única de data para um intervalo válido
#     if isinstance(date_range, tuple) or isinstance(date_range, list):
#         start_date, end_date = date_range[0], date_range[-1]
#     else:
#         start_date, end_date = date_range, date_range

#     # Seleção de Microinversor
#     st.sidebar.subheader("🔌 Selecione Microinversor(es)")
#     microinversores = df["Microinversor"].unique()
#     selected_microinversores = st.sidebar.multiselect(
#         "Escolha os microinversores", microinversores, default=microinversores
#     )

#     # Filtrando os dados com base na seleção
#     df_filtered = df[
#         (df["Date"].dt.date >= start_date) &
#         (df["Date"].dt.date <= end_date) &
#         (df["Microinversor"].isin(selected_microinversores))
#     ]

#     # Agrupar dados por Microinversor, somando a energia total
#     df_grouped = df_filtered.groupby("Microinversor")["Energy (kWh)"].sum().reset_index()

#     # Definir a altura máxima com base no maior valor da lista selecionada
#     max_value = df_grouped["Energy (kWh)"].max()
#     if max_value == 0:
#         max_value = 1  # Evita problemas no eixo Y

#    # Criando visualização estilo cards
#     if not df_filtered.empty:
#         st.subheader("⚡ Geração de Energia")

#         # Filtrar os dados para os microinversores selecionados
#         df_selected = df_filtered[df_filtered['Microinversor'].isin(selected_microinversores)]

#         # Agrupar por microinversor e somar a energia gerada
#         df_totals = df_selected.groupby('Microinversor')['Energy (kWh)'].sum().reset_index()

#         cols = st.columns(min(20, len(df_totals)))  # Ajusta dinamicamente o número de colunas

#         for i, (index, row) in enumerate(df_totals.iterrows()):
#             with cols[i % len(cols)]:
#                 st.markdown(
#                     f"""
#                     <div style="padding: 10px; border-radius: 10px; background-color: #f0f2f6; text-align: center; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
#                         <h4 style="color: #333;">{row['Microinversor']}</h4>
#                         <h2 style="color: #007BFF;">{row['Energy (kWh)']} kWh</h2>
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )

#     # Criar gráfico de barras customizado
#     st.subheader("🔍 Energia Total por Microinversor")
#     fig = go.Figure()

#     for _, row in df_grouped.iterrows():
#         fill_color = "#008CFF" if row["Energy (kWh)"] > 0 else "#444444"  # Azul se houver energia, cinza se for 0
#         text_color = "white" if row["Energy (kWh)"] > 0 else "#BBBBBB"
#         fig.add_trace(go.Bar(
#             x=[row["Microinversor"]],
#             y=[max_value],
#             marker=dict(color="black"),
#             opacity=0.3,
#             showlegend=False
#         ))
#         fig.add_trace(go.Bar(
#             x=[row["Microinversor"]],
#             y=[row["Energy (kWh)"]],
#             text=f"{row['Energy (kWh)']:.2f} kWh",
#             textposition="auto",
#             marker=dict(color=fill_color),
#             name=row["Microinversor"],
#             textfont=dict(color=text_color)
#         ))

#     # Adicionar linhas horizontais nos intervalos das barras
#     for i in range(1, 11):  # 10 intervalos
#         fig.add_shape(
#             go.layout.Shape(
#                 type="line",
#                 x0=-0.5, x1=len(df_grouped["Microinversor"]) - 0.5,
#                 y0=(max_value / 10) * i, y1=(max_value / 10) * i,
#                 line=dict(color="white", width=1, dash="dot")
#             )
#         )

#     fig.update_layout(
#         barmode="overlay",
#         plot_bgcolor="#222",
#         paper_bgcolor="#222",
#         font=dict(color="white"),
#         yaxis=dict(title="Energia Gerada (kWh)", range=[0, max_value * 1.1], showgrid=False),
#         xaxis=dict(title="Microinversor", showgrid=False),
#     )

#     st.plotly_chart(fig, use_container_width=True)

#     st.subheader("📈 Evolução da Geração de Energia")
#     df_time_series = df_filtered.groupby(["Date", "Microinversor"])["Energy (kWh)"].sum().reset_index()

#     fig_line = go.Figure()
#     for micro in selected_microinversores:
#         df_micro = df_time_series[df_time_series["Microinversor"] == micro]
#         fig_line.add_trace(go.Scatter(
#             x=df_micro["Date"], y=df_micro["Energy (kWh)"],
#             mode="lines+markers", name=micro
#         ))

#     fig_line.update_layout(
#         plot_bgcolor="#222", paper_bgcolor="#222", font=dict(color="white"),
#         xaxis_title="Data", yaxis_title="Energia Gerada (kWh)"
#     )
#     st.plotly_chart(fig_line, use_container_width=True)

#     st.subheader("📊 Distribuição da Geração por Microinversor")
#     fig_pie = go.Figure(data=[go.Pie(
#         labels=df_grouped["Microinversor"], values=df_grouped["Energy (kWh)"],
#         hole=0.4, textinfo="percent+label"
#     )])

#     fig_pie.update_layout(plot_bgcolor="#222", paper_bgcolor="#222", font=dict(color="white"))
#     st.plotly_chart(fig_pie, use_container_width=True)

#     st.subheader("📊 Energia Gerada Acumulada ao Longo do Tempo")
#     df_cumulative = df_time_series.copy()
#     df_cumulative["Cumulative Energy"] = df_cumulative.groupby("Microinversor")["Energy (kWh)"].cumsum()

#     fig_area = px.area(
#         df_cumulative, x="Date", y="Cumulative Energy", color="Microinversor",
#         labels={"Cumulative Energy": "Energia Acumulada (kWh)"}
#     )

#     fig_area.update_layout(plot_bgcolor="#222", paper_bgcolor="#222", font=dict(color="white"))
#     st.plotly_chart(fig_area, use_container_width=True)


import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# Título do aplicativo
st.title("📊 Dashboard de Geração de Energia")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])


def main():
    if uploaded_file:
        # Carregar os dados
        df = pd.read_csv(uploaded_file)
        df["Date"] = pd.to_datetime(df["Date"])  # Converter para data

        # Seleção de intervalo de datas
        st.subheader("📅 Selecione uma data ou intervalo de datas")
        min_date = df["Date"].min().date()
        max_date = df["Date"].max().date()
        date_range = st.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date, key="date_selector")

        # Botão para atualizar os gráficos
        if st.button("🔄 Atualizar Gráficos"):
            st.session_state.update_flag = not st.session_state.get("update_flag", False)

        if isinstance(date_range, list) and len(date_range) == 2:
            df_filtered = df[(df["Date"].dt.date >= date_range[0]) & (df["Date"].dt.date <= date_range[1])].copy()
        elif isinstance(date_range, list) and len(date_range) == 1:
            df_filtered = df[df["Date"].dt.date == date_range[0]].copy()
        else:
            df_filtered = df.copy()

        # Gráficos
        st.subheader("📈 Gráficos")
        fig1 = px.line(df_filtered, x="Date", y="Wind", title="Energia Solar")
        st.plotly_chart(fig1)

        # fig2 = px.line(df_filtered, x="Date", y="Hydro", title="Energia Hidroeletrica")

        # # Print para depuração
        # st.write("### Dados filtrados:")
        # st.write(df.head())

# @st.cache_data
# def load_data(uploaded_file):
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data
#     return df

# if uploaded_file:
#     # Carregar os dados
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data

#     # Seleção de intervalo de datas
#     st.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date, key="date_selector")

#     # Botão para atualizar os gráficos
#     if st.button("🔄 Atualizar Gráficos"):
#         st.session_state.update_flag = not st.session_state.get("update_flag", False)

#     if isinstance(date_range, list) and len(date_range) == 2:
#         df_filtered = df[(df["Date"].dt.date >= date_range[0]) & (df["Date"].dt.date <= date_range[1])].copy()
#     elif isinstance(date_range, list) and len(date_range) == 1:
#         df_filtered = df[df["Date"].dt.date == date_range[0]].copy()
#     else:
#         df_filtered = df.copy()

#     # Print para depuração
#     st.write("### Dados filtrados:")
#     st.write(df_filtered.head())

#     # Selecionar os últimos registros de cada microinversor
#     df_filtered = df_filtered.sort_values(by="Date", ascending=False).drop_duplicates(subset=["Microinversor", "Port"])

#     # Criar visualização estilo cards
#     st.subheader(f"⚡ Geração de Energia - {date_range}")

#     cols = st.columns(min(7, len(df_filtered)))  # Ajusta dinamicamente o número de colunas

#     for i, (index, row) in enumerate(df_filtered.iterrows()):
#         with cols[i % len(cols)]:
#             fig = go.Figure(go.Indicator(
#                 mode="number",
#                 value=row["Energy (kWh)"],
#                 title={"text": f"{row['Microinversor']}<br><span style='font-size:0.8em;color:gray;'>{row['SN']} - {row['Port']}</span>"},
#                 number={"suffix": " W"}
#             ))
#             st.plotly_chart(fig, use_container_width=True, key=f"chart_{index}_{st.session_state.update_flag}")

#     # Criar gráfico de barras para mostrar a geração por Port dentro de cada Microinversor
#     st.subheader("📊 Geração de Energia por Port e Microinversor")

#     fig_bar = px.bar(
#         df_filtered,
#         x="Port",
#         y="Energy (kWh)",
#         color="Microinversor",
#         facet_col="Microinversor",
#         title="Geração de Energia por Port dentro de cada Microinversor",
#         labels={"Energy (kWh)": "Energia (kWh)", "Port": "Porta"},
#         template="plotly_white",
#         text_auto=True,
#     )
#     fig_bar.update_traces(marker_line_width=1.5, marker_line_color="black")
#     fig_bar.update_layout(
#         font=dict(size=12),
#         title_font=dict(size=16, family="Arial", color="darkblue"),
#         legend=dict(title="Microinversores", orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
#         margin=dict(l=40, r=40, t=40, b=40),
#         height=500,
#     )
