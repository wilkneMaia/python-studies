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
#     """Exibe os gráficos com base no filtro de Mês ou Ano"""
#     st.subheader("📅 Histórico de Dados")

#     # Filtros na barra lateral para selecionar o período
#     filter_option = st.sidebar.radio("Selecione a visualização", ["Dia", "Semana", "Mês", "Ano", "Total"])

#     # Barra lateral para selecionar o mês (se for Mês)
#     if filter_option == "Mês":
#         # Organizando o mês e ano na mesma linha com st.columns()
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

#             display_performance_indicators(daily_data)
#             plot_energy_bar_chart(daily_data, x, slope, intercept)
#             plot_cumulative_energy_graph(daily_data)

#         else:
#             st.warning("⚠️ Nenhum dado disponível para este período.")

#     # Barra lateral para selecionar o ano (se for Ano)
#     elif filter_option == "Ano":
#         selected_year = st.sidebar.selectbox("Selecione o ano", range(2023, 2026))

#         filtered_data = df[df["Year"] == selected_year]

#         if not filtered_data.empty:
#             daily_data = filtered_data.groupby("Day")["Energy"].sum().reset_index()
#             st.write(f"📈 Dados de geração de energia para o ano {selected_year}")

#             # Exibindo gráficos
#             x = daily_data["Day"]
#             y = daily_data["Energy"]
#             slope, intercept = polyfit(x, y, 1)

#             display_performance_indicators(daily_data)
#             plot_energy_bar_chart(daily_data, x, slope, intercept)
#             plot_cumulative_energy_graph(daily_data)
#             plot_quadrant_graph(filtered_data, selected_year)

#         else:
#             st.warning("⚠️ Nenhum dado disponível para este período.")

# # Função para carregar os dados e exibir gráficos
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

# def plot_comparative_months_by_year_line(df):
#     """Exibe um gráfico de linhas comparativo dos meses por ano"""
#     # Agrupar os dados por Ano e Mês
#     monthly_comparison = df.groupby(["Year", "Month"])["Energy"].sum().reset_index()

#     # Criar gráfico de linhas comparativo
#     fig = px.line(monthly_comparison, x="Month", y="Energy", color="Year",
#                   title="Comparativo de Energia Gerada por Mês e Ano",
#                   labels={"Month": "Mês", "Energy": "Energia Gerada (kWh)", "Year": "Ano"},
#                   template="plotly_dark", markers=True)

#     # Ajustando o layout
#     fig.update_layout(
#         title=dict(text="Comparativo de Energia Gerada por Mês e Ano", x=0.5, font=dict(size=22, color="white")),
#         xaxis=dict(title="Mês", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2,
#                    tickangle=45, tickfont=dict(color="#ffffff")),
#         yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1,
#                    zerolinecolor="gray", tickfont=dict(color="#ffffff")),
#         plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
#     )

#     # Exibe o gráfico
#     st.plotly_chart(fig)

# # Função para exibir gráfico de total de energia gerada por ano (barra)
# def plot_total_by_year(df):
#     """Exibe o total de energia gerada por ano"""
#     total_data = df.groupby("Year")["Energy"].sum().reset_index()

#     fig = px.bar(total_data, x="Year", y="Energy", title="Total de Energia Gerada por Ano",
#                  labels={"Year": "Ano", "Energy": "Total de Energia Gerada (kWh)"},
#                  template="plotly_dark", color="Energy", color_continuous_scale="Blues")

#     fig.update_layout(
#         title=dict(text="Total de Energia Gerada por Ano", x=0.5, font=dict(size=22, color="white")),
#         xaxis=dict(title="Ano", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2,
#                    tickangle=45, tickfont=dict(color="#ffffff")),
#         yaxis=dict(title="Total de Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1,
#                    zerolinecolor="gray", tickfont=dict(color="#ffffff")),
#         plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
#     )

#     st.plotly_chart(fig)

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

# def plot_area_stack_by_year(df):
#     """Exibe um gráfico de área empilhada comparativo dos meses por ano"""
#     # Agrupar os dados por Ano e Mês
#     monthly_comparison = df.groupby(["Year", "Month"])["Energy"].sum().reset_index()

