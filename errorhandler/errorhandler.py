import logging
import traceback
import ujson
import datetime

from telegram import InputFile
from config import DEVELOPER_CHAT_ID, BOT_USERNAME

# Setting up logging basic config for standart output
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

# Getting logger
logger = logging.getLogger()


def error_handler(update, context) -> None:
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = ''.join(tb_list)

    # Build the message with some markup and additional information about what happened.
    # You might need to add some logic to deal with messages longer than the 4096 character limit.
    message = (
        f'An exception was raised while handling an update:\n'
        f'{"".ljust(45, "*")}\n'
        f'update = {ujson.dumps(update.to_dict(), indent=4, ensure_ascii=False)}'
        f'\n'
        f'{"".ljust(45, "*")}\n'
        f'context.user_data = {ujson.dumps(context.user_data, indent=4, ensure_ascii=False)}\n'
        f'{"".ljust(45, "*")}\n'
        f'{tb_string}\n'
        f'{"".ljust(45, "*")}\n'
    )

    path = f'/var/www/html/{BOT_USERNAME}/logs/'
    document_name = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + '.txt'
    full_path = path + document_name

    with open(full_path, 'w') as f:
        f.write(message)

    with open(full_path, 'r') as f:
        document = InputFile(f)

    caption = '#newerror 😥'
    # Finally, send the document
    context.bot.send_document(chat_id=DEVELOPER_CHAT_ID, caption=caption, document=document)
