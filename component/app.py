from flask import Flask

from component.daos.sqlalchemy.daos import DatabaseOperations
from component.daos.sqlalchemy.sqlalchemy_engine import PostgreSQLEngine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_connection_string'
engine = PostgreSQLEngine()
db_ops = DatabaseOperations()

if __name__ == '__main__':
    app.run(debug=True)