#     # Criar gráfico de área empilhada
#     fig = px.area(monthly_comparison, x="Month", y="Energy", color="Year",
#                   title="Comparativo de Energia Gerada por Mês e Ano (Área Empilhada)",
#                   labels={"Month": "Mês", "Energy": "Energia Gerada (kWh)", "Year": "Ano"},
#                   template="plotly_dark")

#     # Ajustando o layout
#     fig.update_layout(
#         title=dict(text="Comparativo de Energia Gerada por Mês e Ano", x=0.5, font=dict(size=22, color="white")),
#         xaxis=dict(title="Mês", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2,
#                    tickangle=45, tickfont=dict(color="#ffffff")),
#         yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1,
#                    zerolinecolor="gray", tickfont=dict(color="#ffffff")),
#         plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
#     )

#     # Exibe o gráfico
#     st.plotly_chart(fig)

# def plot_scatter_by_year(df):
#     """Exibe um gráfico de dispersão comparativo dos meses por ano"""
#     # Agrupar os dados por Ano e Mês
#     monthly_comparison = df.groupby(["Year", "Month"])["Energy"].sum().reset_index()

#     # Criar gráfico de dispersão
#     fig = px.scatter(monthly_comparison, x="Month", y="Energy", color="Year",
#                      title="Comparativo de Energia Gerada por Mês e Ano (Dispersão)",
#                      labels={"Month": "Mês", "Energy": "Energia Gerada (kWh)", "Year": "Ano"},
#                      template="plotly_dark")

#     # Ajustando o layout
#     fig.update_layout(
#         title=dict(text="Comparativo de Energia Gerada por Mês e Ano", x=0.5, font=dict(size=22, color="white")),
#         xaxis=dict(title="Mês", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2,
#                    tickangle=45, tickfont=dict(color="#ffffff")),
#         yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1,
#                    zerolinecolor="gray", tickfont=dict(color="#ffffff")),
#         plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
#     )

#     # Exibe o gráfico
#     st.plotly_chart(fig)

# def plot_candlestick_by_month(df):
#     """Exibe um gráfico Candlestick comparativo dos meses por ano"""
#     # Agrupar os dados por Ano e Mês
#     monthly_comparison = df.groupby(["Year", "Month"])["Energy"].sum().reset_index()

#     # Inicializando listas para cada componente do gráfico Candlestick
#     fig_data = []

#     for year in monthly_comparison["Year"].unique():
#         year_data = monthly_comparison[monthly_comparison["Year"] == year]

#         # Garantindo que cada parâmetro seja uma lista ou série
#         fig_data.append(go.Candlestick(
#             x=year_data["Month"],
#             open=[year_data["Energy"].iloc[0]] * len(year_data),  # Energia do primeiro mês do ano repetida para todos os meses
#             high=[year_data["Energy"].max()] * len(year_data),    # Energia máxima repetida para todos os meses
#             low=[year_data["Energy"].min()] * len(year_data),     # Energia mínima repetida para todos os meses
#             close=[year_data["Energy"].iloc[-1]] * len(year_data),# Energia do último mês repetida para todos os meses
#             name=str(year)
#         ))

#     # Criando o gráfico Candlestick
#     fig = go.Figure(fig_data)

#     # Ajustando o layout
#     fig.update_layout(
#         title=dict(text="Comparativo de Energia Gerada por Mês e Ano (Candlestick)", x=0.5, font=dict(size=22, color="white")),
#         xaxis=dict(title="Mês", tickmode='linear', tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], ticktext=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
#                    showgrid=False, ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
#         yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
#         plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
#     )

#     # Exibe o gráfico
#     st.plotly_chart(fig)

# def plot_box_plot_by_month(df):
#     """Exibe um gráfico de box plot comparativo dos meses por ano"""
#     # Agrupar os dados por Ano e Mês
#     monthly_comparison = df.groupby(["Year", "Month"])["Energy"].sum().reset_index()

