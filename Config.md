# Конфигурационные файлы / конфиги

## Что это и зачем это нужно?

Конфигурационные файлы (конфиги) — это файлы, которые содержат параметры и настройки приложения, отделяя их от основного кода.
Они определяют поведение приложения без необходимости менять исходный код.

Различные параметры приложения могут быть:
- hardcoded: жёстко зашиты в коде (внутри функций / методов)
- вынесены в константы модулей
  - константы намного лучше, чем "магическеские числа" и "магические строки" непосредственно в коде
  - полезно если константы меняются крайне редко, но всё же могут меняться
- вынесены в отдельные конфиги (файлы, используемые для хранения параметров и настроек приложений).

Зачем нужны: отделение логики программы от настроек:
- Логика программы остаётся в коде, а параметры — в конфигурации.
- Упрощается поддержка, обновления и перенос приложения.
- Параметры легче менять / управлять ими

*Почему это важно?*
- Гибкость: Меняя файл конфигурации, вы **меняете поведение** приложения без изменения кода.
- Разные настройки для **для разных окружений** (development, testing, production).
- Читаемость и поддержка: Проще поддерживать проект, если все настройки вынесены в конфиг.

Примеры использования:
- Настройка веб-серверов (nginx, apache)
- Параметры СУБД (MySQL, Postgresql, clickhouse и т.п.)
- Конфигурации микросервисов и т.п.
- 99% сервисов в linux настраиваются через какие-то конфиги.

У конфигурационных файлов два основных назначения:
- Для просмотра / исправления конфигов вручную: чтобы менять настройки приложения напрямую работая с конфигами в текстовом редакторе
- Для хранения настроек: интерфейс для работы с настройками реализован в каком-то ином виде (web-интерфейс, мобильный интерфейс, GUI интерфейс на Desktop)

Преимущества настроек именно через конфиги (а не через GUI):
1. Независимость от интерфейса:
    - Конфигурационные файлы не зависят от доступности GUI или веб-интерфейса.
    - Настройки можно изменять, даже если приложение не запущено.
    - В критических ситуациях вы всегда можете править файл конфигурации вручную.
    - Пример: Приложение упало из-за ошибки конфигурации? Доступа к интерфейсу нет, но файл конфигурации можно отредактировать напрямую.
    - Работа без сети или с «упавшей» системой
2. Быстрота / простота / гибкость редактирования
    - любой текстовый редактор или иные средства редактирования 
3. Возможность автоматизации и скриптового управления
    - Конфиги можно редактировать с помощью скриптов и автоматизированных инструментов (например, sed, awk, jq).
    - Легко автоматизировать развертывание приложений и изменять параметры без участия человека.
4. Множества вариантов доступа к конфигам
    - через ssh / telnet
    - через файловую систему (NFS, FTP, SMB и т.п.)
    - через системы управления версиями
    - используя любые инструменты работы с файлами (scp и т.п.)
5. Поддержка версионного контроля
    - Конфигурационные файлы можно хранить в системах управления версиями (Git и т.п.)
    - Легко увидеть, кто и когда изменил файл
    - Можно откатиться к предыдущей версии файла, если что-то сломалось.
    - С GUI или веб-интерфейсом такой прозрачности и истории изменений нет (только с помощью специальных журналов или трекеров изменений).
    - Итог: У вас есть история изменений, можно откатиться к рабочей версии, понять, кто внёс изменения.
6. Простое развертывание на нескольких машинах
    - Один и тот же файл конфигурации можно развернуть на нескольких серверах.
    - Конфиг-файлы легко переносить с одного сервера на другой.
    - Упрощается миграция приложений на другие серверы или окружения (dev, test, prod)
    - Пример: Один файл config.prod.yaml можно использовать сразу на 100 серверах с одинаковыми настройками.
    Веб-интерфейсом настраивать 100 серверов руками — долго и рискованно.
    - Итог: Копируете конфиг на новый сервер и запускаете приложение. Быстро и надёжно.
7. Сложность реализации настроек через GUI/web интерфейс:
    - Конфиги поддерживают вложенные структуры (YAML, JSON, TOML), в т.ч. списки неограниченной длины
    - В GUI сложные настройки требуют сложного интерфейса — нужен целый конструктор интерфейсов, различные элементы управления.
8. Скорость разработки:
    - Сделать поддержку нового параметра в конфиге — не стоит ничего (просто сослаться на этот параметр)
    - В GUI надо реализовывать поддержку этого параметра, что требует времени


