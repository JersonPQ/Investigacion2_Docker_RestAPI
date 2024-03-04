from db import Database

class AppService:

    def __init__(self, database: Database):
        self.database = database
    
    # ------------------- TASKS -------------------

    def get_tasks(self):
        data = self.database.get_tasks()
        return data