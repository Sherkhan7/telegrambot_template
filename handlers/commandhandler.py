from telegram.ext import Filters, CallbackContext, CommandHandler
from telegram import Update

import json


def do_command(update: Update, context: CallbackContext):
    # with open('jsons/update.json', 'w') as update_file:
    #     update_file.write(update.to_json())
    full_text = update.message.text.split()
    persistence = context.dispatcher.persistence

    if len(full_text) == 2:
        command = full_text[0]
        user_id = int(full_text[-1])

        if command == '/getuserdata':
            user_data = persistence.get_user_data()[user_id]

            if user_data:
                text = json.dumps(user_data, indent=3, ensure_ascii=False)
            else:
                text = 'user_tg_id topilmadi !\n' \
                       f'Tip: {command} user_tg_id'

            text = f'<pre>{text}</pre>'
            update.message.reply_html(text)

    elif len(full_text) == 3:
        command = full_text[0]
        user_id = int(full_text[1])
        conversation_name = full_text[-1]

        if command == '/getuserstate':
            conversation_data = persistence.get_conversations(conversation_name)

            if conversation_data and (user_id, user_id) in conversation_data:
                state = conversation_data[(user_id, user_id)]
            else:
                state = 'user_tg_id yoki conversation_name xato !\n' \
                        f'Tip: {command} user_tg_id conversation_name'

            state = f'<pre>State: {state}</pre>'

            update.message.reply_html(state)

    elif len(full_text) == 4:
        command = full_text[0]
        user_id = int(full_text[1])
        conversation_name = full_text[2]
        new_state = full_text[-1]

        if command == '/updateuserstate':
            conversation_data = persistence.get_conversations(conversation_name)

            if conversation_data and (user_id, user_id) in conversation_data:
                new_state = None if new_state.lower() == 'none' else new_state
                persistence.update_conversation(conversation_name, (user_id, user_id), new_state)
                text = f"[{user_id}], [{conversation_name}] bo'yicha [{new_state}] holatiga o'zgartirildi !"
            else:
                text = 'user_tg_id yoki conversation_name xato !\n' \
                       f'Tip: {command} user_tg_id conversation_name new_state'

            text = f'<pre>{text}</pre>'

            update.message.reply_html(text)


command_handler = CommandHandler(['getuserdata', 'getuserstate', 'updateuserstate'], do_command,
                                 filters=~Filters.update.edited_message)
