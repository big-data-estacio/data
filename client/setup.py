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

from datetime import datetime
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
# import base64
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
from deta import Deta
import client.src.pages.criar_conta as conta
import client.src.pages.informacoes as info
# from src.pages.menu import selecionar
# client/src/pages/📚_Grafico_de_Vendas_por_Categoria.py

############################################################################################
#                                   Variáveis                                              #
############################################################################################

# exibe a imagem e permite que o usuário escolha entre fazer login ou criar uma nova conta
logo_img = Image.open('client/src/public/if-logo.png')
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
users_data = pd.read_csv("client/src/data/login.csv")
logoImg= Image.open('client/src/public/if-logo.png')
titlePlaceholder = st.empty()
MAX_ATTEMPTS = 3  # número máximo de tentativas
usernames = []
passwords = []
DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
db = deta.Base("data")
# TODO - Conecte-se às bases de dados
db_deta_bebidas = deta.Base("bebidas")
db_deta_estoque = deta.Base("estoque")
db_deta_pratos = deta.Base("prato")
db_deta_clientes = deta.Base("cliente")
db_deta_categoriavendas = deta.Base("categoriavendas")
db_deta_reservas = deta.Base("reservasClientes")
db_deta_funcionarios = deta.Base("funcionario")
# Criação de um dataframe com o cardápio
cardapio = pd.DataFrame({
    'Pratos': ['Lasanha', 'Pizza', 'Sopa', 'Hambúrguer', 'Churrasco'],
    'Preços': ['R$ 25,00', 'R$ 30,00', 'R$ 20,00', 'R$ 22,00', 'R$ 35,00']
})

############################################################################################
#                                   Classes                                                #
############################################################################################

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

# TODO - Criar função para converter o banco de dados em um dataframe
def to_dataframe(db):
    items = db.fetch().items
    return pd.DataFrame(items)

# TODO - Criar dataframes para cada base de dados
dataDetaBebidas = to_dataframe(db_deta_bebidas)
dataDetaEstoque = to_dataframe(db_deta_estoque)
dataDetaPratos = to_dataframe(db_deta_pratos)
dataDetaClientes = to_dataframe(db_deta_clientes)
dataDetaCategoriaVendas = to_dataframe(db_deta_categoriavendas)
dataDetaReservas = to_dataframe(db_deta_reservas)
dataDetaFuncionarios = to_dataframe(db_deta_funcionarios)

def imagem():
    logoImg= Image.open('client/src/public/if-logo.png')
    return logoImg


def authenticate_user(username, password):
    """Verifica se o usuário e senha informados são válidos."""
    return (users_data["usernames"] == username).any() and (users_data["passwords"] == password).any()

st.image(logo_img, use_column_width=True)

# TODO - Criando a seção do Apache Spark
# Criar a sessão do Spark
# spark = SparkSession.builder.appName("App").getOrCreate()
# spark.sparkContext.setLogLevel("OFF")

