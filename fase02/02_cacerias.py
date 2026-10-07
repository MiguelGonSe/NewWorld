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

primera_caza_completada = df[df['type'] == 'hunt_completed'].iloc[0]
cazas_completadas = df[df['type'] == 'hunt_completed']

print("\nPRIMERA 'HUNT_COMPLETED' :")
print(primera_caza_completada)

print("'HUNT_COMPLETED' :")
print(cazas_completadas)

# CrEAR TABLA
OUTPUT_DIR = Path('data/processed')

OUTPUT_DIR.mkdir(parents=True, exist_ok=True) #COMPROBACION QUE EXITE

df = pd.read_json(DATASET, lines=True)

def event_table(event_type, columns):
    selected = ['run_id', 'event_index', 'tick', *columns]

    available = [
        column for column in selected
        if column in df.columns
    ] # EVITAMOS ERRORES

    table = df.loc[
        df['type'] == event_type,
        available,
    ] # Filtrar filas y seleccionar columnas.

    if not table.empty:
        # Creamos una nueva columna simulation_day y su valor es la división
        table['simulation_day'] = table['tick'] // 12000

    return table

tables = {
    # NOMBRE PRIMERO Y DESPUES LOS EVENTOS QUE QUIERES GUARDAR
    # PONER EL EVENTO QUE QUIERAS PRIMERO ¡CUIDADO! *** 
    'hunts': event_table('hunt_completed', [
        'type', 'villager_id', 'prey_type',
    ]),
}

for name, table in tables.items():
    # Esto crea la ruta donde se guardará el archivo.
    output = OUTPUT_DIR / f'{name}.csv'

    # convierte el DataFrame en un archivo CSV y lo guarda en output
    # index=False significa que no quieres que Pandas guarde el índice interno del DataFrame.
    # Sin ello, podriamos obtener una salida como: ",amount_before", en lugar de amount_before,
    table.to_csv(output, index=False)

    # Muestra por pantalla el nombre de la tabla y cuántas filas tiene.
    print(name, '->', len(table), 'filas')