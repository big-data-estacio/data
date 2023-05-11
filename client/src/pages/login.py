import streamlit as st
from deta import Deta
from PIL import Image


logo_img = Image.open('client/src/public/if-logo.png')

# Load environment variables
DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"

# Initialize Deta
deta = Deta(DETA_KEY)

db = deta.Base("data")
db_blocked = deta.Base("userbloqueado")


def authenticate_user(username, password):
  user = db.get(username)
  if user:
    if user['password'] == password:
      return True
    else:
        # Se a senha estiver incorreta, aumentar o contador de falhas de login
        user['failed_logins'] = user.get('failed_logins', 0) + 1
        
        # Se o usuário falhou na autenticação 3 vezes, bloqueá-lo
        if user['failed_logins'] >= 3:
          db_blocked.put(user)  # Adicionando o usuário ao banco de dados de usuários bloqueados
          db.delete(username)  # Excluindo o usuário do banco de dados de usuários
          # send_email(user)  # Enviar um email para o desenvolvedor
          st.error("Usuário bloqueado após 3 tentativas falhas de login.")
          return False
        
        db.put(user)  # Atualizando o contador de falhas de login no banco de dados de usuários
        return False
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
        st.info("Se você esqueceu sua senha, entre em contato com o administrador.")
        if st.button("Deseja enviar um email para o administrador?"):
          st.markdown("""
          <style>
            ul[class="css-j7qwjs e1fqkh3o7"]{
              position: relative;
              padding-top: 2rem;
              display: flex;
              justify-content: center;
              flex-direction: column;
              align-items: center;
            }
            .css-17lntkn {
              font-weight: bold;
              font-size: 18px;
              color: grey;
            }
            .css-pkbazv {
              font-weight: bold;
              font-size: 18px;
            }
          </style>""", unsafe_allow_html=True)

          st.header("Contact")

          contact_form = """
            <form action="https://formsubmit.co/{}" method="POST">
              <input type="hidden" name="_captcha" value="false">
              <input type="text" name="name" placeholder="Your name" required>
              <br>
              <input type="email" name="email" placeholder="Your email" required>
              <br>
              <textarea name="message" placeholder="Your message here"></textarea>
              <br>
              <button type="submit">Send</button>
            </form>
            """.format("estevamsouzalaureth@gmail.com")  # Substitua o endereço de e-mail aqui
          st.markdown(contact_form, unsafe_allow_html=True)

    return False