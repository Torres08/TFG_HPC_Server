# pip install matplotlib seaborn pandas
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

data_tps = {
    'Escenario': ['A1', 'A2', 'B1', 'B2', 'B3', 'C1', 'C2'],
    'deepseek-llm-7b-chat TPS': [1042.91, 1042.29, 1295.58, 996.35, 821.50, 1418.69, 2463.40],
    'deepseek-llm-67b-chat TPS': [32.78, 64.77, 62.11, 47.81, 40.54, 75.30, 121.79]
}
df_tps = pd.DataFrame(data_tps)

data_latencia = {
    'Escenario': ['A1', 'A2', 'B1', 'B2', 'B3', 'C1', 'C2'],
    'deepseek-llm-7b-chat Latencia (ms)': [459.70, 454, 1397, 2758, 5620, 6218, 7174],
    'deepseek-llm-67b-chat Latencia (ms)': [14192, 14359, 28895, 57420, 114578, 117722, 127785]
}
df_latencia = pd.DataFrame(data_latencia)

# Crear carpeta para guardar las imágenes
output_dir = 'figs'
os.makedirs(output_dir, exist_ok=True)

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

plt.figure(figsize=(12, 7))
bar_width = 0.35
index = range(len(df_tps['Escenario']))

plt.bar([i - bar_width/2 for i in index], df_tps['deepseek-llm-7b-chat TPS'], bar_width, label='deepseek-llm-7b-chat', color=sns.color_palette("viridis")[0])
plt.bar([i + bar_width/2 for i in index], df_tps['deepseek-llm-67b-chat TPS'], bar_width, label='deepseek-llm-67b-chat', color=sns.color_palette("viridis")[3])

plt.xlabel('Escenarios de Prueba (Carga de Hilos / Longitud de Respuesta Máx.)')
plt.ylabel('TPS (Tokens por Segundo)')
plt.title('Comparación TPS por Escenario y Modelo')
plt.xticks(index, df_tps['Escenario'])
plt.legend(title='Modelo')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'tps_global.png'), dpi=300)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='Escenario', y='deepseek-llm-67b-chat TPS', data=df_tps, palette='viridis')
plt.xlabel('Escenarios de Prueba (Carga de Hilos / Longitud de Respuesta Máx.)')
plt.ylabel('TPS (Tokens por Segundo)')
plt.title('TPS deepseek-llm-67b-chat')
plt.ylim(0, df_tps['deepseek-llm-67b-chat TPS'].max() * 1.2)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'tps_67b.png'), dpi=300)
plt.show()

plt.figure(figsize=(12, 7))
plt.bar([i - bar_width/2 for i in index], df_latencia['deepseek-llm-7b-chat Latencia (ms)'], bar_width, label='deepseek-llm-7b-chat', color=sns.color_palette("plasma")[0])
plt.bar([i + bar_width/2 for i in index], df_latencia['deepseek-llm-67b-chat Latencia (ms)'], bar_width, label='deepseek-llm-67b-chat', color=sns.color_palette("plasma")[3])

plt.xlabel('Escenarios de Prueba (Carga de Hilos / Longitud de Respuesta Máx.)')
plt.ylabel('Latencia Promedio (ms)')
plt.title('Comparación Latencia por Escenario y Modelo')
plt.xticks(index, df_latencia['Escenario'])
plt.legend(title='Modelo')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'latencia_global.png'), dpi=300)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='Escenario', y='deepseek-llm-7b-chat Latencia (ms)', data=df_latencia, palette='plasma')
plt.xlabel('Escenarios de Prueba (Carga de Hilos / Longitud de Respuesta Máx.)')
plt.ylabel('Latencia Promedio (ms)')
plt.title('Latencia deepseek-llm-7b-chat')
plt.ylim(0, df_latencia['deepseek-llm-7b-chat Latencia (ms)'].max() * 1.2)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'latencia_7b.png'), dpi=300)
plt.show()
