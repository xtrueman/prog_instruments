#!/usr/bin/env python3

import configparser

# Функция для чтения INI-файла
def load_ini_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

# Загружаем конфигурацию
config = load_ini_config("config.ini")

# Доступ к параметрам
print("Database Host:", config["database"]["host"])
print("Actions Log:", config["logs"]["actions"])
