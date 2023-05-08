#!/bin/bash

# Instalação dos pacotes necessários
pip install -r requirements.txt

# Debug com streamlit
streamlit debug app.py
