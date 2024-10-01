import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_and_complete_task(self):
        self.task_manager.add_task("выполнить задачу ")
        self.task_manager.complete_task(0)
        self.assertTrue(self.task_manager._tasks[0]['completed'])

    def test_remove_task(self):
        self.task_manager.remove_task(0)
        self.assertFalse(self.task_manager._tasks)

    def test_save_and_load_json(self):
        self.task_manager.add_task("выполнить задачу ")
        self.task_manager.save_to_json("tasks.json")
        loaded_task_manager = TaskManager()
        loaded_task_manager.load_from_json("tasks.json")
        self.assertEqual(self.task_manager._tasks, loaded_task_manager._tasks)


if __name__ == "__main__":
    unittest.main()
