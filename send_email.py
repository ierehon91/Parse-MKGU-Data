import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail:
    def __init__(self, data, config, first_date, last_date):
        self.sender_email = "sender_email"
        self.receiver_email = config.get_email()
        self.password = "sender_password"

        self.first_date = first_date
        self.last_date = last_date

        self.data = data

        self.message = MIMEMultipart("alternative")

    def _set_subject(self):
        first_date_string = self.first_date.strftime('%d.%m.%Y')
        last_date_string = self.last_date.strftime('%d.%m.%Y')
        subject = f'МКГУ за период с {first_date_string} по {last_date_string}'
        self.message["Subject"] = subject

    def _set_from_to_mail(self):
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email
