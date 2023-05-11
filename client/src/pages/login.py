import streamlit as st
from deta import Deta
from PIL import Image


logo_img = Image.open('client/src/public/if-logo.png')

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

  st.image(logo_img, use_column_width=True)
  username = st.text_input("Nome de usuário", key="username_input")
  password = st.text_input("Senha", type="password", key="password_input")

  if st.button("Login"):
    if authenticate_user(username, password):
      st.session_state.logged_in = True
      with st.spinner("Carregando..."):
        st.success("Login efetuado com sucesso!")
        st.balloons()
      return True
    else:
      if username == "" and password == "":
        st.error("Por favor, insira um nome de usuário e senha.")
      elif username != "" and password != "":
        st.error("Nome de usuário ou senha incorretos.")
  return False