#     # Criar gráfico de box plot
#     fig = px.box(monthly_comparison, x="Month", y="Energy", color="Year",
#                  title="Distribuição de Energia Gerada por Mês e Ano (Box Plot)",
#                  labels={"Month": "Mês", "Energy": "Energia Gerada (kWh)", "Year": "Ano"},
#                  template="plotly_dark")

#     # Ajustando o layout
#     fig.update_layout(
#         title=dict(text="Distribuição de Energia Gerada por Mês e Ano", x=0.5, font=dict(size=22, color="white")),
#         xaxis=dict(title="Mês", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2,
#                    tickangle=45, tickfont=dict(color="#ffffff")),
#         yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1,
#                    zerolinecolor="gray", tickfont=dict(color="#ffffff")),
#         plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
#     )

#     # Exibe o gráfico
#     st.plotly_chart(fig)

# Função para exibir gráfico de quadrantes
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
#     """Exibe os gráficos com base no filtro de Mês, Ano ou Total"""
#     st.subheader("📅 Histórico de Dados")

#     # Filtros na barra lateral para selecionar o período
#     filter_option = st.sidebar.radio("Selecione a visualização", ["Dia", "Semana", "Mês", "Ano", "Total"])

#     # Barra lateral para selecionar o mês (se for Mês)
#     if filter_option == "Mês":
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

#             display_performance_indicators(daily_data)
#             plot_energy_bar_chart(daily_data, x, slope, intercept)
#             plot_quadrant_graph(filtered_data, selected_year)
#             plot_cumulative_energy_graph(daily_data)

#         else:
#             st.warning("⚠️ Nenhum dado disponível para este período.")

#     # Barra lateral para selecionar o ano (se for Ano)
#     elif filter_option == "Ano":
#         selected_year = st.sidebar.selectbox("Selecione o ano", range(2023, 2026))

#         filtered_data = df[df["Year"] == selected_year]

#         if not filtered_data.empty:
#             daily_data = filtered_data.groupby("Day")["Energy"].sum().reset_index()
#             st.write(f"📈 Dados de geração de energia para o ano {selected_year}")

#             # Exibindo gráficos
#             x = daily_data["Day"]
#             y = daily_data["Energy"]
#             slope, intercept = polyfit(x, y, 1)

#             display_performance_indicators(daily_data)
#             plot_energy_bar_chart(daily_data, x, slope, intercept)
#             plot_cumulative_energy_graph(daily_data)
#             plot_quadrant_graph(filtered_data, selected_year)

#         else:
#             st.warning("⚠️ Nenhum dado disponível para este período.")

#     # Exibir gráficos para Total
#     elif filter_option == "Total":
#         plot_total_by_year(df)
#         plot_comparative_months_by_year_line(df)
#         plot_area_stack_by_year(df)
#         plot_scatter_by_year(df)
#         plot_box_plot_by_month(df)
#         plot_candlestick_by_month(df)

# # Função para carregar os dados e exibir gráficos
# if uploaded_file:
#     df = load_data(uploaded_file)
#     display_tabs(df)


import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from numpy import polyfit

# Configuração da página
st.set_page_config(page_title="Dashboard de Energia", layout="wide")

# Título do aplicativo
st.title("📊 Dashboard de Geração de Energia")

# Barra lateral para seleção do arquivo
uploaded_file = st.sidebar.file_uploader("📤 Faça upload do arquivo CSV", type=["csv"])

@st.cache_data
def load_data(uploaded_file):
    """Carrega e processa os dados do arquivo CSV"""
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()  # Remove espaços extras nos nomes das colunas
    df.rename(columns={"Energy (kWh)": "Energy"}, inplace=True)  # Renomeia a coluna
    df["Date"] = pd.to_datetime(df["Date"])  # Converter para datetime
    df["Day"] = df["Date"].dt.day  # Adiciona a coluna de dias do mês
    df["Month"] = df["Date"].dt.month  # Adiciona a coluna do mês
    df["Month_Year"] = df["Date"].dt.strftime('%Y-%m')  # Adiciona a coluna Ano-Mês
    df["Year"] = df["Date"].dt.year  # Adiciona a coluna do ano
    return df

