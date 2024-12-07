from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import re

# Votre token
TOKEN = '7763513088:AAHQRX12heO5Yv3w-PMuNpaETb1eZ2SCD5A'

async def start(update: Update, context: CallbackContext) -> None:
    print("Commande /start reçue.")  # Ajout d'un message pour savoir si /start est appelé
    await update.message.reply_text('Bonjour! Je suis votre bot.')

async def respond_to_where(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text.lower()  # On met tout en minuscule pour éviter la casse
    
    print(f"Message reçu: {update.message.text}")  # Affiche le texte du message dans la console
    
    # Vérification de "c'est où"
    if "c'est où" in message_text:
        print("La phrase contient 'c'est où'.")
        await update.message.reply_text("À Montélimar")
    # Vérification de "où" comme dernier mot de la phrase
    elif message_text.endswith(" où"):
        print("Le mot 'où' est le dernier mot de la phrase.")
        await update.message.reply_text("À Montélimar")

def main() -> None:
    print("Démarrage du bot...")  # Ajoutez cette ligne pour confirmer que le bot démarre
    # Créez l'application et passez le token
    application = Application.builder().token(TOKEN).build()

    # Ajoutez les gestionnaires de commandes et de messages
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond_to_where))

    # Démarre le bot
    print("Lancement du polling...")  # Ligne pour confirmer que nous passons à l'étape suivante
    application.run_polling()

if __name__ == '__main__':
    main()
