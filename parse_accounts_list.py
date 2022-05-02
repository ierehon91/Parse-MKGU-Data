import openpyxl


def get_mkgu_accounts_list():
    wb = openpyxl.load_workbook(r'mkgu_accounts_list.xlsx')
    sheet = wb['mkgu_accounts_list']

    mkgu_accouts_list = []
    for i in range(2, sheet.max_row + 1):
        login = sheet.cell(row=i, column=1).value
        password = sheet.cell(row=i, column=2).value
        mkgu_accouts_list.append({'login': login, 'password': password})
    return mkgu_accouts_list


def print_counts_accounts(mkgu_accouts_list):
    message = f'Найдено {len(mkgu_accouts_list)} учетных записей МКГУ.'
    print(message)
