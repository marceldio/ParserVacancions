import psycopg2


class DBManager:
    """Класс, который подключается к БД PostgreSQL."""
    def __init__(self, params):
        self.conn = psycopg2.connect(dbname='hh', **params)
        self.cur = self.conn.cursor()


    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний с количеством открытых вакансий.

        :return: List of tuples with company name and open vacancies count.
        """
        self.cur.execute(f"SELECT company_name, open_vacancies FROM employers")
        return self.cur.fetchall()
