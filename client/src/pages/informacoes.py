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


class ExibidorInformacoesRestaurante:
    
  def __init__(self, horarios):
      self.horarios = horarios
  
  def exibir_informacoes(self):
      st.markdown("## Horário de Funcionamento")
      for dia, horario in self.horarios.items():
          st.markdown(f"{dia.capitalize()}: {horario}")
