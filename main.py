from telegram.ext import Updater, PicklePersistence

from config import TOKEN, SERVER_IP, PORT, URL
from errorhandler import error_handler
from handlers import (
    message_handler,
    callback_query_handler,
    registration_conversation_handler,
    command_handler
)


def main():
    my_persistence = PicklePersistence(filename='my_pickle', single_file=False, store_chat_data=False)

    updater = Updater(TOKEN, persistence=my_persistence)

    updater.dispatcher.add_handler(command_handler)

    updater.dispatcher.add_handler(registration_conversation_handler)

    updater.dispatcher.add_handler(message_handler)

    updater.dispatcher.add_handler(callback_query_handler)

    # ...and the error handler
    updater.dispatcher.add_error_handler(error_handler)

    # updater.start_polling()
    # updater.idle()

    updater.start_webhook(port=PORT, url_path=TOKEN, webhook_url=URL + TOKEN, ip_address=SERVER_IP)
    updater.idle()


if __name__ == '__main__':
    main()
