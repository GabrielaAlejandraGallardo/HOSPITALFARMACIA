<<<<<<< HEAD
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
=======
# TODO - adminFarmacia (farmacia)

- [ ] Fix Django model base class error in `medicamento/models.py` (replace `models.Models` with `models.Model` and correct other obvious field/class issues).
- [ ] Run `python manage.py makemigrations` again and resolve any follow-up migration/model errors.
- [ ] Run `python manage.py migrate` (if makemigrations succeeds) and ensure server startup.
>>>>>>> 2346d110bb51585c67e91c95c716af9be7aba40a

