import logging
import altair as alt
import pandas as pd
import streamlit as st
from deta import Deta


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
db = deta.Base("data")
# TODO - Conecte-se às bases de dados
db_deta_clientes = deta.Base("cliente")
db_deta_categoriavendas = deta.Base("categoriavendas")
db_deta_reservas = deta.Base("reservasClientes")
db_deta_funcionarios = deta.Base("funcionario")

# TODO - Inserir dados no banco cliente
def inserir_cliente(id, nome, gasto):
  # Insert data into the "cliente" database
  db_deta_clientes.put({
      "ID": id,
      "NOME": nome,
      "GASTO": gasto
  })

  st.success('Cliente cadastrado com sucesso!')
  
  show_chart = st.radio('Deseja visualizar o gráfico de bolhas para o total de gastos dos clientes?', ('Sim', 'Não'))

  if show_chart == 'Sim':
    st.markdown("### Comparação de Clientes")
    st.markdown("Neste gráfico, o tamanho da bolha representa o gasto total de cada cliente.")
    st.markdown("##### CLASSIFICAÇÃO DE DADOS DE CLIENTES ★★★★★")

    # Fetch data from the "cliente" database and convert it to a DataFrame
    fetch_response = db_deta_clientes.fetch()
    data = [item for item in fetch_response.items]
    df_clientes = pd.DataFrame(data)

    # Create a bubble chart with client name on x-axis and total spending on y-axis and bubble size
    chart = alt.Chart(df_clientes).mark_circle().encode(
        x=alt.X('NOME', title='Nome'),
        y=alt.Y('GASTO', title='Gasto'),
        size=alt.Size('GASTO', title='Gasto'),
        color=alt.Color('GASTO', title='Gasto'),
        tooltip=['NOME', 'GASTO']
    ).properties(width=700, height=500)

    # Display the chart
    st.altair_chart(chart)