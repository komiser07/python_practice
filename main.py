class ToDoList:
    def __init__(self):
        self._tasks = []
        self._completed_tasks = {}

    def add_task(self, task):
        self._tasks.append(task)
        print(f"Задача {task} добавлена.\n")

    def complete_task(self, task):
        if task in self._tasks:
            index = self._tasks.index(task)
            self._completed_tasks[task] = task + "(выполнено)\n"
            self._tasks[index] = self._completed_tasks[task]
        else:
            print(f"Задача {task} не найдена.\n")

    def remove_task(self, task):
        if task in self._completed_tasks:
            original_task = self._completed_tasks[task]
            index = self._tasks.index(original_task)
            self._tasks.pop(index)
            del self._completed_tasks[task]
            print(f"Задача {task} удалена.\n")
        else:
            print(f"Задача {task} не найдена.\n")

    def list_tasks(self):
        for task in self._tasks:
            if "выполнено" in task:
                print(f"+ {task}")
            else:
                print(f"- {task}")


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
