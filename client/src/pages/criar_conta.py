import logging
import streamlit as st
from deta import Deta

# Load environment variables
DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
# Initialize Deta
deta = Deta(DETA_KEY)
# Get database
db = deta.Base("data")

db_blocked = deta.Base("userbloqueado")


def insert_data(username, name, password):
    return db.put(
    {
        "key": username,
        "name": name,
        "password": password
    }
  )


def criar_conta():
    logging.info('O cliente começou a criar uma conta')

    # Solicitar nome de usuário e senha para criar uma conta
    new_username = st.text_input("Nome de usuário", key="new_username_input")
    new_password = st.text_input("Senha", type="password", key="new_password_input")

    if st.button("Criar conta"):
        # Verificar se o nome de usuário já existe
        if db.get(new_username):
            st.error("Nome de usuário já existe. Por favor, escolha outro.")
            return False
        
        # Verificar se o nome de usuário e senha existem no banco de dados de usuários bloqueados
        blocked_user = db_blocked.get(new_username)
        if blocked_user and blocked_user['password'] == new_password:
          st.error("As credenciais fornecidas estão associadas a uma conta bloqueada. Por favor, escolha um nome de usuário e senha diferentes.")
          return False

        # Caso contrário, adicionar o novo nome de usuário e senha no banco de dados
        insert_data(new_username, new_username, new_password) 

        st.success("Conta criada com sucesso!")
        st.balloons()
        return True

    return False
