import parse_accounts_list
import parse_mkgu
import input_dates
import parse_config
import export_to_xlsx
import send_email


def print_header():
    header = open('header.txt', 'r', encoding='UTF-8')
    print(header.read())
    header.close()


def main():
    print_header()
    mkgu_accounts_list = parse_accounts_list.get_mkgu_accounts_list()
    parse_accounts_list.print_counts_accounts(mkgu_accounts_list)

    config = parse_config.GetSettings()
    mkgu = parse_mkgu.ParseMKGU(config)

    first_date = input_dates.get_first_date()
    last_date = input_dates.get_last_date()
    mkgu.get_interval(first_date.year, first_date.month, first_date.day,
                      last_date.year, last_date.month, last_date.day)

    mkgu_data = []
    i = 1
    count_accounts = len(mkgu_accounts_list)
    for mkgu_account in mkgu_accounts_list:
        login = mkgu_account['login']
        password = mkgu_account['password']
        print(f'Получение данных: {i} / {count_accounts} - {login}')
        mkgu_data.append(mkgu.parse_data(login, password))
        i += 1

    save_xlsx = export_to_xlsx.ExportToXLSX(mkgu_data, config, first_date, last_date)
    save_xlsx.save_file()
    print(f'Файл {save_xlsx.get_file_name()}.xlsx сохранён.')

    if config.get_send_email_status() is True:
        email = send_email.SendEmail(mkgu_data, config, first_date, last_date)
        email.send_email()


if __name__ == '__main__':
    main()
