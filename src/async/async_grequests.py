#!python3

import grequests

urls = [
    'http://yandex.ru/',
    'http://mail.ru/',
    'http://vk.com/',
    'http://ok.ru/',
    'http://www.google.com/',
    'http://www.example.com',
    'http://www.github.com',
]

# Создание списка незаблокированных запросов
rs = (grequests.get(u, allow_redirects=False) for u in urls)

# Отправка запросов в один поток и получение ответов
responses = grequests.map(rs)

# Вывод кодов состояния HTTP и соответствующих URL
for response in responses:
    if response:
        print(f"{response.url} — {response.status_code}")
    else:
        print("No response received.")
