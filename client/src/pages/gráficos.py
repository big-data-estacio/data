import streamlit as st
import plotly.express as px


def visualizar_graficos(dataBebidas, dataEstoque, dataPratos, dataClientes, data):
  getOption = st.selectbox("Selecione o gráfico que deseja visualizar", [
                            "Gráfico de Pizza", "Gráfico de Dispersão"])

  if getOption == "Gráfico de Pizza":
      st.markdown("### GRÁFICO DE PIZZA")
      st.markdown("###### ESTE É O GRÁFICO DE PIZZA PARA BEBIDAS")
      fig_bebidas = px.pie(dataBebidas, values='preco', names='nome')
      st.plotly_chart(fig_bebidas)

      st.markdown(
          "###### ESTE É O GRÁFICO DE PIZZA PARA O ESTOQUE DE MERCADORIAS")
      fig_estoque = px.pie(dataEstoque, values='QUANTIDADE', names='NOME')
      st.plotly_chart(fig_estoque)

      st.markdown("###### ESTE É O GRÁFICO DE PIZZA PARA PRATOS DA CASA")
      fig_pratos = px.pie(dataPratos, values='PRECO', names='NOME')
      st.plotly_chart(fig_pratos)

      st.markdown(
          "###### ESTE É O GRÁFICO DE PIZZA PARA O TOTAL DE GASTOS DE CLIENTES")
      fig_clientes = px.pie(dataClientes, values='GASTO', names='NOME')
      st.plotly_chart(fig_clientes)

  elif getOption == "Gráfico de Dispersão":
      st.markdown("### GRÁFICO DE DISPERSÃO")
      st.markdown(
          "###### ESTE É O GRÁFICO DE DISPERSÃO PARA TODAS AS COMPARAÇÕES")
      st.vega_lite_chart(data, {
          'mark': {'type': 'circle', 'tooltip': 500},
          'encoding': {
              'x': {'field': 'Restaurant_Name', 'type': 'quantitative'},
              'y': {'field': 'Rating', 'type': 'quantitative'},
              'size': {'field': 'Price_Range', 'type': 'quantitative'},
              'color': {'field': 'Rating', 'type': 'quantitative'},
          },
      })

      st.markdown(
          "###### ESTE É O GRÁFICO DE DISPERSÃO PARA TODAS AS COMPARAÇÕES")
      st.vega_lite_chart(dataEstoque, {
          'mark': {'type': 'circle', 'tooltip': 500},
          'encoding': {
              'x': {'field': 'id', 'type': 'quantitative'},
              'y': {'field': 'quantidade', 'type': 'quantitative'},
              'size': {'field': 'totalVendas', 'type': 'quantitative'},
              'color': {'field': 'totalVendas', 'type': 'quantitative'},
          },
      })

      st.markdown(
          "###### ESTE É O GRÁFICO DE DISPERSÃO PARA TODAS AS COMPARAÇÕES")
      st.vega_lite_chart(dataClientes, {
          'mark': {'type': 'circle', 'tooltip': 500},
          'encoding': {
              'x': {'field': 'id', 'type': 'quantitative'},
              'y': {'field': 'quantidade', 'type': 'quantitative'},
              'size': {'field': 'totalVendas', 'type': 'quantitative'},
              'color': {'field': 'totalVendas', 'type': 'quantitative'},
          },
      })
