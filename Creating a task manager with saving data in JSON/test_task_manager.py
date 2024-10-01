import unittest
import json
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_and_complete_task(self):
        self.task_manager.add_task("Go to the store")
        self.task_manager.complete_task(0)
        completed_task = self.task_manager._tasks[0]
        self.assertEqual(completed_task["completed"], True)

    def test_remove_task(self):
        self.task_manager.add_task("Call John")
        self.task_manager.remove_task(0)
        self.assertEqual(len(self.task_manager._tasks), 0)

    def test_save_and_load_json(self):
        self.task_manager.add_task("Write report")
        self.task_manager.save_to_json("tasks.json")
        loaded_task_manager = TaskManager()
        loaded_task_manager.load_from_json("tasks.json")
        saved_tasks = self.task_manager._tasks
        loaded_tasks = loaded_task_manager._tasks
        self.assertCountEqual(saved_tasks, loaded_tasks)

if __name__ == "__main__":
    unittest.main()