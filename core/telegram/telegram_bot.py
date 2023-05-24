import requests
from typing import Union
from pathlib import Path

import config
import logging

logger = logging.getLogger(config.LOGGER_NAME)


def send_message_text(message: str):
    logger.debug("telegram_bot.send_message(): %s", message)

    bot_token = config.BOT_TOKEN
    user_id = config.CHAT_ID

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': user_id,
        'text': message
    }
    response = requests.post(url, data=params)

    if response.status_code == 200:
        logger.info('telegram_bot.send_message(): Message sent successfully')
    else:
        logger.error('telegram_bot.send_message(): Failed to send message')


#TODO test it
def send_message_video(video: Union[str, Path]):
    logger.debug("telegram_bot.send_message_video(): %s", video)

    bot_token = config.BOT_TOKEN
    user_id = config.CHAT_ID

    url = f'https://api.telegram.org/bot{bot_token}/sendVideo'
    params = {
        'chat_id': user_id
    }

    with open(video, 'rb') as f:
        response = requests.post(url, data=params, files={'video': f})

    if response.status_code == 200:
        logger.info('telegram_bot.send_message_video(): Video message sent successfully')
    else:
        logger.error('telegram_bot.send_message_video(): Failed to send video message')



def send_message_document(file: Union[str, Path]):
    logger.debug("telegram_bot.send_message_file(): %s", file)

    bot_token = config.BOT_TOKEN
    user_id = config.CHAT_ID

    url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
    params = {
        'chat_id': user_id
    }

    with open(file, 'rb') as f:
        response = requests.post(url, data=params, files={'document': f})

    if response.status_code == 200:
        logger.info('telegram_bot.send_message_file(): Log file sent successfully')
    else:
        logger.error('telegram_bot.send_message_file(): Failed to send log file')
