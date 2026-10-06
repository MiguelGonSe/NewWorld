| Dato de mi partida | Resultado |
| --- | --- |
| Nombre del archivo JSONL | 01_radiografia.py |
| Número total de eventos | 7253 |
| Número de columnas | 37 |
| Nombres de las columnas | ['schema_version', 'run_id', 'seed', 'event_index', 'tick', 'type', 'started_at_utc', 'building_id', 'building_type', 'cell_x', 'cell_y', 'width', 'height', 'villager_id', 'activity', 'resource_type', 'amount_before', 'amount_after', 'amount_delta', 'population', 'constructed_buildings', 'wood_stock', 'food_stock', 'gold_stock', 'day', 'prey_type', 'actor_id', 'target_id', 'interaction_type', 'topic', 'relationship_actor_to_target_after', 'relationship_target_to_actor_after', 'need_type', 'state', 'name', 'age', 'cause'] |
| Tipo del primer evento registrado | simulation_started |
| Tipo de evento más frecuente y cantidad | villager_activity_changed, 5004 |
| Recuento de todos los tipos de evento |['villager_activity_changed: 5004', 'villager_need_changed: 608', 'world_snapshot: 465', 'resource_changed: 424', 'social_interaction: 346', 'villager_drank: 117', 'construction_abandoned: 113', 'villager_ate: 90', 'construction_expired: 33', 'building_created: 24', 'hunt_completed: 22', 'villager_created: 4', 'simulation_started: 1', 'age_changed: 1', 'villager_died: 1']|
| `run_id`, semilla y versión del esquema de la primera fila |20261005_182621_2099174182941333158_9efcc5b978e44b9ab52ec01820f5931e, 2099174182941333158, 2 |
| Tick mínimo y tick máximo |0 , 279074 |
| Resultado de las validaciones | VALIDACIÓN BÁSICA: OK |

1. ¿Qué te permite afirmar el recuento sobre tu partida? El análisis de los eventos ¿Por qué el tipo más frecuente no tiene que ser el más importante? El tipo más frecuente es el que más se produce, no el más importante.
2. ¿Por qué una celda vacía no significa necesariamente que el registro esté mal? Significa que no se ha producido ese evento, no que esté mal.
3. ¿Qué sabes ahora del archivo y qué pregunta sobre tu partida necesitaría un análisis posterior? Conozco los eventos, los posibles que se pueden producir y sus respectivas cantidades. Y la pregunta sería : ¿Porqué se produce este evento más que el otro? / ¿Debido a que evento se produce el otro?