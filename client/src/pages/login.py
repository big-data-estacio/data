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
          

          blocked_user = db_blocked.get(username)
          if blocked_user:
            st.error("Este usuário está bloqueado. Por favor, entre em contato com o suporte para mais informações.")
            return False
          
          elif db_blocked and db_blocked['password'] == password:
            st.error("As credenciais fornecidas estão associadas a uma conta bloqueada. Por favor, escolha um nome de usuário e senha diferentes.")
            return False
          elif username != "" and password != "":
              st.error("Nome de usuário ou senha incorretos.")
              st.info("Se você esqueceu sua senha, entre em contato com o administrador.")
              st.markdown("""
              <style>
                  .container {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    padding: 2rem;
                  }

                  .form-group {
                    width: 100%;
                    margin-bottom: 1rem;
                  }

                  .form-control {
                    width: 100%;
                    padding: 0.75rem;
                    font-size: 1rem;
                    border-radius: 0.25rem;
                    border: 1px solid #ced4da;
                  }

                  .form-control:focus {
                    outline: none;
                    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
                    border-color: #80bdff;
                  }

                  .btn {
                    display: inline-block;
                    font-weight: 400;
                    color: #212529;
                    text-align: center;
                    vertical-align: middle;
                    user-select: none;
                    background-color: transparent;
                    border: 1px solid transparent;
                    padding: 0.375rem 0.75rem;
                    font-size: 1rem;
                    line-height: 1.5;
                    border-radius: 0.25rem;
                    transition: color 0.15s ease-in-out,
                                background-color 0.15s ease-in-out,
                                border-color 0.15s ease-in-out,
                                box-shadow 0.15s ease-in-out;
                  }

                  .btn-primary {
                      color: #fff;
                      background-color: #007bff;
                      border-color: #007bff;
                  }

                  .btn-primary:hover {
                      color: #fff;
                      background-color: #0069d9;
                      border-color: #0062cc;
                  }

                  .btn-primary:focus {
                      color: #fff;
                      background-color: #0069d9;
                      border-color: #0062cc;
                      box-shadow: 0 0 0 0.2rem rgba(38, 143, 255, 0.5);
                  }
              </style>
              """, unsafe_allow_html=True)

              st.header("Contact")

              contact_form = """
                <div class="container">
                  <form id="contact-form" action="https://formsubmit.co/{}" method="POST">
                    <div class="form-group">
                      <input class="form-control" type="text" name="name" placeholder="Your name" required>
                    </div>
                    <div class="form-group">
                      <input class="form-control" type="email" name="email" placeholder="Your email" required>
                    </div>
                    <div class="form-group">
                      <textarea class="form-control" name="message" placeholder="Your message here"></textarea>
                    </div>
                    <div class="form-group">
                      <button class="btn btn-primary" type="submit" onclick="validateForm(event)">Send</button>
                    </div>
                  </form>
                </div>
                """.format("estevamsouzalaureth@gmail.com")  # Substitua o endereço de e-mail aqui

              javascript_code = """
                <script>
                  function validateForm(event) {
                    var form = document.getElementById('contact-form');
                    var nameInput = form.elements['name'];
                    var emailInput = form.elements['email'];
                    var messageInput = form.elements['message'];

                    if (nameInput.value.trim() === '' || emailInput.value.trim() === '' || messageInput.value.trim() === '') {
                        event.preventDefault();
                        alert('Por favor, preencha todos os campos do formulário.');
                    } else {
                        animateSubmitButton();
                    }
                  }

                  function animateSubmitButton() {
                    var submitButton = document.querySelector('.btn-primary');
                    submitButton.innerHTML = 'Sending...';
                    submitButton.classList.add('animate__animated', 'animate__fadeOut');

                    setTimeout(function() {
                        submitButton.innerHTML = 'Sent!';
                        submitButton.classList.remove('animate__fadeOut');
                        submitButton.classList.add('animate__zoomIn');
                    }, 2000);
                  }
                </script>
                """

              st.markdown(contact_form + javascript_code, unsafe_allow_html=True)

  return False