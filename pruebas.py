import unittest
from unittest.mock import Mock
from app_service import AppService

class TestAppService(unittest.TestCase):

    def setUp(self):
        self.mock_db = Mock()
        self.app_service = AppService(self.mock_db)
        
        
    # Probar la función get_tasks en la base de datos
    def test_get_tasks(self):
        
        self.mock_db.get_tasks.return_value = [("Task 1", "Description 1"), ("Task 2", "Description 2")]
        tasks = self.app_service.get_tasks()
        self.assertEqual(tasks, [("Task 1", "Description 1"), ("Task 2", "Description 2")])
        
        

    # Probar la función get_task_by_id en la base de datos
    def test_get_task_by_id(self):
        self.mock_db.get_task_by_id.return_value = ("Task 1", "Description 1")
        task = self.app_service.get_task_by_id(1)
        self.assertEqual(task, ("Task 1", "Description 1"))



    # Probar la función create_task en la base de datos
    def test_create_task(self):
        new_task = {"title": "New Task", "description": "New Description", "due_date": "2024-03-14", "status": "pending", "user_id": 1}
        self.mock_db.create_task.return_value = new_task
        created_task = self.app_service.create_task(new_task)
        self.assertEqual(created_task, new_task)
        
        
    # Probar la función update_task en la base de datos
    def test_update_task(self):
        updated_task = {"title": "Updated Task", "description": "Updated Description", "due_date": "2024-03-15", "status": "completed", "user_id": 2}
        self.mock_db.update_task.return_value = updated_task
        updated_task_result = self.app_service.update_task(1, updated_task)
        self.assertEqual(updated_task_result, updated_task)


    # Probar la función delete_task en la base de datos
    def test_delete_task(self):
        self.mock_db.delete_task.return_value = "1"
        deleted_task_id = self.app_service.delete_task("1")
        self.assertEqual(deleted_task_id, "1")
        

if __name__ == '__main__':
    unittest.main()
