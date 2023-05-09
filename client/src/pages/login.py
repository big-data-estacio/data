############################################################################################
#                                   Packages                                               #
############################################################################################


import streamlit as st
import client.setup as setup
from deta import Deta
from dotenv import load_dotenv
import os


############################################################################################
#                                   Check Requirements                                     #
############################################################################################


# Lista de funções importadas
funcoes_importadas = [
  'streamlit',
  'client.setup',
]

# Verifica se cada função está presente no arquivo requirements.txt
faltando = []
with open('requirements.txt') as f:
  for line in f:
    for funcao in funcoes_importadas:
      if funcao in line:
        break
      else:
        faltando.append(funcao)

# Imprime as funções que não estão presentes no arquivo
if faltando:
  print('As seguintes funções não estão presentes no arquivo requirements.txt:')
  print('\n'.join(faltando))
else:
  print('Todas as funções importadas estão presentes no arquivo requirements.txt.')


############################################################################################
#                                   Functions                                              #
############################################################################################




# Load environment variables
DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"

# Initialize Deta
deta = Deta(DETA_KEY)

# Get database
db = deta.Base("data")


def authenticate_user(username, password):
    user = db.get(username)
    if user and user['password'] == password:
        return True
    else:
        return False


def login_page():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    username = st.text_input("Nome de usuário", key="username_input")
    password = st.text_input("Senha", type="password", key="password_input")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.logged_in = True
            st.empty()
            return True
        else:
            if username == "" and password == "":
                st.error("Por favor, insira um nome de usuário e senha.")
            elif username != "" and password != "":
                st.error("Nome de usuário ou senha incorretos.")
    return False