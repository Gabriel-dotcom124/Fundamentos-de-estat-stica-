%%writefile nba.csv
height;weight;wage
2.01;86.2;17150000
1.93;106.1;898310
2.11;120.2;9881598
1.88;85.7;15643750
1.88;84.8;2875000
2.11;106.1;2376840
1.98;86.6;2625717
2.08;104.3;37199000
2.03;117.9;28942830
1.83;81.6;522738


import csv
import pandas as pd

df = pd.read_csv('nba.csv', sep= ';')

df.head()


import numpy as np


height_array = np.array(df['height'].to_list())
weight_array = np.array(df['weight'].to_list())
wage_array = np.array(df['wage'].to_list())



import seaborn as sns


with sns.axes_style('whitegrid'):

  grafico = sns.scatterplot(x= weight_array, y= height_array)
  grafico.set(title= "Distribuição de Peso e Altuta dos jogadores da NBA de 2020", xlabel= "Peso (Kg)", ylabel= "Altura (M)");
  


np.corrcoef(weight_array, height_array)

with sns.axes_style('whitegrid'):

  grafico = sns.scatterplot(x= height_array, y= wage_array)
  grafico.set(title= "Distrribuição de Altura e Salario dos jogadores da NBA de 2020", xlabel= "Altuta (m)", ylabel= "Salário (USD)");



