from flask import Flask, render_template, request

from component.constants.music_library_data import SONGS_TABLE_NAME
from component.daos.daos import DatabaseOperations
from component.models.database import PostgreSQLEngine
from component.models.tables import Songs

app = Flask(__name__)
engine = PostgreSQLEngine()
db_ops = DatabaseOperations()


@app.route('/')
def index():
    songs_data = db_ops.select_from_table(table_name=SONGS_TABLE_NAME)
    return render_template("index.html", records=songs_data)


if __name__ == '__main__':
    app.run()


@app.route("/add", methods=["GET", "POST"])
def add_record():
    if request.method == "POST":
        for field in Songs:
            name = request.form[field]

