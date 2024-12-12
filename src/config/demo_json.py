#!/usr/bin/env python3

import json

# Считываем конфигурацию из файла
with open('config.json', 'r') as file:
    config = json.load(file)

# Выводим конфигурацию
print(config)
