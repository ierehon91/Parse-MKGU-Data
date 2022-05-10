import configparser


class GetSettings:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('settings.ini', encoding='utf-8')

    def get_proxy_status(self):
        if self.config['Settings']['proxy'] == '1':
            return True
        else:
            return False

    def get_proxy_config(self):
        http = fr'http://{self.config["Settings"]["proxy_http_ip"]}:{self.config["Settings"]["proxy_http_port"]}'
        https = fr'https://{self.config["Settings"]["proxy_https_ip"]}:{self.config["Settings"]["proxy_https_port"]}'
        return {'http': http, 'https': https}

    def get_emails(self):
        emails = self.config["Settings"]["email"]
        return emails

    def get_xlsx_path(self):
        return self.config["Settings"]["export_xlsx_path"]

    def get_send_email_status(self):
        if self.config['Settings']['send_email'] == '1':
            return True
        else:
            return False


if __name__ == '__main__':
    config = GetSettings()
    print(config.get_emails().split(', '))