### Что хранить в конфигурационных файлах?

1. Параметры подключения / credentials
    - К БД: хост, порт, логин, пароль и т.п.
    - URL API-сервисов (тем более могут отличаться production / в test)
    - Учетные данные для внешних сервисов:
        - Различные ключи, пароли, токены
    - Хотя, хранить секреты в конфигах — не всегда хорошая идея, но уж явно лучше, чем напрямую в коде )
2. Переключатели и флаги:
    - Режимы работы (prod, dev, test)
    - Режим отладки (debug) и логгирование (пути к логам, параметры логирования: уровень логирования)
3. Настройки окружения:
    - Пути к файлам, папкам, логам
    - Временные зоны, региональные настройки (параметры локализации, язык и т.п.)
    - Пути к командам / сервисам / пути поиска для запуска команд ($PATH)
4. Конфигурации модулей:
    - Настройки для библиотек и зависимостей
    - Параметры обработки данных (например, размер пакетов)
5. Конфигурации для devops / CI/CD
    - Параметры для развертывания приложений
        - Параметры для docker и т.п.
    - Секреты и токены для сборки (github_token, aws_access_key и т.п.)
6. Пользовательские настройки
    - Предпочтения пользователя
    - Конфигурации интерфейса (темы, цвета, шрифты и т.п.)
7. Любые константы, которые могут когда-то поменяться
    - Числовые (цены, коэффициенты наценки, и т.п.)
    - Строковые (название компании, промпты для LLM)

## Послойные конфиги

Послойные конфиги — несколько файлов конфигураций накладываются друг на друга слоями. Каждый последующий слой может переопределять значения из предыдущего. Обычно это происходит для разделения конфигураций по окружениям (prod, dev, test) или для локальных изменений без изменения основного файла.

### Зачем нужны послойные конфиги?

1. Гибкость и переопределение значений
    - Один и тот же основной файл конфигурации используется для всех окружений.
    - Локальные изменения можно внести в отдельный файл (например, config.local.yaml), не изменяя основной файл config.yaml.
2.  Разделение окружений (dev, test, staging, prod)
    - Основной файл config.yaml содержит общие настройки для всех окружений.
    - Конфиги для разных окружений (например, config.dev.yaml, config.prod.yaml) содержат только различия.
3. Удобство разработки и тестирования
    - Разработчики могут добавлять локальные изменения в локальные конфиги, не затрагивая продакшен.
    - Конфиги для CI/CD могут отличаться от production-конфигов, но включать общие параметры.
4. Избежание дублирования конфигураций
    - В общих конфиг-файлах можно держать базовые значения, а уникальные параметры добавлять “поверх” в других файлах.

### Когда использовать послойные конфиги

- Мультиокружения (dev, test, staging, production)
    - CI/CD пайплайны (разделение конфига для сборки, теста и деплоя)
- Локальная разработка (например, разработчики могут создавать config.local.yaml с личными настройками)
- Управление секретами и токенами (основной конфиг не содержит секретов, а файл secrets.yaml добавляет токены)
- Для работы с шаблонами конфигов (например, базовый config.yaml используется как шаблон, а “поверх” добавляются значения окружения)

### Как это работает?

1. Базовый слой — файл config.yaml с общими значениями.
2. Средний слой — файл для окружения config.dev.yaml, config.prod.yaml.
3. Локальный слой — локальные изменения разработчика в config.local.yaml или локальные настройки для конкретного сервера

### Пример послойной конфигурации (YAML)

config.yaml (базовая конфигурация):
```yaml
database:
  host: "localhost"
  port: 5432
  username: "default_user"
  password: "default_pass"

logging:
  level: "info"
  file: "/var/log/app.log"
```

config.prod.yaml (продакшен):
```yaml
database:
  host: "prod-db.company.com"
  username: "prod_user"
  password: "secure_pass"
```

config.local.yaml (локальные изменения):
```yaml
database:
  password: "local_pass"
  port: 5433

logging:
  level: "debug"
```

Итоговая конфигурация после объединения слоев:
```yaml
database:
  host: "prod-db.company.com" # Заменено из config.prod.yaml
  port: 5433                  # Заменено из config.local.yaml
  username: "prod_user"       # Заменено из config.prod.yaml
  password: "local_pass"      # Заменено из config.local.yaml

logging:
  level: "debug"              # Заменено из config.local.yaml
  file: "/var/log/app.log"    # Из config.yaml (так как не было замен)
```

