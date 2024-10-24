import psycopg2
from psycopg2.extras import DictCursor

con = psycopg2.connect(database="demodb", user="postgres", password="123", host="127.0.0.1", port="5432")

class PgConfig:
    @staticmethod
    def getCursor():
        cur = con.cursor(cursor_factory=DictCursor)
        return cur

    @staticmethod
    def PgCommit():
        con.commit()
