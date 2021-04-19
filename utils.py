import mysql.connector


class MySQLManager:

    def __init__(self, db_info: dict[str, str]):
        self.conn = mysql.connector.connect(**db_info)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()
