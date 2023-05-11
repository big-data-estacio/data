import pandas as pd
from deta import Deta
import streamlit as st
import plotly.express as px


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)


db_deta_lucrobruto = deta.Base("lucrobruto")


# def fetch_all_items(db):
#   items = []
#   result = db.fetch()
#   for item in result.items:
#       items.extend(item)
#   return items



def analyse_and_add_gross_profit():
  # Buscando todos os dados do banco Deta
  items = db_deta_lucrobruto.fetch().items

  # Se houver itens, calcular o lucro bruto e exibi-lo
  if items:
    # Criando um DataFrame com os dados
    data = pd.DataFrame(items)

    # Convertendo a coluna data para o tipo datetime
    data['data'] = pd.to_datetime(data['data'])
    
    # Ordenando o dataframe pela data
    data.sort_values(by='data', inplace=True)
    
    # Calculando o lucro bruto
    lucro_bruto = data['lucro_bruto'].sum()
    
    # Calculando a média mensal do lucro bruto
    monthly_avg_profit = data.set_index('data').resample('M').mean()

    # Exibindo o lucro bruto total e a média mensal
    st.write(f"O lucro bruto total é: R$ {lucro_bruto:.2f}")
    st.write(f"A média mensal do lucro bruto é: R$ {monthly_avg_profit['lucro_bruto'].mean():.2f}")
    
    # Plotando a série temporal do lucro bruto
    st.line_chart(data.set_index('data')['lucro_bruto'])
    
    # Criando e treinando um modelo ARIMA para fazer uma previsão do lucro bruto
    # model = ARIMA(data.set_index('data')['lucrobruto'], order=(5,1,0))
    # model_fit = model.fit()

    # # Fazendo a previsão para o próximo mês
    # forecast, stderr, conf_int = model_fit.forecast(steps=1)
    
    # st.write(f"A previsão do lucro bruto para o próximo mês é: R$ {forecast[0]:.2f}")







# def analyse_and_add_gross_profit():
#   # Fetch all items from the Deta Base
#   items = fetch_all_items(db_deta_lucrobruto)

#   # Convert the items into a DataFrame
#   df = pd.DataFrame(items)

#   # Calculate the gross profit
#   df["lucro_bruto"] = df["venda"] - df["custo"]

#   # Plot the gross profit
#   fig = px.line(df, x="data", y="lucro_bruto", title="Lucro Bruto ao Longo do Tempo")
#   st.plotly_chart(fig)

#   # Ask the user if they want to add a new sale
#   data = st.date_input("Data da venda:")
#   venda = st.number_input("Valor da venda:")
#   custo = st.number_input("Custo da venda:")

#   # Add a submit button
#   if st.button("Enviar"):
#     # Add the new sale to the Deta Base
#     db_deta_lucrobruto.put({
#         "data": str(data),
#         "venda": venda,
#         "custo": custo
#     })

#     st.success("Venda adicionada com sucesso!")