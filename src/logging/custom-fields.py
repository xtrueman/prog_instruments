#!python3

import logging

default_extra_fields = { 'user_id': 0, 'key_id': 0, 'ext_params': '' }

class CustAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        extra_fields = {}
        for key in ['user_id', 'key_id', 'ext_params']:
            extra_fields[key] = kwargs.pop(key, self.extra[key] )

        kwargs['extra'] = extra_fields
        return msg, kwargs


logger = logging.getLogger('actions')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
#handler = logging.FileHandler( '/var/log/myapp.log' )

formatter = logging.Formatter(
    fmt = '%(asctime)s\t%(message)s\t%(user_id)s\t%(key_id)s\t%(ext_params)s',
    datefmt = '%d.%m.%Y %H:%M:%S',
)
handler.setFormatter(formatter)
logger.addHandler(handler)

logger = CustAdapter(logger, default_extra_fields)

# Пример использования
logger.info('SOME_ACTION')
logger.info('ANOTHER_ACTION', key_id = 777)
logger.info('ACTION1', user_id = '123', ext_params = {'param1': 123, 'param2': ['A','B',456]})
logger.info('ACTION1', user_id = '123', key_id = 77, ext_params = {'param1': 123, 'param2': ['A','B',456]})
