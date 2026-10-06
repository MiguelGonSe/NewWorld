from pathlib import Path
import pandas as pd

DATASET = Path(
    'data/raw/nevworld_2099174182941333158_20261005_182621.jsonl'
)


if not DATASET.exists():
    raise FileNotFoundError(
        f'No se encuentra: {DATASET.resolve()}'
    )

df = pd.read_json(DATASET, lines=True)

required = [
    'run_id', 'event_index', 'tick', 'type'
]

# VALIDACION 

assert not df.empty, 'El dataset está vacío'
assert all(column in df.columns for column in required), \
    'Faltan columnas principales'
assert not df.duplicated(['run_id', 'event_index']).any(), \
    'Hay eventos duplicados'

ordered = df.sort_values('event_index')
assert ordered['tick'].is_monotonic_increasing, \
    'Los ticks retroceden'

print('\nVALIDACIÓN BÁSICA: OK')

#NOMBRE
nombre_archivo = Path(__file__).name
print(nombre_archivo)

filas, columnas = df.shape

#FILAS/COLUMNAS
print('Eventos:', filas)
print('Columnas:', columnas)

#Nombre de las columnas
print('\nNOMBRES DE COLUMNA')
print(df.columns.tolist())

#TIPO PRIMERA FILA 
print('type:', df['type'].iloc[0])

#CANTIDAD PRIMERA FILA 
print(df['type'].value_counts().iloc[0])

#CANTIDAD DEL TIPO
print(df['type'].value_counts())

#PRIMERA FILA
print(df['run_id'].iloc[0])
print(df['seed'].iloc[0])
print(df['schema_version'].iloc[0])

#MAX Y MIN
print('primer tick:', df['tick'].min())
print('último tick:', df['tick'].max())