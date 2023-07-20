msg_on_start_new = 'Hello, it\'s a bot for tracking your dreams. You can add new dream, see your history of dream or statistic. How can I call you?'


def msg_on_start_old(name):
    return f'Hello, {name}. You can see list of commands on the palette or if you use /help.'

def msg_on_name(name):
    return f'Ok, {name}. Tap on your palette or use /help to see list of commands.'

msg_on_help = 'Available commands: \n/add - Let you add new dream. \n/history - Shows your numbered dream. \n' \
              '/statistic - Shows your statistic.\n/rename - Let you choose new name.\n' \
              '/delete - Deletes your last dream.\n/clear - Clears full your history of dreams.\n' \
              '/cancel - Cancels all actions.\n/help - Show list of commands again.\n' \
              'Call some to see information about this command.'


def msg_on_empty_handler(name):
    return f'Sorry, {name}, I can\'t answer you, please use commands. Type /help to see list.'

def msg_on_adding_1(name):
    return f'Good, {name},you need to come up with name for your dream.'

msg_on_adding_2 = 'Then choose type of your dream.'

msg_on_adding_3 = 'Please type me details about your dream.'

def msg_on_adding_4(name):
    return f'Ok, {name}, all is done.'

msg_on_deleting = 'Are you sure that you want delete your last dream? (yes to confirm)'

def msg_after_deleting(name):
    return f'Ok, {name}, deleting is done.'

def msg_delete_denied(name):
    return f'Ok, {name}, deleting canceled.'

msg_on_clear = 'Are you sure that you want clear full history of your dreams? (yes to confirm)'

def msg_after_clear(name):
    return f'Ok, {name}, clearing is done.'

def msg_clear_denied(name):
    return f'Ok, {name}, clearing canceled.'

msg_on_rename = 'How can I call you?'

def msg_on_history(page, number_of_pages, dreams):
    response = f'I show you {page}/{number_of_pages} page, choose one dream to see it\'s type and description. Type it\'s number.\n'
    for dream in dreams:
        response += f'{dream["number"]}. {dream["name"]}\n'
    return response

msg_if_smt_wrong = 'Sorry, but your actions are wrong. Please, follow instructions.\n'

msg_if_no_dreams = 'You don\'t have any dreams now.'

def msg_send_dream(name, dream_type, description):
    response = f'Name: {name}\n'
    response += f'Type: {dream_type}\n'
    response += f'Description: {description}\n'
    return response

msg_choosing_page_error = 'Don\'t press it again'

msg_on_cancel = 'You canceled all actions. Now you can call standard commands'

msg_on_wrong_number = 'You don\'t have a dream with this number'
