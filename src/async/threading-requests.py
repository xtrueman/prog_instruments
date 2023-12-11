#!python3

import threading, requests, time

# Функция, которая будет выполнять HTTP запрос и печатать код ответа
def get_status_code(url, start_time):
    try:
        response = requests.get(url)
        pingtime = (time.time() - start_time) * 1000
        print(f"{url}: {response.status_code} — {pingtime:.2f} ms")
    except requests.RequestException as e:
        print(f"{url}: ошибка - {e}")

# Список URL для проверки
urls = [
    'http://yandex.ru/',
    'http://mail.ru/',
    'http://vk.com/',
    'http://ok.ru/',
    'http://www.google.com/',
    'http://www.example.com',
    'http://www.github.com',
]

global_start_time = time.time()

# Создание и запуск потока для каждого URL
threads = []
for url in urls:
    thread = threading.Thread(target=get_status_code, args=(url, time.time()))
    thread.start()
    threads.append(thread)

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

total_time = (time.time() - global_start_time) * 1000
print(f'Finished in {total_time:.2f}')
