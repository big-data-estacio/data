# from client.src.api.service.mercadorias_service import MercadoriasService
import streamlit as st
from bebidas.bebidasSpark import BebidasCsvReader
from pratos.pratosSpark import PratosCsvReader
from reservas.reservasSpark import ReservasCsvReader
from estoqueMercadoriasService.mercadoriasSpark import EstoqueMercadoriasCsvReader
from previsaoVendas.previsaoVendasSpark import PrevisaoVendasCsvReader
from funcionarios.funcionariosSpark import FuncionariosCsvReader
from cadastroCliente.clientesSpark import CadastroCsvReader


def display_bebidas():
    df = BebidasCsvReader.read_csv("../../src/data/bebidas.csv")
    st.dataframe(df.toPandas())


def display_pratos():
    df = PratosCsvReader.read_csv("../../src/data/pratos.csv")
    st.dataframe(df.toPandas())


def display_reservas():
    df = ReservasCsvReader.read_csv("../../src/data/reservas.csv")
    st.dataframe(df.toPandas())


def display_estoque_mercadorias():
    df = EstoqueMercadoriasCsvReader.read_csv("../../src/data/estoquemercadorias.csv")
    st.dataframe(df.toPandas())


def display_previsao_vendas():
    df = PrevisaoVendasCsvReader.read_csv("../../src/data/previsaoVendas.csv")
    st.dataframe(df.toPandas())


def display_funcionarios():
    df = FuncionariosCsvReader.read_csv("../../src/data/funcionarios.csv")
    st.dataframe(df.toPandas())


def display_cadastro():
    df = CadastroCsvReader.read_csv("../../src/data/cadastro.csv")
    st.dataframe(df.toPandas())


def print_menu():
    st.write("Selecione o arquivo que deseja consultar:")
    option = st.selectbox("", ("Bebidas", "Pratos", "Reservas", "Estoque de Mercadorias", "Previsão de Vendas", "Funcionários", "Cadastro"))

    if option == "Bebidas":
        display_bebidas()
    elif option == "Pratos":
        display_pratos()
    elif option == "Reservas":
        display_reservas()
    elif option == "Estoque de Mercadorias":
        display_estoque_mercadorias()
    elif option == "Previsão de Vendas":
        display_previsao_vendas()
    elif option == "Funcionários":
        display_funcionarios()
    elif option == "Cadastro":
        display_cadastro()


if __name__ == "__main__":
    st.set_page_config(page_title="Consulta de Dados")
    print_menu()
