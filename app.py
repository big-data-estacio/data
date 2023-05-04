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

# Lista de funções importadas
funcoes_importadas = [
    'UserString',
    'BebidasCsvReader',
    'PratosCsvReader',
    'ReservasCsvReader',
    'EstoqueMercadoriasCsvReader',
    'PrevisaoVendasCsvReader',
    'FuncionariosCsvReader',
    'CadastroCsvReader',
    'hashlib',
    'smtplib',
    'yagmail',
    'requests',
    'csv',
    'os',
    'logging',
    'Faker',
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



from collections import UserString
from client.bebidasSpark import BebidasCsvReader
from client.pratosSpark import PratosCsvReader
from client.reservasSpark import ReservasCsvReader
from client.mercadoriasSpark import EstoqueMercadoriasCsvReader
from client.previsaoVendasSpark import PrevisaoVendasCsvReader
from client.funcionariosSpark import FuncionariosCsvReader
from client.clientesSpark import CadastroCsvReader
import hashlib
import smtplib
import yagmail
import requests
import csv
import os
import logging
from faker import Faker
import altair as alt
import pydeck as pdk
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import datetime
import streamlit as st
import time
import streamlit_authenticator as stauth
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
import hydralit_components as hc
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from abc import ABC, abstractmethod
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


"""

Para iniciar um cluster do PySpark no projeto, precisa primeiro garantir que tenha o PySpark instalado e configurado corretamente.
Também precisará de um arquivo .csv contendo os dados que deseja trabalhar.

Assumindo que já possui o PySpark instalado e configurado, pode criar uma instância de SparkSession e ler o arquivo .csv para criar um DataFrame.
Em seguida, pode passar esse DataFrame para a função que gera o gráfico de bolhas.

"""

# Criar a sessão do Spark
spark = SparkSession.builder.appName("App").getOrCreate()
spark.sparkContext.setLogLevel("OFF")

# change actual name for the users
names = ['user-1', 'user-2', 'user-3', 'user-4', 'user-5', 'user-6', 'user-7', 
        'user-8', 'user-9', 'user-10']
# change user name for the users
usernames = ['user-1', 'user-2', 'user-3', 'user-4', 'user-5', 'user-6', 'user-7', 
            'user-8', 'user-9', 'user-10']

# change password for the users
passwords = ['password-1', 'password-2', 'password-3', 'password-4', 'password-5', 'password-6', 'password-7',
            'password-8', 'password-9', 'password-10']


import csv

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

# st.set_page_config(
#     page_title="Gerenciador de Analise",
#     initial_sidebar_state="expanded",
#     layout='wide',
#     page_icon="📊"
# )


URL = os.getenv('URL')
BEBIDAS = os.getenv('BEBIDAS')
ESTOQUE = os.getenv('ESTOQUE')
PRATOS = os.getenv('PRATOS')
CLIENTES = os.getenv('CLIENTES')
FUNCIONARIOS = os.getenv('FUNCIONARIOS')
RESERVAS = os.getenv('RESERVAS')
VENDASCATEGORIAS = os.getenv('VENDASCATEGORIAS')

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

df_bebidas = pd.read_csv('client/src/data/bebidas.csv')

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
  df_bebidas = pd.read_csv('client/src/data/bebidas.csv')
  
  # Criar um gráfico de bolhas com preço no eixo x, quantidade vendida no eixo y e tamanho das bolhas representando o total de vendas
  chart = alt.Chart(df_bebidas.toPandas()).mark_circle().encode(
      x=alt.X('preco', title='Preço'),
      y=alt.Y('quantidade_vendas', title='Quantidade Vendida'),
      size=alt.Size('total_vendas', title='Total de Vendas'),
      color=alt.Color('nome', title='Bebida'),
      tooltip=['nome', 'preco', 'quantidade_vendas', 'total_vendas']
  ).properties(width=700, height=500)

  st.altair_chart(chart)


df_estoque = pd.read_csv('client/src/data/estoque_mercadorias.csv')
df_clientes = pd.read_csv('client/src/data/total_clientes.csv')

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


def gerar_grafico_bolhas_estoque():
    logging.info('Gerando gráfico de bolhas para estoque')
    st.markdown("### Gráfico de Bolhas - Estoque de Mercadorias")
    st.markdown("Esta é a classificação das mercadorias em termos de quantidade. Aqui no eixo Y, o tamanho da bolha descreve a classificação que se espalhou pelo pool de quantidades.")
    st.markdown("##### CLASSIFICAÇÃO DE MERCADORIAS ★★★★★")

    # Criar um gráfico de bolhas com quantidade no eixo x e tamanho das bolhas representando a quantidade
    chart = alt.Chart(df_estoque.toPandas()).mark_circle().encode(
        x=alt.X('QUANTIDADE', title='Quantidade'),
        size=alt.Size('QUANTIDADE', title='Quantidade'),
        color=alt.Color('NOME', title='Mercadoria'),
        tooltip=['NOME', 'QUANTIDADE']
    ).properties(width=700, height=500)

    # Exibir o gráfico
    st.altair_chart(chart)

def gerar_grafico_bolhas_clientes():
    logging.info('Gerando gráfico de bolhas para clientes')
    st.markdown("### Gráfico de Bolhas - Total de Gastos dos Clientes")
    st.markdown("Esta é a classificação dos clientes em termos de faixa de gastos. Aqui no eixo Y, o tamanho da bolha descreve a classificação que se espalhou pelo pool da faixa de gastos.")
    st.markdown("##### CLASSIFICAÇÃO DE CLIENTES ★★★★★")

    # Criar um gráfico de bolhas com gasto no eixo x e tamanho das bolhas representando a quantidade de clientes
    chart = alt.Chart(df_clientes.toPandas()).mark_circle().encode(
        x=alt.X('GASTO', title='Total de Gastos'),
        y=alt.Y('ID', title='ID do Cliente'),
        size=alt.Size('NOME', title='Nome do Cliente'),
        color=alt.Color('NOME', title='Nome do Cliente'),
        tooltip=['ID', 'NOME', 'GASTO']
    ).properties(width=700, height=500)

    # Exibir o gráfico
    st.altair_chart(chart)

def gerar_grafico_bolhas_pratos():
    logging.info('Gerando gráfico de bolhas para pratos')
    st.markdown("### Gráfico de Bolhas - Total de Preços dos Pratos")
    st.markdown("Esta é a classificação dos pratos em termos de faixa de preços. Aqui no eixo Y, o tamanho da bolha descreve a classificação que se espalhou pelo pool da faixa de preços.")
    st.markdown("##### CLASSIFICAÇÃO DE PRATOS ★★★★★")

    # Ler o arquivo CSV e criar um DataFrame com base nele
    df_pratos = pd.read_csv('client/src/data/pratos.csv')

    # Criar um gráfico de bolhas com preço no eixo x e tamanho das bolhas representando a quantidade de pratos
    chart = alt.Chart(df_pratos).mark_circle().encode(
        x=alt.X('PRECO', title='Preço'),
        y=alt.Y('ID', title='ID do Prato'),
        size=alt.Size('NOME', title='Nome do Prato'),
        color=alt.Color('NOME', title='Nome do Prato'),
        tooltip=['ID', 'NOME', 'PRECO']
    ).properties(width=700, height=500)

    # Exibir o gráfico
    st.altair_chart(chart)


def gerar_grafico_bolhas_vendas_categorias():
    logging.info('Gerando gráfico de bolhas para vendas')
    st.markdown("### Gráfico de Bolhas - Vendas por Categoria")
    st.markdown("Esta é a classificação das categorias de vendas em termos de faixa de vendas. Aqui no eixo Y, o tamanho da bolha descreve a classificação que se espalhou pelo pool da faixa de vendas.")
    st.markdown("##### CLASSIFICAÇÃO DE VENDAS ★★★★★")

    # Ler o arquivo CSV e criar um DataFrame com base nele
    df_vendas = pd.read_csv('client/src/data/vendasCategorias.csv')

    # Criar um gráfico de bolhas com vendas no eixo x e tamanho das bolhas representando o preço médio das vendas
    chart = alt.Chart(df_vendas).mark_circle().encode(
        x=alt.X('Vendas', title='Vendas'),
        y=alt.Y('id', title='ID da Categoria'),
        size=alt.Size('PreçoMédio', title='Preço Médio'),
        color=alt.Color('Categoria', title='Categoria'),
        tooltip=['id', 'Categoria', 'Vendas', 'PreçoMédio']
    ).properties(width=700, height=500)

    # Exibir o gráfico
    st.altair_chart(chart)


def display_bebidas():
    logging.info('Exibindo bebidas')
    df = BebidasCsvReader.read_csv("client/src/data/bebidas.csv")
    st.dataframe(df.toPandas())


def display_pratos():
    logging.info('Exibindo pratos')
    df = PratosCsvReader.read_csv("client/src/data/pratos.csv")
    st.dataframe(df.toPandas())


def display_reservas():
    logging.info('Exibindo reservas')
    df = ReservasCsvReader.read_csv("client/src/data/reservas.csv")
    st.dataframe(df.toPandas())


def display_estoque_mercadorias():
    logging.info('Exibindo estoque de mercadorias')
    df = EstoqueMercadoriasCsvReader.read_csv("client/src/data/estoquemercadorias.csv")
    st.dataframe(df.toPandas())


def display_previsao_vendas():
    logging.info('Exibindo previsão de vendas')
    df = PrevisaoVendasCsvReader.read_csv("client/src/data/previsaoVendas.csv")
    st.dataframe(df.toPandas())


def display_funcionarios():
    logging.info('Exibindo funcionários')
    df = FuncionariosCsvReader.read_csv("client/src/data/funcionarios.csv")
    st.dataframe(df.toPandas())


def display_cadastro():
    logging.info('Exibindo cadastro')
    df = CadastroCsvReader.read_csv("client/src/data/cadastro.csv")
    st.dataframe(df.toPandas())


class Data:
  def __init__(self, URL):
      self.URL = URL
      self.BEBIDAS = BEBIDAS
      self.ESTOQUE = ESTOQUE
      self.PRATOS = PRATOS
      self.CLIENTES = CLIENTES
      self.FUNCIONARIOS = FUNCIONARIOS
      self.RESERVAS = RESERVAS
      self.VENDASCATEGORIAS = VENDASCATEGORIAS

  def load(self):
      data=pd.read_csv(self.URL)
      return data

  def loadBebidas(self):
      data=pd.read_csv(self.BEBIDAS)
      return data

  def loadEstoque(self):
      data=pd.read_csv(self.ESTOQUE)
      return data

  def loadPratos(self):
      data=pd.read_csv(self.PRATOS)
      return data

  def loadClientes(self):
      data=pd.read_csv(self.CLIENTES)
      return data

  def loadFuncionarios(self):
      data=pd.read_csv(self.FUNCIONARIOS)
      return data
  
  def loadReservas(self):
      data=pd.read_csv(self.RESERVAS)
      return data
  
  def loadVendasCategorias(self):
      data=pd.read_csv(self.VENDASCATEGORIAS)
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

      # Pede o nome completo do cliente
      name = st.text_input("Digite seu nome completo:")

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
                  for i in range(len(users)):
                      writer.writerow([users[i], names[i], passwords[i]])

              st.success("Senha alterada com sucesso!")
          else:
              st.error("As senhas não coincidem. Por favor, tente novamente.")
      else:
          st.error("Resposta incorreta. Por favor, tente novamente.")

  def login():
      # abre o arquivo CSV e lê os usuários e senhas
      with open('client/src/data/novos_usuarios.csv', newline='') as csvfile:
          reader = csv.reader(csvfile, delimiter=',', quotechar='|')
          users = []
          passwords = []
          for row in reader:
              users.append(row[0])
              passwords.append(row[2])

      start_time = datetime.datetime.now()
      current_time = datetime.datetime.now()

      st.write("Tempo de uso:")
      while True:
          elapsed_time = current_time - start_time
          st.write(str(elapsed_time)[:-7])
          current_time = datetime.datetime.now()

      st.write("Relógio:")
      while True:
        current_time = datetime.datetime.now()
        st.write(current_time.strftime("%H:%M:%S"))
        # verifica se os dados estão corretos
        if user in users:
            index = users.index(user)
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if hashed_password == passwords[index]:
                st.success("Login realizado com sucesso!")
            else:
                st.error("Senha incorreta. Tente novamente.")
        else:
            st.error("Usuário não encontrado. Tente novamente.")

  # exibe a imagem e permite que o usuário escolha entre fazer login ou criar uma nova conta
  logo_img = Image.open('client/src/public/if-logo.png')
  st.image(logo_img, use_column_width=True)
  opcao = st.radio("Escolha uma opção:", ("Fazer login", "Criar nova conta"))

  # chama a função apropriada com base na escolha do usuário
  if opcao == "Fazer login":
    logging.info('O cliente escolheu fazer login')
    # apagar o que esteva antes
    logPlaceholder.empty()
    # login()
    @st.experimental_memo(show_spinner=False)
    def loadLogin():
        logoImg= Image.open('client/src/public/if-logo.png')
        hashed_passwords = stauth.hasher(passwords).generate()
        authenticator = stauth.authenticate(names,usernames,hashed_passwords,
            'authenticator','auth',cookie_expiry_days=0)
        return authenticator, logoImg
    with hc.HyLoader("Loading...",hc.Loaders.standard_loaders,index=1):
        authenticator, logoImg = loadLogin()
    logPlaceholder.image(logoImg, width=350)
    original_title = '<p style="font-family:Monospace; color:Gray; font-size: 25px;">Gerenciador de Analise</p>'
    titlePlaceholder.markdown(original_title, unsafe_allow_html=True)
    name, authentication_status = authenticator.login('Login','main')
    
    if authentication_status:
        logPlaceholder.empty()
        titlePlaceholder.empty()
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
        st.write("Tempo de uso:", time.strftime('%H:%M:%S', time.gmtime(elapsed_time)))

        selecionar = st.sidebar.selectbox("Selecione a página", ["Home",
                                                            "Dados Brutos",
                                                          "Consultar Dados",
                                                        "Inserir Dados",
                                                        "Mapa",
                                                      "Reservas",
                                                    "Sobre",
                                                  "Gráficos",
                                                "Contato",
                                              "Developers",
                                            "funcionarios",
                                          "Grafico de Vendas por Categoria",
                                        "Previsão de Vendas",
                                      "Cardápio",
                                    "Avaliação",
                                  "Grafico de Vendas por Categoria e Mês",
                                "Grafico de Vendas por Categoria e Dia da Semana",
                              "Sugestões",
                            "Grafico de Vendas Mensais",
                          "Previsão de clientes",
                        ]
                      )

        # colocar um video de fundo
        st.video("https://www.youtube.com/watch?v=wDJN95Y_yOM")
        logging.info('Video de fundo')

        # Define a cor do texto
        st.markdown("""
            <style>
            body {
                color: #000000;
            }
            </style>
        """, unsafe_allow_html=True)

        # Define a cor de fundo
        st.markdown("""
            <style>
            body {
                background-color: #FFFFFF;
            }
            </style>
        """, unsafe_allow_html=True)


        st.markdown(
            """
            <style>
            .reportview-container {
                background: url("https://www.wallpaperflare.com/static/1019/100/1007/food-restaurant-restaurant-plate-wallpaper.jpg")
            }
            .sidebar .sidebar-content {
                background: url("https://www.wallpaperflare.com/static/1019/100/1007/food-restaurant-restaurant-plate-wallpaper.jpg")
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <style>
            .sidebar .sidebar-content {
                background: url("https://www.wallpaperflare.com/static/1019/100/1007/food-restaurant-restaurant-plate-wallpaper.jpg")
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        data= Data(URL).load()
        dataBebidas= Data(BEBIDAS).loadBebidas()
        dataEstoque= Data(ESTOQUE).loadEstoque()
        dataPratos= Data(PRATOS).loadPratos()
        dataClientes= Data(CLIENTES).loadClientes()
        dataFuncionarios= Data(FUNCIONARIOS).loadFuncionarios()
        dataReservas= Data(RESERVAS).loadReservas()
        dataVendasCategorias= Data(VENDASCATEGORIAS).loadVendasCategorias()


        #########################################################################################
        #                                Functions                                              #
        #########################################################################################

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
                  gerar_grafico_bolhas_bebidas()

          def inserir_estoque(id, nome, quantidade):
              with open('client/src/data/estoque_mercadorias.csv', 'a', newline='', encoding='utf-8') as file:
                  writer = csv.writer(file, delimiter=',')

                  if file.tell() == 0:
                      writer.writerow(['ID','NOME','QUANTIDADE'])

                  writer.writerow([id, nome, quantidade])

              st.success('Estoque atualizado com sucesso!')

              show_chart = st.radio('Deseja visualizar o gráfico de bolhas para o estoque?', ('Sim', 'Não'))
              if show_chart == 'Sim':
                  gerar_grafico_bolhas_estoque()

          def inserir_cliente(id, nome, gasto):
              with open('client/src/data/total_clientes.csv', 'a', newline='', encoding='utf-8') as file:
                  writer = csv.writer(file, delimiter=',')

                  if file.tell() == 0:
                      writer.writerow(['ID','NOME','GASTO'])

                  writer.writerow([id, nome, gasto])

              st.success('Cliente cadastrado com sucesso!')
              show_chart = st.radio('Deseja visualizar o gráfico de bolhas para o total de gastos dos clientes?', ('Sim', 'Não'))
              if show_chart == 'Sim':
                  gerar_grafico_bolhas_clientes()

          def inserir_prato(id, nome, preco, acompanhamento):
            with open('client/src/data/pratos.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=',')

                if file.tell() == 0:
                    writer.writerow(['ID', 'NOME', 'PRECO', 'ACOMPANHAMENTO'])

                writer.writerow([id, nome, preco, acompanhamento])

            st.success('Prato cadastrado com sucesso!')
            show_chart = st.radio('Deseja visualizar o gráfico de bolhas para os pratos?', ('Sim', 'Não'))
            if show_chart == 'Sim':
              gerar_grafico_bolhas_pratos()

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
              gerar_grafico_bolhas_vendas_categorias()

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
          
        if selecionar == "Dados Brutos":
          st.markdown("### DADOS BRUTOS")

          if st.checkbox("Clique aqui para ver os dados",False):
              st.markdown("###### ESTES SÃO OS DADOS BRUTOS PARA TODAS AS COMPARAÇÕES E GRÁFICO")
              st.write(data)

          if st.checkbox("Clique aqui para ver os dados de bebidas",False):
            st.markdown("###### ESTES SÃO OS DADOS BRUTOS PARA TODAS AS COMPARAÇÕES E GRÁFICO")
            display_bebidas()

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

          df = pd.read_csv('client/src/data/total_clientes.csv')

          st.markdown("### Comparação de Clientes")
          st.markdown("Neste gráfico, o tamanho da bolha representa o gasto total de cada cliente.")
          st.markdown("##### CLASSIFICAÇÃO DE DADOS DE CLIENTES ★★★★★")

          st.vega_lite_chart(df, {
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
          display_reservas()

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
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')

        # verifica se o usuário deseja redefinir a senha
        if st.button("Esqueci minha senha"):
          resetar_senha()
            

  else:
      criar_conta()

if __name__ == '__main__':
  main()

  # Encerrar a sessão do Spark
  spark.stop()
