from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crear instancia del chatbot
chatbot = ChatBot(
    "MyBot",
    tagger_language=None,  # Esto previene el uso de SpaCy para etiquetado
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///db.sqlite3"
)

# Entrenador
trainer = ChatterBotCorpusTrainer(chatbot)

# Entrenar con el corpus en español
trainer.train("chatterbot.corpus.spanish")

print("🤖 Chatbot entrenado y listo para conversar (en español).")

# Interfaz de chat
while True:
    user_input = input("Tú: ")
    if user_input.lower() in ["salir", "exit"]:
        print("Chatbot: ¡Hasta luego!")
        break
    response = chatbot.get_response(user_input)
    print(f"Chatbot: {response}")
