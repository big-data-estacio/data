import logging
import plotly.express as px
import streamlit as st


def vendas_por_categoria(dados):
  # Gráfico de bolhas
  fig = px.scatter(dados, x='Categoria', y='Vendas',
                    size='Preço Médio', hover_name='Categoria')
  st.plotly_chart(fig)

  # Salvar dados em arquivo
  dados.to_csv('client/src/data/vendasCategorias.csv', index=False)

  # Projeção de vendas
  st.subheader('Projeção de vendas para a próxima semana')

  # Calcular média de vendas e preço médio
  media_vendas = dados['Vendas'].mean()
  media_preco = dados['Preço Médio'].mean()

  # Calcular projeção de vendas
  projecao_vendas = media_vendas * 1.1

  # Calcular projeção de receita
  projecao_receita = projecao_vendas * media_preco

  # Exibir resultados
  st.write('Média de vendas da última semana:', media_vendas)
  st.write('Média de preço da última semana:', media_preco)
  st.write('Projeção de vendas para a próxima semana:', projecao_vendas)
  st.write('Projeção de receita para a próxima semana:', projecao_receita)

  # Gráfico de barras
  grafico = px.bar(dados, x='Categoria', y='Vendas', color='Categoria')
  st.plotly_chart(grafico)
