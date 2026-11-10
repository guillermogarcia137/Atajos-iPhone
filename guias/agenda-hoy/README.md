# Consultar la agenda de hoy

**Categoría:** Productividad. **Entrega:** guía de montaje manual.

Muestra los eventos del día ordenados por hora.

## Crear en Atajos

Abre Atajos → + → Nuevo atajo y ponle este nombre. Añade las acciones en este
orden. Los nombres pueden variar con el idioma y la versión; se incluye el nombre
en inglés para buscarlas. Selecciona las variables mágicas, no escribas sus nombres
como texto.

1. **Buscar eventos de calendario / Find Calendar Events.** Filtro Fecha de inicio es hoy. Ordena por fecha de inicio, ascendente. Elige tus calendarios.

2. **Repetir con cada elemento / Repeat with Each.** Dentro del bucle, obtén Título y Fecha de inicio del evento.

3. **Dar formato a fecha / Format Date.** Hora corta de cada inicio.

4. **Texto / Text.** Dentro del bucle crea «[hora] · [título]». Fuera del bucle combina los resultados con nuevas líneas.

5. **Mostrar resultado / Show Result.** Muestra el texto combinado; si no hay eventos, indica «Sin eventos» con una condición Si.

## Prueba en tu iPhone

Ejecuta con contenido de prueba. Revisa cada pantalla y el resultado antes de
usarlo con datos reales. Si solicita permisos, comprueba que corresponden a las
acciones descritas. Cancela si aparece una app o una acción distinta.

## Límites y efectos

La búsqueda por fecha de inicio puede omitir eventos que empezaron ayer y continúan hoy. Los eventos privados quedan visibles en el resultado.

Estado: revisado como receta; no ejecutado ni validado en iOS desde este entorno.
No hay enlace de iCloud ni firma de Apple generados.
