# DB Accesor
from contextlib import contextmanager
import psycopg2
from psycopg2.extras import DictCursor

DATABASE_NAME = 'minecraft_steve'

@contextmanager
def session():
    """
    Returns a cursor to the database
    The configurations of this cursor are as follows
    - autocommit=True
    - cursor_factory=DictCursor
    """
    conn = psycopg2.connect(  # type: ignore
        database=DATABASE_NAME,
        host="minecraft_steve-db-service",
        user='docker',
        password='docker',
        port=5432,
        cursor_factory=DictCursor
    )
    conn.set_session(autocommit=True)  # type: ignore
    curr = conn.cursor()  # type: ignore
    yield curr
    curr.close()  # type: ignore
    conn.close()  # type: ignore
