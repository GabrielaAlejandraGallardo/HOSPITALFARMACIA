# TODO

## Fase 1: Análisis
- [x] Identificar el error TypeError por kwargs no soportados en `Agente()`.
- [x] Ver `Agente` en `AdminFarmacia/agente/models.py` vs campos usados en `agente/views.py` y templates.

## Fase 2: Plan de corrección
- [ ] Actualizar `AdminFarmacia/agente/models.py` para incluir `telefono`, `direccion` y `id_deposito`.
- [ ] Crear migraciones y aplicar con `makemigrations` y `migrate`.

## Fase 3: Validación
- [ ] Probar POST `/alta_agentes/`.
- [ ] Probar POST `/modificaciones_agentes/<id>/`.

