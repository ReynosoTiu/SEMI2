import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_file = 'datos.csv'
df = pd.read_csv(csv_file)

df = df.dropna()
df = df.drop_duplicates()

df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Duration'] = df['Duration'].astype(str)
df['Duration'] = df['Duration'].str.extract('(\d+)').astype(float)
df['Review'] = df['Review'].astype(str)
df['Review'] = df['Review'].str.extract('(\d+)').astype(float)


plt.figure(figsize=(8,6))
df['Level'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Número de cursos por nivel de dificultad')
plt.xlabel('Nivel de dificultad')
plt.ylabel('Número de cursos')
plt.gca().yaxis.set_tick_params(labelcolor='darkblue')
plt.gca().xaxis.set_tick_params(labelcolor='#1f77b4') 
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

