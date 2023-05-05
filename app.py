import streamlit as st
import client.setup as setup

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


if __name__ == '__main__':
  original_title = '<p style="font-family:Monospace; color:Gray; font-size: 25px;"></p>'
  setup.titlePlaceholder.markdown(original_title, unsafe_allow_html=True)
  
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