### Слияние конфигов с помощью готовых библиотек

Есть ряд готовых библилиотек для слияния структур данных, примеры:
```python
from deepmerge import always_merger
from toolz import merge_with
import pydash
```
deepmerge — лучший выбор, если вам нужна библиотека, специально предназначенная для глубокого объединения словарей.

```python
from deepmerge import always_merger
from pprint import pprint

base = {
    'database': { 'host': 'localhost', 'port': 5432, 'username': 'admin' },
    'logging': { 'file': 'app.log', 'level': 'info'}
}

override = {
    'database': { 'port': 3306, 'username': 'dev_user', 'password': 'secret' },
    'logging': { 'level': 'debug' }
}

# Используем always_merger для объединения
merged_config = always_merger.merge( base, override )
pprint( merged_config )
```

## Где хранить конфиги?

- Прямо в модулях любого ЯП. (Python и т.п.),
- Основные форматы: YAML, JSON, INI, TOML, XML, HCL и др.
- Можно хранить в БД.

### В файлах

Возможно хранение в репозитории.
Легко бэкапить.

#### Конфиги прямо в виде модуля любого ЯП

Плюсы:
- самый простой способ, не нужно никаких доп. библиотек и отдельных форматов
- легко делать послойные конфиги
- можно вычислять любые выражения (но это и минус в плане безопасности)

```python
# const.py
API_ID = '21186447'
API_HASH = '1507e2222222221dc6a847dc95b294f36a'

msg_basedir = '/opt/local/var/www/tgmedia/'
tgresources_dir = '/opt/local/var/www/tgresources'
watermarks_samples_dir = os.path.join( tgresources_dir, 'samples' )

advertisement_block_patterns = [
    "#реклама", "Узнать больше", "О рекламодателе",
    r"/\+7[( ]?(?:9|800)/", r"/8[( ]?800/",
]
```

```python
# myapp.py
import const
print(const.API_ID)

from const import *
print(API_ID) # '21186447'
```

##### Послойные конфиги

```python
# const.py
API_ID = '21186448'
API_HASH = '2507edddddd...'

try:
    from myconst import *
except ImportError:
    pass
```

```python
# myconst.py
API_ID = '21186448'
API_HASH = '2507e3333333...'
```

```python
# myapp.py
import const
from const import API_HASH
print(const.API_ID) # '21186448'
print(API_HASH) # '2507e3333333...'
```

#### YAML — YAML Ain't Markup Language

