#!/usr/bin/env python3

from ruamel.yaml import YAML
from pprint import pprint

# Функция для глубокого объединения словарей
def merge_dicts(base, override):
    for key, value in override.items():
        if isinstance(value, dict) and key in base:
            base[key] = merge_dicts(base[key], value)
        else:
            base[key] = value
    return base

# Функция для загрузки YAML
def load_yaml(file_path):
    yaml = YAML(typ="safe")
    with open(file_path, 'r') as file:
        return yaml.load(file)

# Загружаем базовый и локальный конфиг
base_config = load_yaml("config.yaml")
local_config = load_yaml("config_local.yaml")

# Объединяем конфиги
final_config = merge_dicts(base_config, local_config)

# Результат
print("Итоговая конфигурация:")
pprint(final_config, width=40, compact=False, indent=2)
