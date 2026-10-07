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

print("\nPRIMERA LÍNEA CON TYPE 'HUNT_COMPLETED':")
print(primera_caza_completada)
