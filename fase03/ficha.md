| Pregunta | Tabla y columnas necesarias | Operación y motivo |
| --- | --- | --- |
| ¿Cuántas cacerías completadas se registraron? | hunt_completed 22 | hunts_counts = hunts['type'].value_counts() (Cuentas el tipo) |
| ¿Cuántas corresponden a cada tipo de presa? | deer 19, sheep 3 | hunts_counts_type = hunts['prey_type'].value_counts() |
| ¿Qué porcentaje representa cada presa? | deer 86.4, sheep 13.6| hunts_proportions = hunts['prey_type'].value_counts(normalize=True)
hunts_percent = (hunts_proportions * 100).round(1) |
| ¿Cuántas cacerías se registraron en cada día observado? | 0-5, 4-3, 11-3, 12-2, 13-6, 14-2, 15-1 | hunts_counts_simulation_day = hunts['simulation_day'].value_counts().sort_index() |
| ¿Cuánto aumentó, disminuyó y cambió en términos netos la comida? | Balance: 164.0, Incrementos: 364.0, Reducciones: 200.0 | resource_balance = food['amount_delta'].sum(), gains = food[food['amount_delta'] > 0], spending = food[food['amount_delta'] < 0].copy()|


1. ¿Qué presa o presas tienen el mayor recuento? Si hay empate, indícalo; si no hay datos, explica por qué no puedes responder.
Es Deer con 19. 
2. ¿El porcentaje de una presa representa porcentaje de cacerías, de aldeanos o de tiempo? Justifica el denominador.
El porcentaje de una presa representa el numero de veces que se ha cazado esa presa entre el total de cazas de todas las presas
3. ¿El día con más cacerías fue necesariamente el día en que se dedicó más tiempo a cazar?
No, fue el dia que mas efectividad se tuvo, pero no tiene porque ser el dia que mas presas se cazó
4. ¿El balance neto indica las existencias finales de comida? ¿Qué información faltaría?
El balance neto significa las existencias que quedan, faltaría la que necesitas para pasar el dia a dia 
5. ¿Puedes demostrar que todos los incrementos de comida se deben a la caza? ¿Qué vínculo entre eventos necesitarías para justificarlo?
Se puede demostrar con la variable food_change_events, y ver si todos son por el type hunts.