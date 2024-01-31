from sqlalchemy import Table, select

from component.daos.sqlalchemy.create_tables import CreateTables
from component.daos.sqlalchemy.sqlalchemy_engine import PostgreSQLEngine


class DatabaseOperations:
    def __init__(self, db_name: str = "udacity"):
        self.db_name = db_name
        self.db_connector = PostgreSQLEngine(database=self.db_name)
        CreateTables().create_all_tables()

    def select_from_table(self, table_name: str):
        table = self.instantiate_db_table(table_name=table_name)
        with self.db_connector.session as session:
            return session.execute(select(table)).all()

    def instantiate_db_table(self, table_name):
        table = Table(table_name, self.db_connector.metadata, autoload_with=self.db_connector.engine)
        return table

    def insert_table_data(self, table_data):
        try:
            with self.db_connector.session as session:
                for item in table_data:
                    session.add(item)
                session.commit()
        except Exception as e:
            return e
