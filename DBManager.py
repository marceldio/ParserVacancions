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


    def get_all_vacancies(self):
        """
        Получает список всех вакансий с информацией о компании, названии вакансии, зарплате и ссылке.

        :return: List of tuples with company name, vacancy name, salary, and vacancy URL.
        """
        self.cur.execute(f"select employers.company_name, vacancies.vacancy_name, vacancies.salary_from, "
                         f"vacancies.vacancy_url from vacancies join employers using(employer_id)")
        return self.cur.fetchall()


    def get_avg_salary(self):
        """
        Получает среднюю зарплату по всем вакансиям.

        :return: List of tuples with average salary value.
        """
        self.cur.execute(f"select avg(salary_from) from vacancies")
        return self.cur.fetchall()




