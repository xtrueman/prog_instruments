#!/usr/bin/env python3

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
    'database': {
        'host': 'localhost',
        'port': 543222,
        'username': 'admin',
        'password': 'thetopsecret'
    },
    'logging': {'level': 'info', 'file': '/var/log/app.log'}
}

# Валидация конфига
try:
    validated_data = schema(config)
    print("✅ Конфигурация валидна!", validated_data)
except Exception as e:
    print(f"❌ Ошибки: {e}")
