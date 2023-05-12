import streamlit as st
import os
import openai
from PIL import Image

from utils import *

icon = Image.open(os.path.dirname(__file__) + '/../icon.png')

st.set_page_config(page_icon=icon)

st.markdown('# 🤖 Prompt Engine')

st.write("A engenharia de prompt consiste em fornecer instruções corretas ao GPT-4. Quanto mais precisas as instruções, melhores os resultados. O objetivo é gerar código Manim a partir de uma parte específica do código. Então você pode usar o código para renderizar a animação.")

prompt = st.text_area("Escreva sua ideia de animação aqui. Use palavras simples.",
                      "Desenhe um círculo azul e converta-o em um quadrado vermelho")

openai_api_key = st.text_input(
    "Cole o seu [Open API Key](https://platform.openai.com/account/api-keys)", value="", type="password")

openai_model = st.selectbox(
    "Selecione o modelo GPT. Se você não tiver acesso ao GPT-4, selecione GPT-3.5-Turbo", ["GPT-3.5-Turbo", "GPT-4"])

generate_prompt = st.button(
    ":computer: Gerar prompt :sparkles:", type="primary")

if generate_prompt:
  if not openai_api_key:
    st.error("Error: Você precisa fornecer sua própria chave de API aberta para usar esse recurso.")
    st.stop()
  if not prompt:
    st.error("Error: Você precisa fornecer um prompt.")
    st.stop()

  response = openai.ChatCompletion.create(
      model=openai_model.lower(),
      messages=[
          {"role": "system", "content": GPT_SYSTEM_INSTRUCTIONS},
          {"role": "user", "content": wrap_prompt(prompt)}
      ]
  )

  code_response = extract_code(response.choices[0].message.content)

  code_response = extract_construct_code(code_response)

  st.text_area(label="Código gerado: ",
               value=code_response,
               key="code_input")
