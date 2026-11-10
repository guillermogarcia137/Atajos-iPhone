# Añadir un gasto a un CSV

**Categoría:** Finanzas personales. **Entrega:** guía de montaje manual.

Añade una línea a un archivo CSV de gastos elegido por ti.

## Crear en Atajos

Abre Atajos → + → Nuevo atajo y ponle este nombre. Añade las acciones en este
orden. Los nombres pueden variar con el idioma y la versión; se incluye el nombre
en inglés para buscarlas. Selecciona las variables mágicas, no escribas sus nombres
como texto.

1. **Seleccionar archivo / Select File.** Elige un CSV creado previamente con cabecera fecha;concepto;importe.

2. **Solicitar entrada / Ask for Input.** Pide concepto. Sustituye saltos de línea por espacios y cada comilla doble por dos comillas.

3. **Solicitar entrada / Ask for Input.** Pide importe como número positivo; revisa el formato decimal.

4. **Fecha actual / Current Date.** Formato personalizado yyyy-MM-dd.

5. **Texto / Text.** Construye [fecha];"[concepto escapado]";[importe]. Inserta variables, no corchetes literales.

6. **Añadir a archivo de texto / Append to Text File.** Archivo: el CSV seleccionado. Añade una nueva línea.

7. **Mostrar resultado / Show Result.** Confirma el registro y abre el CSV durante la prueba inicial.

## Prueba en tu iPhone

Ejecuta con contenido de prueba. Revisa cada pantalla y el resultado antes de
usarlo con datos reales. Si solicita permisos, comprueba que corresponden a las
acciones descritas. Cancela si aparece una app o una acción distinta.

## Límites y efectos

La acción Añadir a archivo de texto puede variar según proveedor de Archivos; si no aparece, usa una nota en lugar de prometer un CSV. No es contabilidad fiscal. Importa conceptos como texto en hojas de cálculo para evitar fórmulas.

Estado: revisado como receta; no ejecutado ni validado en iOS desde este entorno.
No hay enlace de iCloud ni firma de Apple generados.
