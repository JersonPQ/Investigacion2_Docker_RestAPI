from db import Database

class AppService:

    def __init__(self, database: Database):
        self.database = database
    
    # ------------------- AUTH USER -------------------

    def auth_user(self, user, password):
        ps = self.database.getUser(user)
        if len(ps) == 0:
            return False
        elif ps[0][0] == password:
            return True
        else:
            return False

    # ------------------- TASKS -------------------

    def get_tasks(self):
        data = self.database.get_tasks()
        return data

    
    def get_task_by_id(self, id: int):
        data = self.database.get_task_by_id(id)
        return data
        
    
    def create_task(self, task: dict):
        data_inserted = self.database.create_task(task)
        return data_inserted
        
    
    def update_task(self, id: int, task: dict):
        data_updated = self.database.update_task(id, task)
        return data_updated
        
    
    def delete_task(self, id: str):
        id_deleted = self.database.delete_task(id)
        return id_deleted
    