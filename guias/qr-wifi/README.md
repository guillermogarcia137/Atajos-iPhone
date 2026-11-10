# Crear un QR de Wi-Fi

**Categoría:** Compartir. **Entrega:** guía de montaje manual.

Construye un QR para una red WPA/WPA2 personal.

## Crear en Atajos

Abre Atajos → + → Nuevo atajo y ponle este nombre. Añade las acciones en este
orden. Los nombres pueden variar con el idioma y la versión; se incluye el nombre
en inglés para buscarlas. Selecciona las variables mágicas, no escribas sus nombres
como texto.

1. **Solicitar entrada / Ask for Input.** Pide SSID de la red; guarda como variable SSID.

2. **Solicitar entrada / Ask for Input.** Pide contraseña; guarda como variable Clave. Será visible durante la edición.

3. **Reemplazar texto / Replace Text.** En ambas variables, escapa primero cada barra inversa como dos barras inversas; después antepone una barra inversa a ; , : y comillas dobles. Usa reemplazos literales, no expresiones regulares.

4. **Texto / Text.** Construye WIFI:T:WPA;S:[SSID escapado];P:[Clave escapada];H:false;; insertando las variables, sin los corchetes.

5. **Generar código QR / Generate QR Code.** Usa el texto WIFI anterior.

6. **Vista rápida / Quick Look.** Prueba con un dispositivo de confianza antes de imprimir o compartir.

## Prueba en tu iPhone

Ejecuta con contenido de prueba. Revisa cada pantalla y el resultado antes de
usarlo con datos reales. Si solicita permisos, comprueba que corresponden a las
acciones descritas. Cancela si aparece una app o una acción distinta.

## Límites y efectos

No cubre redes empresariales ni WPA3 exclusivamente. El QR contiene la contraseña. No guardes un valor real como texto fijo en un atajo que vayas a publicar.

Estado: revisado como receta; no ejecutado ni validado en iOS desde este entorno.
No hay enlace de iCloud ni firma de Apple generados.
