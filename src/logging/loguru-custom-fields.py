#!python3

import sys
from loguru import logger

# Создание формата строки для сообщений лога с дополнительными параметрами
log_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | " + \
             "<level>{message}</level> | <cyan>{extra[user_id]}</cyan> | " + \
             "<cyan>{extra[key_id]}</cyan> | <blue>{extra[ext_params]}</blue>"

config = {
    "handlers": [
        {"sink": sys.stdout, "format": log_format},
    ],
    "extra": { "user_id": 0, "key_id": 0, "ext_params": "" }
}
logger.configure(**config)

#logger.add(sys.stderr, level="INFO", format=log_format )

# Пример использования
logger.info('SOME_ACTION')
logger.info('ANOTHER_ACTION', key_id = 777)
logger.info('ACTION1', user_id = '123', ext_params = {'param1': 123, 'param2': ['A','B',456]})
logger.info('ACTION2', user_id = '123', key_id = 77, ext_params = {'par1': 123, 'par2': 'Z'})
