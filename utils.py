import psycopg2
from typing import List, Dict, Any
import requests


def fetch_hh_ru_data(company_list: List[str]) -> List[Dict[str, Any]]:
    """
    Получение данных о работодателях и вакансиях с использованием API HH.ru.

    Параметры:
    - employer_ids: Список строк, представляющих идентификаторы работодателей, для которых нужно получить данные.

    Возвращает:
    Список словарей, где каждый словарь содержит информацию о работодателе и список вакансий.
    """
    data = []
    for employer_id in company_list:
        employer_response = requests.get('https://api.hh.ru/employers/' + employer_id)
        employer_info = employer_response.json()

        vacancies = []
        vacancy_response = requests.get('https://api.hh.ru/vacancies?employer_id=' + employer_id)
        vacancies_text = vacancy_response.json()

        vacancies.extend(vacancies_text['items'])

        data.append({
            'employers': employer_info,
            'vacancies': vacancies
        })
    return data