def mainLogin():
  
  opcao = st.radio("Escolha uma opção:", ("Fazer login", "Criar nova conta"))

  if opcao == "Fazer login":
    logging.info('O cliente escolheu fazer login')
    if 'blocked_time' in st.session_state and st.session_state.blocked_time > time.time():
      st.warning(f"Sua conta foi bloqueada por excesso de tentativas. Tente novamente em {st.session_state.blocked_time - int(time.time())} segundos.")
    else:
      original_title = '<p style="font-family:Monospace; color:Gray; font-size: 25px;"></p>'
      titlePlaceholder.markdown(original_title, unsafe_allow_html=True)
      if authenticate_user:
          titlePlaceholder.empty()
          imagem()
          st.markdown("# Bem-vindo!")
          df = px.data.iris()

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

          logging.info('Iniciando o app')

          load_dotenv()
          
          st.sidebar.image(logoImg , width=215)
          logging.basicConfig(
            filename='client/src/log/app.log',
            level=logging.INFO,
            format='%(asctime)s %(levelname)s %(name)s %(filename)s:%(lineno)d %(funcName)s() [%(process)d] - %(message)s'
          )
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
                      "Previsão de clientes"
                    ]
                  )

          data= Data().load()
          dataBebidas= Data().loadBebidas()
          dataEstoque= Data().loadEstoque()
          dataPratos= Data().loadPratos()
          dataClientes= Data().loadClientes()

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
            
            with st.container():
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

            # Cria o objeto ExibidorInformacoesRestaurante
            exibidor = info.ExibidorInformacoesRestaurante(horarios)

            # Chama o método exibir_informacoes() para exibir as informações na tela
            exibidor.exibir_informacoes()

          if selecionar == "Inserir Dados":
            logging.info('O cliente selecionou a opção de inserir dados')

            # TODO - Inserir dados no banco bebidas
            def inserir_bebida(id, nome, preco, quantidade, descricao, total_vendas, quantidade_vendas):
              # Get database
              db_bebidas = deta.Base("bebidas")

              # Put new drink into the database
              db_bebidas.put({
                  "key": id,
                  "nome": nome,
                  "preco": preco,
                  "quantidade": quantidade,
                  "descricao": descricao,
                  "total_vendas": total_vendas,
                  "quantidade_vendas": quantidade_vendas
              })

              st.success('Bebida inserida com sucesso!')

              # Get the "bebidas" database
              db_bebidas = deta.Base("bebidas")

              # Ask the user if they want to see the bubble chart
              show_chart = st.radio('Deseja visualizar o gráfico de bolhas para as bebidas?', ('Sim', 'Não'))

              if show_chart == 'Sim':
                  st.markdown("##### CLASSIFICAÇÃO DE BEBIDAS ★★★★★")

                  # Fetch data from the "bebidas" database and convert it to a DataFrame
                  fetch_response = db_bebidas.fetch()
                  data = [item for item in fetch_response.items]
                  df_bebidas = pd.DataFrame(data)

                  # Create a bubble chart with price on the x-axis, quantity sold on the y-axis, and bubble size representing total sales
                  chart = alt.Chart(df_bebidas).mark_circle().encode(
                      x=alt.X('preco', title='Preço'),
                      y=alt.Y('quantidade_vendas', title='Quantidade Vendida'),
                      size=alt.Size('total_vendas', title='Total de Vendas'),
                      color=alt.Color('nome', title='Bebida'),
                      tooltip=['nome', 'preco', 'quantidade_vendas', 'total_vendas']
                  ).properties(width=700, height=500)

                  # Display the chart
                  st.altair_chart(chart)

            # TODO - Inserir dados no banco estoque
            def inserir_estoque(id, nome, quantidade):
                # Insert data into the "estoque" database
                db_deta_estoque.put({
                    "ID": id,
                    "NOME": nome,
                    "QUANTIDADE": quantidade
                })

                st.success('Estoque atualizado com sucesso!')

                show_chart = st.radio('Deseja visualizar o gráfico de bolhas para o estoque?', ('Sim', 'Não'))

                if show_chart == 'Sim':
                    st.markdown("### A COMPARAÇÃO DO ESTOQUE DE MERCADORIAS")
                    st.markdown("Esta é a comparação do estoque de mercadorias por ID e quantidade. Aqui no eixo X, temos o ID e no eixo Y, a quantidade em estoque.")
                    st.markdown("##### ESTOQUE DE MERCADORIAS ★★★★★")

                    # Fetch data from the "estoque" database and convert it to a DataFrame
                    fetch_response = db_deta_estoque.fetch()
                    data = [item for item in fetch_response.items]
                    df_mercadorias = pd.DataFrame(data)

                    # Create a bar chart with ID on the x-axis and quantity on the y-axis
                    chart = alt.Chart(df_mercadorias).mark_bar().encode(
                        x=alt.X('ID', title='ID'),
                        y=alt.Y('QUANTIDADE', title='Quantidade em Estoque'),
                        tooltip=['NOME', 'QUANTIDADE']
                    ).properties(width=700, height=500)

                    # Display the chart
                    st.altair_chart(chart)

            # TODO - Inserir dados no banco cliente
            def inserir_cliente(id, nome, gasto):
                # Insert data into the "cliente" database
                db_deta_clientes.put({
                    "ID": id,
                    "NOME": nome,
                    "GASTO": gasto
                })

                st.success('Cliente cadastrado com sucesso!')
                
                show_chart = st.radio('Deseja visualizar o gráfico de bolhas para o total de gastos dos clientes?', ('Sim', 'Não'))

                if show_chart == 'Sim':
                    st.markdown("### Comparação de Clientes")
                    st.markdown("Neste gráfico, o tamanho da bolha representa o gasto total de cada cliente.")
                    st.markdown("##### CLASSIFICAÇÃO DE DADOS DE CLIENTES ★★★★★")

                    # Fetch data from the "cliente" database and convert it to a DataFrame
                    fetch_response = db_deta_clientes.fetch()
                    data = [item for item in fetch_response.items]
                    df_clientes = pd.DataFrame(data)

                    # Create a bubble chart with client name on x-axis and total spending on y-axis and bubble size
                    chart = alt.Chart(df_clientes).mark_circle().encode(
                        x=alt.X('NOME', title='Nome'),
                        y=alt.Y('GASTO', title='Gasto'),
                        size=alt.Size('GASTO', title='Gasto'),
                        color=alt.Color('GASTO', title='Gasto'),
                        tooltip=['NOME', 'GASTO']
                    ).properties(width=700, height=500)

                    # Display the chart
                    st.altair_chart(chart)

            # Get the "prato" database
            db_deta_pratos = deta.Base("prato")

            # TODO Inserir dados no banco prato
            def inserir_prato(id, nome, preco, acompanhamento):
                # Insert data into the "prato" database
                db_deta_pratos.put({
                    "ID": id,
                    "NOME": nome,
                    "PRECO": preco,
                    "ACOMPANHAMENTO": acompanhamento
                })

                st.success('Prato cadastrado com sucesso!')
                
                show_chart = st.radio('Deseja visualizar o gráfico de bolhas para os pratos?', ('Sim', 'Não'))

                if show_chart == 'Sim':
                    st.markdown("### Comparação de Pratos")
                    st.markdown("Neste gráfico, cada bolha representa um prato e o tamanho da bolha representa a quantidade em estoque.")
                    st.markdown("##### CLASSIFICAÇÃO DE DADOS DE PRATOS ★★★★★")

                    # Fetch data from the "prato" database and convert it to a DataFrame
                    fetch_response = db_deta_pratos.fetch()
                    data = [item for item in fetch_response.items]
                    df_pratos = pd.DataFrame(data)

                    # Create a bubble chart with dish name on x-axis, price on y-axis, and color representing the accompaniment
                    chart = alt.Chart(df_pratos).mark_circle(size=100).encode(
                        x='NOME',
                        y='PRECO',
                        color='ACOMPANHAMENTO',
                        tooltip=['NOME', 'PRECO', 'ACOMPANHAMENTO']
                    ).properties(
                        width=600,
                        height=400
                    )

                    # Display the chart
                    st.altair_chart(chart, use_container_width=True)

            # TODO Inserir dados no banco venda
            def inserir_venda(id, categoria, vendas, preco_medio):
                # Insert data into the "venda" database
                db_deta_categoriavendas.put({
                    "ID": id,
                    "Categoria": categoria,
                    "Vendas": vendas,
                    "PrecoMedio": preco_medio
                })

                st.success('Venda cadastrada com sucesso!')
                
                show_chart = st.radio('Deseja visualizar o gráfico de bolhas para as vendas?', ('Sim', 'Não'))

                if show_chart == 'Sim':
                    st.markdown("### Comparação de Categoria de Vendas")
                    st.markdown("Neste gráfico, cada bolha representa uma categoria de vendas e o tamanho da bolha representa o Preço Médio.")
                    st.markdown("##### CLASSIFICAÇÃO DE DADOS DE VENDAS ★★★★★")

                    # Fetch data from the "venda" database and convert it to a DataFrame
                    fetch_response = db_deta_categoriavendas.fetch()
                    data = [item for item in fetch_response.items]
                    df_vendas = pd.DataFrame(data)

                    # Create a bubble chart with category on x-axis, sales on y-axis, and color representing the average price
                    chart = alt.Chart(df_vendas).mark_circle(size=100).encode(
                        x='Categoria',
                        y='Vendas',
                        color='PrecoMedio',
                        tooltip=['Categoria', 'Vendas', 'PrecoMedio']
                    ).properties(
                        width=600,
                        height=400
                    )

                    # Display the chart
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

            # id,Categoria,Vendas,PrecoMedio
            elif arquivo00 == 'Categoria de Vendas':
                logging.info('O cliente selecionou a opção de inserir vendas')
                st.subheader('Inserir Venda')
                id = st.text_input('ID')
                categoria = st.text_input('Categoria')
                vendas = st.text_input('Vendas')
                preco_medio = st.text_input('PrecoMedio')

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

            # TODO - Implementar a atualização de dados do banco bebidas
            if arquivo01 == 'Bebidas':
              class Bebidas:
                def __init__(self, db_bebidas):
                    self.db_bebidas = db_bebidas
                    self.load_data()
                
                def load_data(self):
                    fetch_response = self.db_bebidas.fetch()
                    self.data = pd.DataFrame([item for item in fetch_response.items])
                
                def show_table(self):
                    st.write(self.data)
                
                def update_by_id(self, id):
                    item_key = str(id)
                    update_data = {}
                    for col in self.data.columns:
                        if col != 'key':
                            new_val = st.text_input(f"Novo valor para {col.capitalize()} (deixe em branco para não alterar):", value="")
                            if new_val != "":
                                update_data[col] = new_val
                    return update_data

              bebidas = Bebidas(db_deta_bebidas)

              # Display data in a table
              bebidas.show_table()

              # Allow the user to choose the id to update
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(bebidas.data))

              update_data = None
              # Update record by the selected ID
              if st.button("Atualizar"):
                  update_data = bebidas.update_by_id(id_to_update)

              if update_data and st.button("Confirmar"):
                  bebidas.db_deta_bebidas.put(update_data)
                  st.success("Dados atualizados com sucesso!")
                  bebidas.load_data()

            # TODO - Implementar a atualização de dados do banco estoque
            elif arquivo01 == 'Estoque':
              class Estoque:
                def __init__(self, db_estoque):
                    self.db_estoque = db_estoque
                    self.load_data()
                
                def load_data(self):
                    fetch_response = self.db_estoque.fetch()
                    self.data = pd.DataFrame([item for item in fetch_response.items])
                
                def show_table(self):
                    st.write(self.data)
                
                def update_by_id(self, id):
                    item_key = str(id)
                    update_data = {}
                    for col in self.data.columns:
                        if col != 'key':
                            new_val = st.text_input(f"Novo valor para {col.capitalize()} (deixe em branco para não alterar):", value="")
                            if new_val != "":
                                update_data[col] = new_val
                    return update_data

              # Get the "estoque" database
              estoque = Estoque(db_deta_estoque)

              # Display data in a table
              estoque.show_table()

              # Allow the user to choose the id to update
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(estoque.data))

              update_data = None
              # Update record by the selected ID
              if st.button("Atualizar"):
                  update_data = estoque.update_by_id(id_to_update)

              if update_data and st.button("Confirmar"):
                  estoque.db_deta_estoque.put(update_data)
                  st.success("Dados atualizados com sucesso!")
                  estoque.load_data()

            # TODO - Implementar a atualização de dados do banco cliente
            elif arquivo01 == 'Clientes':
              class Clientes:
                def __init__(self, db_clientes):
                    self.db_clientes = db_clientes
                    self.load_data()
                
                def load_data(self):
                    fetch_response = self.db_clientes.fetch()
                    self.data = pd.DataFrame([item for item in fetch_response.items])
                
                def show_table(self):
                    st.write(self.data)
                
                def update_by_id(self, id):
                    item_key = str(id)
                    update_data = {}
                    for col in self.data.columns:
                        if col != 'key':
                            new_val = st.text_input(f"Novo valor para {col.capitalize()} (deixe em branco para não alterar):", value="")
                            if new_val != "":
                                update_data[col] = new_val
                    return update_data

              clientes = Clientes(db_deta_clientes)

              # Display data in a table
              clientes.show_table()

              # Allow the user to choose the id to update
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(clientes.data))

              update_data = None
              # Update record by the selected ID
              if st.button("Atualizar"):
                  update_data = clientes.update_by_id(id_to_update)

              if update_data and st.button("Confirmar"):
                  clientes.db_deta_clientes.put(update_data)
                  st.success("Dados atualizados com sucesso!")
                  clientes.load_data()

            # TODO - Implementar a atualização de dados do banco prato
            elif arquivo01 == 'Pratos':
              class Pratos:
                def __init__(self, db_pratos):
                    self.db_pratos = db_pratos
                    self.load_data()
                
                def load_data(self):
                    fetch_response = self.db_pratos.fetch()
                    self.data = pd.DataFrame([item for item in fetch_response.items])
                
                def show_table(self):
                    st.write(self.data)
                
                def update_by_id(self, id):
                    item_key = str(id)
                    update_data = {}
                    for col in self.data.columns:
                        if col != 'key':
                            new_val = st.text_input(f"Novo valor para {col.capitalize()} (deixe em branco para não alterar):", value="")
                            if new_val != "":
                                update_data[col] = new_val
                    return update_data

              pratos = Pratos(db_deta_pratos)

              # Display data in a table
              pratos.show_table()

              # Allow the user to choose the id to update
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(pratos.data))

              update_data = None
              # Update record by the selected ID
              if st.button("Atualizar"):
                  update_data = pratos.update_by_id(id_to_update)

              if update_data and st.button("Confirmar"):
                  pratos.db_deta_pratos.put(update_data)
                  st.success("Dados atualizados com sucesso!")
                  pratos.load_data()

            # TODO - Implementar a atualização de dados do banco funcionario
            elif arquivo01 == 'Funcionarios':
              class Funcionarios:
                def __init__(self, db_funcionarios):
                    self.db_funcionarios = db_funcionarios
                    self.load_data()
                
                def load_data(self):
                    fetch_response = self.db_funcionarios.fetch()
                    self.data = pd.DataFrame([item for item in fetch_response.items])
                
                def show_table(self):
                    st.write(self.data)
                
                def update_by_id(self, id):
                    item_key = str(id)
                    update_data = {}
                    for col in self.data.columns:
                        if col != 'key':
                            new_val = st.text_input(f"Novo valor para {col.capitalize()} (deixe em branco para não alterar):", value="")
                            if new_val != "":
                                update_data[col] = new_val
                    return update_data

              funcionarios = Funcionarios(db_deta_funcionarios)

              # Display data in a table
              funcionarios.show_table()

              # Allow the user to choose the id to update
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(funcionarios.data))

              update_data = None
              # Update record by the selected ID
              if st.button("Atualizar"):
                  update_data = funcionarios.update_by_id(id_to_update)

              if update_data and st.button("Confirmar"):
                  funcionarios.db_deta_funcionarios.put(update_data)
                  st.success("Dados atualizados com sucesso!")
                  funcionarios.load_data()

            # TODO - Implementar a atualização de dados do banco vendacategoria
            elif arquivo01 == 'Categoria de Vendas':
              class CategoriaVendas:
                def __init__(self, db_categoriavendas):
                    self.db_categoriavendas = db_categoriavendas
                    self.load_data()
                
                def load_data(self):
                    fetch_response = self.db_categoriavendas.fetch()
                    self.data = pd.DataFrame([item for item in fetch_response.items])
                
                def show_table(self):
                    st.write(self.data)
                
                def update_by_id(self, id):
                    item_key = str(id)
                    update_data = {}
                    for col in self.data.columns:
                        if col != 'key':
                            new_val = st.text_input(f"Novo valor para {col.capitalize()} (deixe em branco para não alterar):", value="")
                            if new_val != "":
                                update_data[col] = new_val
                    return update_data

              categoriavendas = CategoriaVendas(db_deta_categoriavendas)

              # Display data in a table
              categoriavendas.show_table()

              # Allow the user to choose the id to update
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(categoriavendas.data))

              update_data = None
              # Update record by the selected ID
              if st.button("Atualizar"):
                  update_data = categoriavendas.update_by_id(id_to_update)

              if update_data and st.button("Confirmar"):
                  categoriavendas.db_deta_categoriavendas.put(update_data)
                  st.success("Dados atualizados com sucesso!")
                  categoriavendas.load_data()

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

            # TODO - Implementar a deleção de dados do banco estoque
            if arquivo02 == 'Estoque':
              def gerenciar_estoque():
                # Conectar ao banco de dados
                db_deta_estoque = deta.Base('estoque')

                def show_table():
                    # Fetch data from the "estoque" database and convert it to a DataFrame
                    fetch_response = db_deta_estoque.fetch()
                    data = [item for item in fetch_response.items]
                    df_estoque = pd.DataFrame(data)

                    # Display the DataFrame
                    st.write(df_estoque)

                def delete_by_id(id):
                    db_deta_estoque.delete(str(id))  # Convert the ID to string here
                    st.success("Dados deletados com sucesso!")

                # Display data in a table
                show_table()

                # Allow the user to choose the id to delete
                id_to_delete = st.number_input("Digite o ID do registro que deseja deletar:", min_value=1)

                if st.button("Deletar"):
                    delete_by_id(id_to_delete)

                if st.button("Deseja ver os dados atualizados?"):
                    show_table()

              # Call the function
              gerenciar_estoque()

            # TODO - Implementar a deleção de dados do banco bebidas
            elif arquivo02 == 'Bebidas':
                def gerenciar_bebidas():
                  # Conectar ao banco de dados
                  db_deta_bebidas = deta.Base('bebidas')

                  def show_table():
                      # Fetch data from the "bebidas" database and convert it to a DataFrame
                      fetch_response = db_deta_bebidas.fetch()
                      data = [item for item in fetch_response.items]
                      df_bebidas = pd.DataFrame(data)

                      # Display the DataFrame
                      st.write(df_bebidas)

                  def delete_by_id(id):
                      db_deta_bebidas.delete(str(id))  # Convert the ID to string here
                      st.success("Dados deletados com sucesso!")

                  # Display data in a table
                  show_table()

                  # Allow the user to choose the id to delete
                  id_to_delete = st.number_input("Digite o ID do registro que deseja deletar:", min_value=1)

                  if st.button("Deletar"):
                      delete_by_id(id_to_delete)

                  if st.button("Deseja ver os dados atualizados?"):
                      show_table()

                # Call the function
                gerenciar_bebidas()

            # TODO - Implementar a deleção de dados do banco prato
            elif arquivo02 == 'Pratos':
                def gerenciar_pratos():
                  # Conectar ao banco de dados
                  db_deta_pratos = deta.Base('prato')

                  def show_table():
                      # Fetch data from the "pratos" database and convert it to a DataFrame
                      fetch_response = db_deta_pratos.fetch()
                      data = [item for item in fetch_response.items]
                      df_pratos = pd.DataFrame(data)

                      # Display the DataFrame
                      st.write(df_pratos)

                  def delete_by_id(id):
                      db_deta_pratos.delete(str(id))  # Convert the ID to string here
                      st.success("Dados deletados com sucesso!")

                  # Display data in a table
                  show_table()

                  # Allow the user to choose the id to delete
                  id_to_delete = st.number_input("Digite o ID do registro que deseja deletar:", min_value=1)

                  if st.button("Deletar"):
                      delete_by_id(id_to_delete)

                  if st.button("Deseja ver os dados atualizados?"):
                      show_table()

                # Call the function
                gerenciar_pratos()

            # TODO - Implementar a deleção de dados do banco clientes
            elif arquivo02 == 'Clientes':
              def gerenciar_clientes():
                # Conectar ao banco de dados
                db_deta_clientes = deta.Base('clientes')

                def show_table():
                    # Fetch data from the "clientes" database and convert it to a DataFrame
                    fetch_response = db_deta_clientes.fetch()
                    data = [item for item in fetch_response.items]
                    df_clientes = pd.DataFrame(data)

                    # Display the DataFrame
                    st.write(df_clientes)

                def delete_by_id(id):
                    db_deta_clientes.delete(str(id))  # Convert the ID to string here
                    st.success("Dados deletados com sucesso!")

                # Display data in a table
                show_table()

                # Allow the user to choose the id to delete
                id_to_delete = st.number_input("Digite o ID do registro que deseja deletar:", min_value=1)

                if st.button("Deletar"):
                    delete_by_id(id_to_delete)

                if st.button("Deseja ver os dados atualizados?"):
                    show_table()

              # Call the function
              gerenciar_clientes()
        
            # TODO - Implementar a deleção de dados do banco funcionario
            elif arquivo02 == 'Funcionarios':
              def gerenciar_funcionarios():
                # Conectar ao banco de dados
                db_deta_funcionarios = deta.Base('funcionario')

                def show_table():
                    # Fetch data from the "funcionarios" database and convert it to a DataFrame
                    fetch_response = db_deta_funcionarios.fetch()
                    data = [item for item in fetch_response.items]
                    df_funcionarios = pd.DataFrame(data)

                    # Display the DataFrame
                    st.write(df_funcionarios)

                def delete_by_id(id):
                    db_deta_funcionarios.delete(str(id))  # Convert the ID to string here
                    st.success("Dados deletados com sucesso!")

                # Display data in a table
                show_table()

                # Allow the user to choose the id to delete
                id_to_delete = st.number_input("Digite o ID do registro que deseja deletar:", min_value=1)

                if st.button("Deletar"):
                    delete_by_id(id_to_delete)

                if st.button("Deseja ver os dados atualizados?"):
                    show_table()

              # Call the function
              gerenciar_funcionarios()

            # TODO - Implementar a deleção de dados do banco vendasCategorias
            elif arquivo02 == 'Categoria de Vendas':
              def gerenciar_vendas():
                # Conectar ao banco de dados
                db_deta_categoriavendas = deta.Base('vendasCategorias')

                def show_table():
                    # Fetch data from the "vendasCategorias" database and convert it to a DataFrame
                    fetch_response = db_deta_categoriavendas.fetch()
                    data = [item for item in fetch_response.items]
                    df_vendas = pd.DataFrame(data)

                    # Display the DataFrame
                    st.write(df_vendas)

                def delete_by_id(id):
                    db_deta_categoriavendas.delete(str(id))  # Convert the ID to string here
                    st.success("Dados deletados com sucesso!")

                # Display data in a table
                show_table()

                # Allow the user to choose the id to delete
                id_to_delete = st.number_input("Digite o ID do registro que deseja deletar:", min_value=1)

                if st.button("Deletar"):
                    delete_by_id(id_to_delete)

                if st.button("Deseja ver os dados atualizados?"):
                    show_table()

              # Call the function
              gerenciar_vendas()

