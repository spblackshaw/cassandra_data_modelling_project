from sqlalchemy import create_engine, URL, MetaData, inspect
from sqlalchemy.orm import sessionmaker


class PostgreSQLEngine:
    def __init__(self, database: str = "udacity",
                 user: str = "simonblackshaw", password: str = "Amanda@1"):
        self.host = "localhost"
        self.database = database
        self.user = user
        self.password = password

    @property
    def engine(self):
        try:
            url = URL.create(drivername="postgresql+psycopg2", username=self.user, password=self.password,
                             host=self.host, port=5432, database=self.database)
            engine = create_engine(url=url, echo=True)
            return engine
        except Exception as e:
            raise Exception(f"Error: Could not make connection to the database. {e}")

    @property
    def session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    @property
    def metadata(self):
        return MetaData(schema="public")

    @property
    def db_inspection(self):
        return inspect(self.engine)
