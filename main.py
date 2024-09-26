class ToDoList:
    def __init__(self):
        self._tasks = []
        self._completed_tasks = {}

    def add_task(self, task):
        self._tasks.append(task)
        print(f"Задача {task} добавлена.")

    def complete_task(self, task):
        self._completed_tasks[task] = True

    def remove_task(self, task):
        self._tasks.remove(task)
        self._completed_tasks.pop(task, None)
        print(f"Задача {task} удалена.")

    def list_tasks(self):
        status = "[ ]"
        for task in self._tasks:
            if task in self._completed_tasks:
                status = "[x]"
            print(f"{status} {task}")


def main():
    todo_list = ToDoList()

    tasks = ["Купить хлеб", "Заплатить за интернет", "Позвонить другу"]

    for task in tasks:
        todo_list.add_task(task)

    todo_list.list_tasks()

    todo_list.complete_task("Заплатить за интернет")
    todo_list.complete_task("Позвонить другу")

    todo_list.list_tasks()

    todo_list.remove_task("Заплатить за интернет")

    todo_list.list_tasks()


if __name__ == "__main__":
    main()
