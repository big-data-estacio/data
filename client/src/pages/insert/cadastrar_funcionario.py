import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from deta import Deta


DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
db_deta_funcionarios = deta.Base("funcionario")


def cadastrarFuncionario():
  logging.info('O cliente acessou a aba de cadastramento de funcionário')
  st.subheader("Cadastro de Funcionários")

  # Criação do dataframe
  dataFunc = pd.DataFrame(columns=['NOME' , 'Cargo', 'ESPECIALIDADE', 'SALÁRIODIA', 'DIASTRABALHADOS'])
  
  # Adicionar funcionário
  st.write("Preencha os dados do funcionário abaixo:")
  nome = st.text_input("NOME")
  cargo = st.selectbox("Cargo", ["Gerente", "Garçom", "Cozinheiro", "Auxiliar de cozinha"])
  ESPECIALIDADE = st.text_input("ESPECIALIDADE")
  salario_dia = st.number_input("SALÁRIODIA", value=0.0, step=0.01)
  dias_trabalhados = st.number_input("DIASTRABALHADOS", value=0, step=1)

  if st.button("Adicionar funcionário"):
    # Verifica se o funcionário já foi cadastrado anteriormente
    if nome in dataFunc["NOME"].tolist():
        st.warning("Funcionário já cadastrado")
    else:
      # Adiciona o funcionário ao dataframe
      dataFunc = dataFunc.append({
        "NOME": nome,
        "Cargo": cargo,
        "ESPECIALIDADE": ESPECIALIDADE,
        "SALÁRIODIA": salario_dia,
        "DIASTRABALHADOS": dias_trabalhados
      }, ignore_index=True)
      st.success("Funcionário cadastrado com sucesso!")

      # Adicionar os dados ao banco de dados Deta
      db_deta_funcionarios.put({
        "NOME": nome,
        "Cargo": cargo,
        "ESPECIALIDADE": ESPECIALIDADE,
        "SALÁRIODIA": salario_dia,
        "DIASTRABALHADOS": dias_trabalhados
      })

  st.write("Lista de funcionários:")
  st.dataframe(dataFunc)

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
