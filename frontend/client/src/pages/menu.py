import streamlit as st


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