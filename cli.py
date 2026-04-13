import sys
from manager import TaskManager

HELP = """
╔══════════════════════════════════╗
║         📝  TO-DO CLI            ║
╠══════════════════════════════════╣
║  add  <текст>   — добавить       ║
║  list           — все задачи     ║
║  pending        — незакрытые     ║
║  done <номер>   — отметить ✅    ║
║  del  <номер>   — удалить        ║
║  help           — эта справка    ║
╚══════════════════════════════════╝
"""


def print_tasks(tasks: list, label: str = "") -> None:
    if label:
        print(f"\n{label}")
    if not tasks:
        print("  (список пуст)")
        return
    for i, task in enumerate(tasks):
        print(f"  {i}. {task}")


def run():
    manager = TaskManager()
    args = sys.argv[1:]

    if not args or args[0] == "help":
        print(HELP)

    elif args[0] == "add":
        title = " ".join(args[1:])
        if not title:
            print("⚠️  Укажи название задачи: add <текст>")
        else:
            task = manager.add(title)
            print(f"✅ Добавлено: {task.title}")

    elif args[0] == "list":
        print_tasks(manager.list_all(), "📋 Все задачи:")

    elif args[0] == "pending":
        print_tasks(manager.pending(), "⏳ Незавершённые:")

    elif args[0] == "done":
        try:
            task = manager.complete(int(args[1]))
            print(f"🎉 Выполнено: {task.title}")
        except (IndexError, ValueError) as e:
            print(f"⚠️  {e}")

    elif args[0] == "del":
        try:
            task = manager.delete(int(args[1]))
            print(f"🗑️  Удалено: {task.title}")
        except (IndexError, ValueError) as e:
            print(f"⚠️  {e}")

    else:
        print(f"❓ Неизвестная команда '{args[0]}'. Введи 'help'.")