YAML (рекурсивный акроним: «YAML Ain't Markup Language» — «YAML — не язык разметки»).

- отступы из пробелов (символы табуляции не допускаются) используются для обозначения структуры
- комментарии начинаются с символа «решётки» (#), могут начинаться в любом месте строки и продолжаются до конца строки
- списки обозначаются начальным дефисом (-) с одним членом списка на строку, либо члены списка заключаются в квадратные скобки ([ ]) и разделяются запятой и пробелом (, )
- ассоциативные массивы в виде key: value, по одной паре ключ-значение на строку, либо в виде пар, заключённых в { } и разделенных запятой и пробелом (, )

```yaml
# comment
database:
  host: localhost
  port: 5432 # comment
  username: admin
  password: "admin123"

logging:
  level: info
  file: app.log

modules:
  data_processor:
    batch_size: 100
    retry_attempts: 3
  machine_learning:
    model: "xgboost"
    learning_rate: 0.01

ids: [1, 2, 3, 4, 5]
users:
  - { name: Alice, role: admin }
  - { name: Bob, role: editor }
  - { name: Charlie, role: viewer }
```

Плюсы:
- Простой и легкочитаемый формат.
- Компактный
- Поддержка сложных структур любой сложности: списки, словари, любая вложенность.
- Поддерживает комментарии.

Минусы: [Неоднозначность стандартов, «разночтения» в разных библиотеках, проблемы с безопасностью](https://habr.com/ru/articles/710414/).

- YAML задумывался как человекочитаемый формат, однако его спецификация слишком сложна. В отличие от JSON, который прост и стабилен, YAML имеет множество версий и неоднозначных синтаксических правил, что делает его трудным для понимания и использования.
    - Можно «не усложнять» и использовать только понятные конструкции, не вызывающие неоднозначной трактовки
- Булевые значения: В YAML 1.1 такие значения, как `yes`, `no`, `on`, `off`, интерпретировались как булевые литералы. Это создаёт проблемы при парсинге, так как в YAML 1.2 это поведение изменилось, но многие парсеры продолжают поддерживать старые правила
- Неявное преобразование строк в числа: Если строки не заключены в кавычки, они могут быть интерпретированы как числа. Например, версия PostgreSQL `10.23` может быть воспринята как число вместо строки
- Выполнение произвольного кода: YAML поддерживает сериализацию сложных объектов, и при загрузке YAML-файла с помощью небезопасных парсеров (например, `yaml.load()` в Python) злоумышленники могут внедрить вредоносный код, который будет выполнен при десериализации файла.
    - Однако, можно использовать `yaml.safe_load()` и будет счастье

Пример чтения:
```python
import yaml

with open("config.yaml", "r", encoding='utf-8') as file:
    config = yaml.safe_load(file)

    print(config["database"]["host"])
```

##### Послойные конфиги

```yaml
# config.yaml
database:
  host: localhost
  port: 5432
  username: admin
logging:
  level: info
```

```yaml
# config_local.yaml
database:
  port: 3306
  username: dev_user
  password: secret
logging:
  level: debug
```

```python
from ruamel.yaml import YAML

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
print(final_config)
```

Вывод:
```python
{'database':
    {'host': 'localhost',
      'password': 'dev_secret',
      'port': 3306,
      'username': 'dev_user'},
 'logging':
    {'file': 'app.log',
     'level': 'debug'}
}
```

#### JSON — JavaScript Object Notation

JavaScript Object Notation — текстовый формат обмена данными, основанный на JavaScript. Как и многие другие текстовые форматы, JSON легко читается людьми.

Плюсы:
- Легко читается и поддерживается во всех ЯП.
- Строгий формат
- Лишён недостатков YAML в плане неоднозначности, разночтений и проблем с безопасностью
Минусы:
- Не поддерживает комментарии.
- Не слишком удобен для «работы руками» (слишком строгий)
    - Лучше подходит, когда с конфигом не работают напрямую «руками» а есть какой-то другой интерфейс для конфигурирования
- Больше подходит как формат **обмена данными** нежели для хранения конфигурации

```json
{
  "logs": {
    "actions": "/var/log/myservice/action.log",
    "errors": "/var/log/myservice/error.log",
  },
  "database": {
    "host": "localhost",
    "port": 5432,
    "username": "user",
    "password": "pass"
  },
  "array": [1, 2, 3, 4, 5]
}
```

```python
import json

# Считываем конфигурацию из файла
with open('config.json', 'r') as file:
    config = json.load(file)

# Выводим конфигурацию
print(config)
```


#### INI — Initialization file

INI (Initialization file) — старый формат, популярный в системах Windows и для простых конфигураций.

- Широко распространён, но устаревающий.
- Нет формального стандарта — менее строгий, допускает вольности.
- Нет встроенной поддержки вложенности.
    - Подходит только для простых конфигов
- Ограниченные типы данных (только строки)
    - Нужно дополнительно преобразовывать типы данных
- Поддерживает комментарии (; или #).

```ini
; hello world
[logs]
actions = /var/log/myservice/action.log
errors = /var/log/myservice/error.log
[database]
host = localhost
port = 5432
username = user
password = pass
```

```python
import configparser

# Функция для чтения INI-файла
def load_ini_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

# Загружаем конфигурацию
config = load_ini_config("config.ini")

# Выводим конфигурацию
print(config)
```

#### TOML

TOML (Tom’s Obvious, Minimal Language) — это современный формат, созданный для хранения настроек и конфигураций, с фокусом на читаемости и строгой структуре.

- Современный и минималистичный формат.
- Легко читается (легче, чем JSON)
- Подходит для сложных структур.
- Строго специфицирован (TOML spec).
    - Строгий, требует точного следования правилам.
- Поддержка типов данных
- Поддерживает вложенные таблицы и массивы таблиц
- Поддерживает комментарии (#)

##### Поддержка типов данных

- Поддерживает строки, числа, булевы значения, массивы, даты и т.д.
- Не нужно дополнительно преобразовывать типы данных

Пример типов данных:
```
version = 1.2   # Число
debug = true    # Булево значение
date = 2024-11-19T12:34:56Z  # Дата
```

##### Вложенные структуры

```toml
[database]
host = "localhost"

[database.credentials]
username = "admin"
password = "secret"
```

Альтернативная запись:
```toml
[database]
host = "localhost"
port = 5432
credentials.username = "admin"
credentials.password = "secret"
```

Вот как будет выглядеть в python
```python
{
    "database": {
        "host": "localhost",
        "credentials": {
            "username": "admin",
            "password": "secret"
        }
    }
}
```

##### Пример работы с конфигом:

```toml
# comment
[database]
host = "localhost"
port = 5432

[database.credentials]
username = "admin"
password = "secret"

[logging]
level = "info"
file = "app.log"
```

```python
import tomllib  # Встроено в Python 3.11+
# import toml # — если Python < 3.11

# Функция для чтения TOML-файла
def load_toml_config(file_path):
    # Открываем в режиме 'rb'
    with open(file_path, "rb") as file:
        return tomllib.load(file)

# Загружаем конфигурацию
config = load_toml_config("config.toml")

# Выводим конфигурацию
print(config)
```

#### XML

XML — Extensible Markup Language.
Широко используется в старых системах.

Плюсы:
- Поддерживает сложные иерархии, хорошо подходит для структурированных данных.
- Легко выражать отношения и вложенные структуры.
- Валидация структуры: С помощью схем (XSD, DTD и т.п.) можно валидировать структуру XML-файла.
    - Хотя, схемы и инструменты валидация — не только прерогатива XML, для других форматов также есть инструменты, в т.ч. универсальные инструменты, не зависящие от формата

Минусы:
- Избыточен
- Слишком много «свободы» и вариативности способов описания
    - [Неоднозначность преобразования в / из вложенных структур данных высокоуровневых Я.П.](https://habr.com/ru/articles/837542/) — можно преобразовать туда и обратно бесконечным числом способов, нужны дополнительные соглашения
- Сложность в определении схемы (зоопарк схем, их сложно описывать)
- Человеку сложнее читать XML-файлы, особенно если они большие.
- Все данные представлены как строки, и их нужно явно преобразовывать в другие типы.

XML менее подходит, если:
- Конфигурации требуют сложной структуры с отношениями между данными.
- Нужна совместимость со старыми системами или приложениями, которые уже используют XML.
- Требуется валидация структуры (через XML-схемы типа XSD, DTD).
XML не подходит, если:
- Конфигурации просты.
- Нужна компактность и читаемость (используйте YAML, JSON или TOML).

**Примеры вариативности / неоднозначности описания**:

```xml
<logs>
  <actions>/var/log/myservice/action.log</host>
  <errors>/var/log/myservice/error.log</port>
</database>
<database>
  <host>localhost</host>
  <port>5432</port>
  <username>user</username>
  <password>pass</password>
</database>
```

```xml
<logs>
  <log type="actions" path="/var/log/myservice/action.log" />
  <log type="errors" path="/var/log/myservice/error.log" />
</logs>
<database host="localhost" port="5432" username="user" password="pass" />
```

```xml
<log-actions path="/var/log/myservice/action.log" />
<log-errors path="/var/log/myservice/error.log" />
<database>
   <value name="host" val="localhost" />
   <value name="port" val="5432" />
   <value name="username" val="user" />
   <value name="password" val="pass" />
</database>
```

**Пример чтения:**

```python
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
```

#### HCL — HashiCorp Configuration Language

Добавим немного экзотики.<br />
HCL — это декларативный язык, часто используемый в инструментах HashiCorp, таких как Terraform, Consul и Vault. Он поддерживает сложные вложенные структуры и хорошо читается человеком.

```hcl
# single-line comment
/* multiline comment */
database {
  host = "localhost"
  port = 5432

  credentials {
    username = "admin"
    password = "secret"
  }
}

logging {
  level = "info"
  file = "app.log"
}

servers = [
  {
    name = "server1"
    ip   = "192.168.1.1"
  },
  {
    name = "server2"
    ip   = "192.168.1.2"
  }
]
```

Отличия / преимущества / особенности:
- Немного короче и немного более интуитивно понятен, чем JSON;
- Поддерживает комментарии;
- Неограниченная вложенность (в отличие от INI).

**Пример чтения:**

```python
import hcl2

# Функция для загрузки HCL-файла
def load_hcl_config(file_path):
    with open(file_path, "r") as file:
        return hcl2.load(file)

# Пример использования
config = load_hcl_config("config.hcl")

# Вывод результата
print(config)
```

### Хранение конфигов в БД

Может иметь смысл для хранения настроек, когда интерфейс для работы с настройками реализован в каком-то ином виде (web или GUI-интерфейс).

Два сценария, когда может иметь смысл:
1. Храним настройки на локальной машине в локальной лайтовой СУБД (например, SQLite)
2. Храним настройки системы на удалённом сервере, если мы можем заходить в систему с разных машин (и хранить настройки локально не имеет смысла). Например корпоративное приложение с доступом с разных терминалов.

Пример простой структуры таблицы для простого хранения параметров конфигурации типа ключ / значение:
```sql
CREATE TABLE configurations (
    user_id INTEGER UNIQUE KEY,
    key VARCHAR(32) NOT NULL UNIQUE,
    value TEXT NOT NULL
);
```

| user_id | key             | value   |
| ------- | --------------- | ------- |
|     123 | window_bg_color | #f0f0f0 |
|     123 | text_color      | #000000 |
|     123 | ask_before_exit | true    |
|     123 | columns_count   | 5       |


Либо храним конфиг целиком в поле типа JSON.


### Специальные инструменты

#### HashiCorp Vault

HashiCorp Vault — это система управления секретами, которая обеспечивает безопасное хранение, доступ и управление чувствительными данными, такими как пароли, ключи API, токены и сертификаты.

1. Централизованное хранилище секретов
    - Хранит пароли, токены, ключи API, учётные данные баз данных.
    - Доступ к секретам возможен через HTTP API, CLI и клиентские библиотеки.
2. Динамическая генерация секретов
    - Vault может динамически создавать временные учётные данные (например, пароли для баз данных) по запросу.
    - Секреты имеют “время жизни” (TTL) и автоматически истекают.
3. Аудит и контроль доступа
    - Полный контроль над доступом к секретам с помощью политик ACL.
    - Логи аудита фиксируют каждый запрос к секретам.
4. Шифрование и дешифрование данных
    - Vault может шифровать данные для хранения в базе данных или журнале событий.
    - Пример: зашифровать текст до его сохранения в БД.

Пример работы с Vault:
```bash
# Сохранение секретов в Vault:
vault kv put secret/database username="admin" password="supersecret"
# Чтение секретов из Vault
vault kv get secret/database
 Key         Value
 ---         -----
 password    supersecret
 username    admin
```

```python
import hvac

client = hvac.Client(url='http://127.0.0.1:8200', token='s.XXXXX')

# Запись секрета
client.secrets.kv.v2.create_or_update_secret(
    path='database',
    secret={'username': 'admin', 'password': 'supersecret'}
)

# Чтение секрета
response = client.secrets.kv.v2.read_secret_version(path='database')
print(response['data']['data'])
```

*Когда использовать Vault?*

- Для защиты секретов: пароли, ключи API, токены.
- Для автоматического шифрования и дешифрования.
- Когда необходимо управление доступом: разграничение прав доступа к секретам.
- Когда нужен аудит доступа к секретам: кто и когда запросил пароль?


## Лучшие практики / Полезные советы

1. Разделяйте конфигурации по окружениям
    - Могут быть разные среды: development, testing, staging, production
    - Используйте отдельные файлы: `config.dev.yaml`, `config.prod.yaml` и т.п..
2. Не сохраняйте секреты: пароли, токены и ключи API в файлах конфигурации
    - По крайней мере не в системе контроля версий
    - По крайней мере не для production 😀
    - Интеграция с менеджерами секретов (AWS Secrets Manager, HashiCorp Vault).
3. Минимизируйте количество форматов для конфигов
    - Используйте один формат для всего приложения (например, только YAML или TOML).
4. Версионируйте изменения в конфигурациях
    - Если храните в системе управления версиями — уже хорошо (только не стоит там хранить секреты)
5. Возможность валидации конфигураций:
    - Отдельная утилита или опция командной строки для валидации конфигов
    - С помощью pydantic можно валидировать конфиги при загрузке.

<img src="https://media.licdn.com/dms/image/D4E12AQFB7dKsCqC7VA/article-cover_image-shrink_720_1280/0/1693039973797?e=2147483647&v=beta&t=ByzrNAgRQwRWhL6dEhwJzXlMiG9WEGn_0R2mX132vxY" width="600">

### Валидация конфигов

Валидация конфигов — это процесс проверки корректности значений и структуры файлов конфигураций. Это необходимо, чтобы предотвратить ошибки на этапе запуска или работы приложения.

- Хорошо иметь возможность валидировать конфиги без запуска приложения
- При хранении конфигов в репозитории — хорошо бы всроить проверку конфигов в CI/CD как один из этапов тестирования 

Варианты / уровни проверок:
1. Соответствие синтаксису конкретного формата (валидный YAML / JSON / XML и т.п.)
2. Валидация с помощью схем
3. Проверка согласованности конфига в логике приложения
    - При запуске приложения мы в любом случае читаем / валидируем конфиг
    - При указании специального аргумента ком. сроки проводим только этап чтения / валидации конфига и дальше не идём

<img src="https://babok-school.ru/wp-content/uploads/2021/12/ver_val_req0.png" width="300">

#### Валидация с помощью схем

Схема — это формальное описание структуры и правил валидации структуры данных (конфигурационного файла).
Схема определяет, какие поля должны присутствовать в конфиге, их типы, допустимые значения и ограничения. С помощью схем можно автоматически проверять корректность и целостность конфигурационных файлов до или во время работы приложения.

##### Основные элементы схем

- Обязательные и необязательные поля — указывает, какие поля должны присутствовать в конфигурации.
- Типы данных — задаёт тип значения поля (например, int, str, list, dict, bool).
- Допустимые значения — можно ограничивать возможные значения поля (например, level может быть только info, debug, error).
- Вложенные структуры — поддержка вложенных объектов и структур (например, секции database, logging).
- Диапазоны и длина — можно задать диапазон для числовых значений или длину строк (например, пароль должен содержать минимум 8 символов).
- Пользовательские валидаторы — можно создать свои проверки (например, проверка корректности URL или e-mail).

##### Примеры схем:

###### JSON Schema

JSON Schema — это стандарт для описания структуры и валидации JSON-документов.

```json
{
  "type": "object",
  "properties": {
    "database": {
      "type": "object",
      "properties": {
        "host": {"type": "string"},
        "port": {"type": "integer", "minimum": 1024, "maximum": 65535},
        "username": {"type": "string"},
        "password": {"type": "string"}
      },
      "required": ["host", "port"]
    },
    "logging": {
      "type": "object",
      "properties": {
        "level": {"type": "string", "enum": ["debug", "info", "warning", "error"]},
        "file": {"type": "string"}
      }
    }
  },
  "required": ["database", "logging"]
}
```

###### XSD (XML Schema Definition) — Схема для XML

```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="config">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="database">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="host" type="xs:string"/>
              <xs:element name="port" type="xs:integer"/>
              <xs:element name="username" type="xs:string"/>
              <xs:element name="password" type="xs:string"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name="logging">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="level" type="xs:string"/>
              <xs:element name="file" type="xs:string"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

###### Валидация универсальными валидаторами (pydantic, voluptuous)

Pydantic и Voluptuous (можно их считать универсальными валидаторами) — способны валидировать различные типы данных, хранящихся в разных форматах (JSON, YAML, INI, TOML, ENV, XML, HCL и др.).
Они работают не с конкретными файлами, а со структурами данных python (словари, списки, строки, числа и т.д.), которые можно получить из любого формата хранения данных.

###### Pydantic

- Работает с любым форматом: JSON, YAML, TOML, INI, ENV, HCL, XML.
- Поддерживает вложенные структуры (например, словари внутри словарей).
- Валидирует типы данных (int, float, str, bool, list, dict) с помощью type hints.
- Поддерживает пользовательские валидаторы через декораторы @validator.
- Интеграция с FastAPI, что делает его ещё более мощным.

Простое описание схемы:
```python
from pydantic import BaseModel, Field

class DatabaseConfig(BaseModel):
    host: str
    port: int = Field(..., ge=1024, le=65535)  # Порт от 1024 до 65535
    username: str
    password: str

class LoggingConfig(BaseModel):
    level: str
    file: str

class Config(BaseModel):
    database: DatabaseConfig
    logging: LoggingConfig
```

Более сложное описание схемы с различными валидациями:
```python
from pydantic import BaseModel, Field, ValidationError

class DatabaseConfig(BaseModel):
    host: str = Field(..., description="Database hostname, required field")
    port: int = Field(..., ge=1024, le=65535, description="Port number (1024-65535)")
    username: str = Field(..., description="Database username")
    password: str = Field(..., min_length=8, description="Database password, min length 8 characters")

class LoggingConfig(BaseModel):
    level: str = Field(..., regex='^(debug|info|warning|error)$', description="Log level (debug, info, warning, error)")
    file: str

class Config(BaseModel):
    database: DatabaseConfig
    logging: LoggingConfig
```

Валидация конфига и обработка ошибок:
```python
from pydantic import ValidationError

try:
    # Попытка валидации данных с ошибками
    config = Config(**data_with_errors)
except ValidationError as e:
    # Выводим ошибки на stderr
    print("❌ Ошибки валидации конфигурации:")
    print(e.json(indent=4))  # Вывод подробностей об ошибке
```

Должно быть выведено на экран:
```python
❌ Ошибки валидации конфигурации:
[
    {
        "loc": ["database", "port"],
        "msg": "value is not a valid integer (must be between 1024 and 65535)",
        "type": "value_error.number.not_in_range",
        "ctx": {"limit_value": 1024}
    },
    {
        "loc": ["database", "password"],
        "msg": "ensure this value has at least 8 characters",
        "type": "value_error.any_str.min_length",
        "ctx": {"limit_value": 8}
    },
    {
        "loc": ["logging", "level"],
        "msg": "string does not match regex '^(debug|info|warning|error)$'",
        "type": "value_error.str.regex",
        "ctx": {"pattern": "^(debug|info|warning|error)$"}
    },
    {
        "loc": ["logging", "file"],
        "msg": "str type expected",
        "type": "type_error.str"
    }
]
```

Как вывести ошибку более «читаемым» способом:
```python
try:
    config = Config(**data_with_errors)
except ValidationError as e:
    print("❌ Ошибки валидации:")
    for error in e.errors():
        loc = " → ".join(str(l) for l in error['loc'])
        msg = error['msg']
        print(f"Поле: {loc}\nОшибка: {msg}\n\n")
```

Будет выведено:
```
❌ Ошибки валидации:
Поле: database → port
Ошибка: value is not a valid integer (must be between 1024 and 65535)

Поле: database → password
Ошибка: ensure this value has at least 8 characters

Поле: logging → level
Ошибка: string does not match regex '^(debug|info|warning|error)$'

Поле: logging → file
Ошибка: str type expected
```

###### Voluptuous

- Минимум зависимостей: Лёгкая библиотека.
- Поддерживает валидацию словарей, массивов, вложенных структур
- Позволяет задавать кастомные валидаторы (например, проверка длины строки или формата даты).

```python
from voluptuous import Schema, Required, All, Length, Range

# Схема для конфига
schema = Schema({
    'database': {
        'host': str,
        'port': All(int, Range(min=1024, max=65535)),
        'username': str,
        'password': str
    },
    'logging': {
        'level': All(str, Length(min=3, max=10)),
        'file': str
    }
})

# Пример конфига
config = {
    'database': {'host': 'localhost', 'port': 5432, 'username': 'admin', 'password': 'secret'},
    'logging': {'level': 'info', 'file': '/var/log/app.log'}
}

# Валидация конфига
try:
    validated_data = schema(config)
    print("✅ Конфигурация валидна!", validated_data)
except Exception as e:
    print(f"❌ Ошибки: {e}")
```

###### Pydantic vs Voluptuous — Сравнение

| Критерий          | Pydantic | Voluptuous |
| ----------------- | -------- | ---------- | 
| Тип схемы         | Python-классы с аннотациями | Словарь Python
| Автоматическое приведение типов | ✅ (int(“123”) → 123) | ❌ (строка останется строкой)
| Простота кастомизации  | Средняя (через @validator) | Высокая (любой предикат)
| Поддержка типизации | Полная поддержка Python-аннотаций | ❌ Нету (словари)
| Обработка ошибок  |  Автоматическая с подробными отчётами | Простая ошибка Exception

## Статьи

- [Вдогонку к предыдущему посту или О разных методах хранения конфигов](https://habr.com/ru/articles/78976/)
- [Советы, которые могут спасти Вас от ужасов PyYAML](https://habr.com/ru/articles/669684/)
- [Различные конфиги для режима production и режима отладки. Два в одном](https://habr.com/ru/articles/125677/)
- [YAML из Ада](https://habr.com/ru/articles/710414/)
