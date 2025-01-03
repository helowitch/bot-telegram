from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import re

# Votre token
TOKEN = '7763513088:AAHQRX12heO5Yv3w-PMuNpaETb1eZ2SCD5A'

async def start(update: Update, context: CallbackContext) -> None:
    print("Commande /start reçue.")  # Ajout d'un message pour savoir si /start est appelé
    await update.message.reply_text('Bonjour! Je suis votre bot.')

async def respond_to_where(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.message.text:  # Vérifie que le message existe et est du texte
        message_text = update.message.text.lower()  # On met tout en minuscule pour éviter la casse
        if message_text.endswith("où") or message_text == "c'est où":
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
