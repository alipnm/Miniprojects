from ..db_manager import DatabaseManager


class BaseModel:
    table_name = None

    def __init__(self):
        self.db_manager = DatabaseManager()\


    def getall(self):
        query = f"SELECT * FROM {self.table_name}"
        return self.db_manager.execute_query(query)

    def get_by_id(self, id):
        query = f"SELECT * FROM {self.table_name} WHERE id = %s"
        return self.db_manager.execute_query(query, params=(id,))

    def delete(self, id):
        query = f"DELETE FROM {self.table_name} WHERE ID = %s"
        return self.db_manager.execute_query(query, params=(id,))
