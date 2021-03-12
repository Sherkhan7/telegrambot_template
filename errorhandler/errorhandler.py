from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from config import DEVELOPER_CHAT_ID

import logging
import traceback
import html
import json

# Setting up logging basic config for standart output
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

# Getting logger
logger = logging.getLogger()


def error_handler(update: Update, context: CallbackContext):
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
        f'<pre>update = {html.escape(json.dumps(update.to_dict(), indent=4, ensure_ascii=False))}'
        f'</pre>\n'
        f'{"".ljust(45, "*")}\n'
        # f'<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n'
        # f'{"".ljust(45, "*")}\n'
        f'<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n'
        f'{"".ljust(45, "*")}\n'
        f'<pre>{html.escape(tb_string)}</pre>\n'
        f'{"".ljust(45, "*")}\n'
    )

    # Finally, send the message
    context.bot.send_message(chat_id=DEVELOPER_CHAT_ID, text=message, parse_mode=ParseMode.HTML)
