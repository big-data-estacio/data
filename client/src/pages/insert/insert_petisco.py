import logging
import altair as alt
import pandas as pd
import streamlit as st
from deta import Deta


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
db = deta.Base("data")
# TODO - Conecte-se às bases de dados
db_deta_petiscos = deta.Base("petisco")

# TODO Inserir dados no banco petisco
def inserir_petisco(id, nome, preco, acompanhamento):
  # Insert data into the "petisco" database
  db_deta_petiscos.put({
      "ID": id,
      "NOME": nome,
      "PRECO": preco,
      "ACOMPANHAMENTO": acompanhamento
  })

  st.success('Petisco cadastrado com sucesso!')
  
  show_chart = st.radio('Deseja visualizar o gráfico de bolhas para os petiscos?', ('Sim', 'Não'))

  if show_chart == 'Sim':
    st.markdown("### Comparação de Petiscos")
    st.markdown("Neste gráfico, cada bolha representa um petisco e o tamanho da bolha representa a quantidade em estoque.")
    st.markdown("##### CLASSIFICAÇÃO DE DADOS DE PETISCOS ★★★★★")

    # Fetch data from the "petisco" database and convert it to a DataFrame
    fetch_response = db_deta_petiscos.fetch()
    data = [item for item in fetch_response.items]
    df_petiscos = pd.DataFrame(data)

    # Create a bubble chart with dish name on x-axis, price on y-axis, and color representing the accompaniment
    chart = alt.Chart(df_petiscos).mark_circle(size=100).encode(
        x='NOME',
        y='PRECO',
        color='ACOMPANHAMENTO',
        tooltip=['NOME', 'PRECO', 'ACOMPANHAMENTO']
    ).properties(
        width=600,
        height=400
    )

    # Display the chart
    st.altair_chart(chart, use_container_width=True)