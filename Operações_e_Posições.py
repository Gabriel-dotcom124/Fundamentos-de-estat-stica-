!wget -q "https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/dataset/wage.csv" -O wage.csv


import csv
import pandas as pd
import numpy as np
import seaborn as sns


wage_df = pd.read_csv('wage.csv')
wage_df.head()

wage_array = np.array(wage_df['wage'].astype('int').to_list())
print(wage_array[0:5])


with sns.axes_style('whitegrid'):


  grafico = sns.histplot(data=wage_array, binwidth= 100 * 1000)
  grafico.set(title= "Distribuição de Salário Mensal da NBA em 2020", xlabel= "Salário Mensal em(USD)", ylabel= "contagem");



  np.median(wage_array)


q1 = np.quantile(wage_array, 0.25)
print(q1)

q2 = np.quantile(wage_array, 0.50)
print(q2)

q3 = np.quantile(wage_array, 0.75)
print(q3)


iqr = q3 - q1
print(iqr)


with sns.axes_style('whitegrid'):

  grafico = sns.boxplot(data= wage_array)
  grafico.set(title= "Distribuição de Salário Mensal da NBA em 2020", xlabel= "Salário Mensal em(USD)");


with sns.axes_style('whitegrid'):

  grafico = sns.histplot(data= wage_array, binwidth= 100 * 1000)
  grafico.set(title= "Distribuição de Salário Mensal da NBA em 2020", xlabel= "Salário Mensal em(USD)", ylabel= "contagem");

