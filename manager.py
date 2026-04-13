from models import Task
from storage import load_tasks, save_tasks


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = load_tasks()

    def add(self, title: str) -> Task:
        task = Task(title=title)
        self.tasks.append(task)
        save_tasks(self.tasks)
        return task

    def complete(self, index: int) -> Task:
        task = self._get(index)
        task.done = True
        save_tasks(self.tasks)
        return task

    def delete(self, index: int) -> Task:
        task = self._get(index)
        self.tasks.pop(index)
        save_tasks(self.tasks)
        return task

    def list_all(self) -> list[Task]:
        return self.tasks

    def pending(self) -> list[Task]:
        return [t for t in self.tasks if not t.done]

    def _get(self, index: int) -> Task:
        if not (0 <= index < len(self.tasks)):
            raise IndexError(f"Нет задачи с номером {index}")
        return self.tasks[index]
