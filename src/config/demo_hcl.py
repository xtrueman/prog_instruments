#!/usr/bin/env python3

import hcl

# Чтение HCL-файла
def load_hcl(file_path):
    with open(file_path, "r") as file:
        return hcl.load(file)

# Пример использования
config = load_hcl("config.hcl")

# Вывод результата
print(config)
print("Db Host:", config["database"]["host"])
print("Usrname:", config["database"]["credentials"]["username"])
