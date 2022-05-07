def get_mkgu_accounts_list():
    accounts_file = open('accounts.txt', 'r')
    accounts_string = accounts_file.read().split('\n')
    accounts = []
    for account in accounts_string:
        login_password = account.split(' ')
        if login_password != '':
            login = login_password[0]
            password = login_password[1]
            accounts.append({'login': login, 'password': password})
        else:
            break
    return accounts


def print_counts_accounts(mkgu_accouts_list):
    message = f'Найдено {len(mkgu_accouts_list)} учетных записей МКГУ.'
    print(message)
