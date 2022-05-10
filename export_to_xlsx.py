import openpyxl
import os


class ExportToXLSX:
    def __init__(self, data, config, first_date, last_date):
        self.data = data
        self.config = config
        self.first_date = first_date
        self.last_date = last_date

        self.wb = openpyxl.Workbook()
        self.wb.create_sheet(title='МКГУ', index=0)
        self.sheet = self.wb['МКГУ']

    def _check_export_dir(self):
        self.directory = self.config.get_xlsx_path()
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def _append_header(self):
        self.sheet.append(['Название филиала', 'Кол-во телефонных номеров', 'Кол-во оцененных факторов',
                           'Всего оценок', 'Оценок 1', 'Оценок 2', 'Оценок 3', 'Оценок 4', 'Оценок 5',
                           'Удовлетворенность'])

    def _append_data(self):
        for row in self.data:
            self.sheet.append([row['filial_name'],
                               row['count_phone_numbers'],
                               row['count_factors'],
                               row['all_scores'],
                               row['score_1'],
                               row['score_2'],
                               row['score_3'],
                               row['score_4'],
                               row['score_5'],
                               row['rating']
                               ])

    def get_file_name(self):
        return f'{self.first_date.strftime("%d.%m.%Y")}-{self.last_date.strftime("%d.%m.%Y")}'

    def _save_file(self):
        file_name = self.get_file_name()
        self.wb.save(fr'{self.config.get_xlsx_path()}\{file_name}.xlsx')

    def save_file(self):
        self._check_export_dir()
        self._append_header()
        self._append_data()
        self._save_file()
