#!/usr/bin/env python3

import xmltodict

# Чтение XML-файла и преобразование в словарь
def load_xml_config(file_path):
    with open(file_path, "r") as file:
        # Добавляем временный корневой элемент для корректного парсинга
        xml_with_root = f"<root>{file.read()}</root>"
        return xmltodict.parse(xml_with_root)["root"]

# Пример использования
config = load_xml_config("config.xml")

# Вывод результата
print(config)
print("Database Host:", config["database"]["host"])
print("Username:", config["database"]["credentials"]["username"])
