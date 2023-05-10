from datetime import datetime
import altair as alt
import pandas as pd
import streamlit as st
from deta import Deta


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
db = deta.Base("data")
# TODO - Conecte-se às bases de dados
db_deta_reservas = deta.Base("reservasClientes")


def reservar():
    st.header("Reservas")
    st.header("Faça sua Reserva")
    identificar = st.text_input("Coloque o id de identificação para a sua reserva:")
    nome = st.text_input("Nome Completo:")
    data_str = st.date_input("Data da Reserva:")
    reservas_por_data = st.number_input("Quantidade de reservas:", min_value=1, value=1)

    # Verifica se todos os campos foram preenchidos
    if nome and data_str and reservas_por_data:
      # Salva os dados da reserva
      if st.button("Reservar"):
        data = datetime.combine(data_str, datetime.min.time())
        nova_reserva = {"key": identificar, "NOME": nome, "DATA": data.isoformat(), "QTDRESERVAS": reservas_por_data}
        db_deta_reservas.put(nova_reserva)
        st.success("Reserva feita com sucesso!")

      # Obtém todas as reservas do banco de dados
      todas_reservas = []
      last_key = None

      while True:
        fetch_response = db_deta_reservas.fetch(last=last_key)
        todas_reservas.extend(fetch_response.items)
        if fetch_response.last is None:
          break
        last_key = fetch_response.last

      reservas_df = pd.DataFrame(todas_reservas)

      # Converte a coluna 'DATA' para datetime
      reservas_df["DATA"] = pd.to_datetime(reservas_df["DATA"])

      # Agrupa as reservas por data e soma a quantidade de reservas para cada data
      reservas_agrupadas = reservas_df.groupby('DATA')['QTDRESERVAS'].sum().reset_index()

      # Plota um gráfico de linha com a data no eixo x e a quantidade de reservas no eixo y
      chart = alt.Chart(reservas_agrupadas).mark_line().encode(
        x='DATA:T',
        y='QTDRESERVAS:Q',
        tooltip=['DATA:T', 'QTDRESERVAS:Q']
      ).properties(
        width=700,
        height=400
      )

      st.altair_chart(chart, use_container_width=True)
    else:
      st.warning("Preencha todos os campos para fazer uma reserva.")