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

    def get_task_by_id(self, id: int):
        cursor = self.conn.cursor()

        query = "SELECT * FROM tasks WHERE id = %s;"

        # ejecuta query
        cursor.execute(query, (id,))
        data = cursor.fetchall()

        cursor.close()

        return data

    def create_task(self, task: dict):
        cursor = self.conn.cursor()

        query = "INSERT INTO tasks (title, description, due_date, status, user_id) VALUES (%s, %s, %s, %s, %s)"

        # ejecuta query
        cursor.execute(query, (
            task["title"],
            task["description"],
            task["due_date"],
            task["status"],
            task["user_id"]
        ))
        self.conn.commit()

        cursor.close()

        return task

    def update_task(self, id: int, task: dict):
        cursor = self.conn.cursor()

        query = "UPDATE tasks SET title = %s, description = %s, due_date = %s, status = %s, user_id = %s WHERE id = %s;"

        # ejecuta query
        cursor.execute(query, (
            task["title"],
            task["description"],
            task["due_date"],
            task["status"],
            task["user_id"],
            id
        ))
        self.conn.commit()

        cursor.close()

        return task

    def delete_task(self, id: str):
        cursor = self.conn.cursor()

        query = "DELETE FROM tasks WHERE id = %s;"

        # ejecuta query
        cursor.execute(query, (id,))
        self.conn.commit()

        cursor.close()

        return id