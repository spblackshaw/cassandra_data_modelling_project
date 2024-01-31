from cassandra.cluster import Cluster


class CassandraSession:
    def __init__(self, keyspace_name: str):
        self.cluster = Cluster(['localhost'])
        self.session = self.cluster.connect()
        self.keyspace_name = keyspace_name
        self.set_keyspace()

    @property
    def keyspace(self):
        create_keyspace_query = f"""CREATE KEYSPACE IF NOT EXISTS {self.keyspace_name} WITH REPLICATION = 
                                        {'class' : 'SimpleStrategy', 'replication_factor' : 1}"""
        return self.session.execute(create_keyspace_query)

    def set_keyspace(self):
        self.session.execute(f"USE {self.keyspace_name}")

    def run_query(self, query_string):
        try:
            self.session.execute(query_string)
        except Exception as e:
            return e

    def drop_tables(self, tables: list[str]):
        for table in tables:
            self.session.execute(f"DROP TABLE IF EXISTS {table}")

    def create_tables(self, create_tables_list: list[dict]):
        for table_name, table_info in create_tables_list:
            create_string = f"CREATE TABLE IF NOT EXISTS {table_name} "
            columns_string = table_info.get("columns_definition")
            primary_key_string = table_info.get("primary_key_info")
            self.run_query(query_string=create_string + columns_string + primary_key_string)

    def insert_data(self):
        insert_list = [(1970, "The Beatles", "Let It Be", "Liverpool"), (1965, "The Beatles", "Rubber Soul", "Oxford"),
            (1965, "The Who", "My Generation", "London"),
            (1966, "The Monkees", "The Monkees", "Los Angeles"),
            (1970, "The Carpenters", "Close To You", "San Diego")]
        query = "INSERT INTO music_library (year, artist_name, album_name, city) VALUES (%s, %s, %s, %s)"
        for insert in insert_list:
            try:
                self.session.execute(query, insert)
            except Exception as e:
                print(f"There was an error: {e}")

    def describe_keyspace_tables(self):
        return self.session.execute("DESCRIBE TABLES")

    def run(self):
        try:
            print(result)
        except Exception as e:
            print(f"There was an error: {e}")
        self.session.shutdown()
        self.cluster.shutdown()
        print("Success")


CassandraSession(keyspace_name="project_keyspace").run()
print("here")
