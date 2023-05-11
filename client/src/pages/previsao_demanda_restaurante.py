from deta import Deta
import logging
import pandas as pd
import plotly.express as px
import streamlit as st


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
db_deta_previsao_demanda = deta.Base("previsao_demanda")


def fetch_all_items(db):
    items = []
    for item in db.fetch():
        items.extend(item)
    return items

def previsao_demanda():
    st.subheader("Previsão de Demanda")

    # Carrega os dados
    demand_data = fetch_all_items(db_deta_previsao_demanda)
    demand_data = pd.DataFrame(demand_data)

    # Verifica se a coluna 'Data' existe e, em caso afirmativo, se está no formato correto
    if 'Data' not in demand_data.columns:
        st.error("A coluna 'Data' não foi encontrada nos dados.")
        return
    else:
        # Converte a coluna 'Data' para o formato datetime, caso esteja como string
        demand_data['Data'] = pd.to_datetime(demand_data['Data'])

    # Cria uma lista com as datas únicas
    datas = demand_data["Data"].dt.date.unique().tolist()

    # Seleciona a data para análise
    data_selecionada = st.selectbox("Selecione a data para análise:", datas)

    # Filtra os dados pela data selecionada
    data_filtrada = demand_data[demand_data["Data"].dt.date == data_selecionada]

    # Cria um gráfico de barras com a quantidade de clientes por hora
    fig = px.bar(data_filtrada, x="Hora", y="Clientes")
    fig.update_layout(title="Previsão de Demanda - Clientes por Hora",
                    xaxis_title="Hora",
                    yaxis_title="Número de Clientes")
    st.plotly_chart(fig)

    # Previsão de demanda
    media_clientes = int(data_filtrada["Clientes"].mean())
    st.write(f"A média de clientes para o dia {data_selecionada} é de {media_clientes} clientes.")

    # Recomendação de recursos
    if media_clientes <= 50:
        st.success("Recomendamos que sejam alocados recursos para atender até 50 clientes.")
    elif media_clientes > 50 and media_clientes <= 100:
        st.warning("Recomendamos que sejam alocados recursos para atender entre 50 e 100 clientes.")
    else:
        st.error("Recomendamos que sejam alocados recursos para atender mais de 100 clientes.")

    # Perguntar se deseja ver os dados completos do arquivo client/src/data/previsao_demanda.csv
    if st.button("Ver todos os dados do banco de dados Deta"):
        demand_data = fetch_all_items(db_deta_previsao_demanda)
        demand_data = pd.DataFrame(demand_data)
        st.dataframe(demand_data)