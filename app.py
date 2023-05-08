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
#                                   Main                                                   #
############################################################################################


if __name__ == '__main__':
  df = px.data.iris()

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
      