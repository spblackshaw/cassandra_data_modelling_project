from component.constants.music_library_data import ALBUM_VALUES, MUSIC_LIBRARY_TABLE_NAME, SONGS_TABLE_NAME, SONGS_VALUES
from component.daos.sqlalchemy.daos import DatabaseOperations


class UpdateMusicLibrary:
    def __init__(self):
        self.daos = DatabaseOperations()

    def run(self):
        self.daos.insert_table_data(table_data=ALBUM_VALUES)
        album_data = self.daos.select_from_table(table_name=MUSIC_LIBRARY_TABLE_NAME)
        self.daos.insert_table_data(table_data=SONGS_VALUES)
        songs_data = self.daos.select_from_table(table_name=SONGS_TABLE_NAME)
        print("here")


UpdateMusicLibrary().run()
print("here")
