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




# Voy a empezar con las acciones
# Wheat
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



# Hago lo mismo con el oro
ticker='GC=F'
start = dt.date(2017, 4, 30)
stop=dt.date.today()
gold= web.DataReader(ticker, 'yahoo', start, stop)
gold_year= gold.copy()
gold_year=gold_year.resample('Y').mean()
gold_year_plus=gold_year.copy()
gold_year_plus['Percentage Change']=gold_year_plus['Adj Close'].pct_change().multiply(100)
gold_year_plus['Accumulated Percentage Change']=gold_year_plus['Percentage Change'].pct_change().multiply(100)
gold_plus=gold.copy()
gold_plus['Percentage Change']=gold_plus['Adj Close'].pct_change().multiply(100)
gold_plus['Accumulated Percentage Change']=gold_plus['Percentage Change'].pct_change().multiply(100)



# Lo repito para el maiz
ticker='ZC=F'
start = dt.date(2017, 4, 30)
stop=dt.date.today()
corn= web.DataReader(ticker, 'yahoo', start, stop)
corn_year= corn.copy()
corn_year=corn_year.resample('Y').mean()
corn_year_plus=corn_year.copy()
corn_year_plus['Percentage Change']=corn_year_plus['Adj Close'].pct_change().multiply(100)
corn_year_plus['Accumulated Percentage Change']=corn_year_plus['Percentage Change'].pct_change().multiply(100)
corn_plus=corn.copy()
corn_plus['Percentage Change']=corn_plus['Adj Close'].pct_change().multiply(100)
corn_plus['Accumulated Percentage Change']=corn_plus['Percentage Change'].pct_change().multiply(100)






# Ahora voy a empezar con el GDP
# Tengo un diccionario del valor en billones de US$ global del gdp
global_gdp_dic={'Years': [2016, 2017, 2018, 2019, 2020, 2021, 2022],
            'Values': [75153.75, 80823.16, 85883.45, 87390.79, 84971.65, 94935.11, 102404.01]}
# Lo convierto en Data Frame
global_gdp = pd.DataFrame(global_gdp_dic)
# Tengo otro diccionario del valor en porcentaje del gdp/ppp en base al gdp global 
share_gdp_ppp_dic={'Year': [2016, 2017, 2018, 2019, 2020, 2021, 2022],
                'Share': [0.1617, 0.16, 0.1591, 0.1584, 0.1583, 0.1586, 0.1591]}
# Lo convierto en Data Frame
share_gdp_ppp = pd.DataFrame(share_gdp_ppp_dic)
# Los concateno y mofico el data frame a mi gusto 
gdp_ppp=pd.concat([global_gdp, share_gdp_ppp], axis=1)
del(gdp_ppp['Year'])
gdp_ppp.set_index('Years', inplace=True)
# Creo una nueva columna multiplicando los valores del primer df con los del segundo 
# ya que asi puedo quitar el porcentaje y me sale el valor en $
gdp_ppp['GDP_PPP']= np.multiply(gdp_ppp['Values'], gdp_ppp['Share'])
# Añado las columnas de variación porcentual y variqación porcentual acumulada
gdp_ppp['Percentage Change']=gdp_ppp['GDP_PPP'].pct_change().multiply(100)
gdp_ppp['Accumulated Percentage Change']=gdp_ppp['Percentage Change'].pct_change().multiply(100)
# Redondeo toda la tabla a 4 decimales porque no me hacen falta más
gdp_ppp = gdp_ppp.round(4)




# Ahora voy a hacer un df uniendo el valor que más me interesa de las acciones con el qeu más me interesa del GDP
adj_close=pd.DataFrame(wheat_year['Adj Close'])
adj_close=adj_close.reset_index()
GDP_PPP=pd.DataFrame(gdp_ppp['GDP_PPP'][1:])
GDP_PPP=GDP_PPP.reset_index()
joined=pd.concat([GDP_PPP, adj_close], axis=1)
joined=joined.drop(['Date'], axis=1)
joined = joined.set_index('Years')




