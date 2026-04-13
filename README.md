# 📝 TO-DO CLI

Консольное приложение для управления задачами. Задачи хранятся локально в JSON-файле.

## 🚀 Запуск

```bash
python main.py <команда>
```

## 📋 Команды

| Команда | Описание |
|---|---|
| `python main.py help` | Показать справку |
| `python main.py add "Текст"` | Добавить задачу |
| `python main.py list` | Показать все задачи |
| `python main.py pending` | Показать незавершённые |
| `python main.py done <номер>` | Отметить как выполненную |
| `python main.py del <номер>` | Удалить задачу |

## 💡 Примеры

```bash
python main.py add "Купить молоко"
python main.py add "Сделать домашнее задание"
python main.py list
python main.py done 0
python main.py del 1
```

## 🗂 Структура проекта

```
├── main.py       # Точка входа
├── cli.py        # Обработка команд
├── manager.py    # Бизнес-логика
├── models.py     # Модель данных Task
├── storage.py    # Сохранение в JSON
└── tasks.json    # База данных (создаётся автоматически)
```

## ⚙️ Требования

- Python 3.10+
- Сторонние библиотеки не нужны