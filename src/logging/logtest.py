#!python3

import logging

logging.basicConfig(
    level = 'INFO',
    datefmt='%d.%m.%Y %H:%M:%S',
    format = '%(asctime)s\t%(levelname)s\t%(message)s\t%(user_id)s\t%(key_id)s\t%(ext_params)s'
)
logging.info('PAYMENT', extra={'user_id': 123, 'key_id': 456, 'ext_params': '{}'})

# Custom fields
#import logging
#logging.basicConfig(format="%(foo)s - %(message)s")
