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

import os
import time
import json
import base64
import smtplib
import logging
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px

from PIL import Image
from deta import Deta
from dotenv import load_dotenv
from email.mime.text import MIMEText
from streamlit_lottie import st_lottie
from email.mime.multipart import MIMEMultipart

import client.src.pages.mapa as mapa
import client.src.pages.informacoes as info
import client.src.pages.criar_conta as conta
import client.src.pages.reservas as reservas
import client.src.pages.developers as developers
import client.src.pages.previsaoVendas as previsaoVendas
import client.src.pages.analisador_funcionario as analisar
import client.src.pages.categoria_venda as categoria_grafico
import client.src.pages.analise_lucro_liquido as analise_lucro_liquido
import client.src.pages.previsao_demanda_restaurante as previsaoDemanda

import client.src.pages.insert.insert_bebidas as insert
import client.src.pages.insert.insert_prato as insert_prato
import client.src.pages.insert.insert_venda as insert_venda
import client.src.pages.insert.insert_client as insert_client
import client.src.pages.insert.insert_estoque as insert_estoque
import client.src.pages.insert.cadastrar_funcionario as cadastrar_funcionario

import client.src.pages.update.pratos_update as pratos_update
import client.src.pages.update.estoque_update as estoque_update
import client.src.pages.update.bebidas_update as bebidas_clientes
import client.src.pages.update.clientes_update as clientes_update
import client.src.pages.update.funcionarios_update as funcionarios_update
import client.src.pages.update.categoria_vendas_update as categoria_vendas_update

import client.src.pages.delete.gerenciamento_pratos as gerenciamento_pratos
import client.src.pages.delete.gerenciamento_estoque as gerenciamento_estoque
import client.src.pages.delete.gerenciamento_bebidas as gerenciamento_bebidas
import client.src.pages.delete.gerenciamento_clientes as gerenciamento_clientes
import client.src.pages.delete.gerenciamento_funcionarios as gerenciamento_funcionarios
import client.src.pages.delete.gerenciamento_categoria_vendas as gerenciamento_categoria_vendas

############################################################################################
#                                   Variáveis                                              #
############################################################################################

# TODO - Criando a seção do Apache Spark
# Criar a sessão do Spark
# spark = SparkSession.builder.appName("App").getOrCreate()
# spark.sparkContext.setLogLevel("OFF")

logoImg= Image.open('client/src/public/if-logo.png')
users_data = pd.read_csv("client/src/data/login.csv")
titlePlaceholder = st.empty()
MAX_ATTEMPTS = 3  # número máximo de tentativas
usernames = []
passwords = []
DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
db = deta.Base("data")
# TODO - Conecte-se às bases de dados
db_deta_previsao_demanda = deta.Base("previsao_demanda")
db_deta_funcionarios = deta.Base("funcionario")
db_deta_categoriavendas = deta.Base("categoriavendas")
db_deta_bebidas = deta.Base("bebidas")
db_deta_estoque = deta.Base("estoque")
db_deta_pratos = deta.Base("prato")
db_deta_clientes = deta.Base("cliente")
db_deta_reservas = deta.Base("reservasClientes")
# Criação de um dataframe com o cardápio
cardapio = pd.DataFrame({
    'Pratos': ['Lasanha', 'Pizza', 'Sopa', 'Hambúrguer', 'Churrasco'],
    'Preços': ['R$ 25,00', 'R$ 30,00', 'R$ 20,00', 'R$ 22,00', 'R$ 35,00']
})

############################################################################################
#                                   Classes                                                #
############################################################################################

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

