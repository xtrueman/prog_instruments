#!/usr/bin/env python3

from deepmerge import always_merger
from pprint import pprint

base = {
    'database': {'host': 'localhost', 'port': 5432, 'username': 'admin'},
    'logging': {'file': 'app.log', 'level': 'info'}
}

override = {
    'database': {'port': 3306, 'username': 'dev_user', 'password': 'secret'},
    'logging': {'level': 'debug'}
}

# Используем always_merger для объединения
merged_config = always_merger.merge( base, override )
pprint( merged_config )
