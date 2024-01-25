from component.models.tables import MusicLibrary, Songs

MUSIC_LIBRARY_TABLE_NAME = "music_library"
ALBUM_VALUES = [MusicLibrary(album_name="Let It Be", artist_name="The Beatles", year=1970),
                MusicLibrary(album_name="Rubber Soul", artist_name="The Beatles", year=1965)]

SONGS_TABLE_NAME = "songs"
SONGS_VALUES = [Songs(song_title="Across The Universe", artist_name="The Beatles", year=1970, album_name="Let It Be", single=False),
                Songs(song_title="Think For Yourself", artist_name="The Beatles", year=1965, album_name="Rubber Soul", single=False),
                ]

