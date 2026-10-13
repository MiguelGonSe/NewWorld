from pathlib import Path

import pandas as pd

DATA_DIR = Path('data/processed')
REPORTS_DIR = Path('reports')
REPORTS_DIR.mkdir(exist_ok=True)

hunts = pd.read_csv(DATA_DIR / 'hunts.csv')
resources = pd.read_csv(DATA_DIR / 'resources.csv')

hunts_counts_type = hunts['prey_type'].value_counts()
hunts_counts = hunts['type'].value_counts()

hunts_proportions = hunts['prey_type'].value_counts(normalize=True)
hunts_percent = (hunts_proportions * 100).round(1)

hunts_counts_simulation_day = hunts['simulation_day'].value_counts().sort_index()


print('\nCAZAS REGISTRADAS: ')
print(hunts_counts)
print('\nTIPOS DE CAZA REGISTRADAS: ')
print(hunts_counts_type)
print('\nPORCENTAJES')
print(hunts_percent)
print('\nCAZAS POR DIA')
print(hunts_counts_simulation_day)

# Filtra las filas de `resources` cuyo `resource_type` sea `food
food = resources[resources['resource_type'] == 'food']

resource_balance = food['amount_delta'].sum()
print(resource_balance)

# INCREMENTOS REGISTRADOS
gains = food[food['amount_delta'] > 0]
print('\nINCREMENTOS REGISTRADOS')
print(gains['amount_delta'].sum())

# REDUCCIONES REGISTRADAS
spending = food[food['amount_delta'] < 0].copy()
spending['amount_delta'] = spending['amount_delta'].abs()

print('\nREDUCCIONES REGISTRADAS')
print(spending['amount_delta'].sum())

# COMPROBACIONES CON ASSERT

# La suma de las cazas por tipo de presa coincide con el total de cacerías
assert hunts_counts_type.sum() == len(hunts)
# La suma de las cazas por día coincide con el total de cacerías
assert hunts_counts_simulation_day.sum() == len(hunts)
# Los incrementos menos las reducciones coinciden con el balance neto de comida
food_gains = gains['amount_delta'].sum()
food_reductions = spending['amount_delta'].sum()
food_balance = resource_balance

assert food_gains - food_reductions == food_balance

print("\nTodas las comprobaciones se han superado correctamente.")

food_change_events = len(food)

#| `hunt_events` | Total de cacerías completadas registradas |
#| `food_change_events` | Número de eventos de cambio de comida |
#| `food_gains` | Incrementos de comida registrados |
#| `food_reductions` | Reducciones de comida, como cantidad positiva |
#| `food_net_change` | Balance neto de comida |

summary = pd.DataFrame([
    {'metric': 'hunt_events', 'value': len(hunts)},
    {'metric': 'food_change_events', 'value': food_change_events},
    {'metric': 'food_gains', 'value': food_gains},
    {'metric': 'food_reductions', 'value': food_reductions},
    {'metric': 'food_net_change', 'value': food_balance},
])

summary.to_csv(REPORTS_DIR / 'hunting_summary.csv', index=False)