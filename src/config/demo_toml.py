#!/usr/bin/env python3

import tomllib  # Встроено в Python 3.11+
# import toml # — если используете Python ниже версии 3.11

# Функция для чтения TOML-файла
def load_toml_config(file_path):
    # Открываем в режиме 'rb'
    with open(file_path, "rb") as file:
        return tomllib.load(file)

# Загружаем конфигурацию
config = load_toml_config("config.toml")

# Выводим конфигурацию
print(config)
