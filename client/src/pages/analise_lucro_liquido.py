import pandas as pd
import streamlit as st
from deta import Deta
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)


db_deta_lucroliquido = deta.Base("lucroliquido")


def calculate_net_profit():
  # Buscando todos os dados do banco Deta
  items = db_deta_lucroliquido.fetch().items

  # Se houver itens, calcular o lucro líquido e exibi-lo
  if items:
    # Criando um DataFrame com os dados
    data = pd.DataFrame(items)

    # Convertendo a coluna data para o tipo datetime
    data['data'] = pd.to_datetime(data['data'])
    
    # Ordenando o dataframe pela data
    data.sort_values(by='data', inplace=True)
    
    # Calculando o lucro líquido
    lucro_liquido = data['lucro_liquido'].sum()
    
    # Calculando a média mensal do lucro líquido
    monthly_avg_profit = data.set_index('data').resample('M').mean()

    # Exibindo o lucro líquido total e a média mensal
    st.write(f"O lucro líquido total é: R$ {lucro_liquido:.2f}")
    st.write(f"A média mensal do lucro líquido é: R$ {monthly_avg_profit['lucro_liquido'].mean():.2f}")
    
    # Plotando a série temporal do lucro líquido
    st.line_chart(data.set_index('data')['lucro_liquido'])
    
    # Criando e treinando um modelo ARIMA para fazer uma previsão do lucro líquido
    # model = ARIMA(data.set_index('data')['lucro_liquido'], order=(5,1,0))
    # model_fit = model.fit()

    # # Fazendo a previsão para o próximo mês
    # forecast, stderr, conf_int = model_fit.forecast(steps=1)
    
    # st.write(f"A previsão do lucro líquido para o próximo mês é: R$ {forecast[0]:.2f}")