import os
from TTS.api import TTS

# Función para listar las voces disponibles
def listar_voces(ejemplos_dir):
    voces = []
    for archivo in os.listdir(ejemplos_dir):
        if archivo.endswith(".wav"):
            voces.append(archivo)
    return voces

# Main
def main():
    print('\n\n')

    ejemplos_dir = 'examples'
    
    # Mostrar las voces disponibles
    voces_disponibles = listar_voces(ejemplos_dir)
    print('BIENVENIDO! Este programa te permite generar audios basados en el modelo XTTS.')
    print('GUIA DE USO')
    print('1. Crea una carpeta "examples" y una carpeta "output" dentro de la carpeta raíz, es decir, donde esta este archivo.')
    print('2. Dentro de la carpeta examples, añade audios de al menos 6 segundos (a mayor longitud, mejor) de la voz que quieres recrear. Los archivos deben de ser .wav')
    print('3. Abre un cmd dentro de la carpeta raiz y ejecuta "pip install TTS"')
    print('4. Una vez hecho esto, ejecutar generate.py. Si es la primera vez que ejecutas el script, empezará a descargar el modelo. Esto puede tomar algunos minutos.')
    print('5. Una vez descargado el modelo, el program te preguntara que quieres que diga tu audio generado, así como otros parametros, sigue las instrucciones para que empiece la generación de tu audio')
    print('\n')

    #Mostrar las voces disponibles
    print('----------------------------------------------------------')
    print('|                                                        |')
    print("|                Voces disponibles:                      |")
    for idx, voz in enumerate(voces_disponibles, 1):
        print(f"| {str(idx).ljust(2)}. {voz.ljust(50)} |")
    print('|                                                        |')
    print('----------------------------------------------------------')
    print('\n')
    
    # Solicitar datos al usuario
    print("Ingrese el texto que quieres que diga. (E.G. 'Hi, Im sonic the hedgedog')") 
    print("(Puedes copiar y pegar varias líneas. Presiona Enter en una línea vacía para terminar):")
    lineas = []
    while True:
        linea = input()
        if not linea:
            break
        lineas.append(linea)
    texto = "\n".join(lineas)
    idioma = input("Ingrese el idioma (ejemplo: 'en', 'es'): ").strip()
    archivo_salida = input("Ingrese el nombre del archivo de salida (sin extensión): ").strip()
    ejemplo = input(f"Ingrese el archivo de voz de ejemplo (Ejemplo: '{voces_disponibles[0]}'): ").strip()

    # Validar que el archivo de voz de ejemplo está en la lista de voces disponibles
    if ejemplo not in voces_disponibles:
        print(f"Error: El archivo de voz de ejemplo '{ejemplo}' no es válido.")
        return

    # Cargar el modelo TTS
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

    # Ruta del archivo de salida
    archivo_salida_path = f"output/{archivo_salida}.wav"

    # Generar el audio
    tts.tts_to_file(
        text=texto,
        file_path=archivo_salida_path,
        speaker_wav=os.path.join(ejemplos_dir, ejemplo),
        language=idioma
    )

    print(f"Audio generado: {archivo_salida_path}")

if __name__ == "__main__":
    main()
