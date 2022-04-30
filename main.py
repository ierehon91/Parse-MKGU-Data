import parse_accounts_list
import parse_mkgu
import input_dates
import parse_config


def main():
    mkgu_accounts_list = parse_accounts_list.get_mkgu_accounts_list()

    config = parse_config.GetSettings()
    mkgu = parse_mkgu.ParseMKGU(config)

    first_date = input_dates.input_date('начальную')
    last_date = input_dates.input_date('конечную')
    mkgu.get_interval(first_date.year, first_date.month, first_date.day,
                      last_date.year, last_date.month, last_date.day)

    mkgu_data = []
    for mkgu_account in mkgu_accounts_list[:2]:
        login = mkgu_account['login']
        password = mkgu_account['password']
        mkgu_data.append(mkgu.parse_data(login, password))
    print(mkgu_data)


if __name__ == '__main__':
    main()
