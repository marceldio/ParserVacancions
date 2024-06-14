import psycopg2


class DBManager:
    """Класс, который подключается к БД PostgreSQL."""
    def __init__(self, params):
        self.conn = psycopg2.connect(dbname='hh', **params)
        self.cur = self.conn.cursor()
