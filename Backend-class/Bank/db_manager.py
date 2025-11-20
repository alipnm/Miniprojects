from psycopg2 import pool
from config import DB_CONFIG


class DatabaseManager:
    _instance = None
    _conection_pool = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def initialize_pool(self):
        try:
            self._conection_pool = pool.SimpleConnectionPool(
                minconn=1,
                maxconn=10,
                **DB_CONFIG
            )
        except Exception as exc:
            print(exc)

    def get_conn(self):
        if self._conection_pool is None:
            self.initialize_pool()

        return self._conection_pool.getconn()

    def return_connection(self, connection):
        self._conection_pool.putconn(connection)

    def execute_query(self, query: str, params=None):
        connection = self.get_conn()

        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                connection.commit()
                return (rows := cursor.fetchall()) if cursor.description and rows else None
        except Exception as exc:
            print(exc)
            connection.rollback()
        finally:
            self.return_connection(connection)
