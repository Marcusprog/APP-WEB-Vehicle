import pandas as pd
import streamlit as st
import plotly.express as px

df_vh = pd.read_csv('vehicles.csv')

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados
     hist_button = st.button('Criar histograma') # criar um botão
     
     if hist_button: # se o botão for clicado
         # escrever uma mensagem
         st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um histograma
         fig = px.histogram(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
         st.plotly_chart(fig, use_container_width=True)

         # criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram: # se a caixa de seleção for selecionad
  st.write('Criando um histograma para a coluna odometer')