from db import Database

class AppService:

    def __init__(self, database: Database):
        self.database = database
    
    # ------------------- TASKS -------------------

    def get_tasks(self, user, password):
        ps = self.database.getUser(user)
        if len(ps) == 0:
            return "El usuario no existe"
        elif ps[0][0] == password:
            data = self.database.get_tasks()
            return data
        else:
            return "El usuario no tiene permisos."

    
    def get_task_by_id(self, user, password ,id: int):
        ps = self.database.getUser(user)
        if len(ps) == 0:
            return "El usuario no existe"
        elif ps[0][0] == password:
            data = self.database.get_task_by_id(id)
            return data
        else:
            return "El usuario no tiene permisos."
        
    
    def create_task(self, user, password ,task: dict):
        ps = self.database.getUser(user)
        if len(ps) == 0:
            return "El usuario no existe"
        elif ps[0][0] == password:
            data_inserted = self.database.create_task(task)
            return data_inserted
        else:
            return "El usuario no tiene permisos."
        
    
    def update_task(self, user, password, id: int, task: dict):
        ps = self.database.getUser(user)
        if len(ps) == 0:
            return "El usuario no existe"
        elif ps[0][0] == password:
            data_updated = self.database.update_task(id, task)
            return data_updated
        else:
            return "El usuario no tiene permisos."
        
    
    def delete_task(self, user, password, id: str):
        ps = self.database.getUser(user)
        if len(ps) == 0:
            return "El usuario no existe"
        elif ps[0][0] == password:
            id_deleted = self.database.delete_task(id)
            return id_deleted
        else:
            return "El usuario no tiene permisos."
        
    