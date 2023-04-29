# from urllib import request
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pydeck as pdk
import plotly.express as px
import altair as alt
from dotenv import load_dotenv
import os
import logging
import hashlib
import smtplib
import yagmail
import requests
import plotly.graph_objects as go
# from fbprophet import Prophet


logging.basicConfig(filename='src/log/app.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logging.info('Iniciando o app')


load_dotenv()

URL = os.getenv('URL')
BEBIDAS = os.getenv('BEBIDAS')
ESTOQUE = os.getenv('ESTOQUE')
PRATOS = os.getenv('PRATOS')
CLIENTES = os.getenv('CLIENTES')


st.set_page_config(page_title="Pedacinho do Céu", page_icon="🍤", layout="wide")
selecionar = st.sidebar.selectbox("Selecione a página", ["Home",
                                                        "Dados Brutos",
                                                        "Consultar Dados", 
                                                        "Mapa",
                                                        "Gráficos", 
                                                        "Sobre",
                                                        "Contato",
                                                        "Avaliação",
                                                        "Login",
                                                        "Cadastro",
                                                        "funcionarios",
                                                        "Sair",
                                                        "Sugestões",
                                                        "Cardápio",
                                                        "Grafico de Vendas Mensais",
                                                        "Previsão de Vendas",
                                                        "Grafico de Vendas por Categoria",
                                                        "Grafico de Vendas por Categoria e Mês",
                                                        "Grafico de Vendas por Categoria e Dia da Semana",
                                                        "Previsão do Tempo",
                                                        "Previsão de clientes",
                                                         ])

# colocar um video de fundo
st.video("https://www.youtube.com/watch?v=wDJN95Y_yOM")

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


class Data:
  def __init__(self, URL):
      self.URL = URL
      self.BEBIDAS = BEBIDAS
      self.ESTOQUE = ESTOQUE
      self.PRATOS = PRATOS
      self.CLIENTES = CLIENTES

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


data= Data(URL).load()
dataBebidas= Data(BEBIDAS).loadBebidas()
dataEstoque= Data(ESTOQUE).loadEstoque()
dataPratos= Data(PRATOS).loadPratos()
dataClientes= Data(CLIENTES).loadClientes()


if __name__ == "__main__":

  st.markdown("## Pedacinho do Céu")
  st.markdown("###### Tudo o que você pode saber aqui sobre ✎Bebidas ✎Mercadorias ✎Preços ✎Pratos da casa ✎Clientes ✎Avaliações ✎Custo ✎Localização ✎E muito mais")
  st.markdown("Este projeto foi criado para gerenciar um restaurante chamado Pedacinho do Céu. O projeto utiliza Big Data, Power BI, Docker e uma API RESTful para coletar, processar, armazenar e visualizar os dados.")

  pict = Image.open('src/public/pedacinho.png')
  st.sidebar.image(pict, use_column_width=True)

  pic = Image.open('src/public/food-camarao.png')
  st.image(pic, use_column_width=True)

  if selecionar == "Home":
    logging.info('O cliente selecionou a página Home')
    st.markdown("### HOME")
    st.markdown("###### ESTA É A PÁGINA INICIAL DO PROJETO")
    st.markdown("###### AQUI VOCÊ PODE SELECIONAR AS PÁGINAS QUE DESEJA VISUALIZAR")
    st.markdown("###### ABAIXO VOCÊ PODE VER O MAPA, OS GRÁFICOS E OS DADOS BRUTOS")
    st.markdown("###### VOCÊ PODE SELECIONAR O QUE DESEJA VER NO MENU DA ESQUERDA")
    
    # Mapa de localização do restaurante
    # st.markdown("#### Mapa de Localização")
    # st.map(data[['LAT', 'LNG']].dropna())

    # Gráfico de vendas mensais
    st.markdown("#### Gráfico de Vendas Mensais")
    data_vendas = pd.DataFrame({
        'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
        'Vendas': [5000, 7000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000]
    })
    fig = px.line(data_vendas, x='Mês', y='Vendas')
    st.plotly_chart(fig)

    # Tabela de dados brutos
    # st.markdown("#### Tabela de Dados Brutos")
    # st.write(data)

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

  if selecionar == "Sair":
    # Autenticação
    st.header("Autenticação de saída")
    login = st.text_input("Digite seu login:")
    senha = st.text_input("Digite sua senha:", type="password")
    enviar = st.button("Enviar")

    # utilize o arquivo .csv para criar o login e a senha

    with open("src/data/login.csv", "r") as arquivo:
        credenciais_salvas = arquivo.readlines()[1].strip().split(",")
        login_salvo = credenciais_salvas[0]
        senha_salva = credenciais_salvas[1]

    if enviar:
        if login == login_salvo and senha == senha_salva:
            st.success("Autenticação bem-sucedida!")
            st.balloons()
            st.markdown("---------------------------------")
            st.markdown("## Obrigado por utilizar o sistema!")
            st.markdown("## Espero que gostem. ✌︎ ✌︎ ✌︎")
            st.markdown("## Esperamos que tenha tido uma ótima experiência em nosso restaurante. 😃")
            st.markdown("# Até a próxima! 🍔🍕🍻")
            st.empty()
        else:
            st.error("Login ou senha incorretos.")

  if selecionar == "Previsão do Tempo":
    st.markdown("## Previsão do Tempo")
    st.write("Aqui você pode ver a previsão do tempo para os próximos dias.")
    # st.set_page_config(page_title="Previsão do Tempo", page_icon=":sunny:")

    # Chave de API do OpenWeatherMap
    api_key = "sua_api_key_aqui"

    # URL da API para previsão do tempo
    url = "https://api.openweathermap.org/data/2.5/forecast"

    # Cria uma lista de cidades para o usuário escolher
    cidades = ["Florianópolis,BR", "São Paulo,BR", "Rio de Janeiro,BR", "Buenos Aires,AR", "Londres,UK"]

    # Exibe uma caixa de seleção para o usuário escolher a cidade
    cidade = st.selectbox("Selecione uma cidade", cidades)

    # Parâmetros da API
    params = {
        "q": cidade,
        "appid": api_key,
        "units": "metric",
        "lang": "pt_br",
        "cnt": 40
    }

    # Chama a API e obtém os dados da previsão do tempo
    response = requests.get(url, params=params)
    if response.status_code != 200:
        st.error("Erro ao obter previsão do tempo. Tente novamente mais tarde.")
        st.stop()
        
    data = response.json()

    # Extrai os dados relevantes da resposta da API e cria um DataFrame
    forecast = []
    for item in data["list"]:
        previsao = {
            "Data": pd.to_datetime(item["dt_txt"]),
            "Temperatura": item["main"]["temp"],
            "Tempo": item["weather"][0]["description"],
            "Ícone": item["weather"][0]["icon"]
        }
        forecast.append(previsao)

    df = pd.DataFrame(forecast)

    # Cria um gráfico com a previsão do tempo
    fig = px.line(df, x="Data", y="Temperatura", title=f"Previsão do Tempo para {cidade}")
    fig.update_layout(xaxis_title="Data", yaxis_title="Temperatura (°C)")

    st.plotly_chart(fig)

    # Exibe a tabela com os dados da previsão do tempo
    st.write(df)

  if selecionar == "Sobre":
    st.markdown("## Sobre o Restaurante")
    st.write("O Restaurante Pedacinho do Céu foi fundado em 1995 com o objetivo de proporcionar aos seus clientes uma experiência gastronômica única e inesquecível. Com um cardápio diversificado que inclui pratos da cozinha regional e internacional, o restaurante se destaca pela qualidade dos seus ingredientes e pelo atendimento personalizado.")
    st.write("Além da excelência na comida, o Pedacinho do Céu também se preocupa com a experiência dos seus clientes. O ambiente é aconchegante e sofisticado, criando uma atmosfera perfeita para reuniões em família, encontros românticos ou jantares de negócios.")
    st.write("Venha nos visitar e experimentar o melhor da gastronomia!")
    pic = Image.open('src/public/restaurante.jpg')
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
    st.image('src/public/pedacinho.png', use_column_width=True)
    st.markdown("Em 1985, a Dona Maria e o Sr. José, proprietários do Bar e Restaurante Pedacinho do Céu, inauguraram o local em uma pequena casa de pescador, no Sul da Ilha de Florianópolis. Com o tempo, o local cresceu e tornou-se um ponto de encontro para amigos e famílias da região.")
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
            # st.image('src/public/foto_restaurante1.jpg', use_column_width=True)
            pass
        with col2:
            # st.image('src/public/foto_restaurante2.jpg', use_column_width=True)
            pass
        with col3:
            # st.image('src/public/foto_restaurante3.jpg', use_column_width=True)
            pass

    st.markdown("## Horário de Funcionamento")
    st.markdown("Segunda-feira: 18:00 às 23:00")
    st.markdown("Terça-feira: 18:00 às 23:00")
    st.markdown("Quarta-feira: 18:00 às 23:00")
    st.markdown("Quinta-feira: 18:00 às 23:00")
    st.markdown("Sexta-feira: 18:00 às 00:00")
    st.markdown("Sábado: 12:00 às 00:00")
    st.markdown("Domingo: 12:00 às 22:00")
    st.markdown("### Localização")
    st.markdown("Estamos localizados na Rua Joaquim Neves, 152, no Praia da cidade. Venha nos visitar e experimentar nossos deliciosos pratos!")

  if selecionar == "Login":

    # função para salvar os dados em um arquivo .txt
    def salvar_dados(email, senha):
        with open('src/data/usuarios.txt', 'a') as arquivo:
            arquivo.write(f"{email}, {senha}\n")

    # verifica se o arquivo de usuários existe e cria caso não exista
    if not os.path.isfile('src/data/usuarios.txt'):
        open('src/data/usuarios.txt', 'w').close()

    # define as credenciais de acesso
    credenciais = {
        'user': 'user'
    }

    # página de login
    def pagina_login():
        st.write("# Faça o login")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")

        # verifica se as credenciais estão corretas
        if st.button("Entrar"):
            if email in credenciais and senha == credenciais[email]:
                st.success("Login realizado com sucesso!")
                st.balloons()
                st.stop()
            else:
                st.error("E-mail ou senha incorretos. Tente novamente.")

    # página de cadastro
    def pagina_cadastro():
        st.write("# Cadastro de usuário")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")

        # salva os dados em um arquivo .txt
        if st.button("Cadastrar"):
            salvar_dados(email, senha)
            st.success("Cadastro realizado com sucesso!")
            st.balloons()

    # define o fluxo da aplicação
    if __name__ == "__main__":
        # st.set_page_config(page_title="Cadastro de Usuários")
        st.sidebar.write("# Menu")
        opcoes = ["Login", "Cadastro"]
        selecao = st.sidebar.radio("Selecione uma opção", opcoes)

        if selecao == "Login":
            pagina_login()
        elif selecao == "Cadastro":
            pagina_cadastro()

  if selecionar == "Cadastro":
    # Define o nome do arquivo que vai armazenar os dados
    filename = "src/data/cadastro.txt"


    # Verifica se o arquivo já existe
    if not os.path.exists(filename):
        open(filename, "a").close()


    def cadastrar_cliente(nome, email, login, senha):
        """Adiciona um novo cliente ao arquivo de cadastro"""
        with open(filename, "r") as f:
            for line in f:
                # Verifica se o login já está cadastrado
                if login == line.split(",")[2]:
                    st.warning("Já existe um cadastro com esse login")
                    return

        # Se o login ainda não estiver cadastrado, adiciona o novo cliente
        with open(filename, "a") as f:
            f.write(f"{nome},{email},{login},{senha}\n")
            st.success("Cadastro feito com sucesso!")
            st.balloons()

    def main():
        st.title("Cadastro de Cliente")
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        login = st.text_input("Login")
        senha = st.text_input("Senha", type="password")

        if st.button("Cadastrar"):
            cadastrar_cliente(nome, email, login, senha)


    if __name__ == "__main__":
        main()
  
  if selecionar == "Dados Brutos":
    st.markdown("### DADOS BRUTOS")

    if st.checkbox("Clique aqui para ver os dados",False):
        st.markdown("###### ESTES SÃO OS DADOS BRUTOS PARA TODAS AS COMPARAÇÕES E GRÁFICO")
        st.write(data)

    if st.checkbox("Clique aqui para ver os dados de bebidas",False):
      st.markdown("###### ESTES SÃO OS DADOS BRUTOS PARA TODAS AS COMPARAÇÕES E GRÁFICO")
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

  st.sidebar.markdown("### CLASSIFICAÇÃO ★★★★★")
  rate=st.sidebar.slider("Classificar o restaurante",0.0,5.0)
  # Ao selecionar a opção "Classificação", salva o valor da classificação no arquivo "src/data/classificacao.csv" e colocar o tipo de classificação, se é positiva ou negativa
  if st.sidebar.button("Classificar"):
      if rate >= 3.0:
        with open('src/data/classificacao.csv', 'a') as arquivo:
          arquivo.write(f"{rate},positiva\n")
        st.success("Classificação feita com sucesso!")
        st.balloons()
      elif rate < 3.0:
        with open('src/data/classificacao.csv', 'a') as arquivo:
          arquivo.write(f"{rate},negativa\n")
        st.success("Classificação feita com sucesso!")
        st.balloons()
      elif rate == 0.0:
        st.warning("Classificação não realizada!")
        st.balloons()
      elif rate > 5.0:
        with open('src/data/classificacao.csv', 'a') as arquivo:
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
      
      # # Gráfico de salário dos funcionários
      # fig = px.bar(dataFunc, x="Nome do funcionário", y="Salário a receber")
      # st.plotly_chart(fig)

      # Gráfico de salário dos funcionários
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
      if not os.path.isfile("src/data/funcionarios.csv"):
          dataFunc.to_csv("src/data/funcionarios.csv", index=False)
          st.info("Arquivo CSV criado com sucesso!")
      else:
          with open("src/data/funcionarios.csv", "a") as f:
              dataFunc.to_csv(f, header=False, index=False)
              st.info("Dados adicionados ao arquivo CSV com sucesso!")

      # Perguntar se deseja ver os dados completos do arquivo src/data/funcionarios.csv

      if st.button("Ver dados completos do arquivo CSV"):
          data = pd.read_csv("src/data/funcionarios.csv")
          st.dataframe(data)

  if selecionar == "Contato":
    st.markdown("## Contato")
    st.markdown("Estamos sempre prontos para ajudá-lo(a) e tirar todas as suas dúvidas. Se você tiver alguma pergunta, sugestão ou crítica, não hesite em entrar em contato conosco. Você pode nos enviar um e-mail ou ligar para o nosso telefone de contato:")
    st.markdown("### E-mail")
    st.markdown("contato@pedacinhodoceu.com.br")
    st.markdown("### Telefone")
    st.markdown("+55 (11) 1234-5678")
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
        st.write("Obrigado por entrar em contato!")
        st.write(f"Sua mensagem foi enviada para estevamsouzalaureth@gmail.com.")

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
    # id,nome,preco,quantidade,descricao,totalVendas,quantidadeVendas
    select=st.selectbox('Selecione as opções para ver detalhes sobre suas bebidas', ['NOME' , 'PRECO', 'QUANTIDADE', 'DESCRICAO', 'TOTAL DE VENDAS', 'QUANTIDADE DE VENDAS'])
    if select == 'NOME':
      st.write(dataBebidas.query("NOME >= NOME")[["ID","NOME"]])
    elif select == 'PRECO':
      st.write(dataBebidas.query("PRECO >= PRECO")[["ID","PRECO"]])
    elif select == 'QUANTIDADE':
      st.write(dataBebidas.query("QUANTIDADE >= QUANTIDADE")[["ID","QUANTIDADE"]])
    elif select == 'DESCRICAO':
      st.write(dataBebidas.query("DESCRICAO >= DESCRICAO")[["ID","DESCRICAO"]])
    elif select == 'TOTAL_ENDAS':
      st.write(dataBebidas.query("TOTAL_ENDAS >= TOTAL_ENDAS")[["ID","TOTAL_ENDAS"]])
    else :
      st.write(dataBebidas.query("QUANTIDADE_VENDAS >= QUANTIDADE_VENDAS")[["ID","QUANTIDADE_VENDAS"]])

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
    import datetime

    # Dados simulados
    categorias = ['Comida', 'Bebida', 'Sobremesa']
    vendas = np.random.randint(100, 1000, size=3)
    preco_medio = np.random.uniform(5, 20, size=3)
    vendas_categorias = pd.DataFrame({'Categoria': categorias, 'Vendas': vendas, 'Preço Médio': preco_medio})

    # Gráfico de bolhas
    fig = px.scatter(vendas_categorias, x='Categoria', y='Vendas', size='Preço Médio', hover_name='Categoria')
    st.plotly_chart(fig)

    # Salvar dados em arquivo
    vendas_categorias.to_csv('src/data/vendasCategorias.csv', index=False)

    # Projeção de vendas
    st.subheader('Projeção de vendas para a próxima semana')

    # Ler arquivo com dados
    dados = pd.read_csv('src/data/vendasCategorias.csv')

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
    # carregando os dados pré-definidos
    dados_vendas = pd.DataFrame({
        'Data': pd.date_range(start='2023-01-01', end='2023-12-31', freq='MS'),
        'Vendas': np.random.randint(50000, 1000000, size=12)
    })

    # exibindo o gráfico de vendas mensais
    st.title('Previsão de Vendas')
    st.subheader('Gráfico de Vendas Mensais')

    fig = px.line(dados_vendas, x='Data', y='Vendas')
    st.plotly_chart(fig)

    # inserindo os dados gerados no arquivo vendas.csv
    dados_vendas.to_csv('src/data/vendas.csv', index=False, header=False, mode='a')

  # if selecionar == "Previsão de clientes":
  #   st.header("Previsão de clientes")

  #   # Autenticação de usuário
  #   senha = st.text_input("Digite o código de acesso", type="password")
  #   if senha == "acesso123":
  #       st.subheader("Cadastro de usuário")
  #       form = st.form(key='user-form')
  #       nome = form.text_input("Nome")
  #       sobrenome = form.text_input("Sobrenome")
  #       email = form.text_input("E-mail")
  #       telefone = form.text_input("Telefone")
  #       submit_button = form.form_submit_button(label='Cadastrar')

  #       # Salvando dados no arquivo src/data/users.csv
  #       if submit_button:
  #         data = {'Nome': [nome], 'Sobrenome': [sobrenome], 'E-mail': [email], 'Telefone': [telefone]}
  #         df = pd.DataFrame(data)
  #         df.to_csv('src/data/users.csv', mode='a', header=not os.path.exists('src/data/users.csv'), index=False)
  #         st.success("Cadastro realizado com sucesso!")

  #       # Mostrando o gráfico com o total de clientes
  #       st.subheader("Total de clientes")
  #       df = pd.read_csv('src/data/users.csv')
  #       df['Total'] = 1
  #       total_clientes = df.groupby(['Nome', 'Sobrenome']).count().reset_index()
  #       st.bar_chart(total_clientes['Total'])
  #   else:
  #       st.error("Código de acesso inválido!")

  #   # com base nos dados, faça uma projeção de clientes para o próximo mês

  #   # clientes = pd.DataFrame({
  #   #     'Data': pd.date_range(start='2023-01-01', end='2023-12-31', freq='MS'),
  #   #     'Clientes': np.random.randint(50000, 1000000, size=12)
  #   # })

  #   # # exibindo o gráfico de vendas mensais
  #   # st.title('Previsão de Clientes')

  #   # fig = px.line(clientes, x='Data', y='Clientes')
  #   # st.plotly_chart(fig)

  # # Lendo dados dos usuários cadastrados
  #   df = pd.read_csv('src/data/users.csv', index_col=0)

  # # Fazendo a projeção de clientes para o próximo mês
  #   ultimo_mes = df['Unnamed: 0'].iloc[-1].split('-')
  #   proximo_mes = str(int(ultimo_mes[1]) + 1)
  #   proximo_ano = ultimo_mes[0]
  #   if proximo_mes == '13':
  #       proximo_mes = '01'
  #       proximo_ano = str(int(proximo_ano) + 1)
  #   proximo_mes_ano = proximo_ano + '-' + proximo_mes + '-01'
  #   proximo_mes_clientes = np.random.randint(50000, 1000000, size=1)[0]

  #   # Mostrando a projeção de clientes
  #   st.subheader("Projeção de clientes para o próximo mês")
  #   st.write(f"No mês de {proximo_mes_ano} teremos aproximadamente {proximo_mes_clientes} clientes.")

  #   # Mostrando o gráfico com o total de clientes cadastrados
  #   st.subheader("Total de clientes cadastrados")
  #   df['Total'] = 1
  #   df = df.groupby(['Data']).count().reset_index()
  #   fig = px.line(df, x='Data', y='Total', title='Total de clientes cadastrados')
  #   st.plotly_chart(fig)

  if selecionar == "Previsão de clientes":
    st.header("Previsão de clientes")

    st.subheader("Cadastro de usuário")
    form = st.form(key='user-form')
    nome = form.text_input("Nome")
    sobrenome = form.text_input("Sobrenome")
    email = form.text_input("E-mail")
    telefone = form.text_input("Telefone")
    submit_button = form.form_submit_button(label='Cadastrar')

    # Salvando dados no arquivo src/data/users.csv
    if submit_button:
        data = {'Nome': [nome], 'Sobrenome': [sobrenome], 'E-mail': [email], 'Telefone': [telefone]}
        df = pd.DataFrame(data)
        df.to_csv('src/data/users.csv', mode='a', header=not os.path.exists('src/data/users.csv'), index=False)
        st.success("Cadastro realizado com sucesso!")

    # Mostrando o gráfico com o total de clientes
    st.subheader("Total de clientes")
    df = pd.read_csv('src/data/users.csv', index_col=0)
    df['Total'] = 1
    total_clientes = df.groupby(['Nome', 'Sobrenome']).count().reset_index()
    st.bar_chart(total_clientes['Total'])

    # Fazendo a projeção de clientes para o próximo mês
    ultimo_mes = df['Data'].iloc[-1].split('-')
    proximo_ano = ultimo_mes[0]
    if len(ultimo_mes) >= 2:
        proximo_mes = str(int(ultimo_mes[1]) + 1)
    else:
        proximo_mes = '01'
        proximo_ano = str(int(proximo_ano) + 1)
    if proximo_mes == '13':
        proximo_mes = '01'
        proximo_ano = str(int(proximo_ano) + 1)
    proximo_mes_ano = proximo_ano + '-' + proximo_mes + '-01'
    proximo_mes_clientes = np.random.randint(50000, 1000000, size=1)[0]

    # Mostrando a projeção de clientes
    st.subheader("Projeção de clientes para o próximo mês")
    st.write(f"No mês de {proximo_mes_ano} teremos aproximadamente {proximo_mes_clientes} clientes.")

    # Mostrando o gráfico com o total de clientes cadastrados
    st.subheader("Total de clientes cadastrados")
    df['Total'] = 1
    df = df.groupby(['Data']).count().reset_index()
    fig = px.line(df, x='Data', y='Total', title='Total de clientes cadastrados')
    st.plotly_chart(fig)

  if selecionar == "Gráficos":
     getOption = st.selectbox("Selecione o gráfico que deseja visualizar", ["Gráfico de Barras", "Gráfico de Linhas", "Gráfico de Pizza", "Gráfico de Bolha"])
     if getOption == "Gráfico de Barras":
      st.markdown("### GRÁFICO DE BARRAS")
      st.markdown("###### ESTE É O GRÁFICO DE BARRAS PARA TODAS AS COMPARAÇÕES DE CUSTO")
      st.bar_chart(data)

      st.markdown("###### ESTE É O GRÁFICO DE BARRAS PARA TODAS AS COMPARAÇÕES DE ESTOQUE")
      st.bar_chart(dataEstoque)

      st.markdown("###### ESTE É O GRÁFICO DE BARRAS PARA TODAS AS COMPARAÇÕES DE PRATOS")
      st.bar_chart(dataPratos)

      st.markdown("###### ESTE É O GRÁFICO DE BARRAS PARA TODAS AS COMPARAÇÕES DE CLIENTES")
      st.bar_chart(dataClientes)

      st.markdown("###### ESTE É O GRÁFICO DE BARRAS PARA TODAS AS COMPARAÇÕES DE BEBIDAS")
      st.bar_chart(dataBebidas)
    
      if getOption == "Gráfico de Linhas":
        st.markdown("### GRÁFICO DE LINHAS")
        st.markdown("###### ESTE É O GRÁFICO DE LINHAS PARA TODAS AS COMPARAÇÕES")
        st.line_chart(data)

        st.markdown("###### ESTE É O GRÁFICO DE LINHAS PARA TODAS AS COMPARAÇÕES")
        st.line_chart(dataEstoque)

        st.markdown("###### ESTE É O GRÁFICO DE LINHAS PARA TODAS AS COMPARAÇÕES")
        st.line_chart(dataPratos)

        st.markdown("###### ESTE É O GRÁFICO DE LINHAS PARA TODAS AS COMPARAÇÕES")
        st.line_chart(dataClientes)

      if getOption == "Gráfico de Pizza":
        st.markdown("### GRÁFICO DE PIZZA")
        st.markdown("###### ESTE É O GRÁFICO DE PIZZA PARA BEBIDAS")
        fig_bebidas = px.pie(dataBebidas, values='PRECO', names='NOME')
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

      if getOption == "Gráfico de Bolha":
        st.markdown("### GRÁFICO DE BOLHA")
        st.markdown("###### ESTE É O GRÁFICO DE BOLHA PARA TODAS AS COMPARAÇÕES")
        st.vega_lite_chart(data, {
          'mark': {'type': 'circle', 'tooltip': 500},
          'encoding': {
              'x': {'field': 'Restaurant_Name', 'type': 'quantitative'},
              'y': {'field': 'Rating', 'type': 'quantitative'},
              'size': {'field': 'Price_Range', 'type': 'quantitative'},
              'color': {'field': 'Rating', 'type': 'quantitative'},
          },
        })

        st.markdown("###### ESTE É O GRÁFICO DE BOLHA PARA TODAS AS COMPARAÇÕES")
        st.vega_lite_chart(dataEstoque, {
          'mark': {'type': 'circle', 'tooltip': 500},
          'encoding': {
              'x': {'field': 'id', 'type': 'quantitative'},
              'y': {'field': 'quantidade', 'type': 'quantitative'},
              'size': {'field': 'totalVendas', 'type': 'quantitative'},
              'color': {'field': 'totalVendas', 'type': 'quantitative'},
          },
        })

        st.markdown("###### ESTE É O GRÁFICO DE BOLHA PARA TODAS AS COMPARAÇÕES")
        st.vega_lite_chart(dataPratos, {
          'mark': {'type': 'circle', 'tooltip': 500},
          'encoding': {
              'x': {'field': 'id', 'type': 'quantitative'},
              'y': {'field': 'quantidade', 'type': 'quantitative'},
              'size': {'field': 'totalVendas', 'type': 'quantitative'},
              'color': {'field': 'totalVendas', 'type': 'quantitative'},
          },
        })

        st.markdown("###### ESTE É O GRÁFICO DE BOLHA PARA TODAS AS COMPARAÇÕES")
        st.vega_lite_chart(dataClientes, {
          'mark': {'type': 'circle', 'tooltip': 500},
          'encoding': {
              'x': {'field': 'id', 'type': 'quantitative'},
              'y': {'field': 'quantidade', 'type': 'quantitative'},
              'size': {'field': 'totalVendas', 'type': 'quantitative'},
              'color': {'field': 'totalVendas', 'type': 'quantitative'},
          },
        })