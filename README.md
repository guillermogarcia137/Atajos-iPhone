# Atajos-iPhone

**20 guías útiles para la app Atajos de Apple** y **6 borradores nativos `.shortcut`
sin firmar**. Esta entrega no contiene atajos ya firmados ni enlaces de iCloud.
Las guías se pueden montar manualmente en un iPhone; los archivos nativos necesitan
revisión y firma en un Mac antes de compartirlos para importación.

## Estado de la colección

- Se ha comprobado la estructura plist/XML y que las referencias de los borradores
  apuntan a acciones anteriores del mismo flujo.
- No se han ejecutado en iOS ni firmado con Apple. Una estructura válida no garantiza
  que todos los parámetros sean aceptados por tu versión de Atajos.
- Los nombres de acciones y las opciones cambian con iOS y el idioma. Usa la guía
  como referencia y revisa el editor antes de ejecutar.
- No se desactiva ninguna protección de iOS ni se usan servicios externos de firma.

## Catálogo

| Guía | Categoría | Borrador nativo |
| --- | --- | --- |
| [Leer texto en voz alta](guias/leer-texto/README.md) | Accesibilidad | [Sin firmar](plantillas-sin-firmar/leer-texto.shortcut) |
| [Contar palabras de un texto](guias/contar-palabras/README.md) | Texto | [Sin firmar](plantillas-sin-firmar/contar-palabras.shortcut) |
| [Codificar texto en Base64](guias/texto-base64/README.md) | Texto | [Sin firmar](plantillas-sin-firmar/texto-base64.shortcut) |
| [Decodificar texto Base64](guias/decodificar-base64/README.md) | Texto | [Sin firmar](plantillas-sin-firmar/decodificar-base64.shortcut) |
| [Abrir Calendario](guias/abrir-calendario/README.md) | Productividad | [Sin firmar](plantillas-sin-firmar/abrir-calendario.shortcut) |
| [Recordatorio de salida](guias/lista-salida/README.md) | Vida diaria | [Sin firmar](plantillas-sin-firmar/lista-salida.shortcut) |
| [Convertir imágenes a PDF](guias/imagenes-a-pdf/README.md) | Documentos | Montaje manual |
| [Unir documentos PDF](guias/unir-pdf/README.md) | Documentos | Montaje manual |
| [Crear copias de fotos reducidas](guias/reducir-fotos/README.md) | Imágenes | Montaje manual |
| [Extraer texto de una imagen](guias/extraer-texto-foto/README.md) | Imágenes | Montaje manual |
| [Crear un QR con texto](guias/qr-texto/README.md) | Compartir | Montaje manual |
| [Crear un QR de Wi-Fi](guias/qr-wifi/README.md) | Compartir | Montaje manual |
| [Añadir una tarea con fecha](guias/nueva-tarea/README.md) | Productividad | Montaje manual |
| [Consultar la agenda de hoy](guias/agenda-hoy/README.md) | Productividad | Montaje manual |
| [Guardar dónde has aparcado](guias/guardar-aparcamiento/README.md) | Ubicación | Montaje manual |
| [Consultar tiempo hasta un destino](guias/tiempo-hasta-destino/README.md) | Movilidad | Montaje manual |
| [Añadir un gasto a un CSV](guias/registrar-gasto/README.md) | Finanzas personales | Montaje manual |
| [Registrar un hábito](guias/registro-habitos/README.md) | Vida diaria | Montaje manual |
| [Vaciar el portapapeles](guias/limpiar-portapapeles/README.md) | Privacidad | Montaje manual |
| [Menú de accesos para el día](guias/menu-diario/README.md) | Productividad | Montaje manual |

## Usar las guías en un iPhone

1. Abre la guía y crea un atajo nuevo con el mismo nombre.
2. Añade las acciones en el orden indicado y selecciona sus variables mágicas.
3. Prueba con datos sintéticos. Revisa los permisos de Fotos, Ubicación, Notas,
   Calendario, Recordatorios o Archivos solo cuando la guía los necesite.
4. Si funciona, puedes compartirlo desde Atajos para obtener tu propio enlace de
   iCloud. No publiques datos personales ni credenciales dentro del flujo.

## Revisar y firmar los borradores con un Mac

En macOS con la utilidad `shortcuts`, firma una copia de un borrador. El modo
`anyone` permite compartir esa copia sin limitarla a tus contactos:

```console
mkdir firmados
shortcuts sign --mode anyone --input plantillas-sin-firmar/lista-salida.shortcut --output firmados/lista-salida.shortcut
```

Si la herramienta rechaza el formato o un parámetro, no intentes saltarte la
validación: crea el atajo con la guía en el editor de Atajos y expórtalo desde allí.
Abre la copia firmada en Atajos, inspecciona todas las acciones y pruébala antes de
compartir. La firma no demuestra que una automatización sea correcta o segura.
No se ha podido comprobar este proceso en un Mac desde el entorno Linux de trabajo.

## Alcance

La colección está orientada a versiones recientes de iOS; la disponibilidad exacta
debe comprobarse en tu dispositivo. Añadir a pantalla de inicio o al botón Acción
es opcional; este último requiere un iPhone compatible. No se crean automatizaciones
personales, no se envían mensajes ni se borran fotos automáticamente. Algunas guías
sí crean archivos, notas o recordatorios cuando tú las ejecutas.

## Comprobaciones reproducibles

`python3 tests/validar.py` valida los seis plist, las veinte guías y los enlaces del
catálogo. No necesita paquetes externos y no ejecuta acciones de Apple.
