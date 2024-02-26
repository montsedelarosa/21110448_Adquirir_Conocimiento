class BaseConocimiento:
    def __init__(self):
        self.conocimiento = {
            "Hola Chat": "¡Hola! ¿En qué puedo ayudarte?",
            "¿Cómo estás?": "Estoy bien, gracias por preguntar. ¿Y tú?",
            "¿De qué te gustaría hablar?": "Podemos hablar de muchos temas interesantes. ¿Hay algo en particular que te interese?",
            "¿Cuál es el animal más grande del mundo?": "El animal más grande el mundo es la ballena azul, midiendo hasta 29 metros de largo!. ¿Tienes otra pregunta?",
            "¿Cuál es el planeta más lejano al sol?": "Neptuno, Está más de 30 veces más lejos del Sol que la Tierra. ¿Otra pregunta :)?",
            "¿Qué animal tiene la piel con rayas negras y blancas?": "Fácil! La cebra de montaña. ¿Te gustaría saber dónde viven las cebras?",
            "Si": "Viven en  África meridional (Namibia y Sudáfrica).",
        }

    def obtener_respuesta(self, mensaje):
        if mensaje in self.conocimiento:
            return self.conocimiento[mensaje]
        else:
            respuesta_nueva = input("Lo siento, no conozco esa respuesta. ¿Cuál sería la respuesta adecuada a esta pregunta? ")
            self.actualizar_conocimiento(mensaje, respuesta_nueva)
            return "Gracias por enseñarme algo nuevo."

    def actualizar_conocimiento(self, pregunta, respuesta):
        self.conocimiento[pregunta] = respuesta


def mostrar_menu():
    print("1. Hola Chat")
    print("2. Cómo estás")
    print("3. ¿De qué te gustaría hablar?")
    print("4. ¿Cuál es el animal más grande del mundo?")
    print("5. ¿Cuál es el planeta más lejano al sol?")
    print("6. ¿Qué animal tiene la piel con rayas negras y blancas?")
    print("7. Si")
    print("8. Hacer una pregunta personalizada")
    print("9. Salir")
    


base_de_conocimiento = BaseConocimiento()

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("Bot:", base_de_conocimiento.obtener_respuesta("Hola Chat"))
    elif opcion == "2":
        print("Bot:", base_de_conocimiento.obtener_respuesta("¿Cómo estás?"))
    elif opcion == "3":
        print("Bot:", base_de_conocimiento.obtener_respuesta("¿De qué te gustaría hablar?"))
    elif opcion == "4":
        print("Bot:", base_de_conocimiento.obtener_respuesta("¿Cuál es el animal más grande del mundo?"))
    elif opcion == "5":
        print("Bot:", base_de_conocimiento.obtener_respuesta("¿Cuál es el planeta más lejano al sol?"))
    elif opcion == "6":
        print("Bot:", base_de_conocimiento.obtener_respuesta("¿Qué animal tiene la piel con rayas negras y blancas?"))  
    elif opcion == "7":
        print("Bot:", base_de_conocimiento.obtener_respuesta("Si"))   
    elif opcion == "8":
        pregunta_personalizada = input("Ingresa tu pregunta: ")
        print("Bot:", base_de_conocimiento.obtener_respuesta(pregunta_personalizada))  
    elif opcion == "9":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

