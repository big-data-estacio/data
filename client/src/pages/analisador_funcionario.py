import logging
import pandas as pd
import base64
import streamlit as st
import time
import plotly.graph_objects as go
from deta import Deta


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
# TODO - Conecte-se às bases de dados
db_deta_funcionarios = deta.Base("funcionario")

def employee_performance_analysis():
  # Obtém todos os funcionários do banco de dados
  all_funcionarios = list(db_deta_funcionarios.fetch().items)
  dataFunc = pd.DataFrame(all_funcionarios)

  st.subheader("Cadastro de Funcionários")

  # Adicionar funcionário
  st.write("Preencha os dados do funcionário abaixo:")
  nome = st.text_input("NOME")
  cargo = st.selectbox("Cargo", ["Gerente", "Garçom", "Cozinheiro", "Auxiliar de cozinha"])
  ESPECIALIDADE = st.text_input("ESPECIALIDADE")
  salario = st.number_input("Salário", value=0.0, step=0.01)
  dias_trabalhados = st.number_input("DIASTRABALHADOS", value=0, step=1)
  salario_dia = salario / dias_trabalhados if dias_trabalhados != 0 else 0

  # Botão para adicionar funcionário
  if st.button("Adicionar funcionário"):
    # Verifica se o funcionário já foi cadastrado anteriormente
    if nome in dataFunc["NOME"].tolist():
        st.warning("Funcionário já cadastrado")
    else:
      # Adiciona o funcionário ao banco de dados
      # id = 1 if dataFunc.empty else dataFunc.iloc[-1]['ID'] + 1
      db_deta_funcionarios.put({
        # "ID": id,
        "NOME": nome,
        "Cargo": cargo,
        "ESPECIALIDADE": ESPECIALIDADE,
        "DIASTRABALHADOS": dias_trabalhados,
        "SALÁRIODIA": salario_dia
      })
      st.success("Funcionário cadastrado com sucesso!")

  # Lista de funcionários
  st.write("Lista de funcionários:")
  st.dataframe(dataFunc[["NOME", "Cargo", "ESPECIALIDADE", "DIASTRABALHADOS", "SALÁRIODIA"]])

  # Cálculo do salário dos funcionários
  dataFunc["Salário a receber"] = dataFunc["SALÁRIODIA"] * dataFunc["DIASTRABALHADOS"] * 1.10

  # Gráfico de salário dos funcionários
  fig = go.Figure()
  fig.add_trace(go.Bar(x=dataFunc["NOME"],
                      y=dataFunc["Salário a receber"],
                      marker_color='purple'))
  fig.update_layout(title="Salário dos Funcionários",
                    xaxis_title="NOME",
                    yaxis_title="Salário a Receber")
  st.plotly_chart(fig)

  # Análise de desempenho dos funcionários
  st.subheader("Análise de desempenho dos funcionários")

  # Selecionar o funcionário para analisar
  selected_func = st.selectbox("Selecione um funcionário para análise:", dataFunc["NOME"].tolist())

  # Mostrar os dados do funcionário selecionado
  selected_func_data = dataFunc[dataFunc["NOME"] == selected_func]
  st.write(f"Dados de desempenho de {selected_func}:")
  st.write(selected_func_data)

  # Gráfico de desempenho do funcionário selecionado
  fig = go.Figure()
  fig.add_trace(go.Bar(x=selected_func_data["Cargo"],
                      y=selected_func_data["DIASTRABALHADOS"],
                      marker_color='green'))
  fig.update_layout(title=f"Desempenho de {selected_func}",
                    xaxis_title="Cargo",
                    yaxis_title="DIASTRABALHADOS")
  st.plotly_chart(fig)