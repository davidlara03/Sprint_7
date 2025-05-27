import streamlit as st
import pandas as pd
import plotly.express as px

df= pd.read_csv("C:/Users/larag/Sprint_7/vehicles_us.csv")
st.header("Estadísticas básicas")
          
if st.button("Mostrar histograma de precios"):
    fig = px.histogram(df, x="price", nbins=50, title="Distribución de precios")
    st.plotly_chart(fig)

if st.button("Mostrar gráfico de dispersión: Precio vs. Año del modelo"):
    fig2 = px.scatter(df, x="model_year", y="price", 
                      title="Precio vs. Año del modelo", 
                      labels={"model_year": "Año del Modelo", "price": "Precio"})
                      
    st.plotly_chart(fig2)