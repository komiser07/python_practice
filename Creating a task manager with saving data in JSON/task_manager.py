import json

class TaskManager:
    def __init__(self):
        self._tasks = []

    def add_task(self, description):
        self._tasks.append({"description": description, "completed": False})

    def complete_task(self, index):
        if 0 <= index < len(self._tasks):
            self._tasks[index]["completed"] = True
        else:
            print(f"Задача с индексом {index} не найдена.")

    def remove_task(self, index):
        if 0 <= index < len(self._tasks):
            self._tasks.pop(index)
            print(f"Задача с индексом {index} удалена.")
        else:
            print(f"Задача с индексом {index} не найдена.")

    def save_to_json(self, filename):
        with open(filename, "w") as f:
            json.dump(self._tasks, f)

    def load_from_json(self, filename):
        with open(filename, "r") as f:
            self._tasks = json.load(f)

manager = TaskManager()
manager.add_task("Выполнить задачу №1")
manager.add_task("Выполнить задачу №2")
manager.add_task("Выполнить задачу №3")

manager.complete_task(0)
manager.complete_task(2)
manager.remove_task(1)

manager.save_to_json("tasks.json")

new_manager = TaskManager()
new_manager.load_from_json("tasks.json")

for task in new_manager._tasks:
    print(f"Задача: {task['description']}, завершена: {task['completed']}")