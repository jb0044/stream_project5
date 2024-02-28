import streamlit as st 
import pandas as pd 
import plotly_express as plt 

car_data = pd.read_csv('vehicles_us.csv') # leer los datos