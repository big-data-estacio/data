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

  import base64

  def get_img_as_base64(file):
      with open(file, "rb") as f:
          data = f.read()
      return base64.b64encode(data).decode()


  page_bg_img = f"""
  <style>
  [data-testid="stAppViewContainer"] > .main {{
  background-size: 180%;
  background-position: top left;
  background-repeat: no-repeat;
  background-attachment: local;
  /* Adicionado: cor de fundo verde claro */
  background-color: rgba(144, 238, 144, 0.5);
  }}

  [data-testid="stSidebar"] > div:first-child {{
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  }}

  [data-testid="stHeader"] {{
  background: rgba(0,0,0,0);
  }}

  [data-testid="stToolbar"] {{
  right: 2rem;
  }}
  </style>
  """

  st.markdown(page_bg_img, unsafe_allow_html=True)

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
