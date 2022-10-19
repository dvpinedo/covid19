import pandas as pd
import numpy as np
import matplotlib as mpl

url = "covid_colombia_09_04_2020.csv"
data = pd.read_csv(url)


num_infected = data.shape[0]
print('Número total de infectado es:', num_infected)


num_cities = data.groupby('Ciudad de ubicación').size()
print('Número total de municipos afectados es:', num_cities.shape[0])


list_infected = data['Ciudad de ubicación'].unique()
print('Lista de municipios afectados:', list_infected)


in_house = data[data['Atención**'] == 'Casa']
print('Número de personas atentidas en casa:', in_house.shape[0])

recovered = data[data['Atención**'] == 'Recuperado']
print('Número de recuperadoes es:', recovered.shape[0])


deceased = data[data['Atención**'] == 'Fallecido']
print('Número de Fallecidos es:', deceased.shape[0])


type_case = data.groupby('Tipo*').size().sort_values(ascending=False)
print('Orden de mayor a menor tipo de caso', type_case)


num_dep = data.groupby('Departamento o Distrito').size()
print('Número de departamentos afectados es:', num_dep.shape[0])


list_dep = data['Departamento o Distrito'].unique()
print('Lista de departamenos afectados', list_dep)


type_atten = data.groupby('Atención**').size().sort_values(ascending=False)
print('Orden de mayor a menor tipo de atención:', type_atten)


dp_top10_infected = data.groupby('Departamento o Distrito').size().sort_values(ascending=False).head(10)
print('Los 10 departamentos con mas contagiados son:', dp_top10_infected)


dp_top10_deceased = data[data['Atención**']=='Fallecido'].groupby('Departamento o Distrito').size().sort_values(ascending=False).head(10)
print('Los 10 departamentos con mas fallecidos son:', dp_top10_deceased)


dp_top10_recovered = data[data['Atención**']=='Recuperado'].groupby('Departamento o Distrito').size().sort_values(ascending=False).head(10)
print('Los 10 departamentos con mas recuperados son:', dp_top10_recovered)


mp_top10_infected = data.groupby('Ciudad de ubicación').size().sort_values(ascending=False).head(10)
print('Los 10 Municipios con mas infectados son:', mp_top10_infected)


mp_top10_deceased = data[data['Atención**']=='Fallecido'].groupby('Ciudad de ubicación').size().sort_values(ascending=False).head(10)
print('Los 10 municipios con mas fallecidos son:', mp_top10_deceased)


mp_top10_recovered = data[data['Atención**']=='Recuperado'].groupby('Ciudad de ubicación').size().sort_values(ascending=False).head(10)
print('Los 10 municipios con mas recuperados son:', mp_top10_recovered)


dp_mp = data.groupby(['Departamento o Distrito','Ciudad de ubicación']).size().sort_values(ascending=False)
print('Lista de  Departamenos agrupudos de mayor a menor con ciudades con mas casos: ', dp_mp)


dp_men_women_infected = data.groupby(['Departamento o Distrito','Ciudad de ubicación','Sexo']).size()
print('Numero de hombre y mujeres infectados por Ciudad de cada departamento es:', dp_men_women_infected)


prom_ed = data.groupby(['Departamento o Distrito', 'Ciudad de ubicación','Sexo']).mean()
prom_ed.drop('ID de caso', axis = 1)


country_p = data.groupby('País de procedencia').size().sort_values(ascending = False)
print('Lista de paises de mayor a menos de contagiados por:', country_p)


diagnosis_date = data.groupby('Fecha de diagnóstico').size().sort_values(ascending = False)
print('Fechas de mayor a menor con mas infectados:', diagnosis_date)


z = data.groupby('Atención**').size().sort_values(ascending = False)
k = z / z.sum() * 100
print('Tasa de mortalidad en toda colombia es:',k.iloc[4:5])
print('Tasa de recuperados en toda colombia es:',k.iloc[2:3])


z = data.groupby(['Departamento o Distrito','Atención**']).size()
k = z / z.sum() * 100


z = data.groupby(['Ciudad de ubicación','Atención**']).size()
k = z / z.sum() * 100


data.groupby(['Ciudad de ubicación','Atención**']).size()


prom_ed = data.groupby(['Ciudad de ubicación','Sexo']).mean()
prom_ed.drop('ID de caso', axis = 1)



dc = data[data['Atención**']=='Fallecido']
rc = data[data['Atención**']=='Recuperado']
inf_plot = data.groupby('Fecha de diagnóstico').size().cumsum().plot()
dec_plot = dc.groupby('Fecha de diagnóstico').size().cumsum().plot()
rec_plot = rc.groupby('Fecha de diagnóstico').size().cumsum().plot()
print('Grafica acumulada de Contagio, Fallecidos y Recuperados :', inf_plot, rec_plot, dec_plot)


dc1 = data[data['Atención**']=='Fallecido']
rc1 = data[data['Atención**']=='Recuperado']
inf_plot_dep = data.groupby(['Departamento o Distrito' ]).size().sort_values(ascending=False).head(10).plot()
dec_plot_dep = dc1.groupby('Departamento o Distrito').size().sort_values(ascending=False).head(10).plot()
rec_plot_dep = rc1.groupby('Departamento o Distrito').size().sort_values(ascending=False).head(10).plot()
print('Grafica acumulada de Contagio, Fallecidos y Recuperados :', inf_plot_dep, rec_plot_dep, dec_plot_dep)


dc2 = data[data['Atención**']=='Fallecido']
rc2 = data[data['Atención**']=='Recuperado']
inf_plot_ct = data.groupby(['Ciudad de ubicación' ]).size().sort_values(ascending=False).head(10).plot()
dec_plot_ct = dc2.groupby('Ciudad de ubicación').size().sort_values(ascending=False).head(10).plot()
rec_plot_ct = rc2.groupby('Ciudad de ubicación').size().sort_values(ascending=False).head(10).plot()
print('Grafica acumulada de Contagio, Fallecidos y Recuperados :', inf_plot_ct, rec_plot_ct, dec_plot_ct)


a_deceased = data[data['Atención**'] == 'Fallecido'].groupby('Edad').size().sort_values(ascending = False)
print('Liste de mayor a menor la cantidad de fallecidos por edad en toda Colombia: ', a_deceased)


list_at = data.groupby('Atención**').size()
sm = data.groupby('Atención**').size().sum()
res = (list_at.iloc[0:7]/sm)*100
print('Porcentajes por atención:', res)


at = data.groupby('Atención**').size()
at.plot(kind='bar')


sx = data.groupby('Sexo').size()
sx.plot(kind='bar')


tp = data.groupby('Tipo*').size()
tp.plot(kind='bar')


at1 = data.groupby('Fecha de diagnóstico').size().plot(kind ='bar')
print('Grafica de barras con numero de contagiado por fecha:', at)

rc3 = data[data['Atención**']=='Recuperado']
rc_at = rc3.groupby(['Fecha de diagnóstico','Atención**']).size().plot(kind ='bar')
print('Grafica de barras con numero de recuperados por fecha:', rc_at)

dc3 = data[data['Atención**']=='Fallecido']
dc_at = dc3.groupby(['Fecha de diagnóstico','Atención**']).size().plot(kind ='bar')
print('Grafica de barras con numero de fallecidos por fecha:', dc_at)


