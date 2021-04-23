import mysql.connector
from mysql.connector.cursor import MySQLCursor


class MySQLManager:
    """Context manager voor MySQL database connecties.
    Returnt een MySQLCursor"""

    def __init__(self, db_info: dict[str, str]):
        """Constructor voor MySQLManager, opent een connectie met de
        database en maakt een cursor aan.

        :param dict[str, str] db_info: dictionary met connection
        parameters.
        """
        self.conn = mysql.connector.connect(**db_info)
        self.cursor = self.conn.cursor()

    def __enter__(self) -> MySQLCursor:
        """Wordt aangeroepen aan het begin van een with statement.

        :return: MySQLCursor
        """
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Wordt aangeroepen aan het einde van een with statement.
        Eventuele exceptions worden niet afgevangen.

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        """
        self.cursor.close()
        self.conn.close()
