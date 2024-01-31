from component.daos.sqlalchemy.sqlalchemy_engine import PostgreSQLEngine
from component.models.tables import Base


class CreateTables:
    def __init__(self):
        self.engine = PostgreSQLEngine().engine

    def create_all_tables(self):
        try:
            Base.metadata.create_all(self.engine)
            return Base.metadata.sorted_tables
        except Exception as e:
            raise Exception(f"There was an error creating tables: {e}")