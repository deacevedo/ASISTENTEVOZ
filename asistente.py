#Importar librerias.
#Libreria para el reconocimiento de voz
import speech_recognition as sr
#Libreria para el controlador web que permite abrir
#documentos de un sistio web
import webbrowser as wb

#Crear la funcion para el asistente virtual
def asistente_personal():
    sr.Microphone(device_index = 0)

    reconocimiento = sr.Recognizer()

    reconocimiento.energy_threshold=1000
    reconocimiento.dynamic_energy_threshold = False

    with sr.Microphone() as source:

        print('Hola Daniel, ¿Qué Necesitas?:')
        #reconocimiento.adjust_for_ambient_noise(source)
        audio = reconocimiento.listen(source)
        try:
            texto = reconocimiento.recognize_google(audio, language='es-EC')
            print(f"Acabas de decir:{texto}?")
            navegador = "https://www.google.com/search?q="
            busqueda = navegador + texto
            wb.open(busqueda) 
        except TimeoutException as msg:
            print(msg)
        except WaitTimeoutError:
            print("El tiempo de escucha se agotó, mientras se esperaba la frase. Adios..")
            quit()
        except LookupError:
            print("Lo siento mucho, no se puede procesar tu solicitud.")
        else: 
            print("Los resultados deben aparecer en tu navegador web")

asistente_personal()