import logging
import pandas as pd
import plotly.express as px
import streamlit as st
from deta import Deta


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
db_deta_previsao_demanda = deta.Base("previsao_demanda")


def previsao_demanda():
  st.subheader("Previsão de Demanda")

  # Fetch data from Deta Base
  demand_data = list(db_deta_previsao_demanda.fetch())
  demand_data = pd.DataFrame(demand_data)

  # Create a list with unique dates
  dates = demand_data["Data"].unique().tolist()

  # Select the date for analysis
  selected_date = st.selectbox("Selecione a data para análise:", dates)

  # Filter the data by the selected date
  filtered_data = demand_data[demand_data["Data"] == selected_date]

  # Create a bar chart with the number of customers per hour
  fig = px.bar(filtered_data, x="Hora", y="Clientes")
  fig.update_layout(title="Previsão de Demanda - Clientes por Hora",
                    xaxis_title="Hora",
                    yaxis_title="Número de Clientes")
  st.plotly_chart(fig)

  # Forecast of demand
  average_clients = int(filtered_data["Clientes"].mean())
  st.write(f"A média de clientes para o dia {selected_date} é de {average_clients} clientes.")

  # Recommendation of resources
  if average_clients <= 50:
    st.success("Recomendamos que sejam alocados recursos para atender até 50 clientes.")
  elif average_clients > 50 and average_clients <= 100:
    st.warning("Recomendamos que sejam alocados recursos para atender entre 50 e 100 clientes.")
  else:
    st.error("Recomendamos que sejam alocados recursos para atender mais de 100 clientes.")

  # Saving the data in CSV file is not required when using Deta Base
  # You can directly use the Deta Base for future operations

  # Ask if you want to see the full data from the Deta Base
  if st.button("Ver dados completos do Deta Base"):
    st.dataframe(demand_data)