# ------------------------------------------------------------------------------------------------------------------------------------------------------

          # TODO - Implementar a deleção de dados do banco
          if selecionar == "Análise de rentabilidade":
            from typing import List, Dict

            class AtualizadorDeItem:
              def __init__(self, rentabilidade):
                  self.rentabilidade = rentabilidade

              def atualizar(self, id_item):
                item_atualizado = exibe_formulario_atualiza_item_valores(self.rentabilidade, id_item)


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

                def load_data(self):
                    self.data = pd.read_csv(self.csv_file)

                def exibe_formulario_deleta_item(self):
                  id_item = st.text_input("Digite o ID do item que deseja deletar")
                  
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

                    import pandas as pd
                    import plotly.express as px

                    def plot_graphs(file_name):
                        # Ler arquivo CSV
                        data = pd.read_csv(file_name)
                        
                        # Calcular a rentabilidade (Preço de Venda - Custo de Produção) * Quantidade Vendida
                        data['Rentabilidade'] = (data['Preço de Venda'] - data['Custo de Produção']) * data['Quantidade Vendida']
                        
                        # Gráfico de barras da rentabilidade por item
                        fig = px.bar(data, x='Item', y='Rentabilidade', title="Rentabilidade por Item")
                        fig.show()
                        
                        # Gráfico de dispersão do preço de venda vs custo de produção
                        fig2 = px.scatter(data, x='Preço de Venda', y='Custo de Produção', color='Item', title="Preço de Venda vs Custo de Produção")
                        fig2.show()
                        
                    # Chamar a função com o nome do arquivo
                    plot_graphs("client/src/data/rentabilidade.csv")

                
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

              # Adicionando gráficos Plotly
              # Gráfico de linhas do valor de vendas ao longo do tempo
              fig = px.line(df_vendas, x='DataVenda', y='Valor', title='Vendas ao Longo do Tempo')
              st.plotly_chart(fig)

              # Histograma da distribuição do valor de vendas
              fig2 = px.histogram(df_vendas, x='Valor', nbins=50, title='Distribuição do Valor de Vendas')
              st.plotly_chart(fig2)

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
                st.write(dataDetaBebidas)

            if st.checkbox("Clique aqui para ver os dados de estoque",False):
                st.markdown("###### ESTES SÃO OS DADOS BRUTOS PARA TODAS AS COMPARAÇÕES E GRÁFICO")
                st.write(dataDetaEstoque)

            if st.checkbox("Clique aqui para ver os dados de pratos",False):
                st.markdown("###### ESTES SÃO OS DADOS BRUTOS PARA TODAS AS COMPARAÇÕES E GRÁFICO")
                st.write(dataDetaPratos)

            if st.checkbox("Clique aqui para ver os dados de clientes",False):
                st.markdown("###### ESTES SÃO OS DADOS BRUTOS PARA TODAS AS COMPARAÇÕES E GRÁFICO")
                st.write(dataDetaClientes)

            st.markdown("### A COMPARAÇÃO DA BOLHA")
            st.markdown("Esta é a classificação das bebidas em termos de faixa de preço. Aqui no eixo Y, o tamanho da bolha descreve a classificação que se espalhou pelo pool da faixa de preço.")
            st.markdown("##### CLASSIFICAÇÃO DE BEBIDAS ★★★★★")

            # Criar um gráfico de bolhas com preço no eixo x, quantidade vendida no eixo y e tamanho das bolhas representando o total de vendas
            chart = alt.Chart(dataDetaBebidas).mark_circle().encode(
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

            # Criar um gráfico de barras com ID no eixo x e quantidade no eixo y
            chart = alt.Chart(dataDetaEstoque).mark_bar().encode(
                x=alt.X('ID', title='ID'),
                y=alt.Y('QUANTIDADE', title='Quantidade em Estoque'),
                tooltip=['NOME', 'QUANTIDADE']
            ).properties(width=700, height=500)

            # Exibir o gráfico
            st.altair_chart(chart)

            st.markdown("### Comparação de Pratos")
            st.markdown("Neste gráfico, cada bolha representa um prato e o tamanho da bolha representa a quantidade em estoque.")
            st.markdown("##### CLASSIFICAÇÃO DE DADOS DE PRATOS ★★★★★")

            # Criando o gráfico de bolhas com Altair
            chart = alt.Chart(dataDetaPratos).mark_circle(size=100).encode(
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


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------


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
            dataFunc = pd.DataFrame(columns=['NOME' , 'Cargo', 'ESPECIALIDADE', 'SALÁRIODIA', 'DIASTRABALHADOS'])
            

            # Adicionar funcionário
            st.write("Preencha os dados do funcionário abaixo:")
            nome = st.text_input("NOME")
            cargo = st.selectbox("Cargo", ["Gerente", "Garçom", "Cozinheiro", "Auxiliar de cozinha"])
            ESPECIALIDADE = st.text_input("ESPECIALIDADE")
            salario_dia = st.number_input("SALÁRIODIA", value=0.0, step=0.01)
            dias_trabalhados = st.number_input("DIASTRABALHADOS", value=0, step=1)

            # Botão para adicionar funcionário
            if st.button("Adicionar funcionário"):
                # Verifica se o funcionário já foi cadastrado anteriormente
                if nome in dataFunc["NOME"].tolist():
                    st.warning("Funcionário já cadastrado")
                else:
                    # Adiciona o funcionário ao dataframe
                    dataFunc = dataFunc.append({
                        "NOME": nome,
                        "Cargo": cargo,
                        "ESPECIALIDADE": ESPECIALIDADE,
                        "SALÁRIODIA": salario_dia,
                        "DIASTRABALHADOS": dias_trabalhados
                    }, ignore_index=True)
                    st.success("Funcionário cadastrado com sucesso!")

                    # Adicionar os dados ao banco de dados Deta
                    db_deta_funcionarios.put({
                        "NOME": nome,
                        "Cargo": cargo,
                        "ESPECIALIDADE": ESPECIALIDADE,
                        "SALÁRIODIA": salario_dia,
                        "DIASTRABALHADOS": dias_trabalhados
                    })

            st.write("Lista de funcionários:")
            st.dataframe(dataFunc)

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


          if selecionar == "Análise de desempenho dos funcionários":
              def employee_performance_analysis():
                # Criação do dataframe
                if not os.path.isfile("client/src/data/funcionarios.csv"):
                    dataFunc = pd.DataFrame(columns=["ID", "NOME", "Cargo", "ESPECIALIDADE", "Salário", "Dias trabalhados", "Salário dia"])
                else:
                    dataFunc = pd.read_csv("client/src/data/funcionarios.csv")

                st.subheader("Cadastro de Funcionários")

                # Adicionar funcionário
                st.write("Preencha os dados do funcionário abaixo:")
                nome = st.text_input("NOME")
                cargo = st.selectbox("Cargo", ["Gerente", "Garçom", "Cozinheiro", "Auxiliar de cozinha"])
                ESPECIALIDADE = st.text_input("ESPECIALIDADE")
                salario = st.number_input("Salário", value=0.0, step=0.01)
                dias_trabalhados = st.number_input("Dias trabalhados", value=0, step=1)
                salario_dia = salario / dias_trabalhados if dias_trabalhados != 0 else 0

                # Botão para adicionar funcionário
                if st.button("Adicionar funcionário"):
                    # Verifica se o funcionário já foi cadastrado anteriormente
                    if nome in dataFunc["NOME"].tolist():
                        st.warning("Funcionário já cadastrado")
                    else:
                        # Adiciona o funcionário ao dataframe
                        id = 1 if dataFunc.empty else dataFunc.iloc[-1]['ID'] + 1
                        dataFunc = dataFunc.append({
                            "ID": id,
                            "NOME": nome,
                            "Cargo": cargo,
                            "ESPECIALIDADE": ESPECIALIDADE,
                            "Salário": salario,
                            "Dias trabalhados": dias_trabalhados,
                            "Salário dia": salario_dia
                        }, ignore_index=True)
                        st.success("Funcionário cadastrado com sucesso!")
                        # st.empty()

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
                # y=selected_func_data["DIASTRABALHADOS"],
                marker_color='green'))
                fig.update_layout(title=f"Desempenho de {selected_func}",
                xaxis_title="ESPECIALIDADE",
                yaxis_title="DIASTRABALHADOS")
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
                  <input type="email" name="email" placeholder="Your email" required>
                  <textarea name="message" placeholder="Your message here"></textarea>
                  <button type="submit">Send</button>
              </form>
              """.format("estevamsouzalaureth@gmail.com")  # Substitua o endereço de e-mail aqui

              st.markdown(contact_form, unsafe_allow_html=True)


              # Use Local CSS File
              def local_css(file_name):
                  path = os.path.dirname(__file__)
                  file_name = path+"/"+file_name
                  with open(file_name) as f:
                      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

              local_css("src/styles/email_style.css")

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

            # TODO - Criar um selectbox para selecionar o tipo de dado que o usuário quer ver no banco bebidas
            select=st.selectbox('Selecione as opções para ver detalhes sobre suas bebidas', ['nome' , 'preco', 'quantidade', 'descricao', 'total_vendas', 'quantidade_vendas'])
            if select == 'nome':
                st.write(dataDetaBebidas.query("nome >= nome")[["key","nome"]])
            elif select == 'preco':
                st.write(dataDetaBebidas.query("preco >= preco")[["key","preco"]])
            elif select == 'quantidade':
                st.write(dataDetaBebidas.query("quantidade >= quantidade")[["key","quantidade"]])
            elif select == 'descricao':
                st.write(dataDetaBebidas.query("descricao >= descricao")[["key","descricao"]])
            elif select == 'total_vendas':
                st.write(dataDetaBebidas.query("total_vendas >= total_vendas")[["key","total_vendas"]])
            else:
                st.write(dataDetaBebidas.query("quantidade_vendas >= quantidade_vendas")[["key","quantidade_vendas"]])

            # TODO - Criar um selectbox para selecionar o tipo de dado que o usuário quer ver no banco estoque
            select = st.selectbox('Selecione as opções para ver detalhes sobre seus estoque', ['NOME' , 'QUANTIDADE'])
            if select == 'NOME':
                st.write(dataDetaEstoque.query("NOME >= NOME")[["key","NOME"]])
            else:
                st.write(dataDetaEstoque.query("QUANTIDADE >= QUANTIDADE")[["key","QUANTIDADE"]])

            # TODO - Criar um selectbox para selecionar o tipo de dado que o usuário quer ver no banco pratos
            select = st.selectbox('Selecione as opções para ver detalhes sobre seus funcionários', ['NOME' , 'Cargo', 'ESPECIALIDADE', 'SALÁRIODIA', 'DIASTRABALHADOS'])
            if select == 'NOME':
                st.write(dataDetaFuncionarios.query("NOME >= NOME")[["key","NOME"]])
            elif select == 'Cargo':
                st.write(dataDetaFuncionarios.query("Cargo >= Cargo")[["key","Cargo"]])
            elif select == 'ESPECIALIDADE':
                st.write(dataDetaFuncionarios.query("ESPECIALIDADE >= ESPECIALIDADE")[["key","ESPECIALIDADE"]])
            elif select == 'DIASTRABALHADOS':
                st.write(dataDetaFuncionarios.query("DIASTRABALHADOS >= DIASTRABALHADOS")[["key","DIASTRABALHADOS"]])
            else :
                st.write(dataDetaFuncionarios.query("SALÁRIODIA >= SALÁRIODIA")[["key","SALÁRIODIA"]])

            # TODO - Criar um selectbox para selecionar o tipo de dado que o usuário quer ver no banco pratos
            select = st.selectbox('Selecione as opções para ver detalhes sobre seus pratos', ['NOME' , 'PRECO', 'ACOMPANHAMENTO'])
            if select == 'NOME':
                st.write(dataDetaPratos.query("NOME >= NOME")[["key","NOME"]])
            elif select == 'PRECO':
                st.write(dataDetaPratos.query("PRECO >= PRECO")[["key","PRECO"]])
            else :
                st.write(dataDetaPratos.query("ACOMPANHAMENTO >= ACOMPANHAMENTO")[["key","ACOMPANHAMENTO"]])

            # TODO - Criar um selectbox para selecionar o tipo de dado que o usuário quer ver no banco reservas
            select = st.selectbox('Selecione as opções para ver detalhes sobre suas reservas', ['NOME' , 'DATA', 'QTDRESERVAS'])
            if select == 'NOME':
                st.write(dataDetaReservas.query("NOME >= NOME")[["key","NOME"]])
            elif select == 'DATA':
                st.write(dataDetaReservas.query("DATA >= DATA")[["key","DATA"]])
            elif select == 'QTDRESERVAS':
                st.write(dataDetaReservas.query("QTDRESERVAS >= QTDRESERVAS")[["key","QTDRESERVAS"]])

            # TODO - Criar um selectbox para selecionar o tipo de dado que o usuário quer ver no banco vendascategoria
            select = st.selectbox('Selecione as opções para ver detalhes sobre suas vendas por categoria', ['ID', 'Categoria' , 'Vendas', 'PrecoMedio'])
            if select == 'Categoria':
                st.write(dataDetaCategoriaVendas.query("Categoria >= Categoria")[["key","Categoria"]])
            elif select == 'Vendas':
                st.write(dataDetaCategoriaVendas.query("Vendas >= Vendas")[["key","Vendas"]])
            else :
                st.write(dataDetaCategoriaVendas.query("PrecoMedio >= PrecoMedio")[["key","PrecoMedio"]])

          if selecionar == "Cardápio":
            st.title("Cardápio")
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
            def vendas_por_categoria(dados):
              # Gráfico de bolhas
              fig = px.scatter(dados, x='Categoria', y='Vendas', size='PrecoMedio', hover_name='Categoria')
              st.plotly_chart(fig)

              # Salvar dados em arquivo
              dados.to_csv('client/src/data/vendasCategorias.csv', index=False)

              # Projeção de vendas
              st.subheader('Projeção de vendas para a próxima semana')

              # Calcular média de vendas e PrecoMedio
              media_vendas = dados['Vendas'].mean()
              media_preco = dados['PrecoMedio'].mean()

              # Calcular projeção de vendas
              projecao_vendas = media_vendas * 1.1

              # Calcular projeção de receita
              projecao_receita = projecao_vendas * media_preco

              # Exibir resultados
              st.write('Média de vendas da última semana:', media_vendas)
              st.write('Média de preço da última semana:', media_preco)
              st.write('Projeção de vendas para a próxima semana:', projecao_vendas)
              st.write('Projeção de receita para a próxima semana:', projecao_receita)

              # Gráfico de barras
              grafico = px.bar(dados, x='Categoria', y='Vendas', color='Categoria')
              st.plotly_chart(grafico)
            categorias = ['Comida', 'Bebida', 'Sobremesa']
            vendas = np.random.randint(100, 1000, size=3)
            preco_medio = np.random.uniform(5, 20, size=3)
            dados = pd.DataFrame({'Categoria': categorias, 'Vendas': vendas, 'PrecoMedio': preco_medio})

            vendas_por_categoria(dados)


          if selecionar == "Previsão de clientes":
            import base64
            import json

            from streamlit_lottie import st_lottie

            def get_img_as_base64(file):
                with open(file, "rb") as f:
                    data = f.read()
                return base64.b64encode(data).decode()

            def load_lottiefile(filepath: str):
                with open(filepath, "r") as f:
                    return json.load(f)

            img = get_img_as_base64("client/src/public/tree.png")
            snow_animation = load_lottiefile("client/src/public/lottie-snow.json")

            page_bg_img = f"""
                <style>
                    [data-testid="stSidebar"] > div:first-child {{
                        background-image: url("data:image/png;base64,{img}");
                    }}

                    [data-testid="stSidebarNav"] span {{
                        color:white;
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

            st_lottie(snow_animation, height=600, key="initial")

          if selecionar == "Previsão de Vendas":
            import base64
            import json

            from streamlit_lottie import st_lottie

            def get_img_as_base64(file):
                with open(file, "rb") as f:
                    data = f.read()
                return base64.b64encode(data).decode()

            def load_lottiefile(filepath: str):
                with open(filepath, "r") as f:
                    return json.load(f)

            img = get_img_as_base64("client/src/public/tree.png")
            snow_animation = load_lottiefile("client/src/public/lottie-snow.json")

            page_bg_img = f"""
                <style>
                    [data-testid="stSidebar"] > div:first-child {{
                        background-image: url("data:image/png;base64,{img}");
                    }}

                    [data-testid="stSidebarNav"] span {{
                        color:white;
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

            st_lottie(snow_animation, height=600, key="initial")

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
            st.header("Reservas")

            # Pergunta para o usuário os dados da reserva
            st.header("Faça sua Reserva")
            identificar = st.text_input("Coloque o id de identificação para a sua reserva:")
            nome = st.text_input("Nome Completo:")
            data_str = st.date_input("Data da Reserva:")
            reservas_por_data = st.number_input("Quantidade de reservas:", min_value=1, value=1)

            # Verifica se todos os campos foram preenchidos
            if nome and data_str and reservas_por_data:
                # Salva os dados da reserva
                if st.button("Reservar"):
                    data = datetime.combine(data_str, datetime.min.time())
                    nova_reserva = {"key": identificar, "NOME": nome, "DATA": data.isoformat(), "QTDRESERVAS": reservas_por_data}
                    db_deta_reservas.put(nova_reserva)
                    st.success("Reserva feita com sucesso!")

                # Obtém todas as reservas do banco de dados
                todas_reservas = []
                last_key = None

                while True:
                    fetch_response = db_deta_reservas.fetch(last=last_key)
                    todas_reservas.extend(fetch_response.items)
                    if fetch_response.last is None:
                        break
                    last_key = fetch_response.last

                reservas_df = pd.DataFrame(todas_reservas)

                # Converte a coluna 'DATA' para datetime
                reservas_df["DATA"] = pd.to_datetime(reservas_df["DATA"])

                # Agrupa as reservas por data e soma a quantidade de reservas para cada data
                reservas_agrupadas = reservas_df.groupby('DATA')['QTDRESERVAS'].sum().reset_index()

                # Plota um gráfico de linha com a data no eixo x e a quantidade de reservas no eixo y
                chart = alt.Chart(reservas_agrupadas).mark_line().encode(
                    x='DATA:T',
                    y='QTDRESERVAS:Q',
                    tooltip=['DATA:T', 'QTDRESERVAS:Q']
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

      elif authenticate_user == False:
          # st.error('Username/password is incorrect')
          pass
      elif authenticate_user == None:
          st.warning('Please enter your username and password')
      
      # Inicializa o tempo de uso
      session_start_time = st.session_state.get('session_start_time', time.time())

      # exibe o tempo de uso
      elapsed_time = time.time() - session_start_time
      st.write("Tempo de uso:", time.strftime('%H:%M:%S', time.gmtime(elapsed_time)))

  else:
      conta.criar_conta()