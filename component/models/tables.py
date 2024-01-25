from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class MusicLibrary(Base):
    __tablename__ = "music_library"

    album_name: Mapped[str] = mapped_column(String(500), primary_key=True)
    artist_name: Mapped[str] = mapped_column(String(500), primary_key=True)
    year: Mapped[int] = mapped_column(Integer)


class Songs(Base):
    __tablename__ = "songs"

    song_title: Mapped[str] = mapped_column(String(500), primary_key=True)
    artist_name: Mapped[str] = mapped_column(String(500), primary_key=True)
    year: Mapped[int] = mapped_column(Integer)
    album_name: Mapped[str] = mapped_column(String(500), primary_key=True)
    single: Mapped[bool] = mapped_column(Boolean)
