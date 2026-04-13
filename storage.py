import json
from pathlib import Path
from models import Task

DB_FILE = Path("tasks.json")


def load_tasks() -> list[Task]:
    if not DB_FILE.exists():
        return []
    with DB_FILE.open("r", encoding="utf-8") as f:
        return [Task.from_dict(t) for t in json.load(f)]


def save_tasks(tasks: list[Task]) -> None:
    with DB_FILE.open("w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tasks], f, ensure_ascii=False, indent=2)
