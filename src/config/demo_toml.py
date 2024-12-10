#!/usr/bin/env python3

import tomllib  # Встроено в Python 3.11+
# import toml # — если используете Python ниже версии 3.11

# Функция для чтения TOML-файла
def load_toml_config(file_path):
    with open(file_path, "rb") as file:  # Открываем в режиме 'rb'
        return tomllib.load(file)

# Загружаем конфигурацию
config = load_toml_config("config.toml")

# Доступ к параметрам
print("Database Host:", config["database"]["host"])
print("DB User:", config["database"]["credentials"]["username"])
print("Logging Level:", config["logging"]["level"])
