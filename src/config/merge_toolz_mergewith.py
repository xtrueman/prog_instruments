#!/usr/bin/env python3

from toolz import merge_with
from pprint import pprint

base = {
    'database': {'host': 'localhost', 'port': 5432, 'username': 'admin'},
    'logging': {'file': 'app.log', 'level': 'info'}
}

override = {
    'database': {'port': 3306, 'username': 'dev_user', 'password': 'secret'},
    'logging': {'level': 'debug'}
}

# Функция объединения
def merge_dicts(d1, d2):
    return merge_with(lambda x: x[-1], d1, d2)

merged_config = merge_dicts(base, override)
pprint(merged_config)
