#                               File Name: app.py                                #
#                           Creation Date: 5 de maio, 2023                               #
#                         Source Language: Python                                          #
#         Repository:    https://github.com/big-data-project/data.git                      #
#                              --- Code Description ---                                    #
#         Streamlit app designed for visualizing U.S. real estate data and market trends   #
############################################################################################

############################################################################################
#                                   Packages                                               #
############################################################################################


# from client.bebidasSpark import BebidasCsvReader
# from client.pratosSpark import PratosCsvReader
# from client.reservasSpark import ReservasCsvReader
# from client.mercadoriasSpark import EstoqueMercadoriasCsvReader
# from client.previsaoVendasSpark import PrevisaoVendasCsvReader
# from client.funcionariosSpark import FuncionariosCsvReader
# from client.clientesSpark import CadastroCsvReader
# import requests
# import datetime
# from plotly.subplots import make_subplots
# from abc import ABC, abstractmethod
# from imaplib import _Authenticator
# import streamlit_authenticator as stauth
# from collections import UserString
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col


# Lista de funções importadas
funcoes_importadas = [
    'UserString',
    'hashlib',
    'smtplib',
    'yagmail',
    'requests',
    'csv',
    'os',
    'logging',
    'altair',
    'pydeck',
    'pandas',
    'numpy',
    'plotly.express',
    'plotly.graph_objects',
    'dotenv',
    'matplotlib.pyplot',
    'datetime',
    'streamlit',
    'time',
    'streamlit_authenticator',
    'make_subplots',
    'Image',
    'hydralit_components',
    'SparkSession',
    'col',
    'StructType',
    'StructField',
    'StringType',
    'IntegerType',
    'FloatType',
    'ABC',
    'abstractmethod'
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


import hashlib
# import json
import smtplib
import csv
import os
import logging
import altair as alt
import pydeck as pdk
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import streamlit as st
import time
import plotly.graph_objects as go
from PIL import Image
import hydralit_components as hc
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Criar a sessão do Spark
# spark = SparkSession.builder.appName("App").getOrCreate()
# spark.sparkContext.setLogLevel("OFF")


############################################################################################
#                                   Variáveis                                              #
############################################################################################

MAX_ATTEMPTS = 3  # número máximo de tentativas
df_bebidas = pd.read_csv('client/src/data/bebidas.csv')
df_estoque = pd.read_csv('client/src/data/estoque_mercadorias.csv')
df_clientes = pd.read_csv('client/src/data/total_clientes.csv')
URL = "client/src/data/restaurante.csv"
BEBIDAS = "client/src/data/bebidas.csv"
ESTOQUE = "client/src/data/estoque_mercadorias.csv"
PRATOS = "client/src/data/pratos.csv"
CLIENTES = "client/src/data/total_clientes.csv"
FUNCIONARIOS = "client/src/data/funcionarios.csv"
RESERVAS = "client/src/data/reservas.csv"
VENDASCATEGORIAS = "client/src/data/vendasCategorias.csv"
dadosClientes = pd.read_csv('client/src/data/total_clientes.csv')


# coloca os nomes dos usuários em uma lista
names = ['user-1', 'user-2', 'user-3', 'user-4', 'user-5', 'user-6', 'user-7', 
        'user-8', 'user-9', 'user-10', 'admin']

# coloca os nomes de usuário em uma lista
usernames = ['user-1', 'user-2', 'user-3', 'user-4', 'user-5', 'user-6', 'user-7', 
            'user-8', 'user-9', 'user-10', 'admin']

# coloca as senhas em uma lista
passwords = ['password-1', 'password-2', 'password-3', 'password-4', 'password-5', 'password-6', 'password-7',
            'password-8', 'password-9', 'password-10', 'admin00']


# abre o arquivo CSV e lê os usuários e senhas
with open('client/src/data/novos_usuarios.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    names = []
    usernames = []
    passwords = []
    for row in reader:
        names.append(row[0])
        usernames.append(row[1])
        passwords.append(row[2])


bebidas_schema = StructType([
    StructField('id', IntegerType()),
    StructField('nome', StringType()),
    StructField('preco', FloatType()),
    StructField('quantidade', IntegerType()),
    StructField('descricao', StringType()),
    StructField('total_vendas', IntegerType()),
    StructField('quantidade_vendas', IntegerType())
])

estoque_schema = StructType([
    StructField('ID', IntegerType()),
    StructField('NOME', StringType()),
    StructField('QUANTIDADE', IntegerType())
])

clientes_schema = StructType([
    StructField('ID', IntegerType()),
    StructField('NOME', StringType()),
    StructField('GASTO', IntegerType())
])


def gerar_grafico_bolhas_bebidas():
  logging.info('Gerando gráfico de bolhas para bebidas')
  st.markdown("### Gráfico de Bolhas - Bebidas")
  st.markdown("Esta é a classificação das bebidas em termos de faixa de preço. Aqui no eixo Y, o tamanho da bolha descreve a classificação que se espalhou pelo pool da faixa de preço.")
  st.markdown("##### CLASSIFICAÇÃO DE BEBIDAS ★★★★★")

  # Ler os dados do arquivo CSV
  bebidas_schema = StructType([
      StructField('id', IntegerType()),
      StructField('nome', StringType()),
      StructField('preco', FloatType()),
      StructField('quantidade', IntegerType()),
      StructField('descricao', StringType()),
      StructField('total_vendas', IntegerType()),
      StructField('quantidade_vendas', IntegerType())
  ])
  df_bebidasLocal = pd.read_csv('client/src/data/bebidas.csv')
  
  # Criar um gráfico de bolhas com preço no eixo x, quantidade vendida no eixo y e tamanho das bolhas representando o total de vendas
  chart = alt.Chart(df_bebidasLocal.toPandas()).mark_circle().encode(
      x=alt.X('preco', title='Preço'),
      y=alt.Y('quantidade_vendas', title='Quantidade Vendida'),
      size=alt.Size('total_vendas', title='Total de Vendas'),
      color=alt.Color('nome', title='Bebida'),
      tooltip=['nome', 'preco', 'quantidade_vendas', 'total_vendas']
  ).properties(width=700, height=500)

  st.altair_chart(chart)


############################################################################################
#                                   Classes                                                #
############################################################################################

class ExibidorInformacoesRestaurante:
    
    def __init__(self, horarios, localizacao):
        self.horarios = horarios
        self.localizacao = localizacao
    
    def exibir_informacoes(self):
        st.markdown("## Horário de Funcionamento")
        for dia, horario in self.horarios.items():
            st.markdown(f"{dia.capitalize()}: {horario}")
        st.markdown("### Localização")
        st.markdown(self.localizacao)


class Data:

  def __init__(self) -> None:
     pass

  def load(self):
      data=pd.read_csv(URL)
      return data

  def loadBebidas(self):
      data=pd.read_csv(BEBIDAS)
      return data

  def loadEstoque(self):
      data=pd.read_csv(ESTOQUE)
      return data

  def loadPratos(self):
      data=pd.read_csv(PRATOS)
      return data

  def loadClientes(self):
      data=pd.read_csv(CLIENTES)
      return data

  def loadFuncionarios(self):
      data=pd.read_csv(FUNCIONARIOS)
      return data
  
  def loadReservas(self):
      data=pd.read_csv(RESERVAS)
      return data
  
  def loadVendasCategorias(self):
      data=pd.read_csv(VENDASCATEGORIAS)
      return data
  

def main():

  #########################################################################################
  #                                Variables                                              #
  #########################################################################################

  logPlaceholder = st.empty()
  titlePlaceholder = st.empty()
    
  def criar_conta():
    logging.info('O clientes começou a criar uma conta')
    names = []
    usernames= []
    passwords = []
    # abre o arquivo CSV e lê os usuários e senhas
    with open('client/src/data/novos_usuarios.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            names.append(row[0])
            usernames.append(row[1])
            passwords.append(row[2])

    # recebe os dados do usuário
    new_user = st.text_input("Digite o nome de usuário:")
    new_name = st.text_input("Digite o nome:")
    new_password = st.text_input("Digite a senha:", type="password")

    # verifica se o nome de usuário já está em uso
    if new_user in names:
        st.error("Este nome de usuário já está em uso. Por favor, escolha outro.")
    else:
        # exibe um botão para enviar os dados ao arquivo CSV
        if st.button("Criar conta"):
            # adiciona a nova conta ao arquivo CSV
            with open('client/src/data/novos_usuarios.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([new_user, new_name, new_password])

            st.success("Conta criada com sucesso!")

  
  def resetar_senha():
      logging.info('O cliente começou a resetar a senha')
      # Lê o arquivo CSV com os usuários e senhas
      with open('client/src/data/novos_usuarios.csv', newline='') as csvfile:
          reader = csv.reader(csvfile, delimiter=',', quotechar='|')
          names = []
          usernames= []
          passwords = []
          for row in reader:
              names.append(row[0])
              usernames.append(row[1])
              passwords.append(row[2])

      # Pede o nome de usuário do cliente
      user = st.text_input("Digite o nome de usuário:")

      if user not in names:
          st.error("Nome de usuário não encontrado. Por favor, tente novamente.")
          return

      # Pede a resposta para a pergunta de segurança
      question = "Qual o nome do seu animal de estimação?"
      answer = st.text_input(question)

      # Procura o índice do usuário
      index = names.index(user)

      # Verifica se a resposta está correta
      if answer.lower() == names[index].lower():
          # Pede a nova senha
          new_password = st.text_input("Digite a nova senha:", type="password")
          confirm_password = st.text_input("Confirme a nova senha:", type="password")

          # Verifica se as senhas coincidem
          if new_password == confirm_password:
              # Gera o hash da nova senha
              hashed_password = hashlib.sha256(new_password.encode()).hexdigest()

              # Atualiza a senha no arquivo CSV
              passwords[index] = hashed_password

              # Escreve as novas informações no arquivo CSV
              with open('client/src/data/novos_usuarios.csv', 'w', newline='') as csvfile:
                  writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                  writer.writerow(['user', 'name', 'password'])
                  for i in range(len(usernames)):
                      writer.writerow([usernames[i], names[i], passwords[i]])

              st.success("Senha alterada com sucesso!")
          else:
              st.error("As senhas não coincidem. Por favor, tente novamente.")
      else:
          st.error("Resposta incorreta. Por favor, tente novamente.")

  # exibe a imagem e permite que o usuário escolha entre fazer login ou criar uma nova conta
  logo_img = Image.open('client/src/public/if-logo.png')
  st.image(logo_img, use_column_width=True)
  opcao = st.radio("Escolha uma opção:", ("Fazer login", "Criar nova conta"))

  # chama a função apropriada com base na escolha do usuário
  logPlaceholder = st.empty()
  titlePlaceholder = st.empty()

  # # Lê o arquivo usuarios.csv com as informações de usuários e senhas
  #   users_data = pd.read_csv("client/src/data/login.csv")

  #   def authenticate_user(username, password):
  #       """Verifica se o usuário e senha informados são válidos."""
  #       return (users_data["usernames"] == username).any() and (users_data["passwords"] == password).any()

  #   def login_page():
  #       """Página de login do sistema."""
  #       # Configurações de bloqueio após algumas tentativas
  #       MAX_ATTEMPTS = 3
  #       locked_out = False

  #       # Cria espaço vazio na tela
  #       login_space = st.empty()
  #       original_title = '<p style="font-family:Monospace; color:Gray; font-size: 25px;"></p>'
  #       titlePlaceholder.markdown(original_title, unsafe_allow_html=True)

  #       # Solicitar nome de usuário e senha
  #       username = st.text_input("Nome de usuário", key="username_input")
  #       password = st.text_input("Senha", type="password", key="password_input")

  #       # Botão de login
  #       if st.button("Login", key="login_button"):
  #           if authenticate_user(username, password):
  #               # Limpa espaço vazio e exibe mensagem de sucesso
  #               login_space.empty()
  #               st.success("Login realizado com sucesso!")
  #               authentication_status = True
  #           else:
  #               # Informa que o nome de usuário ou senha estão incorretos
  #               st.error("Nome de usuário ou senha incorretos.")
  #               # Decrementa o número de tentativas restantes
  #               MAX_ATTEMPTS -= 1
  #               if MAX_ATTEMPTS == 0:
  #                   # Bloqueia o acesso após o número de tentativas acabar
  #                   st.error("Acesso bloqueado! Tente novamente mais tarde.")
  #                   locked_out = True
  #               else:
  #                   # Informa ao usuário a quantidade de tentativas restantes
  #                   st.error(f"Nome de usuário ou senha incorretos. {MAX_ATTEMPTS} tentativas restantes.")
  #               authentication_status = False
  #       else:
  #           authentication_status = False

  #       return authentication_status

  if opcao == "Fazer login":
    # apagar o que esteva antes
    logPlaceholder.empty()

    logging.info('O cliente escolheu fazer login')

    # @st.experimental_memo(show_spinner=False)
    @st.cache_data()
    def loadLogin(usernames, passwords):
        logoImg= Image.open('client/src/public/if-logo.png')
        return logoImg

    # chama a função apropriada com base na escolha do usuário
    logPlaceholder = st.empty()
    titlePlaceholder = st.empty()

      # # Lê o arquivo usuarios.csv com as informações de usuários e senhas
    users_data = pd.read_csv("client/src/data/login.csv")

    def authenticate_user(username, password):
        """Verifica se o usuário e senha informados são válidos."""
        return (users_data["usernames"] == username).any() and (users_data["passwords"] == password).any()

    def login_page():
        """Página de login do sistema."""
        # Configurações de bloqueio após algumas tentativas
        MAX_ATTEMPTS = 3
        locked_out = False

        # Cria espaço vazio na tela
        login_space = st.empty()
        original_title = '<p style="font-family:Monospace; color:Gray; font-size: 25px;"></p>'
        titlePlaceholder.markdown(original_title, unsafe_allow_html=True)

        # Solicitar nome de usuário e senha
        username = st.text_input("Nome de usuário", key="username_input")
        password = st.text_input("Senha", type="password", key="password_input")

        st.button("Login")

        # Botão de login
        # if st.button("Login", key="login_button"):
        if authenticate_user(username, password):
            # Limpa espaço vazio e exibe mensagem de sucesso
            login_space.empty()
            st.success("Login realizado com sucesso!")
            authentication_status = True
        else:
            # Informa que o nome de usuário ou senha estão incorretos
            if username == "" and password == "":
              st.error("Por favor, insira um nome de usuário e senha.")
            # caso o usuario tenha inserido nome de usuario e senha incorretos
            elif username != "" and password != "":
              st.error("Nome de usuário ou senha incorretos.")
            # Decrementa o número de tentativas restantes
            # MAX_ATTEMPTS -= 1
            # if MAX_ATTEMPTS == 0:
            #     # Bloqueia o acesso após o número de tentativas acabar
            #     st.error("Acesso bloqueado! Tente novamente mais tarde.")
            #     locked_out = True
            # else:
            #     # Informa ao usuário a quantidade de tentativas restantes
            #     st.error(f"Nome de usuário ou senha incorretos. {MAX_ATTEMPTS} tentativas restantes.")
            authentication_status = False

        return authentication_status

    with hc.HyLoader("Loading...",hc.Loaders.standard_loaders,index=1):
        logoImg = loadLogin(usernames, passwords)

    # logPlaceholder.image(logoImg, width=350)

    authentication_status = login_page()
    empty_slot = st.empty()
    
    def logout():
      # Define a variável de autenticação para False
      st.session_state.authentication_status = False
      # Redireciona o usuário de volta para a tela de login
      login_page()

    def initial():
        st.sidebar.title("Configurações")
        menu = ["Página Inicial", "Dashboard", "Configurações", "Ajuda"]
        choice = st.sidebar.selectbox("Selecione uma opção", menu)

        if choice == "Página Inicial":
            home()
        elif choice == "Dashboard":
            dashboard()
        elif choice == "Configurações":
            settings()
        else:
            help()

    def home():
        st.write("Bem-vindo à página inicial!")

    def dashboard():
        st.write("Dashboard")

    def settings():
        st.write("Configurações")

    def help():
        st.write("Ajuda")

    # Verifica se a conta está bloqueada
    if 'blocked_time' in st.session_state and st.session_state.blocked_time > time.time():
      st.warning(f"Sua conta foi bloqueada por excesso de tentativas. Tente novamente em {st.session_state.blocked_time - int(time.time())} segundos.")
    else:
      original_title = '<p style="font-family:Monospace; color:Gray; font-size: 25px;"></p>'
      titlePlaceholder.markdown(original_title, unsafe_allow_html=True)
      if authentication_status:
          titlePlaceholder.empty()
          st.markdown("# Bem-vindo!")
          st.sidebar.image(logoImg , width=215)
          logging.basicConfig(
            filename='client/src/log/app.log',
            level=logging.INFO,
            format='%(asctime)s %(levelname)s %(name)s %(filename)s:%(lineno)d %(funcName)s() [%(process)d] - %(message)s'
          )

          logging.info('Iniciando o app')

          load_dotenv()

          # exibe o relógio
          st.write("Horário atual:")
          current_time = time.strftime('%H:%M:%S')
          st.write(current_time)
          logging.info('Horário atual: %s', current_time)

          # exibe o tempo de uso
          session_start_time = st.session_state.get('session_start_time', time.time())
          elapsed_time = time.time() - session_start_time


          selecionar = st.sidebar.selectbox("Selecione a página", [
                                                                "Home",
                                                              "Dados Brutos",
                                                            "Consultar Dados",
                                                          "Inserir Dados",
                                                        "Atualizar Dados",
                                                      "Deletar Dados",
                                                    "Mapa",
                                                  "Análise de rentabilidade",
                                                "Reservas",
                                              "Previsão de demanda",
                                            "Análise de lucro líquido",
                                          "Análise de Tendências de Vendas",
                                        "Sobre",
                                      "Gráficos",
                                    "Contato",
                                  "Developers",
                                "funcionarios",
                              "Análise de desempenho dos funcionários",
                            "Grafico de Vendas por Categoria",
                          "Previsão de Vendas",
                        "Cardápio",
                      "Previsão de clientes",
                    ]
                  )

          data= Data().load()
          dataBebidas= Data().loadBebidas()
          dataEstoque= Data().loadEstoque()
          dataPratos= Data().loadPratos()
          dataClientes= Data().loadClientes()
          dataFuncionarios= Data().loadFuncionarios()
          dataReservas= Data().loadReservas()

          # dataVendasCategorias= Data().loadVendasCategorias()
          st.markdown("## Pedacinho do Céu")
          st.markdown("###### Tudo o que você pode saber aqui sobre ✎Bebidas ✎Mercadorias ✎Preços ✎Pratos da casa ✎Clientes ✎Avaliações ✎Custo ✎Localização ✎E muito mais")
          st.markdown("Este projeto foi criado para gerenciar um restaurante chamado Pedacinho do Céu. O projeto utiliza Big Data, Power BI, Docker e uma API RESTful para coletar, processar, armazenar e visualizar os dados.")
          logging.info('O cliente selecionou a página Pedacinho do Céu')

          pict = Image.open('client/src/public/pedacinho.png')
          st.sidebar.image(pict, use_column_width=True)

          pic = Image.open('client/src/public/food-camarao.png')
          st.image(pic, use_column_width=True)

          if selecionar == "Home":

            logging.info('O cliente selecionou a página Home')
            st.markdown("### HOME")
            
            # Gráfico de vendas mensais
            st.markdown("#### Gráfico de Vendas Mensais")
            data_vendas = pd.DataFrame({
                'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                'Vendas': [5000, 7000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000]
            })
            fig = px.line(data_vendas, x='Mês', y='Vendas')
            st.plotly_chart(fig)

            # Fotos dos Pratos
            st.markdown("## Fotos dos Pratos")
            # Cria duas colunas de largura igual
            col1, col2 = st.columns(2)

            # Adiciona conteúdo na primeira coluna
            with col1:
                st.header("Primeira Coluna")
                st.write("Conteúdo da primeira coluna")

            # Adiciona conteúdo na segunda coluna
            with col2:
                st.header("Segunda Coluna")
                st.write("Conteúdo da segunda coluna")

            # Avaliação dos Clientes
            st.markdown("## Avaliação dos Clientes")
            st.write("Média de avaliação: 4.5")
            st.write("Comentários:")
            st.write("- Comida deliciosa!")
            st.write("- Ótimo atendimento!")
            st.write("- Preços justos!")

            
            # colocar um video de fundo
            st.video("https://www.youtube.com/watch?v=wDJN95Y_yOM")
            logging.info('Video de fundo')

          if selecionar == "Sobre":
            logging.info('O cliente selecionou a página Sobre')
            
            st.markdown("## Sobre o Restaurante")
            st.write("O Restaurante Pedacinho do Céu foi fundado em 1995 com o objetivo de proporcionar aos seus clientes uma experiência gastronômica única e inesquecível. Com um cardápio diversificado que inclui pratos da cozinha regional e internacional, o restaurante se destaca pela qualidade dos seus ingredientes e pelo atendimento personalizado.")
            st.write("Além da excelência na comida, o Pedacinho do Céu também se preocupa com a experiência dos seus clientes. O ambiente é aconchegante e sofisticado, criando uma atmosfera perfeita para reuniões em família, encontros românticos ou jantares de negócios.")
            st.write("Venha nos visitar e experimentar o melhor da gastronomia!")
            pic = Image.open('client/src/public/restaurante.jpg')
            st.image(pic, use_column_width=True)

            st.markdown("## Sobre o Restaurante")
            st.markdown("### História")
            st.markdown("### Bar e Restaurante Pedacinho do Céu do Sul da Ilha de Florianópolis")
            st.markdown("### História do Bar e Restaurante Pedacinho do Céu")
            st.markdown("Desde 1985, o Pedacinho do Céu tem sido um lugar de encontro para amigos e famílias. Iniciado como um pequeno bar em uma casa de pescador, o local cresceu ao longo dos anos e tornou-se um restaurante renomado na região.")
            st.markdown("Com uma localização privilegiada na Rua Principal, número 123, no centro da cidade, o Pedacinho do Céu é conhecido por sua culinária diversificada e de alta qualidade, que combina ingredientes locais frescos com técnicas de cozinha inovadoras.")
            st.markdown("Além da excelente comida, o ambiente acolhedor e descontraído é o que mantém os clientes voltando. O bar é conhecido por seus coquetéis artesanais, e a carta de vinhos apresenta uma seleção cuidadosa de rótulos regionais e internacionais.")
            st.markdown("O Pedacinho do Céu também é um local de eventos, oferecendo opções personalizadas de cardápios e decoração para casamentos, aniversários e outras celebrações. O jardim encantador e a vista para o mar proporcionam o cenário perfeito para qualquer ocasião especial.")
            st.markdown("Se você está procurando por um lugar para se divertir com amigos, desfrutar de um jantar romântico ou celebrar um evento especial, o Pedacinho do Céu é o lugar perfeito. Venha nos visitar e experimente a magia deste lugar único no Sul da Ilha de Florianópolis!")
            st.image('client/src/public/pedacinho.png', use_column_width=True)
            st.markdown("Em 1985, a Dona Zenaide, proprietária do Bar e Restaurante Pedacinho do Céu, inaugurou o local em uma pequena casa de pescador, no Sul da Ilha de Florianópolis. Com o tempo, o local cresceu e tornou-se um ponto de encontro para amigos e famílias da região.")
            st.markdown("O cardápio do Pedacinho do Céu sempre foi diversificado, mas com foco em ingredientes locais frescos e frutos do mar. A partir de 2005, com a chegada do Chef Juca, a cozinha tornou-se ainda mais inovadora, combinando técnicas tradicionais com as mais modernas tendências culinárias.")
            st.markdown("Hoje, o Pedacinho do Céu é um restaurante renomado, conhecido não só pela excelente comida, mas também pelo ambiente acolhedor e descontraído. O local é frequentado por moradores locais e turistas, que buscam uma experiência única de gastronomia e convívio.")
            
            st.markdown("### Nossos Pratos")
            st.markdown("Nosso cardápio apresenta pratos tradicionais da culinária brasileira, bem como pratos internacionais para atender a todos os gostos. Nós usamos apenas os melhores ingredientes, cuidadosamente selecionados para criar pratos saborosos e saudáveis.")
            st.markdown("### Avaliações dos Clientes")
            st.markdown("Nós valorizamos o feedback dos nossos clientes e estamos sempre procurando maneiras de melhorar a experiência no nosso restaurante. Abaixo estão algumas avaliações dos nossos clientes mais recentes:")
            
            st.write(dataClientes.head(5))

            st.markdown("## Fotos do Restaurante")
            
            with st.beta_container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    # st.image('client/src/public/foto_restaurante1.jpg', use_column_width=True)
                    pass
                with col2:
                    # st.image('client/src/public/foto_restaurante2.jpg', use_column_width=True)
                    pass
                with col3:
                    # st.image('client/src/public/foto_restaurante3.jpg', use_column_width=True)
                    pass

            # Dicionário com os horários de funcionamento do restaurante
            horarios = {
                'segunda-feira': '08:30 às 22:00',
                'terça-feira': '08:30 às 22:00',
                'quarta-feira': '08:30 às 22:00',
                'quinta-feira': '08:30 às 22:00',
                'sexta-feira': '08:30 às 00:00',
                'sábado': '08:30 às 23:00',
                'domingo': '08:30 às 23:00'
            }

            # Localização do restaurante
            localizacao = "Estamos localizados na Rua Joaquim Neves, 152, no Praia da cidade. Venha nos visitar e experimentar nossos deliciosos pratos!"

            # Cria o objeto ExibidorInformacoesRestaurante
            exibidor = ExibidorInformacoesRestaurante(horarios, localizacao)

            # Chama o método exibir_informacoes() para exibir as informações na tela
            exibidor.exibir_informacoes()

          if selecionar == "Inserir Dados":
            logging.info('O cliente selecionou a opção de inserir dados')
            def inserir_bebida(id, nome, preco, quantidade, descricao, total_vendas, quantidade_vendas):
                with open('client/src/data/bebidas.csv', 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=',')

                    if file.tell() == 0:
                        writer.writerow(['id', 'nome', 'preco', 'quantidade', 'descricao', 'total_vendas', 'quantidade_vendas'])

                    writer.writerow([id, nome, preco, quantidade, descricao, total_vendas, quantidade_vendas])

                st.success('Bebida inserida com sucesso!')

                show_chart = st.radio('Deseja visualizar o gráfico de bolhas para as bebidas?', ('Sim', 'Não'))
                if show_chart == 'Sim':
                    st.markdown("##### CLASSIFICAÇÃO DE BEBIDAS ★★★★★")

                    # Ler os dados do arquivo CSV
                    df_bebidas = pd.read_csv('client/src/data/bebidas.csv')

                    # Criar um gráfico de bolhas com preço no eixo x, quantidade vendida no eixo y e tamanho das bolhas representando o total de vendas
                    chart = alt.Chart(df_bebidas).mark_circle().encode(
                        x=alt.X('preco', title='Preço'),
                        y=alt.Y('quantidade_vendas', title='Quantidade Vendida'),
                        size=alt.Size('total_vendas', title='Total de Vendas'),
                        color=alt.Color('nome', title='Bebida'),
                        tooltip=['nome', 'preco', 'quantidade_vendas', 'total_vendas']
                    ).properties(width=700, height=500)

                    # Exibir o gráfico
                    st.altair_chart(chart)

            def inserir_estoque(id, nome, quantidade):
                with open('client/src/data/estoque_mercadorias.csv', 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=',')

                    if file.tell() == 0:
                        writer.writerow(['ID','NOME','QUANTIDADE'])

                    writer.writerow([id, nome, quantidade])

                st.success('Estoque atualizado com sucesso!')

                show_chart = st.radio('Deseja visualizar o gráfico de bolhas para o estoque?', ('Sim', 'Não'))
                if show_chart == 'Sim':
                    st.markdown("### A COMPARAÇÃO DO ESTOQUE DE MERCADORIAS")
                    st.markdown("Esta é a comparação do estoque de mercadorias por ID e quantidade. Aqui no eixo X, temos o ID e no eixo Y, a quantidade em estoque.")
                    st.markdown("##### ESTOQUE DE MERCADORIAS ★★★★★")

                    # Ler os dados do arquivo CSV
                    df_mercadorias = pd.read_csv('client/src/data/estoque_mercadorias.csv')

                    # Criar um gráfico de barras com ID no eixo x e quantidade no eixo y
                    chart = alt.Chart(df_mercadorias).mark_bar().encode(
                        x=alt.X('ID', title='ID'),
                        y=alt.Y('QUANTIDADE', title='Quantidade em Estoque'),
                        tooltip=['NOME', 'QUANTIDADE']
                    ).properties(width=700, height=500)

                    # Exibir o gráfico
                    st.altair_chart(chart)

            def inserir_cliente(id, nome, gasto):
                with open('client/src/data/total_clientes.csv', 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=',')

                    if file.tell() == 0:
                        writer.writerow(['ID','NOME','GASTO'])

                    writer.writerow([id, nome, gasto])

                st.success('Cliente cadastrado com sucesso!')
                show_chart = st.radio('Deseja visualizar o gráfico de bolhas para o total de gastos dos clientes?', ('Sim', 'Não'))
                if show_chart == 'Sim':
                    st.markdown("### Comparação de Clientes")
                    st.markdown("Neste gráfico, o tamanho da bolha representa o gasto total de cada cliente.")
                    st.markdown("##### CLASSIFICAÇÃO DE DADOS DE CLIENTES ★★★★★")

                    st.vega_lite_chart(dadosClientes, {
                        'mark': {'type': 'circle', 'tooltip': True},
                        'encoding': {
                            'x': {'field': 'NOME', 'type': 'ordinal'},
                            'y': {'field': 'GASTO', 'type': 'quantitative'},
                            'size': {'field': 'GASTO', 'type': 'quantitative'},
                            'color': {'field': 'GASTO', 'type': 'quantitative'},
                        },
                    }, use_container_width=True)

            def inserir_prato(id, nome, preco, acompanhamento):
              with open('client/src/data/pratos.csv', 'a', newline='', encoding='utf-8') as file:
                  writer = csv.writer(file, delimiter=',')

                  if file.tell() == 0:
                      writer.writerow(['ID', 'NOME', 'PRECO', 'ACOMPANHAMENTO'])

                  writer.writerow([id, nome, preco, acompanhamento])

              st.success('Prato cadastrado com sucesso!')
              show_chart = st.radio('Deseja visualizar o gráfico de bolhas para os pratos?', ('Sim', 'Não'))
              if show_chart == 'Sim':
                st.markdown("### Comparação de Pratos")
                st.markdown("Neste gráfico, cada bolha representa um prato e o tamanho da bolha representa a quantidade em estoque.")
                st.markdown("##### CLASSIFICAÇÃO DE DADOS DE PRATOS ★★★★★")

                # Carregando os dados do arquivo CSV
                dataBebidas = pd.read_csv("client/src/data/pratos.csv")

                # Criando o gráfico de bolhas com Altair
                chart = alt.Chart(dataBebidas).mark_circle(size=100).encode(
                    x='NOME',
                    y='PRECO',
                    color='ACOMPANHAMENTO',
                    tooltip=['NOME', 'PRECO', 'ACOMPANHAMENTO']
                ).properties(
                    width=600,
                    height=400
                )

                # Exibindo o gráfico na tela
                st.altair_chart(chart, use_container_width=True)

            def inserir_venda(id, categoria, vendas, preco_medio):
              with open('client/src/data/vendasCategorias.csv', 'a', newline='', encoding='utf-8') as file:
                  writer = csv.writer(file, delimiter=',')

                  if file.tell() == 0:
                      writer.writerow(['id', 'Categoria', 'Vendas', 'PreçoMédio'])

                  writer.writerow([id, categoria, vendas, preco_medio])

              print('Venda cadastrada com sucesso!')
              st.success('Venda cadastrada com sucesso!')
              show_chart = st.radio('Deseja visualizar o gráfico de bolhas para as vendas?', ('Sim', 'Não'))
              if show_chart == 'Sim':
                st.markdown("### Comparação de Categoria de Vendas")
                st.markdown("Neste gráfico, cada bolha representa uma categoria de vendas e o tamanho da bolha representa o preço médio.")
                st.markdown("##### CLASSIFICAÇÃO DE DADOS DE VENDAS ★★★★★")

                # Carregando os dados do arquivo CSV
                dataBebidas = pd.read_csv("client/src/data/vendasCategorias.csv")

                # Criando o gráfico de bolhas com Altair
                chart = alt.Chart(dataBebidas).mark_circle(size=100).encode(
                    x='Categoria',
                    y='Vendas',
                    color='PreçoMédio',
                    tooltip=['Categoria', 'Vendas', 'PreçoMédio']
                ).properties(
                    width=600,
                    height=400
                )

                # Exibindo o gráfico na tela
                st.altair_chart(chart, use_container_width=True)

            st.title('Inserção de Dados')
            arquivo00 = st.radio('Escolha o arquivo para inserir os dados', ('Bebidas', 'Estoque', 'Clientes', 'Pratos', 'Categoria de Vendas'))

            # Texto explicativo sobre a escolha do arquivo
            st.markdown(f"Você escolheu inserir os dados no arquivo **{arquivo00}**.")

            # Texto explicativo sobre a importância da inserção de dados para Big Data
            st.markdown("A inserção de dados é uma etapa fundamental em qualquer projeto de Big Data e análise de dados. "
                        "Garantir que os dados sejam inseridos corretamente em seus respectivos arquivos é essencial "
                        "para que as análises e tomadas de decisão sejam precisas e confiáveis.")

            # Texto explicativo sobre a importância da qualidade dos dados
            st.markdown("Além disso, é importante garantir que os dados inseridos sejam de alta qualidade, ou seja, "
                        "que sejam precisos, completos e consistentes. Dessa forma, os resultados das análises "
                        "tendem a ser mais confiáveis e as decisões tomadas com base nesses resultados são mais "
                        "acertadas e eficazes.")

            # Texto explicativo sobre a importância da validação dos dados
            st.markdown("Por fim, é importante validar os dados inseridos, verificando se estão no formato correto "
                        "e se atendem aos requisitos estabelecidos para cada arquivo em particular. Isso garante a "
                        "integridade dos dados e evita erros e inconsistências nos resultados das análises.") 

            # TODO: adicionar as funções de inserção de dados e gerar gráficos de bolhas para cada arquivo escolhido

            if arquivo00 == 'Bebidas':
                logging.info('O cliente selecionou a opção de inserir bebidas')
                st.subheader('Inserir Bebida')
                id = st.text_input('id')
                nome = st.text_input('nome')
                preco = st.text_input('preco')
                quantidade = st.text_input('quantidade')
                descricao = st.text_input('descricao')
                total_vendas = st.text_input('total_vendas')
                quantidade_vendas = st.text_input('quantidade_vendas')

                if st.button('Inserir'):
                    inserir_bebida(id, nome, preco, quantidade, descricao, total_vendas, quantidade_vendas)
                    st.button('Voltar')

            elif arquivo00 == 'Estoque':
                logging.info('O cliente selecionou a opção de inserir estoque')
                st.subheader('Inserir Estoque')
                id = st.text_input('ID')
                nome = st.text_input('NOME')
                quantidade = st.text_input('QUANTIDADE')

                if st.button('Inserir'):
                    inserir_estoque(id, nome, quantidade)
                    st.button('Voltar')

            elif arquivo00 == 'Clientes':
                logging.info('O cliente selecionou a opção de inserir clientes')
                st.subheader('Inserir Cliente')
                id = st.text_input('ID')
                nome = st.text_input('NOME')
                gasto = st.text_input('GASTO')

                if st.button('Inserir'):
                    inserir_cliente(id, nome, gasto)
                    st.button('Voltar')

            elif arquivo00 == 'Pratos':
                logging.info('O cliente selecionou a opção de inserir pratos')
                st.subheader('Inserir Prato')
                id = st.text_input('ID')
                nome = st.text_input('NOME')
                preco = st.text_input('PRECO')
                acompanhamento = st.text_input('ACOMPANHAMENTO')

                if st.button('Inserir'):
                    inserir_prato(id, nome, preco, acompanhamento)
                    st.button('Voltar')

            # id,Categoria,Vendas,PreçoMédio
            elif arquivo00 == 'Categoria de Vendas':
                logging.info('O cliente selecionou a opção de inserir vendas')
                st.subheader('Inserir Venda')
                id = st.text_input('id')
                categoria = st.text_input('Categoria')
                vendas = st.text_input('Vendas')
                preco_medio = st.text_input('PreçoMédio')

                if st.button('Inserir'):
                    inserir_venda(id, categoria, vendas, preco_medio)
                    st.button('Voltar')

          if selecionar == "Atualizar Dados":
            arquivo01 = st.radio('Escolha o arquivo para inserir os dados', ('Bebidas', 'Estoque', 'Clientes', 'Pratos', 'Funcionarios', 'Categoria de Vendas'))

            # Texto explicativo sobre a escolha do arquivo
            st.markdown(f"Você escolheu deletar os dados no arquivo **{arquivo01}**.")

            # Texto explicativo sobre a importância da atualização de dados para Big Data
            st.markdown("A atualização de dados é uma etapa fundamental em qualquer projeto de Big Data e análise de dados. "
                        "Garantir que os dados sejam inseridos corretamente em seus respectivos arquivos é essencial "
                        "para que as análises e tomadas de decisão sejam precisas e confiáveis.")

            # Texto explicativo sobre a importância da qualidade dos dados
            st.markdown("Além disso, é importante garantir que os dados inseridos sejam de alta qualidade, ou seja, "
                        "que sejam precisos, completos e consistentes. Dessa forma, os resultados das análises "
                        "tendem a ser mais confiáveis e as decisões tomadas com base nesses resultados são mais "
                        "acertadas e eficazes.")

            # Texto explicativo sobre a importância da validação dos dados
            st.markdown("Por fim, é importante validar os dados inseridos, verificando se estão no formato correto "
                        "e se atendem aos requisitos estabelecidos para cada arquivo em particular. Isso garante a "
                        "integridade dos dados e evita erros e inconsistências nos resultados das análises.") 

            # TODO: adicionar as funções de atualização de dados e gerar gráficos de bolhas para cada arquivo escolhido

            if arquivo01 == 'Bebidas':
              class Bebidas:
                  def __init__(self, csv_file):
                      self.csv_file = csv_file
                      self.data = pd.read_csv(csv_file)
                  
                  def load_data(self):
                      self.data = pd.read_csv(self.csv_file)
                  
                  def show_table(self):
                      st.write(self.data)
                      
                  def update_by_id(self, id):
                      index = self.data.index[self.data['id'] == id].tolist()[0]
                      for col in self.data.columns:
                          if col != 'id':
                              new_val = st.text_input(f"{col.capitalize()}:", value=str(self.data.loc[index, col]))
                              self.data.loc[index, col] = new_val
                      st.success("Dados atualizados com sucesso!")
                      
                  def save_data(self):
                      self.data.to_csv(self.csv_file, index=False)

              bebidas = Bebidas('client/src/data/bebidas.csv')

              # Exibir dados em uma tabela
              bebidas.show_table()

              # Permitir que o usuário escolha o id para atualizar
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(bebidas.data))

              # Atualizar registro pelo ID selecionado
              if st.button("Atualizar"):
                  bebidas.update_by_id(id_to_update)
                  
              # Salvar os dados atualizados de volta no arquivo CSV
              if st.button("Salvar"):
                  bebidas.save_data()

            elif arquivo01 == 'Estoque':
              class Estoque:
                  def __init__(self, csv_file):
                      self.csv_file = csv_file
                      self.data = pd.read_csv(csv_file)
                  
                  def load_data(self):
                      self.data = pd.read_csv(self.csv_file)
                  
                  def show_table(self):
                      st.write(self.data)
                      
                  def update_by_id(self, id):
                      index = self.data.index[self.data['ID'] == id].tolist()[0]
                      for col in self.data.columns:
                          if col != 'ID':
                              new_val = st.text_input(f"{col.capitalize()}:", value=str(self.data.loc[index, col]))
                              self.data.loc[index, col] = new_val
                      st.success("Dados atualizados com sucesso!")
                      
                  def save_data(self):
                      self.data.to_csv(self.csv_file, index=False)

              estoque = Estoque('client/src/data/estoque_mercadorias.csv')

              # Exibir dados em uma tabela
              estoque.show_table()

              # Permitir que o usuário escolha o id para atualizar
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(estoque.data))

              # Atualizar registro pelo ID selecionado
              if st.button("Atualizar"):
                  estoque.update_by_id(id_to_update)
                  
              # Salvar os dados atualizados de volta no arquivo CSV
              if st.button("Salvar"):
                  estoque.save_data()

            elif arquivo01 == 'Clientes':
              class Clientes:
                  def __init__(self, csv_file):
                      self.csv_file = csv_file
                      self.data = pd.read_csv(csv_file)
                  
                  def load_data(self):
                      self.data = pd.read_csv(self.csv_file)
                  
                  def show_table(self):
                      st.write(self.data)
                      
                  def update_by_id(self, id):
                      index = self.data.index[self.data['ID'] == id].tolist()[0]
                      for col in self.data.columns:
                          if col != 'ID':
                              new_val = st.text_input(f"{col.capitalize()}:", value=str(self.data.loc[index, col]))
                              self.data.loc[index, col] = new_val
                      st.success("Dados atualizados com sucesso!")
                      
                  def save_data(self):
                      self.data.to_csv(self.csv_file, index=False)

              clientes = Clientes('client/src/data/total_clientes.csv')

              # Exibir dados em uma tabela
              clientes.show_table()

              # Permitir que o usuário escolha o id para atualizar
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(clientes.data))

              # Atualizar registro pelo ID selecionado
              if st.button("Atualizar"):
                  clientes.update_by_id(id_to_update)
                  
              # Salvar os dados atualizados de volta no arquivo CSV
              if st.button("Salvar"):
                  clientes.save_data()

            elif arquivo01 == 'Pratos':
              class Pratos:
                  def __init__(self, csv_file):
                      self.csv_file = csv_file
                      self.data = pd.read_csv(csv_file)
                  
                  def load_data(self):
                      self.data = pd.read_csv(self.csv_file)
                  
                  def show_table(self):
                      st.write(self.data)
                      
                  def update_by_id(self, id):
                      index = self.data.index[self.data['ID'] == id].tolist()[0]
                      for col in self.data.columns:
                          if col != 'ID':
                              new_val = st.text_input(f"{col.capitalize()}:", value=str(self.data.loc[index, col]))
                              self.data.loc[index, col] = new_val
                      st.success("Dados atualizados com sucesso!")
                      
                  def save_data(self):
                      self.data.to_csv(self.csv_file, index=False)

              pratos = Pratos('client/src/data/pratos.csv')

              # Exibir dados em uma tabela
              pratos.show_table()

              # Permitir que o usuário escolha o id para atualizar
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(pratos.data))

              # Atualizar registro pelo ID selecionado
              if st.button("Atualizar"):
                  pratos.update_by_id(id_to_update)
                  
              # Salvar os dados atualizados de volta no arquivo CSV
              if st.button("Salvar"):
                  pratos.save_data()

            elif arquivo01 == 'Funcionarios':
              class Funcionarios:
                  def __init__(self, csv_file):
                      self.csv_file = csv_file
                      self.data = pd.read_csv(csv_file)
                  
                  def load_data(self):
                      self.data = pd.read_csv(self.csv_file)
                  
                  def show_table(self):
                      st.write(self.data)
                      
                  def update_by_id(self, id):
                      index = self.data.index[self.data['ID'] == id].tolist()[0]
                      for col in self.data.columns:
                          if col != 'ID':
                              new_val = st.text_input(f"{col.capitalize()}:", value=str(self.data.loc[index, col]))
                              self.data.loc[index, col] = new_val
                      st.success("Dados atualizados com sucesso!")
                      
                  def save_data(self):
                      self.data.to_csv(self.csv_file, index=False)

              funcionarios = Funcionarios('client/src/data/funcionarios.csv')

              # Exibir dados em uma tabela
              funcionarios.show_table()

              # Permitir que o usuário escolha o id para atualizar
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(funcionarios.data))

              # Atualizar registro pelo ID selecionado
              if st.button("Atualizar"):
                  funcionarios.update_by_id(id_to_update)
                  
              # Salvar os dados atualizados de volta no arquivo CSV
              if st.button("Salvar"):
                  funcionarios.save_data()

            # Categoria de Vendas
            elif arquivo01 == 'Categoria de Vendas':
              class CategoriaVendas:
                  def __init__(self, csv_file):
                      self.csv_file = csv_file
                      self.data = pd.read_csv(csv_file)
                  
                  def load_data(self):
                      self.data = pd.read_csv(self.csv_file)
                  
                  def show_table(self):
                      st.write(self.data)
                      
                  def update_by_id(self, id):
                      index = self.data.index[self.data['id'] == id].tolist()[0]
                      for col in self.data.columns:
                          if col != 'id':
                              new_val = st.text_input(f"{col.capitalize()}:", value=str(self.data.loc[index, col]))
                              self.data.loc[index, col] = new_val
                      st.success("Dados atualizados com sucesso!")
                      
                  def save_data(self):
                      self.data.to_csv(self.csv_file, index=False)

              categoriaVendas = CategoriaVendas('client/src/data/vendasCategorias.csv')

              # Exibir dados em uma tabela
              categoriaVendas.show_table()

              # Permitir que o usuário escolha o id para atualizar
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(categoriaVendas.data))

              # Atualizar registro pelo ID selecionado
              if st.button("Atualizar"):
                  categoriaVendas.update_by_id(id_to_update)
                  
              # Salvar os dados atualizados de volta no arquivo CSV
              if st.button("Salvar"):
                  categoriaVendas.save_data()

          if selecionar == "Deletar Dados":
            arquivo02 = st.radio('Escolha o arquivo para inserir os dados', ('Bebidas', 'Estoque', 'Clientes', 'Pratos', 'Funcionarios', 'Categoria de Vendas'))

            # Texto explicativo sobre a escolha do arquivo
            st.markdown(f"Você escolheu deletar os dados no arquivo **{arquivo02}**.")

            # Texto explicativo sobre a importância da deleção de dados para Big Data
            st.markdown("A deleção de dados é uma etapa fundamental em qualquer projeto de Big Data e análise de dados. "
                        "Garantir que os dados sejam inseridos corretamente em seus respectivos arquivos é essencial "
                        "para que as análises e tomadas de decisão sejam precisas e confiáveis.")

            # Texto explicativo sobre a importância da qualidade dos dados
            st.markdown("Além disso, é importante garantir que os dados inseridos sejam de alta qualidade, ou seja, "
                        "que sejam precisos, completos e consistentes. Dessa forma, os resultados das análises "
                        "tendem a ser mais confiáveis e as decisões tomadas com base nesses resultados são mais "
                        "acertadas e eficazes.")

            # Texto explicativo sobre a importância da validação dos dados
            st.markdown("Por fim, é importante validar os dados inseridos, verificando se estão no formato correto "
                        "e se atendem aos requisitos estabelecidos para cada arquivo em particular. Isso garante a "
                        "integridade dos dados e evita erros e inconsistências nos resultados das análises.") 

            # TODO: adicionar as funções de deleção de dados e gerar gráficos de bolhas para cada arquivo escolhido

            if arquivo02 == 'Estoque':
              class Estoque:
                def __init__(self, csv_file):
                    self.csv_file = csv_file
                    self.data = pd.read_csv(csv_file)

                def load_data(self):
                    self.data = pd.read_csv(self.csv_file)

                def show_table(self):
                    st.write(self.data)

                def update_by_id(self, ID):
                    index = self.data.index[self.data['ID'] == ID].tolist()[0]
                    for col in self.data.columns:
                        if col != 'ID':
                            new_val = st.text_input(f"{col.capitalize()}:", value=str(self.data.loc[index, col]))
                            self.data.loc[index, col] = new_val
                    st.success("Dados atualizados com sucesso!")
                    st.markdown(f"""
                        ## A linha do arquivo **{arquivo02}** foi deletado pelo ID **{ID}**
                    """)

                def delete_by_id(self, ID):
                    self.data = self.data[self.data.ID != ID]
                    st.success("Dados deletados com sucesso!")

                def save_data(self):
                    self.data.to_csv(self.csv_file, index=False)

              estoque = Estoque('client/src/data/estoque_mercadorias.csv')

              # Exibir dados em uma tabela
              # mostrar em markdown o arquivo escolhido como era antes e como ficou depois
              st.markdown("# Arquivo antes da deleção:")
              estoque.show_table()
              st.markdown(f"**Total de Registros que sobraram** {len(estoque.data)}")
              # st.markdown(f"**Total em Estoque:** R$ {estoque.data['valor'].sum():.2f}")

              # Permitir que o usuário escolha o id para deletar
              id_to_delete = st.number_input("Digite o ID do registro que deseja deletar:", min_value=1, max_value=len(estoque.data))

              if st.button("Deletar"):
                  estoque.delete_by_id(id_to_delete)
                  estoque.save_data()
                  estoque.load_data()
                  st.success("Dados salvos e atualizados com sucesso!")
                  st.markdown("# Arquivo depois da deleção:")
                  estoque.show_table()


            elif arquivo02 == 'Bebidas':
                class Bebidas:
                  def __init__(self, csv_file):
                      self.csv_file = csv_file
                      self.data = pd.read_csv(csv_file)
                            
                  def load_data(self):
                      self.data = pd.read_csv(self.csv_file)
                            
                  def show_table(self):
                      st.write(self.data)
                                    
                  def update_by_id(self, id):
                      index = self.data.index[self.data['id'] == id].tolist()[0]
                      for col in self.data.columns:
                          if col != 'id':
                              new_val = st.text_input(f"{col.capitalize()}:", value=str(self.data.loc[index, col]))
                              self.data.loc[index, col] = new_val
                      st.success("Dados atualizados com sucesso!")
                      st.markdown(f"""
                          ## A linha do arquivo **{arquivo02}** foi deletado pelo ID **{id}**
                      """)
                        
                  def delete_by_id(self, id):
                      self.data = self.data[self.data.id != id]
                      st.success("Dados deletados com sucesso!")
                        
                  def save_data(self):
                      self.data.to_csv(self.csv_file, index=False)

                bebidas = Bebidas('client/src/data/bebidas.csv')

                # Exibir dados em uma tabela
                st.markdown("# Arquivo antes da deleção:")
                bebidas.show_table()                
                st.success("Dados deletados com sucesso!")
                st.markdown(f"**Total de Registros que sobraram** {len(bebidas.data)}")

                # Permitir que o usuário escolha o id para deletar
                id_to_delete = st.number_input("Digite o ID do registro que deseja deletar:", min_value=1, max_value=len(bebidas.data))

                if st.button("Deletar"):
                    bebidas.delete_by_id(id_to_delete)
                    bebidas.save_data()
                    bebidas.load_data()
                    st.success("Dados salvos e atualizados com sucesso!")
                    st.markdown("# Arquivo depois da deleção:")
                    bebidas.show_table()

            elif arquivo02 == 'Pratos':
                class Pratos:
                  def __init__(self, csv_file):
                      self.csv_file = csv_file
                      self.data = pd.read_csv(csv_file)
                            
                  def load_data(self):
                      self.data = pd.read_csv(self.csv_file)
                            
                  def show_table(self):
                      st.write(self.data)
                                    
                  def update_by_id(self, ID):
                      index = self.data.index[self.data['ID'] == ID].tolist()[0]
                      for col in self.data.columns:
                          if col != 'id':
                              new_val = st.text_input(f"{col.capitalize()}:", value=str(self.data.loc[index, col]))
                              self.data.loc[index, col] = new_val
                      st.success("Dados atualizados com sucesso!")
                      st.markdown(f"""
                          ## A linha do arquivo **{arquivo02}** foi deletado pelo ID **{ID}**
                      """)
                        
                  def delete_by_id(self, ID):
                      self.data = self.data[self.data.ID != ID]
                      st.success("Dados deletados com sucesso!")
                        
                  def save_data(self):
                      self.data.to_csv(self.csv_file, index=False)

                pratos = Pratos('client/src/data/pratos.csv')

                # Exibir dados em uma tabela
                st.markdown("# Arquivo antes da deleção:")
                pratos.show_table()
                st.success("Dados deletados com sucesso!")
                st.markdown(f"**Total de Registros que sobraram** {len(pratos.data)}")

                # Permitir que o usuário escolha o id para deletar
                id_to_delete = st.number_input("Digite o ID do registro que deseja deletar:", min_value=1, max_value=len(pratos.data))

                if st.button("Deletar"):
                    pratos.delete_by_id(id_to_delete)
                    pratos.save_data()
                    pratos.load_data()
                    st.success("Dados salvos e atualizados com sucesso!")
                    st.markdown("# Arquivo depois da deleção:")
                    pratos.show_table()

            elif arquivo02 == 'Clientes':
              class Clientes:
                def __init__(self, csv_file):
                    self.csv_file = csv_file
                    self.data = pd.read_csv(csv_file)

                def load_data(self):
                    self.data = pd.read_csv(self.csv_file)

                def show_table(self):
                    st.write(self.data)

                def update_by_id(self, ID):
                    index = self.data.index[self.data['ID'] == ID].tolist()[0]
                    for col in self.data.columns:
                        if col != 'ID':
                            new_val = st.text_input(f"{col.capitalize()}:", value=str(self.data.loc[index, col]))
                            self.data.loc[index, col] = new_val
                    st.success("Dados atualizados com sucesso!")
                    st.markdown(f"""
                        ## A linha do arquivo **{arquivo02}** foi deletado pelo ID **{ID}**
                    """)

                def delete_by_id(self, ID):
                    self.data = self.data[self.data.ID != ID]
                    st.success("Dados deletados com sucesso!")

                def save_data(self):
                    self.data.to_csv(self.csv_file, index=False)

              clientes = Clientes('client/src/data/total_clientes.csv')

              # Exibir dados em uma tabela
              st.markdown("# Arquivo antes da deleção:")
              clientes.show_table()
              st.success("Dados deletados com sucesso!")
              st.markdown(f"**Total de Registros que sobraram** {len(clientes.data)}")

              # Permitir que o usuário escolha o id para deletar
              id_to_delete = st.number_input("Digite o ID do registro que deseja deletar:", min_value=1, max_value=len(clientes.data))

              if st.button("Deletar"):
                  clientes.delete_by_id(id_to_delete)
                  clientes.save_data()
                  clientes.load_data()
                  st.success("Dados salvos e atualizados com sucesso!")
                  st.markdown("# Arquivo depois da deleção:")
                  clientes.show_table()
            
            elif arquivo02 == 'Funcionarios':
              class Funcionarios:
                def __init__(self, csv_file):
                    self.csv_file = csv_file
                    self.data = pd.read_csv(csv_file)

                def load_data(self):
                    self.data = pd.read_csv(self.csv_file)

                def show_table(self):
                    st.write(self.data)

                def update_by_id(self, ID):
                    index = self.data.index[self.data['ID'] == ID].tolist()[0]
                    for col in self.data.columns:
                        if col != 'ID':
                            new_val = st.text_input(f"{col.capitalize()}:", value=str(self.data.loc[index, col]))
                            self.data.loc[index, col] = new_val
                    st.success("Dados atualizados com sucesso!")
                    st.markdown(f"""
                        ## A linha do arquivo **{arquivo02}** foi deletado pelo ID **{ID}**
                    """)

                def delete_by_id(self, ID):
                    self.data = self.data[self.data.ID != ID]
                    st.success("Dados deletados com sucesso!")

                def save_data(self):
                    self.data.to_csv(self.csv_file, index=False)

              funcionarios = Funcionarios('client/src/data/funcionarios.csv')

              # Exibir dados em uma tabela
              st.markdown("# Arquivo antes da deleção:")
              funcionarios.show_table()
              st.success("Dados deletados com sucesso!")
              st.markdown(f"**Total de Registros que sobraram** {len(funcionarios.data)}")

              # Permitir que o usuário escolha o id para deletar
              id_to_delete = st.number_input("Digite o ID do registro que deseja deletar:", min_value=1, max_value=len(funcionarios.data))

              if st.button("Deletar"):
                  funcionarios.delete_by_id(id_to_delete)
                  funcionarios.save_data()
                  funcionarios.load_data()
                  st.success("Dados salvos e atualizados com sucesso!")
                  st.markdown("# Arquivo depois da deleção:")
                  funcionarios.show_table()

            elif arquivo02 == 'Categoria de Vendas':
              class Vendas:
                def __init__(self, csv_file):
                    self.csv_file = csv_file
                    self.data = pd.read_csv(csv_file)

                def load_data(self):
                    self.data = pd.read_csv(self.csv_file)

                def show_table(self):
                    st.write(self.data)

                def update_by_id(self, id):
                    index = self.data.index[self.data['id'] == id].tolist()[0]
                    for col in self.data.columns:
                        if col != 'id':
                            new_val = st.text_input(f"{col.capitalize()}:", value=str(self.data.loc[index, col]))
                            self.data.loc[index, col] = new_val
                    st.success("Dados atualizados com sucesso!")

                def delete_by_id(self, id):
                    self.data = self.data[self.data.id != id]
                    st.success("Dados deletados com sucesso!")
                    st.markdown(f"""
                        ## A linha do arquivo **{arquivo02}** foi deletado pelo ID **{id}**
                    """)

                def save_data(self):
                    self.data.to_csv(self.csv_file, index=False)

              vendas = Vendas('client/src/data/vendasCategorias.csv')

              # Exibir dados em uma tabela
              st.markdown("# Arquivo antes da deleção:")
              vendas.show_table()
              st.success("Dados deletados com sucesso!")
              st.markdown(f"**Total de Registros que sobraram** {len(vendas.data)}")

              # Permitir que o usuário escolha o id para deletar
              id_to_delete = st.number_input("Digite o ID do registro que deseja deletar:", min_value=1, max_value=len(vendas.data))

              if st.button("Deletar"):
                  vendas.delete_by_id(id_to_delete)
                  vendas.save_data()
                  vendas.load_data()
                  st.success("Dados salvos e atualizados com sucesso!")
                  st.markdown("# Arquivo depois da deleção:")
                  vendas.show_table()
          
          if selecionar == "Análise de rentabilidade":
            from typing import List, Dict

            class AtualizadorDeItem:
              def __init__(self, rentabilidade):
                  self.rentabilidade = rentabilidade

              def atualizar(self, id_item):
                item_atualizado = exibe_formulario_atualiza_item_valores(self.rentabilidade, id_item)

                # if all(val or val == 0 for val in item_atualizado) and any(item_atualizado):
                #   # self.rentabilidade.update_item(id_item, item_atualizado[0], item_atualizado[1], item["Nome do Item"])
                #   st.success("Item atualizado com sucesso!")


            class DeletadorDeItem:
                def __init__(self, rentabilidade):
                    self.rentabilidade = rentabilidade

                def deletar(self, id_item):
                    self.rentabilidade.remove_item(id_item)
                    self.rentabilidade.save_data()
                    st.success("Item deletado com sucesso!")


            class Rentabilidade:
                def __init__(self, csv_file):
                    self.csv_file = csv_file
                    self.data = pd.DataFrame(columns=["ID", "Item", "Preço de Venda", "Custo de Produção"])
                    # self.lista_produtos = self.carrega_dados()

                # def carrega_dados(self):
                #   try:
                #       with open(self.csv_file, "r") as arquivo:
                #           return json.load(arquivo)
                #   except FileNotFoundError:
                #       return []

                # def get_ids(self):
                #   return [produto["ID"] for produto in self.lista_produtos]

                def load_data(self):
                    self.data = pd.read_csv(self.csv_file)

                def exibe_formulario_deleta_item(self):
                  # Mostra os IDs dos produtos existentes
                  # lista_ids = [produto["ID"] for produto in self.lista_produtos]
                  id_item = st.text_input("Digite o ID do item que deseja deletar")
                  # id_item = st.selectbox("Selecione o ID do item que deseja deletar")
                  
                  if st.button("Deletar"):
                      deletador = DeletadorDeItem(self)
                      deletador.deletar(id_item)
                      st.success("Item deletado com sucesso!")

                def deletar_item(self, id_item):
                  # Encontra o item com o ID correspondente
                  item_encontrado = False
                  for i, produto in enumerate(self.lista_produtos):
                      if produto["ID"] == id_item:
                          del self.lista_produtos[i]
                          item_encontrado = True
                          break
                  # Salva os dados atualizados
                  if item_encontrado:
                      self.salva_dados()
                      st.success(f"Item com ID {id_item} foi deletado com sucesso!")
                  else:
                      st.error(f"Item com ID {id_item} não encontrado.")

                def save_data(self):
                    if not os.path.isfile(self.csv_file):
                        self.data.to_csv(self.csv_file, index=False)
                        st.info("Arquivo CSV criado com sucesso!")
                    else:
                        with open(self.csv_file, "a") as f:
                            self.data.to_csv(f, header=False, index=False)
                            st.info("Dados adicionados ao arquivo CSV com sucesso!")

                def add_item(self, nome, preco, custo):
                  id = len(self.data) + 1
                  self.data = self.data.append({
                      "ID": id,
                      "Item": nome,
                      "Preço de Venda": preco,
                      "Custo de Produção": custo
                  }, ignore_index=True)
                  st.success("Item adicionado com sucesso!")

                def remove_item(self, id):
                    self.data = self.data[self.data.ID != id]
                    st.success("Item removido com sucesso!")

                def update_item(self, id, nome, preco, custo):
                    index = self.data.index[self.data['ID'] == id].tolist()[0]
                    self.data.loc[index, "Item"] = nome
                    self.data.loc[index, "Preço de Venda"] = preco
                    self.data.loc[index, "Custo de Produção"] = custo
                    st.success("Item atualizado com sucesso!")

                def lista_produtos(self):
                  return self.lista_produtos

                def show_table(self):
                    st.write(self.data)

                def get_item(self, id_item):
                  return self.data.loc[self.data["ID"] == id_item]

                def plot_rentabilidade(self):
                    self.data['Margem de Lucro'] = self.data['Preço de Venda'] - self.data['Custo de Produção']
                    self.data.sort_values(by=['Margem de Lucro'], inplace=True, ascending=False)
                    fig = px.bar(self.data, x='Item', y='Margem de Lucro')
                    fig.update_layout(title="Rentabilidade dos Itens do Menu",
                                        xaxis_title="Item",
                                        yaxis_title="Margem de Lucro")
                    st.plotly_chart(fig)

            def exibe_formulario_atualiza_item_valores(rentabilidade, id_item):
              item = rentabilidade.get_item(id_item)
              nome_item = item["Item"]
              preco_venda = st.number_input("Novo preço de venda", min_value=0.01, value=float(item["Preço de Venda"]), step=0.01, max_value=1e9)
              custo_producao = st.number_input("Novo custo de produção", min_value=0.01, value=float(item["Custo de Produção"]), step=0.01, max_value=1e9)
              quantidade_vendida = st.number_input("Nova quantidade vendida", min_value=1, value=int(item["Quantidade Vendida"]), step=1, max_value=int(1e9))
              item_atualizado = (nome_item, preco_venda, custo_producao, quantidade_vendida)
              return item_atualizado

            def exibe_formulario_atualiza_item(rentabilidade):
              items = rentabilidade.data['Item'].tolist()
              item = st.selectbox("Selecione o item a ser atualizado", items)
              if st.button("Buscar"):
                  item_id = rentabilidade.data[rentabilidade.data['Item'] == item]['ID'].tolist()[0]
                  return item_id
            
            def plot_rentabilidade(self):
              fig = go.Figure()
              fig.add_trace(go.Bar(x=self.data["Item"], y=self.data["Margem de Lucro"], marker_color='green'))
              fig.update_layout(title="Margem de Lucro dos Itens do Menu",
                                xaxis_title="Item",
                                yaxis_title="Margem de Lucro (%)")
              st.plotly_chart(fig)

            def exibe_formulario_deleta_item(rentabilidade):
              """
              Exibe um formulário para selecionar o item que será deletado.

              Parameters:
              ----------
              rentabilidade : Rentabilidade
                  Objeto que contém os dados brutos de rentabilidade.

              Returns:
              -------
              int or None
                  O ID do item a ser deletado, ou None se nenhum item for selecionado.
              """
              # Obtém a lista de IDs dos itens
              # lista_ids = rentabilidade.get_ids()

              # Exibe um menu suspenso para selecionar o item
              id_item = st.selectbox("Selecione o ID do item a ser deletado:")

              # Exibe as informações do item selecionado
              if id_item is not None:
                  st.write("Informações do item:")
                  st.write(rentabilidade.get_item(id_item))

              # Retorna o ID do item selecionado, ou None se nenhum item for selecionado
              if st.button("Deletar Item"):
                  return id_item
              else:
                  return None

            def main__repr():
                st.sidebar.title("Análise de Rentabilidade")
                pagina = st.sidebar.selectbox("Selecione a página", [
                    "Início",
                    "Dados Brutos",
                    "Adicionar Item",
                    "Atualizar Item",
                    "Deletar Item",
                    "Análise de Rentabilidade",
                    "Sobre"
                ])

                rentabilidade = Rentabilidade("client/src/data/rentabilidade.csv")

                if pagina == "Início":
                    st.write("Bem-vindo à página de Análise de Rentabilidade")
                    st.write("Selecione uma página na barra lateral para começar")

                elif pagina == "Dados Brutos":
                    st.subheader("Dados Brutos")
                    # Carrega dados brutos de rentabilidade
                    rentabilidade.load_data()
                    # Exibe os dados brutos na tela
                    st.write("A seguir, são apresentados os dados brutos de rentabilidade registrados:")
                    rentabilidade.show_table()

                    rentabilidade.load_data()
                    st.write("Preencha os dados do item abaixo:")
                    nome_item = st.text_input("Item")
                    preco_venda = st.number_input("Preço de venda", value=0.0, step=0.01)
                    custo_producao = st.number_input("Custo de produção", value=0.0, step=0.01)

                elif st.button("Adicionar item"):
                    def exibe_formulario_novo_item():
                      st.write("Entre com as informações do novo item:")
                      nome_item = st.text_input("Item")
                      preco_venda = st.number_input("Preço de Venda", min_value=0.0)
                      custo_producao = st.number_input("Custo de Produção", min_value=0.0)

                      if st.button("Adicionar Item"):
                          if nome_item is not None:
                              rentabilidade.add_item(nome_item, preco_venda, custo_producao)
                          else:
                              st.error("Por favor, preencha todos os campos.")
                    exibe_formulario_novo_item()

                elif pagina == "Atualizar Item":
                  st.subheader("Atualizar Item")
                  # Carrega dados brutos de rentabilidade
                  rentabilidade.load_data()
                  # Exibe o formulário para atualizar um item existente
                  id_item = exibe_formulario_atualiza_item(rentabilidade)
                  if id_item is not None:
                      atualizador = AtualizadorDeItem(rentabilidade)
                      atualizador.atualizar(id_item)
















                elif pagina == "Deletar Item":
                  st.subheader("Deletar Item")
                  rentabilidade.load_data()
                  rentabilidade.exibe_formulario_deleta_item()

                elif pagina == "Análise de Rentabilidade":
                    st.subheader("Análise de Rentabilidade")
                    # Carrega dados brutos de rentabilidade
                    rentabilidade.load_data()
                    # Exibe gráfico com a análise de rentabilidade
                    rentabilidade.plot_rentabilidade()
                
            main__repr()

          if selecionar == "Análise de lucro líquido":

            class DadosRestaurante:
                def __init__(self, csv_file):
                    self.csv_file = csv_file
                    self.data = pd.DataFrame()

                def load_data(self):
                    self.data = pd.read_csv(self.csv_file)

                def show_table(self):
                    st.write(self.data)

                def save_data(self):
                    self.data.to_csv(self.csv_file, index=False)


            class AnaliseLucroLiquido:
                def __init__(self, dados: DadosRestaurante):
                    self.dados = dados

                def calcular_lucro_liquido(self):
                    custos_fixos = self.dados.data["Custos fixos"].sum()
                    custos_variaveis = self.dados.data["Custos variáveis"].sum()
                    receita_total = self.dados.data["Receita total"].sum()

                    lucro_liquido = receita_total - custos_fixos - custos_variaveis

                    return lucro_liquido


            def analise_lucro_liquido(dados: DadosRestaurante):
                st.subheader("Análise de Lucro Líquido")

                # Exibir dados em uma tabela
                dados.show_table()

                # Calcular lucro líquido
                lucro_liquido = AnaliseLucroLiquido(dados).calcular_lucro_liquido()

                st.write(f"Lucro líquido: R$ {lucro_liquido:.2f}")

                # Salvando os dados em arquivo CSV
                if not os.path.isfile("client/src/data/lucro_liquido.csv"):
                    lucro_liquido_df = pd.DataFrame({"Lucro líquido": [lucro_liquido]})
                    lucro_liquido_df.to_csv("client/src/data/lucro_liquido.csv", index=False)
                    st.info("Arquivo CSV criado com sucesso!")
                else:
                    with open("client/src/data/lucro_liquido.csv", "a") as f:
                        lucro_liquido_df = pd.DataFrame({"Lucro líquido": [lucro_liquido]})
                        lucro_liquido_df.to_csv(f, header=False, index=False)
                        st.info("Dados adicionados ao arquivo CSV com sucesso!")

                # Perguntar se deseja ver os dados completos do arquivo client/src/data/lucro_liquido.csv
                if st.button("Ver dados completos do arquivo CSV"):
                    data = pd.read_csv("client/src/data/lucro_liquido.csv")
                    st.dataframe(data)
            
            dados = DadosRestaurante("client/src/data/lucro_liquido.csv")
            dados.load_data()
            analise_lucro_liquido(dados)

          if selecionar == "Análise de Tendências de Vendas":
            from datetime import date, timedelta
            class Vendas:
                def __init__(self, csv_file):
                    self.csv_file = csv_file
                    self.data = pd.DataFrame(columns=["ID", "DataVenda", "Valor"])

                def load_data(self):
                    self.data = pd.read_csv(self.csv_file)

                def save_data(self):
                    if not os.path.isfile(self.csv_file):
                        self.data.to_csv(self.csv_file, index=False)
                        st.info("Arquivo CSV criado com sucesso!")
                    else:
                        with open(self.csv_file, "a") as f:
                            self.data.to_csv(f, header=False, index=False)
                            st.info("Dados adicionados ao arquivo CSV com sucesso!")

                def add_venda(self, data_venda, valor):
                    id = len(self.data) + 1
                    self.data = self.data.append({
                        "ID": id,
                        "DataVenda": data_venda,
                        "Valor": valor
                    }, ignore_index=True)
                    self.save_data()
                    st.success("Venda adicionada com sucesso!")
                  
                def remove_venda(self, id):
                    self.data = self.data[self.data.ID != id]
                    self.save_data()
                    st.success("Venda removida com sucesso!")
                  
                def update_venda(self, id, data_venda, valor):
                    index = self.data.index[self.data['ID'] == id].tolist()[0]
                    self.data.loc[index, "DataVenda"] = data_venda
                    self.data.loc[index, "Valor"] = valor
                    self.save_data()
                    st.success("Venda atualizada com sucesso!")
                  
                def show_table(self):
                    st.write(self.data)

                def plot_vendas(self):
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=self.data['DataVenda'], y=self.data['Valor'], mode='lines+markers', name='Vendas'))
                    fig.update_layout(title="Tendências de Vendas",
                                      xaxis_title="DataVenda",
                                      yaxis_title="Valor")
                    st.plotly_chart(fig)

            def remover_todas_vendas():
              vendas = Vendas("client/src/data/vendas.csv")
              if st.button("Remover todas as vendas"):
                  vendas.data.drop(vendas.data.index, inplace=True)
                  vendas.save_data()
                  st.success("Todas as vendas foram removidas com sucesso!")
                  vendas.show_table()

            def plot_vendas_bar():
              vendas = Vendas("client/src/data/vendas.csv")
              vendas.load_data()
              venda_agrupada = vendas.data.groupby(['DataVenda']).sum()
              venda_agrupada.reset_index(inplace=True)

              fig = go.Figure(data=[go.Bar(x=venda_agrupada['DataVenda'], y=venda_agrupada['Valor'])])
              fig.update_layout(title="Vendas por data",
                                xaxis_title="Data da venda",
                                yaxis_title="Valor",
                                xaxis_tickangle=-45)
              st.plotly_chart(fig)

            def filtrar_vendas_por_data():
              vendas = Vendas("client/src/data/vendas.csv")
              vendas.load_data()

              st.subheader("Filtrar Vendas por Data")

              min_date = pd.to_datetime(vendas.data['DataVenda']).min().to_pydatetime().date()
              max_date = pd.to_datetime(vendas.data['DataVenda']).max().to_pydatetime().date()

              data_inicio = st.date_input("Data Início", min_date, min_value=min_date, max_value=max_date)
              data_fim = st.date_input("Data Fim", max_date, min_value=min_date, max_value=max_date)

              if data_inicio > data_fim:
                  st.error("A data de início não pode ser maior que a data fim.")
                  return

              mask = (vendas.data['DataVenda'] >= data_inicio.isoformat()) & (vendas.data['DataVenda'] <= data_fim.isoformat())

              vendas_filtradas = vendas.data.loc[mask]

              if vendas_filtradas.empty:
                  st.warning("Não há vendas registradas no intervalo selecionado.")
              else:
                  st.write("Vendas registradas no intervalo selecionado:")
                  st.write(vendas_filtradas)


            def adicionar_venda():
                st.subheader("Adicionar Venda")

                vendas = Vendas("client/src/data/vendas.csv")
                vendas.load_data()

                data_venda = vendas.data['DataVenda'].iloc[-1]
                data_venda = date.fromisoformat(data_venda) if isinstance(data_venda, str) else date.today()

                new_data_venda = st.date_input("DataVenda", data_venda)
                if isinstance(new_data_venda, date):
                    data_venda = new_data_venda.isoformat()

                    valor = st.number_input("Valor da Venda", value=0.0, step=0.01)
                    if st.button("Adicionar venda"):
                        vendas.add_venda(data_venda, valor)
                        st.success("Venda adicionada com sucesso!")
                        vendas.show_table()
            
            def buscar_venda():
              st.subheader("Buscar Venda")
              vendas = Vendas("client/src/data/vendas.csv")
              vendas.load_data()
              vendas.show_table()

              venda_id = st.number_input("Digite o ID da venda que deseja buscar:", value=1)

              if st.button("Buscar Venda"):
                  if venda_id not in vendas.data["ID"].values:
                      st.error("ID da venda não encontrado na tabela")
                      return
                  data = vendas.data[vendas.data['ID'] == venda_id].iloc[0]
                  st.write("ID: ", data['ID'])
                  st.write("Data da Venda: ", data['DataVenda'])
                  st.write("Valor: ", data['Valor'])

                  opcoes_graficos = ["Gráfico de Linhas", "Gráfico de Barras", "Gráfico de Área", "Gráfico de Dispersão"]
                  tipo_grafico = st.selectbox("Selecione o tipo de gráfico:", opcoes_graficos)

                  if tipo_grafico == "Gráfico de Linhas":
                      fig = go.Figure()
                      fig.add_trace(go.Scatter(x=[data['DataVenda']], y=[data['Valor']], mode='lines+markers', name='Vendas'))
                      fig.update_layout(title="Vendas",
                                        xaxis_title="DataVenda",
                                        yaxis_title="Valor")
                      st.plotly_chart(fig)

                  elif tipo_grafico == "Gráfico de Barras":
                      fig = go.Figure()
                      fig.add_trace(go.Bar(x=[data['DataVenda']], y=[data['Valor']], name='Vendas'))
                      fig.update_layout(title="Vendas",
                                        xaxis_title="DataVenda",
                                        yaxis_title="Valor")
                      st.plotly_chart(fig)

                  elif tipo_grafico == "Gráfico de Área":
                      fig = go.Figure()
                      fig.add_trace(go.Scatter(x=[data['DataVenda']], y=[data['Valor']], mode='lines', name='Vendas'))
                      fig.add_trace(go.Scatter(x=[data['DataVenda']], y=[0], mode='lines', name='Base'))
                      fig.update_layout(title="Vendas",
                                        xaxis_title="DataVenda",
                                        yaxis_title="Valor")
                      st.plotly_chart(fig)

                  elif tipo_grafico == "Gráfico de Dispersão":
                      fig = go.Figure()
                      fig.add_trace(go.Scatter(x=[data['DataVenda']], y=[data['Valor']], mode='markers', name='Vendas'))
                      fig.update_layout(title="Vendas",
                                        xaxis_title="DataVenda",
                                        yaxis_title="Valor")
                      st.plotly_chart(fig)


            def remover_todas_vendas():
                st.warning("Tem certeza que deseja remover todas as vendas?")
                if st.button("Sim, remover tudo!"):
                    vendas = Vendas("client/src/data/vendas.csv")
                    vendas.load_data()
                    vendas.data = pd.DataFrame(columns=["ID", "DataVenda", "Valor"])
                    vendas.save_data()
                    st.success("Todas as vendas foram removidas com sucesso!")

            def gerar_relatorio():
                st.subheader("Gerar Relatório de Vendas")

                # Criação dos widgets para inserir as datas de início e fim
                data_inicio = st.date_input("Data de início", date(2022, 1, 1))
                data_fim = st.date_input("Data de fim", date.today())

                vendas = Vendas("client/src/data/vendas.csv")
                vendas.load_data()

                vendas_periodo = vendas.data[(vendas.data["DataVenda"] >= str(data_inicio)) & (vendas.data["DataVenda"] <= str(data_fim))]
                valor_total = vendas_periodo["Valor"].sum()
                st.write("Valor total de vendas no período selecionado: ", valor_total)

                # Seletor de tipo de gráfico
                tipo_grafico = st.selectbox("Selecione o tipo de gráfico", ["Linha", "Barra", "Bolha", "Dispersão", "Tabela"])

                if tipo_grafico == "Linha":
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=vendas_periodo['DataVenda'], y=vendas_periodo['Valor'], mode='lines+markers', name='Vendas'))
                    fig.update_layout(title="Tendências de Vendas no Período Selecionado",
                                        xaxis_title="DataVenda",
                                        yaxis_title="Valor")
                    st.plotly_chart(fig)

                elif tipo_grafico == "Barra":
                    fig = px.bar(vendas_periodo, x="DataVenda", y="Valor", title="Tendências de Vendas no Período Selecionado")
                    st.plotly_chart(fig)

                elif tipo_grafico == "Bolha":
                    fig = px.scatter(vendas_periodo, x="DataVenda", y="Valor", size="Valor", title="Tendências de Vendas no Período Selecionado")
                    st.plotly_chart(fig)

                elif tipo_grafico == "Dispersão":
                    fig = px.scatter(vendas_periodo, x="DataVenda", y="Valor", title="Tendências de Vendas no Período Selecionado")
                    st.plotly_chart(fig)

                else:
                    st.write(vendas_periodo)

            def resumo_vendas():
              st.subheader("Resumo de Vendas por Período")

              vendas = Vendas("client/src/data/vendas.csv")
              vendas.load_data()

              data_inicio = st.date_input("Data Inicial", value=(date.today() - timedelta(days=30)))
              data_fim = st.date_input("Data Final", value=date.today())

              df_vendas = vendas.data[(vendas.data["DataVenda"] >= data_inicio.isoformat()) & (vendas.data["DataVenda"] <= data_fim.isoformat())]

              if df_vendas.empty:
                  st.warning("Nenhuma venda realizada no período selecionado")
                  return

              total_vendas = df_vendas["Valor"].sum()
              media_vendas = df_vendas["Valor"].mean()
              max_vendas = df_vendas["Valor"].max()
              min_vendas = df_vendas["Valor"].min()

              st.write(f"Total de vendas no período: R$ {total_vendas:.2f}")
              st.write(f"Média de vendas no período: R$ {media_vendas:.2f}")
              st.write(f"Maior venda no período: R$ {max_vendas:.2f}")
              st.write(f"Menor venda no período: R$ {min_vendas:.2f}")

            def analise_vendas():
              st.subheader("Análise de Vendas")

              vendas = Vendas("client/src/data/vendas.csv")
              vendas.load_data()

              valor_minimo = vendas.data['Valor'].min()
              valor_maximo = vendas.data['Valor'].max()
              valor_medio = vendas.data['Valor'].mean()

              st.write(f"Valor mínimo de venda: R${valor_minimo:.2f}")
              st.write(f"Valor máximo de venda: R${valor_maximo:.2f}")
              st.write(f"Valor médio de venda: R${valor_medio:.2f}")

              st.markdown("---")

              fig = px.histogram(vendas.data, x="Valor", nbins=30)
              st.plotly_chart(fig)

              st.markdown("---")

              vendas.plot_vendas()

            def deletar_venda():
              st.subheader("Deletar Venda")
              vendas = Vendas("client/src/data/vendas.csv")
              vendas.load_data()
              vendas.show_table()
              venda_id = st.number_input("Digite o ID da venda que deseja deletar:", value=1)

              if st.button("Deletar Venda"):
                  vendas.remove_venda(venda_id)
                  st.success("Venda removida com sucesso!")
                  vendas.show_table()

            def atualizar_venda():
              st.subheader("Atualizar Venda")

              vendas = Vendas("client/src/data/vendas.csv")
              vendas.load_data()

              venda_id = st.number_input("Digite o ID da venda que deseja atualizar", value=0)

              # Verifica se o ID existe na tabela
              if venda_id not in vendas.data["ID"].values:
                  st.error("ID da venda não encontrado na tabela")
                  return

              data = vendas.data[vendas.data['ID'] == venda_id].iloc[0]

              data_venda = st.date_input("Data da Venda", data['DataVenda'])
              valor = st.number_input("Valor da Venda", value=data['Valor'], step=0.01)

              if st.button("Atualizar venda"):
                  vendas.update_venda(venda_id, data_venda, valor)
                  st.success("Venda atualizada com sucesso!")
                  vendas.show_table()

            def __mainVendas():
                st.title("Análise de Tendências de Vendas")
                pagina = st.selectbox("Selecione a página",
                [
                   "Início", "Dados Brutos", "Resumo de Vendas", "Adicionar Venda",
                   "Buscar Venda", "Atualizar Venda", "Deletar Venda", "Remover Todas as Vendas",
                   "Gerar Relatório de Vendas", "Filtrar Venda por Data", "Análise de Vendas", "Sobre"
                ])

                if pagina == "Início":
                    st.write("Bem-vindo à página de Análise de Tendências de Vendas")
                    st.write("Selecione uma página na barra lateral para começar")

                elif pagina == "Dados Brutos":
                  st.subheader("Dados Brutos")

                  visualizacao = st.radio("Selecione como visualizar os dados", ["Tabela", "Gráfico de Linhas", "Gráfico de Bolhas"])
                  vendas = Vendas("client/src/data/vendas.csv")
                  vendas.load_data()

                  if visualizacao == "Tabela":
                      vendas.show_table()
                  elif visualizacao == "Gráfico de Linhas":
                      fig = go.Figure()
                      fig.add_trace(go.Scatter(x=vendas.data['DataVenda'], y=vendas.data['Valor'], mode='lines+markers', name='Vendas'))
                      fig.update_layout(title="Tendências de Vendas",
                                        xaxis_title="DataVenda",
                                        yaxis_title="Valor")
                      st.plotly_chart(fig)
                  elif visualizacao == "Gráfico de Bolhas":
                      fig = px.scatter(vendas.data, x='DataVenda', y='Valor', size='Valor')
                      fig.update_layout(title="Tendências de Vendas",
                                        xaxis_title="DataVenda",
                                        yaxis_title="Valor")
                      st.plotly_chart(fig)


                elif pagina == "Resumo de Vendas":
                  resumo_vendas()

                elif pagina == "Adicionar Venda":
                    adicionar_venda()

                elif pagina == "Buscar Venda":
                    buscar_venda()

                elif pagina == "Atualizar Venda":
                    atualizar_venda()

                elif pagina == "Deletar Venda":
                    deletar_venda()

                elif pagina == "Remover Todas as Vendas":
                    remover_todas_vendas()
                  
                elif pagina == "Gerar Relatório de Vendas":
                    gerar_relatorio()

                elif pagina == "Filtrar Venda por Data":
                   filtrar_vendas_por_data()

                elif pagina == "Análise de Vendas":
                    analise_vendas()


            __mainVendas()


          if selecionar == "Previsão de demanda":
            def load_data():
                return pd.read_csv("client/src/data/previsao_demanda.csv")
            
            def previsao_demanda():
              st.subheader("Previsão de Demanda")

              # Carrega os dados
              data = load_data()

              # Cria uma lista com as datas únicas
              datas = data["Data"].unique().tolist()

              # Seleciona a data para análise
              data_selecionada = st.selectbox("Selecione a data para análise:", datas)

              # Filtra os dados pela data selecionada
              data_filtrada = data[data["Data"] == data_selecionada]

              # Cria um gráfico de barras com a quantidade de clientes por hora
              fig = px.bar(data_filtrada, x="Hora", y="Clientes")
              fig.update_layout(title="Previsão de Demanda - Clientes por Hora",
                                xaxis_title="Hora",
                                yaxis_title="Número de Clientes")
              st.plotly_chart(fig)

              # Previsão de demanda
              media_clientes = int(data_filtrada["Clientes"].mean())
              st.write(f"A média de clientes para o dia {data_selecionada} é de {media_clientes} clientes.")

              # Recomendação de recursos
              if media_clientes <= 50:
                  st.success("Recomendamos que sejam alocados recursos para atender até 50 clientes.")
              elif media_clientes > 50 and media_clientes <= 100:
                  st.warning("Recomendamos que sejam alocados recursos para atender entre 50 e 100 clientes.")
              else:
                  st.error("Recomendamos que sejam alocados recursos para atender mais de 100 clientes.")

              # Salvando os dados em arquivo CSV
              if not os.path.isfile("client/src/data/previsao_demanda.csv"):
                  data_filtrada.to_csv("client/src/data/previsao_demanda.csv", index=False)
                  st.info("Arquivo CSV criado com sucesso!")
              else:
                  with open("client/src/data/previsao_demanda.csv", "a") as f:
                      data_filtrada.to_csv(f, header=False, index=False)
                      st.info("Dados adicionados ao arquivo CSV com sucesso!")

              # Perguntar se deseja ver os dados completos do arquivo client/src/data/previsao_demanda.csv
              if st.button("Ver dados completos do arquivo CSV"):
                  data = pd.read_csv("client/src/data/previsao_demanda.csv")
                  st.dataframe(data)

            previsao_demanda()

          if selecionar == "Dados Brutos":
            st.markdown("### DADOS BRUTOS")

            if st.checkbox("Clique aqui para ver os dados",False):
                st.markdown("###### ESTES SÃO OS DADOS BRUTOS PARA TODAS AS COMPARAÇÕES E GRÁFICO")
                st.write(data)

            if st.checkbox("Clique aqui para ver os dados de bebidas",False):
              st.markdown("###### ESTES SÃO OS DADOS BRUTOS PARA TODAS AS COMPARAÇÕES E GRÁFICO")
              # display_bebidas()
              st.write(dataBebidas)

            if st.checkbox("Clique aqui para ver os dados de estoque",False):
              st.markdown("###### ESTES SÃO OS DADOS BRUTOS PARA TODAS AS COMPARAÇÕES E GRÁFICO")
              st.write(dataEstoque)

            if st.checkbox("Clique aqui para ver os dados de pratos",False):
              st.markdown("###### ESTES SÃO OS DADOS BRUTOS PARA TODAS AS COMPARAÇÕES E GRÁFICO")
              st.write(dataPratos)

            if st.checkbox("Clique aqui para ver os dados de clientes",False):
              st.markdown("###### ESTES SÃO OS DADOS BRUTOS PARA TODAS AS COMPARAÇÕES E GRÁFICO")
              st.write(dataClientes)

            st.markdown("### A COMPARAÇÃO DA BOLHA")
            st.markdown("Esta é a classificação das bebidas em termos de faixa de preço. Aqui no eixo Y, o tamanho da bolha descreve a classificação que se espalhou pelo pool da faixa de preço.")
            st.markdown("##### CLASSIFICAÇÃO DE BEBIDAS ★★★★★")

            # Ler os dados do arquivo CSV
            df_bebidas = pd.read_csv('client/src/data/bebidas.csv')

            # Criar um gráfico de bolhas com preço no eixo x, quantidade vendida no eixo y e tamanho das bolhas representando o total de vendas
            chart = alt.Chart(df_bebidas).mark_circle().encode(
                x=alt.X('preco', title='Preço'),
                y=alt.Y('quantidade_vendas', title='Quantidade Vendida'),
                size=alt.Size('total_vendas', title='Total de Vendas'),
                color=alt.Color('nome', title='Bebida'),
                tooltip=['nome', 'preco', 'quantidade_vendas', 'total_vendas']
            ).properties(width=700, height=500)

            # Exibir o gráfico
            st.altair_chart(chart)


            st.markdown("### A COMPARAÇÃO DO ESTOQUE DE MERCADORIAS")
            st.markdown("Esta é a comparação do estoque de mercadorias por ID e quantidade. Aqui no eixo X, temos o ID e no eixo Y, a quantidade em estoque.")
            st.markdown("##### ESTOQUE DE MERCADORIAS ★★★★★")

            # Ler os dados do arquivo CSV
            df_mercadorias = pd.read_csv('client/src/data/estoque_mercadorias.csv')

            # Criar um gráfico de barras com ID no eixo x e quantidade no eixo y
            chart = alt.Chart(df_mercadorias).mark_bar().encode(
                x=alt.X('ID', title='ID'),
                y=alt.Y('QUANTIDADE', title='Quantidade em Estoque'),
                tooltip=['NOME', 'QUANTIDADE']
            ).properties(width=700, height=500)

            # Exibir o gráfico
            st.altair_chart(chart)

            st.markdown("### Comparação de Pratos")
            st.markdown("Neste gráfico, cada bolha representa um prato e o tamanho da bolha representa a quantidade em estoque.")
            st.markdown("##### CLASSIFICAÇÃO DE DADOS DE PRATOS ★★★★★")

            # Carregando os dados do arquivo CSV
            dataBebidas = pd.read_csv("client/src/data/pratos.csv")

            # Criando o gráfico de bolhas com Altair
            chart = alt.Chart(dataBebidas).mark_circle(size=100).encode(
                x='NOME',
                y='PRECO',
                color='ACOMPANHAMENTO',
                tooltip=['NOME', 'PRECO', 'ACOMPANHAMENTO']
            ).properties(
                width=600,
                height=400
            )

            # Exibindo o gráfico na tela
            st.altair_chart(chart, use_container_width=True)

            st.markdown("### Comparação de Clientes")
            st.markdown("Neste gráfico, o tamanho da bolha representa o gasto total de cada cliente.")
            st.markdown("##### CLASSIFICAÇÃO DE DADOS DE CLIENTES ★★★★★")

            st.vega_lite_chart(dadosClientes, {
                'mark': {'type': 'circle', 'tooltip': True},
                'encoding': {
                    'x': {'field': 'NOME', 'type': 'ordinal'},
                    'y': {'field': 'GASTO', 'type': 'quantitative'},
                    'size': {'field': 'GASTO', 'type': 'quantitative'},
                    'color': {'field': 'GASTO', 'type': 'quantitative'},
                },
            }, use_container_width=True)

          st.sidebar.markdown("### CLASSIFICAÇÃO ★★★★★")
          st.sidebar.markdown("""
            A avaliação dos restaurantes pode ser feita através de uma escala de 0 a 5 estrelas, sendo 0 o pior e 5 o melhor. Utilize o slider abaixo para classificar o restaurante:
          """)
          rate=st.sidebar.slider("Classificar o restaurante",0.0,5.0)

          initial()

          # Lista de opções
          options = ["Menu", "Reservas", "Avaliações"]

          # Configurações da barra lateral
          st.sidebar.markdown("# Opções")
          st.sidebar.markdown("Selecione uma das opções abaixo para continuar:")

          # Obtém a opção selecionada pelo usuário
          option = st.sidebar.selectbox("", options)

          # Verifica qual opção foi selecionada e exibe as informações correspondentes
          if option == "Menu":
              st.sidebar.markdown("# Menu")
              st.sidebar.markdown("""
              ### Entradas
              * Salada de folhas verdes com tomate seco e queijo de cabra - R$ 22,00
              * Ceviche de peixe branco com cebola roxa e coentro - R$ 32,00
              * Bolinho de bacalhau com maionese de alho e limão - R$ 28,00

              ### Pratos Principais
              * Filé mignon grelhado com molho de cogumelos e risoto de parmesão - R$ 62,00
              * Salmão assado com molho de maracujá e purê de batata doce - R$ 48,00
              * Massa ao molho de camarão e tomate fresco - R$ 42,00

              ### Sobremesas
              * Cheesecake de frutas vermelhas - R$ 18,00
              * Brownie de chocolate com sorvete de creme - R$ 16,00
              * Pudim de leite com calda de caramelo - R$ 14,00
              """)

          elif option == "Reservas":
              st.sidebar.markdown("# Reservas")
              st.sidebar.markdown("""
              Para fazer uma reserva, entre em contato com o restaurante pelos seguintes meios:

              * Telefone: (11) 1234-5678
              * E-mail: reservas@restaurantexyz.com.br
              * Site: www.restaurantexyz.com.br/reservas
              """)

          else:
              st.sidebar.markdown("# Avaliações")
              st.sidebar.markdown("""
              ### Avaliações dos Clientes

              * "Adorei o restaurante! Comida deliciosa e atendimento excelente!" - João, São Paulo
              * "Ambiente super agradável e pratos muito bem elaborados!" - Maria, Rio de Janeiro
              * "Comida ótima, porém achei um pouco caro. Mesmo assim, recomendo!" - Pedro, Belo Horizonte
              """)

          
          # Ao selecionar a opção "Classificação", salva o valor da classificação no arquivo "client/src/data/classificacao.csv" e colocar o tipo de classificação, se é positiva ou negativa
          if st.sidebar.button("Classificar"):
              if rate == 0.0:
                st.warning("Classificação não realizada!")
                st.balloons()
              elif rate < 1.0:
                with open('client/src/data/classificacao.csv', 'a') as arquivo:
                  arquivo.write(f"{rate},negativa\n")
                st.success("Classificação feita com sucesso!")
                st.balloons()
              elif rate >= 1.0 and rate < 2.0:
                with open('client/src/data/classificacao.csv', 'a') as arquivo:
                  arquivo.write(f"{rate},negativa\n")
                st.success("Classificação feita com sucesso!")
                st.balloons()
              elif rate >= 2.0 and rate < 3.0:
                with open('client/src/data/classificacao.csv', 'a') as arquivo:
                  arquivo.write(f"{rate},negativa\n")
                st.success("Classificação feita com sucesso!")
                st.balloons()
              elif rate >= 3.0 and rate < 4.0:
                with open('client/src/data/classificacao.csv', 'a') as arquivo:
                  arquivo.write(f"{rate},positiva\n")
                st.success("Classificação feita com sucesso!")
                st.balloons()
              elif rate >= 4.0 and rate < 5.0:
                with open('client/src/data/classificacao.csv', 'a') as arquivo:
                  arquivo.write(f"{rate},positiva\n")
                st.success("Classificação feita com sucesso!")
                st.balloons()
              elif rate >= 5.0:
                with open('client/src/data/classificacao.csv', 'a') as arquivo:
                  arquivo.write(f"{rate},positiva\n")
                st.success("Classificação feita com sucesso!")
                st.balloons()

          if selecionar == "funcionarios":
              st.subheader("Cadastro de Funcionários")
              
              # Criação do dataframe
              dataFunc = pd.DataFrame(columns=["Nome do funcionário", "Cargo", "Especialidade", "Salário do dia", "Dias de trabalho"])
              
              # Adicionar funcionário
              st.write("Preencha os dados do funcionário abaixo:")
              nome = st.text_input("Nome do funcionário")
              cargo = st.selectbox("Cargo", ["Gerente", "Garçom", "Cozinheiro", "Auxiliar de cozinha"])
              especialidade = st.text_input("Especialidade")
              salario_dia = st.number_input("Salário do dia trabalhado", value=0.0, step=0.01)
              dias_trabalhados = st.number_input("Dias de trabalho", value=0, step=1)
              
              # Botão para adicionar funcionário
              if st.button("Adicionar funcionário"):
                  # Verifica se o funcionário já foi cadastrado anteriormente
                  if nome in dataFunc["Nome do funcionário"].tolist():
                      st.warning("Funcionário já cadastrado")
                  else:
                      # Adiciona o funcionário ao dataframe
                      dataFunc = dataFunc.append({
                          "Nome do funcionário": nome,
                          "Cargo": cargo,
                          "Especialidade": especialidade,
                          "Salário do dia": salario_dia,
                          "Dias de trabalho": dias_trabalhados
                      }, ignore_index=True)
                      st.success("Funcionário cadastrado com sucesso!")
                  
              st.write("Lista de funcionários:")
              st.dataframe(dataFunc)
              
              # Cálculo do salário dos funcionários
              dataFunc["Salário a receber"] = dataFunc["Salário do dia"] * dataFunc["Dias de trabalho"] * 1.10
              
              # Gráfico de salário dos funcionários
              fig = go.Figure()
              fig.add_trace(go.Bar(x=dataFunc["Nome do funcionário"],
                                  y=dataFunc["Salário a receber"],
                                  marker_color='purple'))
              fig.update_layout(title="Salário dos Funcionários",
                                xaxis_title="Nome do Funcionário",
                                yaxis_title="Salário a Receber")
              st.plotly_chart(fig)
                    
              # Salvando os dados em arquivo CSV
              if not os.path.isfile("client/src/data/funcionarios.csv"):
                  dataFunc.to_csv("client/src/data/funcionarios.csv", index=False)
                  st.info("Arquivo CSV criado com sucesso!")
              else:
                  with open("client/src/data/funcionarios.csv", "a") as f:
                      dataFunc.to_csv(f, header=False, index=False)
                      st.info("Dados adicionados ao arquivo CSV com sucesso!")

              # Perguntar se deseja ver os dados completos do arquivo client/src/data/funcionarios.csv

              if st.button("Ver dados completos do arquivo CSV"):
                  data = pd.read_csv("client/src/data/funcionarios.csv")
                  st.dataframe(data)

          if selecionar == "Análise de desempenho dos funcionários":
              def employee_performance_analysis():
                # Criação do dataframe
                if not os.path.isfile("client/src/data/funcionarios.csv"):
                    dataFunc = pd.DataFrame(columns=["ID", "Nome do funcionário", "Cargo", "Especialidade", "Salário", "Dias trabalhados", "Salário dia"])
                else:
                    dataFunc = pd.read_csv("client/src/data/funcionarios.csv")

                st.subheader("Cadastro de Funcionários")

                # Adicionar funcionário
                st.write("Preencha os dados do funcionário abaixo:")
                nome = st.text_input("Nome do funcionário")
                cargo = st.selectbox("Cargo", ["Gerente", "Garçom", "Cozinheiro", "Auxiliar de cozinha"])
                especialidade = st.text_input("Especialidade")
                salario = st.number_input("Salário", value=0.0, step=0.01)
                dias_trabalhados = st.number_input("Dias trabalhados", value=0, step=1)
                salario_dia = salario / dias_trabalhados if dias_trabalhados != 0 else 0

                # Botão para adicionar funcionário
                if st.button("Adicionar funcionário"):
                    # Verifica se o funcionário já foi cadastrado anteriormente
                    if nome in dataFunc["Nome do funcionário"].tolist():
                        st.warning("Funcionário já cadastrado")
                    else:
                        # Adiciona o funcionário ao dataframe
                        id = 1 if dataFunc.empty else dataFunc.iloc[-1]['ID'] + 1
                        dataFunc = dataFunc.append({
                            "ID": id,
                            "Nome do funcionário": nome,
                            "Cargo": cargo,
                            "Especialidade": especialidade,
                            "Salário": salario,
                            "Dias trabalhados": dias_trabalhados,
                            "Salário dia": salario_dia
                        }, ignore_index=True)
                        st.success("Funcionário cadastrado com sucesso!")
                        st.empty()

                # Lista de funcionários
                st.write("Lista de funcionários:")
                st.dataframe(dataFunc[["ID", "NOME", "CARGO", "ESPECIALIDADE", "SALÁRIO", "DIASTRABALHADOS", "SALÁRIODIA"]])

                # Cálculo do salário dos funcionários
                dataFunc["Salário a receber"] = dataFunc["SALÁRIODIA"] * dataFunc["DIASTRABALHADOS"] * 1.10

                # Gráfico de salário dos funcionários
                fig = go.Figure()
                fig.add_trace(go.Bar(x=dataFunc["NOME"],
                                    y=dataFunc["Salário a receber"],
                                    marker_color='purple'))
                fig.update_layout(title="Salário dos Funcionários",
                                  xaxis_title="NOME",
                                  yaxis_title="Salário a Receber")
                st.plotly_chart(fig)

                # Salvando os dados em arquivo CSV
                if not os.path.isfile("client/src/data/funcionarios.csv"):
                    dataFunc.to_csv("client/src/data/funcionarios.csv", index=False)
                    st.info("Arquivo CSV criado com sucesso!")
                else:
                    dataFunc.to_csv("client/src/data/funcionarios.csv", index=False)
                    st.info("Dados adicionados/atualizados no arquivo CSV com sucesso!")
                    
                # Ver dados completos do arquivo CSV
                if st.button("Ver dados completos do arquivo CSV"):
                  with open("client/src/data/funcionarios.csv", "r") as f:
                      contents = f.read()
                  st.code(contents, language="csv")

                # Análise de desempenho dos funcionários
                st.subheader("Análise de desempenho dos funcionários")

                # Selecionar o funcionário para analisar
                selected_func = st.selectbox("Selecione um funcionário para análise:", dataFunc["NOME"].tolist())

                # Mostrar os dados do funcionário selecionado
                selected_func_data = dataFunc[dataFunc["NOME"] == selected_func]
                st.write(f"Dados de desempenho de {selected_func}:")
                st.write(selected_func_data)

                # Gráfico de desempenho do funcionário selecionado
                fig = go.Figure()
                fig.add_trace(go.Bar(x=selected_func_data["ESPECIALIDADE"],
                # y=selected_func_data["Dias de trabalho"],
                marker_color='green'))
                fig.update_layout(title=f"Desempenho de {selected_func}",
                xaxis_title="ESPECIALIDADE",
                yaxis_title="Dias de trabalho")
                st.plotly_chart(fig)

              employee_performance_analysis()


          if selecionar == "Developers":
            from client.resources.developers import developers
            developers()

          class EnviadorEmail:

              def __init__(self, remetente_email, remetente_senha, destinatario_email):
                  self.remetente_email = remetente_email
                  self.remetente_senha = remetente_senha
                  self.destinatario_email = destinatario_email

              def enviar_email(self, assunto, mensagem):
                  try:
                      # Cria a mensagem de email
                      msg = MIMEMultipart()
                      msg['From'] = self.remetente_email
                      msg['To'] = self.destinatario_email
                      msg['Subject'] = assunto
                      msg.attach(MIMEText(mensagem))

                      # Conecta ao servidor SMTP e faz login na conta
                      server = smtplib.SMTP('smtp.gmail.com', 587)
                      server.starttls()
                      server.login(self.remetente_email, self.remetente_senha)

                      # Envia o email
                      server.sendmail(self.remetente_email, self.destinatario_email, msg.as_string())

                      # Exibe a mensagem de sucesso
                      st.write("Obrigado por entrar em contato!")
                      st.write(f"Sua mensagem foi enviada para {self.destinatario_email}.")
                      return True

                  except Exception as e:
                      st.error("Ocorreu um erro ao enviar a mensagem.")
                      st.error(str(e))
                      return False

                  finally:
                      server.quit()


          # Cria o objeto EnviadorEmail
          enviador_email = EnviadorEmail("seuemail@gmail.com", "suasenha", "estevamsouzalaureth@gmail.com")

          if selecionar == "Contato":
              st.markdown("## Contato")
              st.markdown("Estamos sempre prontos para ajudá-lo(a) e tirar todas as suas dúvidas. Se você tiver alguma pergunta, sugestão ou crítica, não hesite em entrar em contato conosco. Você pode nos enviar um e-mail ou ligar para o nosso telefone de contato:")
              st.markdown("### E-mail")
              st.markdown("contato@pedacinhodoceu.com.br")
              st.markdown("### Telefone")
              st.markdown("+55 (48) 3237-7280")
              st.markdown("### Endereço")
              st.markdown("Rua Joaquim Neves, 152 - Praia")
              st.markdown("Florianópolis - SC")
              st.markdown("Brasil")

              st.markdown("## Contato")
              st.write("Entre em contato conosco para tirar suas dúvidas, dar sugestões ou fazer críticas construtivas!")
              st.write("Preencha o formulário abaixo com seus dados e entraremos em contato em breve.")
              st.write("")

              with st.form("form_contato"):
                  nome = st.text_input("Nome")
                  email = st.text_input("E-mail")
                  mensagem = st.text_area("Mensagem")
                  submit = st.form_submit_button("Enviar")

              if submit:
                  assunto = f"Mensagem de {nome} ({email})"
                  enviado_com_sucesso = enviador_email.enviar_email(assunto, mensagem)


          if selecionar == "Mapa":
            st.markdown("### MAPA")
            st.markdown("###### AQUI VOCÊ PODE VER O MAPA DE FLORIANÓPOLIS COM TODOS OS RESTAURANTES")
            st.markdown("### Mapa")
            st.markdown("Este mapa mostra a localização do restaurante Pedacinho do Céu.")
            # Definindo as informações de latitude e longitude manualmente
            locations = [
                [-27.7817, -48.5092]
            ]

            # Criando um dataframe com as informações de latitude e longitude
            df_locations = pd.DataFrame(
                locations,
                columns=['latitude', 'longitude']
            )

            # Exibindo o mapa com as informações de latitude e longitude
            st.map(df_locations)

            st.markdown("Estamos localizados na Rua Joaquim Neves, 152, no Praia do Sul da Ilha. Venha nos visitar e experimentar nossos deliciosos pratos!")

          if selecionar == "Consultar Dados":
            st.markdown("### AVALIAÇÕES DE RESTAURANTES / CUSTO E MUITO MAIS")
            select=st.selectbox('Selecione as opções para ver detalhes sobre o seu restaurante favorito', ['Cuisines' , 'Address','Clientes','City'])
            if select == 'Cuisines':
              st.write(data.query("Cuisines >= Cuisines")[["Restaurant_Name","Cuisines"]])
            elif select == 'Address':
              st.write(data.query("Address >= Address")[["Restaurant_Name","Address"]])
            elif select == 'Clientes':
              st.write(data.query("Clientes>= Clientes")[["Restaurant_Name","Clientes"]])
            elif select == 'City':
              st.write(data.query("City >= City")[["Restaurant_Name","City"]])
            else :
              st.write(data.query("cost_for_two >= cost_for_two")[["Restaurant_Name","cost_for_two"]])
            select=st.selectbox('Selecione as opções para ver detalhes sobre suas bebidas', ['nome' , 'preco', 'quantidade', 'descricao', 'total_vendas', 'quantidade_vendas'])
            if select == 'nome':
              st.write(dataBebidas.query("nome >= nome")[["id","nome"]])
            elif select == 'preco':
              st.write(dataBebidas.query("preco >= preco")[["id","preco"]])
            elif select == 'quantidade':
              st.write(dataBebidas.query("quantidade >= quantidade")[["id","quantidade"]])
            elif select == 'descricao':
              st.write(dataBebidas.query("descricao >= descricao")[["id","descricao"]])
            elif select == 'total_vendas':
              st.write(dataBebidas.query("total_vendas >= total_vendas")[["id","total_vendas"]])
            else :
              st.write(dataBebidas.query("quantidade_vendas >= quantidade_vendas")[["id","quantidade_vendas"]])
            select=st.selectbox('Selecione as opções para ver detalhes sobre seus pratos', ['NOME' , 'QUANTIDADE'])
            if select == 'NOME':
              st.write(dataEstoque.query("NOME >= NOME")[["ID","NOME"]])
            else :
              st.write(dataEstoque.query("QUANTIDADE >= QUANTIDADE")[["ID","QUANTIDADE"]])
            select=st.selectbox('Selecione as opções para ver detalhes sobre seus funcionários', ['NOME' , 'CARGO', 'ESPECIALIDADE', 'SALÁRIO', 'DIASTRABALHADOS', 'SALÁRIODIA'])
            if select == 'NOME':
              st.write(dataFuncionarios.query("NOME >= NOME")[["ID","NOME"]])
            elif select == 'CARGO':
              st.write(dataFuncionarios.query("CARGO >= CARGO")[["ID","CARGO"]])
            elif select == 'ESPECIALIDADE':
              st.write(dataFuncionarios.query("ESPECIALIDADE >= ESPECIALIDADE")[["ID","ESPECIALIDADE"]])
            elif select == 'SALÁRIO':
              st.write(dataFuncionarios.query("SALÁRIO >= SALÁRIO")[["ID","SALÁRIO"]])
            elif select == 'DIASTRABALHADOS':
              st.write(dataFuncionarios.query("DIASTRABALHADOS >= DIASTRABALHADOS")[["ID","DIASTRABALHADOS"]])
            else :
              st.write(dataFuncionarios.query("SALÁRIODIA >= SALÁRIODIA")[["ID","SALÁRIODIA"]])
            select=st.selectbox('Selecione as opções para ver detalhes sobre seus pratos', ['NOME' , 'PRECO', 'ACOMPANHAMENTO'])
            if select == 'NOME':
              st.write(dataPratos.query("NOME >= NOME")[["ID","NOME"]])
            elif select == 'PRECO':
              st.write(dataPratos.query("PRECO >= PRECO")[["ID","PRECO"]])
            else :
              st.write(dataPratos.query("ACOMPANHAMENTO >= ACOMPANHAMENTO")[["ID","ACOMPANHAMENTO"]])
            select=st.selectbox('Selecione as opções para ver detalhes sobre suas reservas', ['NOME' , 'DATA', 'RESERVASDATA'])
            if select == 'NOME':
              st.write(dataReservas.query("NOME >= NOME")[["ID","NOME"]])
            elif select == 'DATA':
              st.write(dataReservas.query("DATA >= DATA")[["ID","DATA"]])
            else :
              st.write(dataReservas.query("RESERVASDATA >= RESERVASDATA")[["ID","RESERVASDATA"]])
            vendasCategorias = pd.read_csv('client/src/data/vendasCategorias.csv')
            select=st.selectbox('Selecione as opções para ver detalhes sobre su as vendas por categoria', ['Categoria' , 'Vendas', 'PreçoMédio'])
            if select == 'Categoria':
              st.write(vendasCategorias.query("Categoria >= Categoria")[["id","Categoria"]])
            elif select == 'VENDAS':
              st.write(vendasCategorias.query("Vendas >= Vendas")[["id","Vendas"]])
            else :
              st.write(vendasCategorias.query("PreçoMédio >= PreçoMédio")[["id","PreçoMédio"]])

          if selecionar == "Cardápio":
            st.title("Cardápio")

            # Criação de um dataframe com o cardápio
            cardapio = pd.DataFrame({
                'Pratos': ['Lasanha', 'Pizza', 'Sopa', 'Hambúrguer', 'Churrasco'],
                'Preços': ['R$ 25,00', 'R$ 30,00', 'R$ 20,00', 'R$ 22,00', 'R$ 35,00']
            })

            # Exibição do cardápio
            st.write(cardapio)

            # Adição de imagens dos pratos
            st.write("Imagens dos pratos:")
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                # st.image("strognoff.jpg", width=150)
                pass
            with col2:
                # st.image("sequencia.jpg", width=150)
                pass
            with col3:
                # st.image("peixe.jpg", width=150)
                pass
            with col4:
                # st.image("petisco.jpg", width=150)
                pass
            with col5:
                # st.image("ostra.jpg", width=150)
                pass

          if selecionar == "Grafico de Vendas por Categoria":
            # Dados simulados
            categorias = ['Comida', 'Bebida', 'Sobremesa']
            vendas = np.random.randint(100, 1000, size=3)
            preco_medio = np.random.uniform(5, 20, size=3)
            vendas_categorias = pd.DataFrame({'Categoria': categorias, 'Vendas': vendas, 'Preço Médio': preco_medio})

            # Gráfico de bolhas
            fig = px.scatter(vendas_categorias, x='Categoria', y='Vendas', size='Preço Médio', hover_name='Categoria')
            st.plotly_chart(fig)

            # Salvar dados em arquivo
            vendas_categorias.to_csv('client/src/data/vendasCategorias.csv', index=False)

            # Projeção de vendas
            st.subheader('Projeção de vendas para a próxima semana')

            # Ler arquivo com dados
            dados = pd.read_csv('client/src/data/vendasCategorias.csv')

            # Calcular média de vendas e preço médio
            media_vendas = dados['Vendas'].mean()
            media_preco = dados['Preço Médio'].mean()

            # Calcular projeção de vendas
            projecao_vendas = media_vendas * 1.1

            # Calcular projeção de receita
            projecao_receita = projecao_vendas * media_preco

            # Exibir resultados
            st.write('Média de vendas da última semana:', media_vendas)
            st.write('Média de preço da última semana:', media_preco)
            st.write('Projeção de vendas para a próxima semana:', projecao_vendas)
            st.write('Projeção de receita para a próxima semana:', projecao_receita)

            # agora faça em um gráfico de barras

            grafico = px.bar(dados, x='Categoria', y='Vendas', color='Categoria')
            st.plotly_chart(grafico)

          if selecionar == "Previsão de Vendas":
            def cadastrar_venda(data, total_vendas):
              """Adiciona uma nova venda ao arquivo de vendas"""
              filename = "client/src/data/previsaoVendas.csv"

              # Verifica se o arquivo já existe
              if not os.path.exists(filename):
                  open(filename, "a").close()

              # Adiciona a nova venda
              with open(filename, "a") as f:
                  f.write(f"{data},{total_vendas}\n")
                  st.success("Venda cadastrada com sucesso!")
                  st.balloons()

            def __main():
              # Título
              st.title("Previsão de Vendas")

              # Input para a data da venda
              data = st.date_input("Data da venda")

              # Input para o total de vendas
              total_vendas = st.number_input("Total de vendas")

              # Botão para cadastrar a venda
              if st.button("Cadastrar Venda"):
                  cadastrar_venda(data, total_vendas)

              # Leitura do arquivo
              filename = "client/src/data/previsaoVendas.csv"
              if os.path.exists(filename):
                  dados = pd.read_csv(filename, usecols=["Data", "Total Vendas"])
                  dados["Data"] = pd.to_datetime(dados["Data"], format="%Y-%m-%d")

                  # Gráfico de linha
                  fig, ax = plt.subplots()
                  ax.plot(dados["Data"], dados["Total Vendas"])
                  ax.set_xlabel("Data")
                  ax.set_ylabel("Total de Vendas")
                  ax.set_title("Previsão de Vendas")
                  st.pyplot(fig)

            if __name__ == "__main__":
                __main()

          if selecionar == "Reservas":
            from datetime import datetime
            # Carrega ou cria o arquivo de reservas
            try:
                reservas = pd.read_csv('client/src/data/reservas.csv', parse_dates=['DATA'])
            except FileNotFoundError:
                reservas = pd.DataFrame(columns=['NOME', 'DATA', 'RESERVASDATA'])
                reservas.to_csv('client/src/data/reservas.csv', index=False)

            # Exibe o arquivo de reservas

            st.header("Reservas")
            # display_reservas()

            # Pergunta para o usuário os dados da reserva
            st.header("Faça sua Reserva")
            nome = st.text_input("Nome Completo:")
            data_str = st.date_input("Data da Reserva:")
            reservas_por_data = st.number_input("Quantidade de reservas:", min_value=1, value=1)

            # Verifica se todos os campos foram preenchidos
            if nome and data_str and reservas_por_data:
                # Salva os dados da reserva
                if st.button("Reservar"):
                    data = datetime.combine(data_str, datetime.min.time())
                    reservas = pd.concat([reservas, pd.DataFrame({'Nome': [nome], 'DATA': [data], 'RESERVASDATA': [reservas_por_data]})])
                    reservas.to_csv('client/src/data/reservas.csv', index=False)
                    st.success("Reserva feita com sucesso!")
                
                # Agrupa as reservas por data e soma a quantidade de reservas para cada data
                reservas_agrupadas = reservas.groupby('DATA')['RESERVASDATA'].sum().reset_index()

                # Plota um gráfico de linha com a data no eixo x e a quantidade de reservas no eixo y
                chart = alt.Chart(reservas_agrupadas).mark_line().encode(
                    x='DATA:T',
                    y='RESERVASDATA:Q',
                    tooltip=['DATA:T', 'RESERVASDATA:Q']
                ).properties(
                    width=700,
                    height=400
                )

                st.altair_chart(chart, use_container_width=True)
            else:
                st.warning("Preencha todos os campos para fazer uma reserva.")

          if selecionar == "Gráficos":
            getOption = st.selectbox("Selecione o gráfico que deseja visualizar", ["Gráfico de Pizza", "Gráfico de Dispersão"])

            if getOption == "Gráfico de Pizza":
              st.markdown("### GRÁFICO DE PIZZA")
              st.markdown("###### ESTE É O GRÁFICO DE PIZZA PARA BEBIDAS")
              fig_bebidas = px.pie(dataBebidas, values='preco', names='nome')
              st.plotly_chart(fig_bebidas)

              st.markdown("###### ESTE É O GRÁFICO DE PIZZA PARA O ESTOQUE DE MERCADORIAS")
              fig_estoque = px.pie(dataEstoque, values='QUANTIDADE', names='NOME')
              st.plotly_chart(fig_estoque)

              st.markdown("###### ESTE É O GRÁFICO DE PIZZA PARA PRATOS DA CASA")
              fig_pratos = px.pie(dataPratos, values='PRECO', names='NOME')
              st.plotly_chart(fig_pratos)

              st.markdown("###### ESTE É O GRÁFICO DE PIZZA PARA O TOTAL DE GASTOS DE CLIENTES")
              fig_clientes = px.pie(dataClientes, values='GASTO', names='NOME')
              st.plotly_chart(fig_clientes)

            elif getOption == "Gráfico de Dispersão":
              st.markdown("### GRÁFICO DE DISPERSÃO")
              st.markdown("###### ESTE É O GRÁFICO DE DISPERSÃO PARA TODAS AS COMPARAÇÕES")
              st.vega_lite_chart(data, {
                'mark': {'type': 'circle', 'tooltip': 500},
                'encoding': {
                    'x': {'field': 'Restaurant_Name', 'type': 'quantitative'},
                    'y': {'field': 'Rating', 'type': 'quantitative'},
                    'size': {'field': 'Price_Range', 'type': 'quantitative'},
                    'color': {'field': 'Rating', 'type': 'quantitative'},
                },
              })

              st.markdown("###### ESTE É O GRÁFICO DE DISPERSÃO PARA TODAS AS COMPARAÇÕES")
              st.vega_lite_chart(dataEstoque, {
                'mark': {'type': 'circle', 'tooltip': 500},
                'encoding': {
                    'x': {'field': 'id', 'type': 'quantitative'},
                    'y': {'field': 'quantidade', 'type': 'quantitative'},
                    'size': {'field': 'totalVendas', 'type': 'quantitative'},
                    'color': {'field': 'totalVendas', 'type': 'quantitative'},
                },
              })

              st.markdown("###### ESTE É O GRÁFICO DE DISPERSÃO PARA TODAS AS COMPARAÇÕES")
              st.vega_lite_chart(dataPratos, {
                'mark': {'type': 'circle', 'tooltip': 500},
                'encoding': {
                    'x': {'field': 'id', 'type': 'quantitative'},
                    'y': {'field': 'quantidade', 'type': 'quantitative'},
                    'size': {'field': 'totalVendas', 'type': 'quantitative'},
                    'color': {'field': 'totalVendas', 'type': 'quantitative'},
                },
              })

              st.markdown("###### ESTE É O GRÁFICO DE DISPERSÃO PARA TODAS AS COMPARAÇÕES")
              st.vega_lite_chart(dataClientes, {
                'mark': {'type': 'circle', 'tooltip': 500},
                'encoding': {
                    'x': {'field': 'id', 'type': 'quantitative'},
                    'y': {'field': 'quantidade', 'type': 'quantitative'},
                    'size': {'field': 'totalVendas', 'type': 'quantitative'},
                    'color': {'field': 'totalVendas', 'type': 'quantitative'},
                },
              })

      elif authentication_status == False:
          # st.error('Username/password is incorrect')
          pass
      elif authentication_status == None:
          st.warning('Please enter your username and password')

          # verifica se o usuário deseja redefinir a senha
          if st.button("Esqueci minha senha"):
            resetar_senha()
      
      
      # Inicializa o tempo de uso
      session_start_time = st.session_state.get('session_start_time', time.time())

      # exibe o tempo de uso
      elapsed_time = time.time() - session_start_time
      st.write("Tempo de uso:", time.strftime('%H:%M:%S', time.gmtime(elapsed_time)))
      # Botão de logout
      if authentication_status:
        st.button("Logout", on_click=logout)

  else:
      criar_conta()

if __name__ == '__main__':
  main()

  # Encerrar a sessão do Spark
  # spark.stop()