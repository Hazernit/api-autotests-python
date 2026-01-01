# API Autotests (Python)

Учебный проект по автоматизации тестирования REST API, приближённый к рабочему.

## Стек
- Python 3
- pytest
- requests

## Что тестируется
Публичный REST API: https://jsonplaceholder.typicode.com

Реализованы проверки:
- получение списка постов (`GET /posts`)
- проверка структуры ответа (`GET /posts/1`)
- негативный сценарий для несуществующего ресурса

## Структура проекта
api-autotests-python/
├── tests/
│ └── test_basic.py
├── requirements.txt
└── README.md


## Как запустить
1. Установить зависимости:
```bash
pip install -r requirements.txt
Запустить тесты:

pytest -q

Примечания

Проект создан как демонстрация базовых навыков API-тестирования и Python-автоматизации.


После этого:
```bash
git add README.md
git commit -m "Add README"
git push
