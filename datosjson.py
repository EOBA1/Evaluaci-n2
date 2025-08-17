import json # Importamos la librería json para trabajar con archivos JSON
import datetime # Importamos la librería datetime para trabajar con fechas y horas

# --- 1. Definir la ruta del archivo JSON ---
# Asegúrate de que 'myfile.json' esté en la misma ubicación que tu script,
# o proporciona la ruta completa al archivo si está en otra carpeta.
nombre_archivo_json = 'myfile.json'

# --- 2. Abrir el archivo JSON y cargarlo ---
try:
    with open(nombre_archivo_json, 'r') as json_file:
        # json_file es la variable que establece la conexión con el archivo.
        # 'r' significa que abrimos el archivo en modo lectura.

        # Utilizamos json.load para cargar el contenido del archivo JSON
        # en una variable de Python. Ahora 'ourjson' es un diccionario de Python.
        ourjson = json.load(json_file)
    print(f"Archivo '{nombre_archivo_json}' cargado exitosamente.\n")

    # --- 3. Extraer e imprimir la información del token y su expiración ---
    # Asumimos que la información del token y su expiración está en las claves 'token' y 'expires_in'.
    # Si las claves en tu JSON tienen nombres diferentes, deberás cambiarlas aquí.

    # Obtener el valor del token
    token_valor = ourjson.get('token')
    if token_valor:
        print(f"Valor del Token: {token_valor}")
    else:
        print("La clave 'token' no se encontró en el archivo JSON.")

    # Obtener el tiempo de expiración
    tiempo_expiracion_segundos = ourjson.get('expires_in')
    if tiempo_expiracion_segundos is not None:
        try:
            # Convertimos el tiempo de expiración a un número entero
            tiempo_expiracion_segundos = int(tiempo_expiracion_segundos)

            # Calculamos la fecha y hora de expiración
            # Esto asume que 'expires_in' son segundos desde el momento de la emisión del token.
            # Para mayor precisión, si el JSON tiene un timestamp de emisión, se usaría.
            # Aquí, simplemente mostraremos los segundos que quedan.
            print(f"Tiempo restante antes de que caduque el Token: {tiempo_expiracion_segundos} segundos")

            # Opcional: Si quieres calcular la hora exacta de expiración desde ahora:
            # Puedes usar datetime.timedelta para sumar los segundos a la hora actual.
            # hora_actual = datetime.datetime.now()
            # hora_expiracion = hora_actual + datetime.timedelta(seconds=tiempo_expiracion_segundos)
            # print(f"El token caducará aproximadamente a las: {hora_expiracion.strftime('%Y-%m-%d %H:%M:%S')}")

        except ValueError:
            print("La clave 'expires_in' no contiene un valor numérico válido.")
    else:
        print("La clave 'expires_in' no se encontró en el archivo JSON.")

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo_json}' no se encontró en la ruta especificada.")
except json.JSONDecodeError:
    print(f"Error: No se pudo decodificar el archivo '{nombre_archivo_json}'. Asegúrate de que es un JSON válido.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")