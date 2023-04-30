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
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dotenv import load_dotenv
from PIL import Image
import matplotlib.pyplot as plt
import datetime

def developers():
  st.title("Sentiment Analysis of Tweets about US Airlines")
  st.sidebar.title("Sentiment Analysis of Tweets about US Airlines")

  st.markdown("This application is a Streamlit dashboard to analyze the sentiment of Tweets 🐦🐦")
  st.sidebar.markdown("This application is a Streamlit dashboard to analyze the sentiment of Tweets 🐦🐦")

  st.title('Streamlit Tutorial')
  st.markdown('')
  st.markdown('''
  - developped by [`@happy-jihye`](https://github.com/happy-jihye)
  - [`Github 💻 streamlit-tutorial`](https://github.com/happy-jihye/Streamlit-Tutorial)
  ''')
  st.info('Streamlit is an open-source python framework for building web apps for Machine Learning and Data Science. We can instantly develop web apps and deploy them easily using Streamlit. Streamlit allows you to write an app the same way you write a python code. Streamlit makes it seamless to work on the interactive loop of coding and viewing results in the web app.')

  st.header('Streamlit Gallery 🖼️')

  with st.expander('Example 1'):
      st.markdown('''
  ## 💸 Stock Price Dashboard ✨

  ```
  pip install yfinance fbprophet plotly
  ```
      ''')

  with st.expander('Example 2'):
      st.markdown('''
  ## 🙃 Cartoon StyleGAN ✨

  - [`happy-jihye/Cartoon-StyleGAN`](https://github.com/happy-jihye/Cartoon-StyleGAN)

  ```
  pip install bokeh ftfy regex tqdm gdown

  # for styleclip
  pip install git+https://github.com/openai/CLIP.git
  ```
      ''')

  with st.expander('Example 3'):
      st.markdown('''
  ## 🖼️ VQGAN-CLIP ✨


  ```
  # install python packages
  pip install ftfy regex tqdm omegaconf pytorch-lightning IPython kornia imageio imageio-ffmpeg einops torch_optimizer

  # clone other repositories
  git clone 'https://github.com/openai/CLIP'
  git clone 'https://github.com/CompVis/taming-transformers'

  # download checkpoints
  mkdir checkpoints
  curl -L -o checkpoints/vqgan_imagenet_f16_16384.yaml -C - 'https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1' #ImageNet 16384
  curl -L -o checkpoints/vqgan_imagenet_f16_16384.ckpt -C - 'https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fckpts%2Flast.ckpt&dl=1' #ImageNet 16384
  ```
      ''')


  st.markdown('---')
  st.header('Streamlit API reference')
  st.markdown('')
  st.markdown('''
  **📒 Useful resource**
  - [`streamlit.io`](https://docs.streamlit.io/)
  - [`awesome-streamlit`](https://github.com/MarcSkovMadsen/awesome-streamlit)
  - [`streamlit gallery`](https://streamlit.io/gallery)
  - [`Python Streamlit 사용법 - 프로토타입 만들기`](https://zzsza.github.io/mlops/2021/02/07/python-streamlit-dashboard/)

  ''')

  st.code('import streamlit as st')