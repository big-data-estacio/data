import logging
import altair as alt
import pandas as pd
import streamlit as st
from deta import Deta


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
db_deta_bebidas = deta.Base("bebidas")

def inserir_bebida(id, nome, preco, quantidade, descricao, total_vendas, quantidade_vendas):
              # Get database
  db_bebidas = deta.Base("bebidas")

  # Put new drink into the database
  db_bebidas.put({
      "key": id,
      "nome": nome,
      "preco": preco,
      "quantidade": quantidade,
      "descricao": descricao,
      "total_vendas": total_vendas,
      "quantidade_vendas": quantidade_vendas
  })

  st.success('Bebida inserida com sucesso!')

  # Get the "bebidas" database
  db_bebidas = deta.Base("bebidas")

  # Ask the user if they want to see the bubble chart
  show_chart = st.radio('Deseja visualizar o gráfico de bolhas para as bebidas?', ('Sim', 'Não'))

  if show_chart == 'Sim':
    st.markdown("##### CLASSIFICAÇÃO DE BEBIDAS ★★★★★")

    # Fetch data from the "bebidas" database and convert it to a DataFrame
    fetch_response = db_bebidas.fetch()
    data = [item for item in fetch_response.items]
    df_bebidas = pd.DataFrame(data)

    # Create a bubble chart with price on the x-axis, quantity sold on the y-axis, and bubble size representing total sales
    chart = alt.Chart(df_bebidas).mark_circle().encode(
        x=alt.X('preco', title='Preço'),
        y=alt.Y('quantidade_vendas', title='Quantidade Vendida'),
        size=alt.Size('total_vendas', title='Total de Vendas'),
        color=alt.Color('nome', title='Bebida'),
        tooltip=['nome', 'preco', 'quantidade_vendas', 'total_vendas']
    ).properties(width=700, height=500)

    # Display the chart
    st.altair_chart(chart)
