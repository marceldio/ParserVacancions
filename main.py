from utils import fetch_hh_ru_data, create_base, save_base
from config import config
from DBManager import DBManager


def main():

    company_list = [
                '95255',
                '5136148',
                '999442',
                '1050336',
                '4580428',
                '2104558',
                '5599143',
                '1911144',
                '5987072',
                '4714154',
                '4307',
                '8582',
                '2987',
                '6528',
                '4787018',
                '2283457',
                ]

    params = config()
    data = fetch_hh_ru_data(company_list)

    create_base('hh', params)
    save_base(data, 'hh', params)

    m = DBManager(params)

    m.get_companies_and_vacancies_count()
    m.get_all_vacancies()
    m.get_avg_salary()
    m.get_vacancies_with_higher_salary()
    m.get_vacancies_with_keyword()


if __name__ == '__main__':
    main()
