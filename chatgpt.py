import openai
import sys

openai.api_key = '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'

historial = []
buffer = []

def obtener_entrada():
    try:

        entrada_usuario = input("Tú: ")

        if entrada_usuario.strip():
            historial.append(entrada_usuario)
        return entrada_usuario
    except KeyboardInterrupt:
        print("\nPrograma interrumpido. Saliendo...")
        sys.exit(1)

def invocar_chat_gpt(entrada_usuario):
    try:

        respuesta = openai.Completion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "user", "content": entrada_usuario}
            ],
            temperature=1,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return respuesta.choices[0].message.content
    except Exception as e:
        print("Se produjo un error al invocar chatGPT:", e)
        return None


def manejar_interaccion():
    try:
        while True:

            entrada_usuario = obtener_entrada()


            if not entrada_usuario:
                print("Por favor, proporciona una entrada válida.")
                continue


            respuesta = invocar_chat_gpt(entrada_usuario)


            if respuesta:
                print("chatGPT:", respuesta)
                buffer.append(respuesta)

    except KeyboardInterrupt:
        print("\nPrograma interrumpido. Saliendo...")
        sys.exit(1)


def modo_conversacion():
    try:
        print("Modo de conversación habilitado. Presiona Ctrl+C para salir del modo de conversación.")
        while True:

            entrada_usuario = obtener_entrada()


            if not entrada_usuario:
                print("Por favor, proporciona una entrada válida.")
                continue

            ultima_consulta = historial[-1] if historial else None

            respuesta = invocar_chat_gpt(ultima_consulta)

            if respuesta:
                print("chatGPT:", respuesta)
                buffer.append(respuesta)

    except KeyboardInterrupt:
        print("\nSaliendo del modo de conversación...")

def principal():
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "--convers":

            modo_conversacion()
        else:

            manejar_interaccion()
    except Exception as e:
        print("Se produjo un error:", e)
        sys.exit(1)

if __name__ == "__main__":
    principal()
