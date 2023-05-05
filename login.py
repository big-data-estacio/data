############################################################################################
#                                   Packages                                               #
############################################################################################


import streamlit as st
import client.setup as setup


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


def login_page():
  st.title("Login")

  username = st.text_input("Nome de usuário", key="username_input")
  password = st.text_input("Senha", type="password", key="password_input")
  st.button("Login")

  if setup.authenticate_user(username, password):
    st.empty()
    return True
  else:
    if username == "" and password == "":
      st.error("Por favor, insira um nome de usuário e senha.")
    elif username != "" and password != "":
      st.error("Nome de usuário ou senha incorretos.")
    return False