def authenticate_user(username, password):
    """Verifica se o usuário e senha informados são válidos."""
    return (users_data["usernames"] == username).any() and (users_data["passwords"] == password).any()

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
          st.markdown("# Bem-vindo!")
          df = px.data.iris()

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
                                                  "Reservas",
                                                "Previsão de demanda",
                                              "Análise de lucro líquido",
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
                    insert.inserir_bebida(id, nome, preco, quantidade, descricao, total_vendas, quantidade_vendas)
                    st.button('Voltar')

            elif arquivo00 == 'Estoque':
                logging.info('O cliente selecionou a opção de inserir estoque')
                st.subheader('Inserir Estoque')
                id = st.text_input('ID')
                nome = st.text_input('NOME')
                quantidade = st.text_input('QUANTIDADE')

                if st.button('Inserir'):
                  insert_estoque.inserir_estoque(id, nome, quantidade)
                  st.button('Voltar')

            elif arquivo00 == 'Clientes':
                logging.info('O cliente selecionou a opção de inserir clientes')
                st.subheader('Inserir Cliente')
                id = st.text_input('ID')
                nome = st.text_input('NOME')
                gasto = st.text_input('GASTO')

                if st.button('Inserir'):
                    insert_client.inserir_cliente(id, nome, gasto)
                    st.button('Voltar')

            elif arquivo00 == 'Pratos':
                logging.info('O cliente selecionou a opção de inserir pratos')
                st.subheader('Inserir Prato')
                id = st.text_input('ID')
                nome = st.text_input('NOME')
                preco = st.text_input('PRECO')
                acompanhamento = st.text_input('ACOMPANHAMENTO')

                if st.button('Inserir'):
                    insert_prato.inserir_prato(id, nome, preco, acompanhamento)
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
                    insert_venda.inserir_venda(id, categoria, vendas, preco_medio)
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

            if arquivo01 == 'Bebidas':
              bebidas = bebidas_clientes.Bebidas(db_deta_bebidas)
              bebidas.show_table()
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(bebidas.data))
              update_data = None
              if st.button("Atualizar"):
                  update_data = bebidas.update_by_id(id_to_update)
              if update_data and st.button("Confirmar"):
                  bebidas.db_deta_bebidas.put(update_data)
                  st.success("Dados atualizados com sucesso!")
                  bebidas.load_data()

            elif arquivo01 == 'Estoque':
              estoque = estoque_update.Estoque(db_deta_estoque)
              estoque.show_table()
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(estoque.data))
              update_data = None
              if st.button("Atualizar"):
                  update_data = estoque.update_by_id(id_to_update)
              if update_data and st.button("Confirmar"):
                  estoque.db_deta_estoque.put(update_data)
                  st.success("Dados atualizados com sucesso!")
                  estoque.load_data()

            elif arquivo01 == 'Clientes':
              clientes = clientes_update.Clientes(db_deta_clientes)
              clientes.show_table()
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(clientes.data))
              update_data = None
              if st.button("Atualizar"):
                  update_data = clientes.update_by_id(id_to_update)
              if update_data and st.button("Confirmar"):
                  clientes.db_deta_clientes.put(update_data)
                  st.success("Dados atualizados com sucesso!")
                  clientes.load_data()

            elif arquivo01 == 'Pratos':
              pratos = pratos_update.Pratos(db_deta_pratos)
              pratos.show_table()
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(pratos.data))
              update_data = None
              if st.button("Atualizar"):
                  update_data = pratos.update_by_id(id_to_update)
              if update_data and st.button("Confirmar"):
                  pratos.db_deta_pratos.put(update_data)
                  st.success("Dados atualizados com sucesso!")
                  pratos.load_data()

            elif arquivo01 == 'Funcionarios':
              funcionarios = funcionarios_update.Funcionarios(db_deta_funcionarios)
              funcionarios.show_table()
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(funcionarios.data))
              update_data = None
              if st.button("Atualizar"):
                  update_data = funcionarios.update_by_id(id_to_update)
              if update_data and st.button("Confirmar"):
                  funcionarios.db_deta_funcionarios.put(update_data)
                  st.success("Dados atualizados com sucesso!")
                  funcionarios.load_data()

            elif arquivo01 == 'Categoria de Vendas':
              categoriavendas = categoria_vendas_update.CategoriaVendas(db_deta_categoriavendas)
              categoriavendas.show_table()
              id_to_update = st.number_input("Digite o ID do registro que deseja atualizar:", min_value=1, max_value=len(categoriavendas.data))
              update_data = None
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

            if arquivo02 == 'Estoque':
              gerenciamento_estoque.gerenciar_estoque()

            elif arquivo02 == 'Bebidas':
              gerenciamento_bebidas.gerenciar_bebidas()

            elif arquivo02 == 'Pratos':
              gerenciamento_pratos.gerenciar_pratos()

            elif arquivo02 == 'Clientes':
              gerenciamento_clientes.gerenciar_clientes()
        
            elif arquivo02 == 'Funcionarios':
              gerenciamento_funcionarios.gerenciar_funcionarios()

            elif arquivo02 == 'Categoria de Vendas':
              gerenciamento_categoria_vendas.gerenciar_vendas()

          if selecionar == "Análise de lucro líquido":
            analise_lucro_liquido.calculate_net_profit()

          if selecionar == "Previsão de demanda":
            # previsaoDemanda.previsao_demanda()
            # def insert_demand_data(data):
            #   db_deta_previsao_demanda.put(data)

            # data = {"Data": "2023-05-12", "Hora": "10:00", "Clientes": 50}
            # insert_demand_data(data)
            # adicionar uma mensagem de sucesso
            # st.success("Dados inseridos com sucesso!")
            previsaoDemanda.previsao_demanda()

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
            cadastrar_funcionario.cadastrarFuncionario()

          if selecionar == "Análise de desempenho dos funcionários":
            analisar.employee_performance_analysis()

          if selecionar == "Developers":
            developers.developers()

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
            mapa.mapaVisual()

          if selecionar == "Consultar Dados":

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

            select = st.selectbox('Selecione as opções para ver detalhes sobre seus estoque', ['NOME' , 'QUANTIDADE'])
            if select == 'NOME':
                st.write(dataDetaEstoque.query("NOME >= NOME")[["key","NOME"]])
            else:
                st.write(dataDetaEstoque.query("QUANTIDADE >= QUANTIDADE")[["key","QUANTIDADE"]])

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

            select = st.selectbox('Selecione as opções para ver detalhes sobre seus pratos', ['NOME' , 'PRECO', 'ACOMPANHAMENTO'])
            if select == 'NOME':
                st.write(dataDetaPratos.query("NOME >= NOME")[["key","NOME"]])
            elif select == 'PRECO':
                st.write(dataDetaPratos.query("PRECO >= PRECO")[["key","PRECO"]])
            else :
                st.write(dataDetaPratos.query("ACOMPANHAMENTO >= ACOMPANHAMENTO")[["key","ACOMPANHAMENTO"]])

            select = st.selectbox('Selecione as opções para ver detalhes sobre suas reservas', ['NOME' , 'DATA', 'QTDRESERVAS'])
            if select == 'NOME':
                st.write(dataDetaReservas.query("NOME >= NOME")[["key","NOME"]])
            elif select == 'DATA':
                st.write(dataDetaReservas.query("DATA >= DATA")[["key","DATA"]])
            elif select == 'QTDRESERVAS':
                st.write(dataDetaReservas.query("QTDRESERVAS >= QTDRESERVAS")[["key","QTDRESERVAS"]])

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
            categoria_grafico.vendas_por_categoria()

          # TODO - Criar um selectbox para selecionar o tipo de dado que o usuário quer ver no banco cliente
          if selecionar == "Previsão de clientes":
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
            previsaoVendas.cadastrar_venda()

          if selecionar == "Reservas":
            reservas.reservar()

          if selecionar == "Gráficos":
            getOption = st.selectbox("Selecione o gráfico que deseja visualizar", ["Gráfico de Pizza", "Gráfico de Dispersão"])

            if getOption == "Gráfico de Pizza":
               pass
            else:
              pass

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