#importo librerias 
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime as dt





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



print(gdp_ppp)