# TODO - Fix alta_agentes returning None

- [ ] Revisar `agente/views.py` para encontrar por qué `alta_agentes` retorna `None` (no retorna HttpResponse en GET o si falla la validación).
- [ ] Implementar un `return render(...)` en todos los caminos (GET y POST inválido).
- [ ] Opcional: eliminar/evitar consultas innecesarias (`Agente.objects.all()`) en `alta_agentes`.
- [ ] Ejecutar el servidor / chequear el endpoint `GET /alta_agentes/`.

