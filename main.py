import configparser
import logging

# import telegram
from telegram import Update
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters, Updater, CallbackContext

# Load data from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Initial Flask app
#app = Flask(__name__)

# Initial bot by Telegram access token
# bot = telegram.Bot(token=(config['TELEGRAM']['ACCESS_TOKEN']))


# @app.route('/hook', methods=['POST'])
# def webhook_handler():
#     """Set route /hook with POST method will trigger this method."""
#     if request.method == "POST":
#         update = telegram.Update.de_json(request.get_json(force=True), bot)

#         # Update dispatcher process that handler to process this message
#         dispatcher.process_update(update)
#     return 'ok'


def reply_handler(update: Update, context: CallbackContext):
    """Reply message."""
    text = update.message.text
    user = update.message.chat.first_name
    replyMsg = "Hello " + user
    update.message.reply_text(replyMsg)


def main() -> None:
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(config['TELEGRAM']['ACCESS_TOKEN'])
    dispatcher = updater.dispatcher
    
    # New a dispatcher for bot
    # dispatcher = Dispatcher(bot, None)

    # Add handler for handling message, there are many kinds of message. For this handler, it particular handle text
    # message.
    dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == "__main__":
    # Running server
    # app.run(debug=True)
    main()

    