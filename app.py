############################################################################################
#                                   Packages                                               #
############################################################################################


import streamlit as st
import client.setup as setup
# import base64
import plotly.express as px
# from client.src.pages.👻_Login import login_page
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'client', 'src', 'pages')))
from login import login_page



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


# def login_page():
#   st.title("Login")

#   username = st.text_input("Nome de usuário", key="username_input")
#   password = st.text_input("Senha", type="password", key="password_input")
#   st.button("Login")

#   if setup.authenticate_user(username, password):
#     st.empty()
#     return True
#   else:
#     if username == "" and password == "":
#       st.error("Por favor, insira um nome de usuário e senha.")
#     elif username != "" and password != "":
#       st.error("Nome de usuário ou senha incorretos.")
#     return False


############################################################################################
#                                   Main                                                   #
############################################################################################


if __name__ == '__main__':
  df = px.data.iris()

  # # @st.experimental_memo
  # def get_img_as_base64(file):
  #     with open(file, "rb") as f:
  #         data = f.read()
  #     return base64.b64encode(data).decode()


  # img = get_img_as_base64("client/src/public/image.jpg")

  # page_bg_img = f"""
  # <style>
  # [data-testid="stAppViewContainer"] > .main {{
  # background-image: url("https://cdn.folhape.com.br/img/pc/1100/1/dn_arquivo/2022/11/copia-de-enquadramento-capa_2.jpg");
  # background-size: 180%;
  # background-position: top left;
  # background-repeat: no-repeat;
  # background-attachment: local;
  # }}

  # [data-testid="stSidebar"] > div:first-child {{
  # background-image: url("data:image/png;base64,{img}");
  # background-position: center; 
  # background-repeat: no-repeat;
  # background-attachment: fixed;
  # }}

  # [data-testid="stHeader"] {{
  # background: rgba(0,0,0,0);
  # }}

  # [data-testid="stToolbar"] {{
  # right: 2rem;
  # }}
  # </style>
  # """

  # st.markdown(page_bg_img, unsafe_allow_html=True)
  
  # st.title("It's summer!")
  # st.sidebar.header("Configuration")

  if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

  if not st.session_state.logged_in:
    logged_in = login_page()

    if logged_in:
        st.session_state.logged_in = True
        st.experimental_rerun()
  else:
    st.empty()
    setup.mainLogin()
    if st.button("Logout"):
      st.session_state.logged_in = False
      st.experimental_rerun()
      