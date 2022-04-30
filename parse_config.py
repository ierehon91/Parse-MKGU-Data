import configparser


class GetSettings:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('settings.ini')

    def get_proxy_status(self):
        if self.config['Settings']['proxy'] == '1':
            return True
        else:
            return False

    def get_proxy_config(self):
        http = fr'http://{self.config["Settings"]["proxy_http_ip"]}:{self.config["Settings"]["proxy_http_port"]}'
        https = fr'https://{self.config["Settings"]["proxy_https_ip"]}:{self.config["Settings"]["proxy_https_port"]}'
        return {'http': http, 'https': https}

    def get_email(self):
        return self.config["Settings"]["email"]
