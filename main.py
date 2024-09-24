class ToDoList:
    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        self._tasks.append(task)

    def complete_task(self, task):
        try:
            index = self._tasks.index(task)
            self._tasks[index] = task + " (выполнено)"
        except ValueError as e:
            print(f"Задача {task} не найдена.")

    def remove_task(self, task):
        try:
            index = self._tasks.index(task)
            self._tasks.pop(index)
        except ValueError as e:
            print(f"Задача {task} не найдена.")

    def list_tasks(self):
        for task in self._tasks:
            if "выполнено" in task:
                print(f"- {task}")
            else:
                print(f"+ {task}")


def main():
    todo_list = ToDoList()

    tasks = ["Купить хлеб", "Заплатить за интернет", "Позвонить другу"]

    for task in tasks:
        todo_list.add_task(task)

    todo_list.complete_task("Заплатить за интернет")
    todo_list.complete_task("Позвонить другу")

    todo_list.remove_task("Заплатить за интернет")

    todo_list.list_tasks()


if __name__ == "__main__":
    main()