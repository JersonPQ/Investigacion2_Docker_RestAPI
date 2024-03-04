import psycopg2

class Database:
    def __init__(
            self, database="db_name", host="db_host", user="db_user",
            password="db_password", port="db_port"
    ):
        self.conn = psycopg2.connect(
            database=database, host=host, user=user,
            password=password, port=port
        )

    def get_tasks(self):
        cursor = self.conn.cursor()
        
        # ejecuta query
        cursor.execute("SELECT * FROM tasks;")
        data = cursor.fetchall()

        cursor.close()

        return data

    def get_task_by_id(self):
        pass

    def create_task(self):
        pass

    def update_task(self):
        pass

    def delete_task(self):
        pass