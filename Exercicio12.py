!wget -q "https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/develop/dataset/traffic.csv" -O traffic.csv


import pandas as pd

df = pd.read_csv("traffic.csv", sep= ";")


df.head()

df.iloc[[13]]


import numpy as np


incident_columns = df.columns.drop(['hour', 'slowness_traffic_%'])


for col in incident_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)


df['total_incidents'] = df[incident_columns].sum(axis=1)


num_days = len(df) // 27


df_full_days = df.head(num_days * 27)


daily_incident_arrays = df_full_days['total_incidents'].values.reshape(num_days, 27)


daily_incident_arrays = daily_incident_arrays[:, 1:-1]


display(daily_incident_arrays)



daily_incident_means = np.mean(daily_incident_arrays, axis=1)


display(daily_incident_means)



daily_incident_stds = np.std(daily_incident_arrays, axis=1)


display(daily_incident_stds)



Qual dia apresenta a maior média de acidentes por meia hora?
resposta: dia 16
Qual dia apresenta a menor variação de acidentes por meia hora?
resposta: dia 14


