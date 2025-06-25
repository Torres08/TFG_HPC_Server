import pandas as pd
import plotly.express as px

# CSV
df = pd.read_csv("Clockify_Time_Report_Detailed_07_09_2024-06_07_2025.csv")

# Convertir fechas y horas a datetime
df['Start'] = pd.to_datetime(df['Start Date'] + ' ' + df['Start Time'], dayfirst=True)
df['End'] = pd.to_datetime(df['End Date'] + ' ' + df['End Time'], dayfirst=True)

# Ajustar las filas donde Start y End son iguales para que End sea Start + 1 hora
same_time = df['Start'] == df['End']
df.loc[same_time, 'End'] = df.loc[same_time, 'Start'] + pd.Timedelta(hours=1)

# Agrupar por día y descripción, sumando la duración total por actividad y día
agg_df = df.copy()
agg_df['Date'] = agg_df['Start'].dt.date
agg_df['Start_hour'] = agg_df['Start'].dt.hour + agg_df['Start'].dt.minute/60 + agg_df['Start'].dt.second/3600
agg_df['End_hour'] = agg_df['End'].dt.hour + agg_df['End'].dt.minute/60 + agg_df['End'].dt.second/3600
agg_df['Duration'] = agg_df['End_hour'] - agg_df['Start_hour']

# Sumar duración por actividad y día
agg = agg_df.groupby(['Date', 'Description'], as_index=False).agg({'Duration': 'sum'})
agg['Start'] = pd.to_datetime(agg['Date'].astype(str) + ' 00:00:00')
agg['End'] = agg['Start'] + pd.to_timedelta(agg['Duration'], unit='h')

# Hacer que las barras sean más largas: sumar una duración mínima (por ejemplo, 4 horas) a cada barra
DURACION_MINIMA = 4  # horas
agg['Duration'] = agg['Duration'].apply(lambda x: max(x, DURACION_MINIMA))
agg['End'] = agg['Start'] + pd.to_timedelta(agg['Duration'], unit='h')

# Crear el diagrama de Gantt agrupado
fig = px.timeline(
    agg,
    x_start="Start",
    x_end="End",
    y="Description",
    color="Description",
    title="Diagrama de Gantt - Actividades TFG (Agrupado por día)"
)

# Justificar el texto de las actividades a la derecha y colores a la izquierda
fig.update_yaxes(autorange="reversed", ticklabelposition="outside right")
fig.update_layout(
    xaxis_title="Fecha",
    yaxis_title="Actividad",
    legend_title="Actividad",
    height=1080,
    width=1920,
    font=dict(size=18),
    margin=dict(l=50, r=350, t=100, b=100),
    yaxis=dict(ticklabelposition="outside right", tickfont=dict(size=18), automargin=True, side="right", anchor="x"),
    showlegend=False,
    plot_bgcolor='white',  # Fondo blanco
    paper_bgcolor='white'  # Fondo del papel blanco
)

import plotly.colors as pc
colors = pc.qualitative.Bold  
for i, d in enumerate(fig.data):
    d.marker.color = colors[i % len(colors)]

fig.write_image("gantt_tfg.png")
