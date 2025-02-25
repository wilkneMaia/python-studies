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

if uploaded_file:
    # Carregar os dados
    df = pd.read_csv(uploaded_file)
    df["Date"] = pd.to_datetime(df["Date"])  # Converter para data

    # Seleção de intervalo de datas
    st.subheader("📅 Selecione uma data ou intervalo de datas")
    min_date = df["Date"].min().date()
    max_date = df["Date"].max().date()
    date_range = st.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date)

    if isinstance(date_range, list) and len(date_range) == 2:
        df_filtered = df[(df["Date"] >= pd.Timestamp(date_range[0])) & (df["Date"] <= pd.Timestamp(date_range[1]))]
    elif isinstance(date_range, list) and len(date_range) == 1:
        df_filtered = df[df["Date"] == pd.Timestamp(date_range[0])]
    else:
        df_filtered = df

    # Selecionar os últimos registros de cada microinversor
    df_filtered = df_filtered.sort_values(by="Date", ascending=False).drop_duplicates(subset=["Microinversor"]).head(7)

    # Criar visualização estilo cards
    st.subheader(f"⚡ Geração de Energia - {date_range}")

    cols = st.columns(7)  # Definir número de colunas para 7 microinversores

    for i, (index, row) in enumerate(df_filtered.iterrows()):
        with cols[i]:
            fig = go.Figure(go.Indicator(
                mode="number",
                value=row["Energy (kWh)"],
                title={"text": f"{row['Microinversor']}<br><span style='font-size:0.8em;color:gray;'>{row['SN']} - {row['Port']}</span>"},
                number={"suffix": " W"}
            ))
            st.plotly_chart(fig, use_container_width=True, key=f"chart_{index}")

    # Criar gráfico de barras para mostrar a geração por Port dentro de cada Microinversor
    st.subheader("📊 Geração de Energia por Port e Microinversor")

    fig_bar = px.bar(
        df,
        x="Port",
        y="Energy (kWh)",
        color="Microinversor",
        facet_col="Microinversor",
        title="Geração de Energia por Port dentro de cada Microinversor",
        labels={"Energy (kWh)": "Energia (kWh)", "Port": "Porta"},
        template="plotly_white",
        text_auto=True,
    )
    fig_bar.update_traces(marker_line_width=1.5, marker_line_color="black")
    fig_bar.update_layout(
        font=dict(size=12),
        title_font=dict(size=16, family="Arial", color="darkblue"),
        legend=dict(title="Microinversores", orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
        margin=dict(l=40, r=40, t=40, b=40),
        height=500,
    )

    st.plotly_chart(fig_bar, use_container_width=True)

# # import streamlit as st
# # import pandas as pd
# # import plotly.express as px
# # import plotly.graph_objects as go

# # # Configuração da página
# # st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# # # Título do aplicativo
# # st.title("📊 Dashboard de Geração de Energia")

# # # Upload do arquivo CSV
# # uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

# # if uploaded_file:
# #     # Carregar os dados
# #     df = pd.read_csv(uploaded_file)
# #     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data

# #     # Seleção de intervalo de datas
# #     st.subheader("📅 Selecione uma data ou intervalo de datas")
# #     min_date = df["Date"].min().date()
# #     max_date = df["Date"].max().date()
# #     date_range = st.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date)

# #     if isinstance(date_range, list) and len(date_range) == 2:
# #         df_filtered = df[(df["Date"] >= pd.Timestamp(date_range[0])) & (df["Date"] <= pd.Timestamp(date_range[1]))]
# #     elif isinstance(date_range, list) and len(date_range) == 1:
# #         df_filtered = df[df["Date"] == pd.Timestamp(date_range[0])]
# #     else:
# #         df_filtered = df

# #     # Selecionar os últimos registros de cada microinversor
# #     df_filtered = df_filtered.sort_values(by="Date", ascending=False).drop_duplicates(subset=["Microinversor"]).head(7)

# #     # Criar visualização estilo cards
# #     st.subheader(f"⚡ Geração de Energia - {date_range}")

# #     cols = st.columns(7)  # Definir número de colunas para 7 microinversores

# #     for i, (index, row) in enumerate(df_filtered.iterrows()):
# #         with cols[i]:
# #             fig = go.Figure(go.Indicator(
# #                 mode="number",
# #                 value=row["Energy (kWh)"],
# #                 title={"text": f"{row['Microinversor']}<br><span style='font-size:0.8em;color:gray;'>{row['SN']} - {row['Port']}</span>"},
# #                 number={"suffix": " W"}
# #             ))
# #             st.plotly_chart(fig, use_container_width=True, key=f"chart_{index}")


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

# if uploaded_file:
#     # Carregar os dados
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data

#     # Seleção de intervalo de datas
#     st.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date)

#     if isinstance(date_range, list) and len(date_range) == 2:
#         df_filtered = df[(df["Date"] >= pd.Timestamp(date_range[0])) & (df["Date"] <= pd.Timestamp(date_range[1]))]
#     elif isinstance(date_range, list) and len(date_range) == 1:
#         df_filtered = df[df["Date"] == pd.Timestamp(date_range[0])]
#     else:
#         df_filtered = df

#     # Selecionar os últimos registros de cada microinversor
#     df_filtered = df_filtered.sort_values(by="Date", ascending=False).drop_duplicates(subset=["Microinversor"]).head(7)

#     # Criar visualização estilo cards
#     st.subheader(f"⚡ Geração de Energia - {date_range}")

#     cols = st.columns(7)  # Definir número de colunas para 7 microinversores

#     for i, (index, row) in enumerate(df_filtered.iterrows()):
#         with cols[i]:
#             fig = go.Figure(go.Indicator(
#                 mode="number",
#                 value=row["Energy (kWh)"],
#                 title={"text": f"{row['Microinversor']}<br><span style='font-size:0.8em;color:gray;'>{row['SN']} - {row['Port']}</span>"},
#                 number={"suffix": " W"}
#             ))
#             st.plotly_chart(fig, use_container_width=True, key=f"chart_{index}")

#     # Criar gráfico de barras para mostrar a geração por Port
#     st.subheader("📊 Geração de Energia por Port")

#     fig_bar = px.bar(
#         df_filtered,
#         x="Port",
#         y="Energy (kWh)",
#         color="Microinversor",
#         title="Geração de Energia por Port",
#         labels={"Energy (kWh)": "Energia (kWh)", "Port": "Porta"},
#     )

#     st.plotly_chart(fig_bar, use_container_width=True)

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

# if uploaded_file:
#     # Carregar os dados
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data

#     # Seleção de intervalo de datas
#     st.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date)

#     if isinstance(date_range, list) and len(date_range) == 2:
#         df_filtered = df[(df["Date"] >= pd.Timestamp(date_range[0])) & (df["Date"] <= pd.Timestamp(date_range[1]))]
#     elif isinstance(date_range, list) and len(date_range) == 1:
#         df_filtered = df[df["Date"] == pd.Timestamp(date_range[0])]
#     else:
#         df_filtered = df

#     # Selecionar os últimos registros de cada microinversor
#     df_filtered = df_filtered.sort_values(by="Date", ascending=False).drop_duplicates(subset=["Microinversor"]).head(7)

#     # Criar visualização estilo cards
#     st.subheader(f"⚡ Geração de Energia - {date_range}")

#     cols = st.columns(7)  # Definir número de colunas para 7 microinversores

#     for i, (index, row) in enumerate(df_filtered.iterrows()):
#         with cols[i]:
#             fig = go.Figure(go.Indicator(
#                 mode="number",
#                 value=row["Energy (kWh)"],
#                 title={"text": f"{row['Microinversor']}<br><span style='font-size:0.8em;color:gray;'>{row['SN']} - {row['Port']}</span>"},
#                 number={"suffix": " W"}
#             ))
#             st.plotly_chart(fig, use_container_width=True, key=f"chart_{index}")

#     # Criar gráfico de barras para mostrar a geração por Port dentro de cada Microinversor
#     st.subheader("📊 Geração de Energia por Port e Microinversor")

#     fig_bar = px.bar(
#         df,
#         x="Port",
#         y="Energy (kWh)",
#         color="Microinversor",
#         facet_col="Microinversor",
#         title="Geração de Energia por Port dentro de cada Microinversor",
#         labels={"Energy (kWh)": "Energia (kWh)", "Port": "Porta"},
#     )

#     st.plotly_chart(fig_bar, use_container_width=True)


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

# if uploaded_file:
#     # Carregar os dados
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data

#     # Seleção de intervalo de datas
#     st.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date)

#     if isinstance(date_range, list) and len(date_range) == 2:
#         df_filtered = df[(df["Date"] >= pd.Timestamp(date_range[0])) & (df["Date"] <= pd.Timestamp(date_range[1]))]
#     elif isinstance(date_range, list) and len(date_range) == 1:
#         df_filtered = df[df["Date"] == pd.Timestamp(date_range[0])]
#     else:
#         df_filtered = df

#     # Selecionar os últimos registros de cada microinversor
#     df_filtered = df_filtered.sort_values(by="Date", ascending=False).drop_duplicates(subset=["Microinversor"]).head(7)

#     # Criar visualização estilo cards
#     st.subheader(f"⚡ Geração de Energia - {date_range}")

#     cols = st.columns(7)  # Definir número de colunas para 7 microinversores

#     for i, (index, row) in enumerate(df_filtered.iterrows()):
#         with cols[i]:
#             fig = go.Figure(go.Indicator(
#                 mode="number",
#                 value=row["Energy (kWh)"],
#                 title={"text": f"{row['Microinversor']}<br><span style='font-size:0.8em;color:gray;'>{row['SN']} - {row['Port']}</span>"},
#                 number={"suffix": " W"}
#             ))
#             st.plotly_chart(fig, use_container_width=True, key=f"chart_{index}")

#     # Criar gráfico de barras para mostrar a geração por Port dentro de cada Microinversor
#     st.subheader("📊 Geração de Energia por Port e Microinversor")

#     fig_bar = px.bar(
#         df,
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

#     st.plotly_chart(fig_bar, use_container_width=True)


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

# if uploaded_file:
#     # Carregar os dados
#     df = pd.read_csv(uploaded_file)
#     df["Date"] = pd.to_datetime(df["Date"])  # Converter para data

#     # Seleção de intervalo de datas
#     st.subheader("📅 Selecione uma data ou intervalo de datas")
#     min_date = df["Date"].min().date()
#     max_date = df["Date"].max().date()
#     date_range = st.date_input("Selecione a data ou intervalo", [min_date, max_date], min_value=min_date, max_value=max_date)

#     if isinstance(date_range, list) and len(date_range) == 2:
#         df_filtered = df[(df["Date"] >= pd.Timestamp(date_range[0])) & (df["Date"] <= pd.Timestamp(date_range[1]))].copy()
#     elif isinstance(date_range, list) and len(date_range) == 1:
#         df_filtered = df[df["Date"] == pd.Timestamp(date_range[0])].copy()
#     else:
#         df_filtered = df.copy()

#     # Selecionar os últimos registros de cada microinversor
#     df_filtered = df_filtered.sort_values(by="Date", ascending=False).drop_duplicates(subset=["Microinversor"]).head(7)

#     # Criar visualização estilo cards
#     st.subheader(f"⚡ Geração de Energia - {date_range}")

#     cols = st.columns(7)  # Definir número de colunas para 7 microinversores

#     for i, (index, row) in enumerate(df_filtered.iterrows()):
#         with cols[i]:
#             fig = go.Figure(go.Indicator(
#                 mode="number",
#                 value=row["Energy (kWh)"],
#                 title={"text": f"{row['Microinversor']}<br><span style='font-size:0.8em;color:gray;'>{row['SN']} - {row['Port']}</span>"},
#                 number={"suffix": " W"}
#             ))
#             st.plotly_chart(fig, use_container_width=True, key=f"chart_{index}_{date_range}")

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

#     st.plotly_chart(fig_bar, use_container_width=True)
