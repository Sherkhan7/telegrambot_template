from DB import get_user


def set_user_data(user_id, user_data):
    value = user_data.setdefault('user_data', None)

    if not value:
        value = get_user(user_id)

        if value:
            value.pop('created_at')
            value.pop('updated_at')

        user_data['user_data'] = value


def wrap_tags(*args):
    symbol = ' ' if len(args) > 1 else ''

    return f'<b><i><u>{symbol.join(args)}</u></i></b>'