# Voy a crear un data frame que una todos los adj close de mis commodities con el gdp_ppp
# Para eso voy a crear df de cada commodity solo con la columna adj Close
adj_close_gold=pd.DataFrame(gold_year['Adj Close'])
adj_close_gold=adj_close_gold.reset_index()
adj_close_gold=adj_close_gold.set_axis(['Year', 'Adj Close Gold'], axis=1)
adj_close_corn=pd.DataFrame(corn_year['Adj Close'])
adj_close_corn=adj_close_corn.reset_index()
adj_close_corn=adj_close_corn.set_axis(['Year', 'Adj Close Corn'], axis=1)
adj_close_wheat=pd.DataFrame(wheat_year['Adj Close'])
adj_close_wheat=adj_close_wheat.reset_index()
adj_close_wheat=adj_close_wheat.set_axis(['Year', 'Adj Close Wheat'], axis=1)
# Hago lo mismo para el gdp_ppp que he hecho con cada commodity
GDP_PPP=pd.DataFrame(gdp_ppp['GDP_PPP'][1:])
GDP_PPP=GDP_PPP.reset_index()
# Ahora lo concateno
joined=pd.concat([GDP_PPP, adj_close_wheat, adj_close_gold, adj_close_corn], axis=1)
joined=joined.drop(['Year'], axis=1)
joined = joined.set_index('Years')
joined.round(4)



# Voy a crear un df solo del adj close de cada commodity sin el gdp_ppp que me servirá para hacer graficos
commodities = joined.drop(['GDP_PPP'], axis=1)




# Creo un lineplots para cada commodity
x = np.linspace(0, 10, 100) 
fig = plt.figure()
plt.xlabel('Date')
plt.ylabel('US $')
plt.plot(gold['Adj Close'], '#dba643');


x = np.linspace(0, 10, 100) 
fig = plt.figure()
plt.xlabel('Date')
plt.ylabel('US $')
plt.plot(corn['Adj Close'], '#2b3f48');


x = np.linspace(0, 10, 100) 
fig = plt.figure()
plt.xlabel('Date')
plt.ylabel('US $')
plt.plot(wheat['Adj Close'], '#8a3c46');


# Ahora creo un line plot de todas juntas 
fig, ax = plt.subplots(1, 1, figsize=(6,4))
ax.plot(wheat['Adj Close'], label='Adj Close Weat', color='#8a3c46')
ax.plot(corn['Adj Close'], label='Adj Close Corn', color='#2b3f48')
ax.plot(gold['Adj Close'], label='Adj Close Gold', color='#dba643')
ax.set_xlabel('Years')
ax.set_ylabel('US $')
ax.legend();



# Creo un heatmap
plt.figure(figsize=(10,10))
sns.heatmap(joined.corr(), # correlacion de pearson. es un estadistico que te mira la relación lineal que hay entre dos variables.
#  te mide como de fuerte es la relación lineal entre dos variables.
vmin=-1,
vmax=1,

cmap=sns.color_palette("Spectral_r", 200),
annot=True, # que salga en la grafica el numerito puesto
square=True,
linewidth=.5)



# Mas graficos
fig = plt.figure()
ax = joined['Adj Close Gold'].plot(kind='bar',grid=True, color='#dba643')
ax1 = ax.twinx()
plt.title('Gold')
ax.set_ylabel('US $')
ax1.set_ylabel('billion US $')
ax1.plot(joined['GDP_PPP'].values, linestyle='-', linewidth=2.0, color='#f98c8d');



fig = plt.figure()
ax = joined['Adj Close Corn'].plot(kind='bar',grid=True, color='#2b3f48')
ax1 = ax.twinx()
plt.title('Corn')
ax.set_ylabel('US $')
ax1.set_ylabel('billion US $')
ax1.plot(joined['GDP_PPP'].values, linestyle='-', linewidth=2.0,color='#f98c8d');


fig = plt.figure()
ax = joined['Adj Close Wheat'].plot(kind='bar',grid=True, color='#8a3c46')
ax1 = ax.twinx()
ax.set_ylabel('US $')
ax1.set_ylabel('billion US $')
plt.title('Wheat')
ax1.plot(joined['GDP_PPP'].values, linestyle='-', linewidth=2.0,color='#f98c8d');