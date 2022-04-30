import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup


class ParseMKGU:
    def __init__(self, config):
        self.session = requests.Session()
        if config.get_proxy_status() is True:
            proxy = config.get_proxy_config()
            self.session.proxies.update(proxy)
        self.login_url = "https://vashkontrol.ru/users/sign_in"
        self.parse_data_url = "https://vashkontrol.ru/hershel/regions/20/reports/general"
        self.logout_url = "https://vashkontrol.ru/users/sign_out"
        self.first_date = datetime(datetime.now().year, datetime.now().month, 1)
        self.last_date = datetime(datetime.now().year, datetime.now().month, datetime.now().day)

    def get_interval(self, first_year, first_month, first_day, last_year, last_month, last_day):
        self.first_date = datetime(first_year, first_month, first_day)
        self.last_date = datetime(last_year, last_month, last_day)

    def _get_csrf_token(self, url):
        """Получаем csrf_token для авторизации"""
        token_request = self.session.get(url)
        csrf_token = re.findall(r"[^\"\>\{\}\\]{86}==", token_request.text)
        return csrf_token[0]

    def _authorization(self, login, password, csrf_token):
        """Авторизация на сайте Ваш контроль по логину и паролю"""
        login_data = {'user[login]': login, 'user[password]': password, 'authenticity_token': csrf_token}
        self.session.post(url='https://vashkontrol.ru/users/sign_in', data=login_data)

    def _to_str_date(self):
        """Преобразовывает дату в строку для дальнейшего парсинга данных"""
        str_first_date = self.first_date.strftime('%Y-%m-%d')
        str_last_date = self.last_date.strftime('%Y-%m-%d')
        return (str_first_date, str_last_date)

    def _get_reception_data_string(self):
        reception_data = 'report_type=custom' \
                         f'&year={datetime.now().year}' \
                         '&quarter=1' \
                         '&month=1' \
                         f'&date_start={self._to_str_date()[0]}' \
                         f'&date_end={self._to_str_date()[1]}' \
                         '&category_ids%5B%5D=4' \
                         '&category_ids%5B%5D=5' \
                         '&category_ids%5B%5D=1' \
                         '&category_ids%5B%5D=2' \
                         '&category_ids%5B%5D=3' \
                         '&mfc_ids%5B%5D=all' \
                         '&service_type=all' \
                         '&service_ids%5B%5D=all'
        return reception_data

    def _get_raw_data(self, csrf_token):
        """Получаем сырые данные в виде JavaScript строки"""
        headers = {
            'x-csrf-token': csrf_token,
            'x-requested-with': 'XMLHttpRequest',
            'origin': 'https://vashkontrol.ru',
            'referer': self.parse_data_url,
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin'
        }
        reception_data = self._get_reception_data_string()
        url = "https://vashkontrol.ru/hershel/regions/20/reports/general/submit"
        raw_data = self.session.post(url=url, data=reception_data, headers=headers)
        return raw_data.text

    def _get_clean_data(self, raw_data):
        soup = BeautifulSoup(raw_data, "html.parser").get_text().split("<\/td>")
        clean_data = {
            "filial_name": soup[1].split('<')[0],
            "count_phone_numbers": int(soup[2].split('<')[0]),
            "count_factors": int(soup[3].split('<')[0]),
            "all_scores": int(soup[4].split('<')[0]),
            "score_1": int(soup[5].split('<')[0]),
            "score_2": int(soup[6].split('<')[0]),
            "score_3": int(soup[7].split('<')[0]),
            "score_4": int(soup[8].split('<')[0]),
            "score_5": int(soup[9].split('<')[0]),
            "rating": float(soup[10].split('<')[0])
            }
        return clean_data

    def _log_out(self, logout_cstf_token):
        data = {"_method" : "delete", "authenticity_token" : logout_cstf_token}
        self.session.post(self.logout_url, data=data)

    def parse_data(self, login, password):
        login_csrf_token = self._get_csrf_token(self.login_url)
        self._authorization(login, password, login_csrf_token)

        data_csrf_token = self._get_csrf_token(self.parse_data_url)
        raw_data = self._get_raw_data(data_csrf_token)
        clean_data = self._get_clean_data(raw_data)

        self._log_out(data_csrf_token)

        return clean_data
