# Importo librerias
# Seguramente no haya utilizado todas pero las copio por si acaso se me olvida alguna no me vaya a dar error
# Para todo
import numpy as np
import pandas as pd

# Para sacar mis datos de Yahoo
import pandas_datareader.data as web

# Para fechas
import datetime as dt

# Para matplotlib
import matplotlib.pyplot as plt

# Para seaborn
from sklearn.datasets import load_iris, load_boston
import seaborn as sns

# Para plotly
import plotly
plotly.offline.init_notebook_mode()
from plotly.offline import init_notebook_mode, iplot, plot





# Leo los datos y los saco en un dataframe
wheat= web.DataReader('ZW=F', 'yahoo', '2017-04-30', '2022-04-30')





#hago una copia para no alterar el principal y poder acudir a el siemrpe que quiera
wheat_year= wheat.copy()

# Voy a crear un df solo con los años 
wheat_year=wheat_year.resample('Y').mean()

# Se que esta copia es innecesaria pero me gusta para poder cambiarle de nombre y no modificar nada por error arriba
wheat_year_plus=wheat_year.copy()

# Añado las columnas de variación porcentual y variqación porcentual acumulada
wheat_year_plus['Percentage Change']=wheat_year_plus['Adj Close'].pct_change().multiply(100)
wheat_year_plus['Accumulated Percentage Change']=wheat_year_plus['Percentage Change'].pct_change().multiply(100)





# Hago una copia nueva de mi df original para coger esta vez todas las fechas por días
wheat_plus=wheat.copy()

# Añado las columnas de variación porcentual y variqación porcentual acumulada
wheat_plus['Percentage Change']=wheat_plus['Adj Close'].pct_change().multiply(100)
wheat_plus['Accumulated Percentage Change']=wheat_plus['Percentage Change'].pct_change().multiply(100)