# Função genérica para gráficos de barras
def create_bar_chart(data, x, y, title, xlabel, ylabel):
    fig = px.bar(data, x=x, y=y, title=title, labels={x: xlabel, y: ylabel}, template="plotly_dark")
    fig.update_layout(
        title=dict(text=title, x=0.5, font=dict(size=22, color="white")),
        xaxis=dict(title=xlabel, showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title=ylabel, showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )
    return fig

# Função para exibir gráfico de barras com linha de tendência
def plot_energy_bar_chart(daily_data, x, slope, intercept):
    fig = create_bar_chart(daily_data, "Day", "Energy", "Geração de Energia por Dia", "Dia", "Geração de Energia (kWh)")
    fig.add_trace(go.Scatter(x=x, y=slope * x + intercept, mode='lines', name='Tendência', line=dict(color='#ff5722', width=3, dash='solid')))
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
        title=dict(text="Comparativo de Energia Gerada por Mês e Ano", x=0.5, font=dict(size=22, color="white")),
        xaxis=dict(title="Mês", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig)

# Função para gráfico de total de energia gerada por ano (barra)
def plot_total_by_year(df):
    """Exibe o total de energia gerada por ano"""
    total_data = df.groupby("Year")["Energy"].sum().reset_index()
    fig = create_bar_chart(total_data, "Year", "Energy", "Total de Energia Gerada por Ano", "Ano", "Total de Energia Gerada (kWh)")
    st.plotly_chart(fig)

# Função para exibir gráfico de linha acumulada
def plot_cumulative_energy_graph(daily_data):
    fig_line = px.line(daily_data, x="Day", y="Energy", title="Geração Acumulada de Energia por Dia", labels={"Day": "Dia", "Energy": "Geração Acumulada (kWh)"}, template="plotly_dark")
    fig_line.update_traces(mode='lines+markers', line=dict(color="#00bcd4", width=2), marker=dict(size=6, color="#ff5722", line=dict(width=1, color="white")))
    fig_line.update_layout(title=dict(text="Geração Acumulada de Energia por Dia", x=0.5, font=dict(size=16, color="#ffffff")),
                           xaxis=dict(title="Dia", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
                           yaxis=dict(title="Geração Acumulada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
                           plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40))
    st.plotly_chart(fig_line)

# Função para exibir gráfico de área empilhada
def plot_area_stack_by_year(df):
    """Exibe um gráfico de área empilhada comparativo dos meses por ano"""
    monthly_comparison = df.groupby(["Year", "Month"])["Energy"].sum().reset_index()
    fig = px.area(monthly_comparison, x="Month", y="Energy", color="Year", title="Comparativo de Energia Gerada por Mês e Ano (Área Empilhada)", labels={"Month": "Mês", "Energy": "Energia Gerada (kWh)", "Year": "Ano"}, template="plotly_dark")
    fig.update_layout(title=dict(text="Comparativo de Energia Gerada por Mês e Ano", x=0.5, font=dict(size=22, color="white")),
                      xaxis=dict(title="Mês", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
                      yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
                      plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40))
    st.plotly_chart(fig)

# Função para exibir gráfico de dispersão
def plot_scatter_by_year(df):
    """Exibe um gráfico de dispersão comparativo dos meses por ano"""
    monthly_comparison = df.groupby(["Year", "Month"])["Energy"].sum().reset_index()
    fig = px.scatter(monthly_comparison, x="Month", y="Energy", color="Year", title="Comparativo de Energia Gerada por Mês e Ano (Dispersão)", labels={"Month": "Mês", "Energy": "Energia Gerada (kWh)", "Year": "Ano"}, template="plotly_dark")
    fig.update_layout(title=dict(text="Comparativo de Energia Gerada por Mês e Ano", x=0.5, font=dict(size=22, color="white")),
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
        title=dict(text="Comparativo de Energia Gerada por Mês e Ano (Candlestick)", x=0.5, font=dict(size=22, color="white")),
        xaxis=dict(title="Mês", tickmode='linear', tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], ticktext=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                   showgrid=False, ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Energia Gerada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig)

# Função para exibir gráficos de indicadores
def display_performance_indicators(daily_data):
    total_energy = daily_data["Energy"].sum()
    avg_energy = daily_data["Energy"].mean()
    max_energy = daily_data["Energy"].max()
    min_energy = daily_data["Energy"].min()
    std_dev_energy = daily_data["Energy"].std()

    # Supondo que a eficiência ideal de geração seja 90% da capacidade máxima
    ideal_energy = total_energy * 0.9
    efficiency = (total_energy / ideal_energy) * 100 if ideal_energy > 0 else 0

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1: st.metric(label="🔋 Total de Energia Gerada", value=f"{total_energy:,.2f} kWh", delta=f"+{total_energy - avg_energy:,.2f} kWh", delta_color="inverse")
    with col2: st.metric(label="📊 Média de Energia Diária", value=f"{avg_energy:,.2f} kWh")
    with col3: st.metric(label="⚡ Máxima de Energia Diária", value=f"{max_energy:,.2f} kWh")
    with col4: st.metric(label="📉 Mínima de Energia Diária", value=f"{min_energy:,.2f} kWh")
    with col5: st.metric(label="📊 Desvio Padrão", value=f"{std_dev_energy:,.2f} kWh")
    with col6: st.metric(label="💡 Eficiência (%)", value=f"{efficiency:,.2f}%")

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

# Função para exibir gráfico de barras de energia por semana
def plot_energy_by_week(df, selected_year):
    """Exibe gráfico de barras com a energia gerada por semana"""
    # Adiciona a coluna de semana do ano
    df["Week"] = df["Date"].dt.isocalendar().week
    # Filtrar os dados para o ano selecionado
    weekly_data = df[df["Year"] == selected_year].groupby("Week")["Energy"].sum().reset_index()

    # Criar gráfico de barras para energia gerada por semana
    fig = create_bar_chart(weekly_data, "Week", "Energy", f"Energia Gerada por Semana ({selected_year})", "Semana", "Energia Gerada (kWh)")
    st.plotly_chart(fig)

# Função para exibir gráfico de linha de energia acumulada por semana
def plot_cumulative_energy_by_week(df, selected_year):
    """Exibe gráfico de linha de energia acumulada por semana"""
    # Adiciona a coluna de semana do ano
    df["Week"] = df["Date"].dt.isocalendar().week
    # Filtrar os dados para o ano selecionado
    weekly_data = df[df["Year"] == selected_year].groupby("Week")["Energy"].sum().reset_index()

    # Criar gráfico de linha para energia acumulada por semana
    fig_line = px.line(weekly_data, x="Week", y="Energy", title=f"Geração Acumulada de Energia por Semana ({selected_year})",
                       labels={"Week": "Semana", "Energy": "Geração Acumulada (kWh)"}, template="plotly_dark")

    fig_line.update_traces(mode='lines+markers', line=dict(color="#00bcd4", width=2),
                           marker=dict(size=6, color="#ff5722", line=dict(width=1, color="white")))

    fig_line.update_layout(
        title=dict(text=f"Geração Acumulada de Energia por Semana ({selected_year})", x=0.5, font=dict(size=16, color="#ffffff")),
        xaxis=dict(title="Semana", showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Geração Acumulada (kWh)", showgrid=True, zeroline=True, zerolinewidth=1, zerolinecolor="gray", tickfont=dict(color="#ffffff")),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40)
    )

    st.plotly_chart(fig_line)

# Função para exibir gráfico de quadrantes (semanal)
def plot_quadrant_by_week(filtered_data, selected_year):
    """Exibe gráfico de quadrantes comparativo semanal"""
    # Agrupar por semana e dia
    quadrante_data = filtered_data.pivot_table(index="Week", columns="Day", values="Energy", aggfunc="sum", fill_value=0)
    fig_quadrante = go.Figure()

    # Adicionando os pontos de quadrante
    for week in quadrante_data.index:
        fig_quadrante.add_trace(go.Scatter(
            x=quadrante_data.columns,
            y=[str(week)] * len(quadrante_data.columns),
            mode='markers',
            marker=dict(size=10, color=quadrante_data.loc[week].values, colorscale='teal', showscale=True,
                        colorbar=dict(title="Energia (kWh)", tickvals=[0, 10, 20, 30], ticktext=["0", "10", "20", "30"])),
            text=quadrante_data.loc[week].values,
            hoverinfo="text",
            name=str(week),
        ))

    fig_quadrante.update_layout(
        title=f"Quadrante de Produção de Energia por Semana ({selected_year})",
        title_font=dict(size=18, color="#ffffff"),
        xaxis=dict(title="Dia", title_font=dict(size=14, color="#ffffff"),
                   showgrid=False, tickmode='linear', ticks="outside", tickwidth=2, tickangle=45, tickfont=dict(color="#ffffff")),
        yaxis=dict(title="Semana", title_font=dict(size=14, color="#ffffff"),
                   showgrid=False, tickfont=dict(color="#ffffff"), type='category'),
        plot_bgcolor="#181818", paper_bgcolor="#181818", margin=dict(l=40, r=40, t=40, b=40),
        colorway=["#007bff"]
    )

    st.plotly_chart(fig_quadrante)

# Função principal para exibir os gráficos
def display_tabs(df):
    """Exibe os gráficos com base no filtro de Mês, Semana, Ano ou Total"""
    st.subheader("📅 Histórico de Dados")
    filter_option = st.sidebar.radio("Selecione a visualização", ["Dia", "Semana", "Mês", "Ano", "Total"])

    # Barra lateral para selecionar o ano (se for Semana)
    if filter_option == "Semana":
        selected_year = st.sidebar.selectbox("Selecione o ano", range(2023, 2026))
        filtered_data = df[df["Year"] == selected_year]

        if not filtered_data.empty:
            st.write(f"📈 Dados de geração de energia para o ano {selected_year}")
            # Exibir os gráficos semanais
            plot_energy_by_week(filtered_data, selected_year)
            plot_cumulative_energy_by_week(filtered_data, selected_year)
            plot_quadrant_by_week(filtered_data, selected_year)

        else:
            st.warning("⚠️ Nenhum dado disponível para este período.")

    elif filter_option == "Mês":
        col1, col2 = st.sidebar.columns(2)
        with col1: selected_month = st.selectbox("Selecione o mês", range(1, 13), format_func=lambda x: f"{x:02d}")
        with col2: selected_year = st.selectbox("Selecione o ano", range(2023, 2026))
        filtered_data = df[(df["Year"] == selected_year) & (df["Month"] == selected_month)]

        if not filtered_data.empty:
            daily_data = filtered_data.groupby("Day")["Energy"].sum().reset_index()
            st.write(f"📈 Dados de geração de energia para {selected_year}-{selected_month:02d}")
            x = daily_data["Day"]
            y = daily_data["Energy"]
            slope, intercept = polyfit(x, y, 1)

            display_performance_indicators(daily_data)
            plot_energy_bar_chart(daily_data, x, slope, intercept)
            plot_cumulative_energy_graph(daily_data)

        else:
            st.warning("⚠️ Nenhum dado disponível para este período.")

    elif filter_option == "Ano":
        selected_year = st.sidebar.selectbox("Selecione o ano", range(2023, 2026))
        filtered_data = df[df["Year"] == selected_year]

        if not filtered_data.empty:
            daily_data = filtered_data.groupby("Day")["Energy"].sum().reset_index()
            st.write(f"📈 Dados de geração de energia para o ano {selected_year}")
            x = daily_data["Day"]
            y = daily_data["Energy"]
            slope, intercept = polyfit(x, y, 1)

            display_performance_indicators(daily_data)
            plot_energy_bar_chart(daily_data, x, slope, intercept)
            plot_cumulative_energy_graph(daily_data)
            # TODO - verificar por que não está exibindo o gráfico de quadrantes
            plot_quadrant_graph(filtered_data, selected_year)  # Exibindo o gráfico de quadrantes para o ano selecionado

        else:
            st.warning("⚠️ Nenhum dado disponível para este período.")

    elif filter_option == "Total":
        plot_total_by_year(df)
        plot_comparative_months_by_year_line(df)
        plot_area_stack_by_year(df)
        plot_scatter_by_year(df)
        plot_candlestick_by_month(df)

if uploaded_file:
    df = load_data(uploaded_file)
    display_tabs(df)
