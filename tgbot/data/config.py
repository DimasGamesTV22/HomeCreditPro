# - *- coding: utf- 8 - *-
import configparser

read_config = configparser.ConfigParser()
read_config.read('settings.ini')

BOT_TOKEN = read_config['settings']['token'].strip()  # Токен бота
PATH_DATABASE = 'tgbot/data/database.db'  # Путь к БД
PATH_LOGS = 'tgbot/data/logs.log'  # Путь к Логам
BOT_VERSION = '3.1'

# Получение администраторов бота
def get_admins():
    read_admins = configparser.ConfigParser()
    read_admins.read('settings.ini')

    admins = read_admins['settings']['admin_id'].strip()
    admins = admins.replace(' ', '')

    if ',' in admins:
        admins = admins.split(',')
    else:
        if len(admins) >= 1:
            admins = [admins]
        else:
            admins = []

    while '' in admins: admins.remove('')
    while ' ' in admins: admins.remove(' ')
    while '\r' in admins: admins.remove('\r')

    admins = list(map(int, admins))

    return admins


# УДАЛИШЬ ИЛИ ИЗМЕНИШЬ ССЫЛКИ НА ДОНАТ, КАНАЛ И ТЕМУ БОТА - КАСТРИРУЮ БЛЯТЬ
BOT_DESCRIPTION = f'<b>⚜ Bot Version: <code>{BOT_VERSION}</code>\n' \
                  f'🔗 Topic Link: <a href="https://lolz.guru/threads/1888814">Click me</a>\n' \
                  f'♻ Bot created by @djimbox\n' \
                  f'🍩 Donate to the author: <a href="https://qiwi.com/n/DJIMBO">Click me</a>\n' \
                  f'🤖 Bot channel [NEWS | UPDATES]: <a href="https://t.me/djimbo_shop">Click me</a></b>'
