import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail:
    def __init__(self, data, config, first_date, last_date):
        sender_file = open('sender.txt', 'r')
        login_password = sender_file.read().split(' ')
        self.sender_email = login_password[0]
        self.password = login_password[1]
        self.receiver_email = config.get_email()

        self.first_date = first_date
        self.last_date = last_date

        self.data = data

        self.message = MIMEMultipart("alternative")

    def _set_subject(self):
        first_date_string = convert_datetime_to_string(self.first_date)
        last_date_string = convert_datetime_to_string(self.last_date)
        subject = f'МКГУ за период с {first_date_string} по {last_date_string}'
        self.message["Subject"] = subject

    def _set_from_to_mail(self):
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email

    def _create_message_text(self):
        text = ''
        header_test = 'Это тестовое сообщение, отвечать на него не нужно!!!\n\n\n'
        header = f'Данные из МКГУ за период с {convert_datetime_to_string(self.first_date)} ' \
                 f'по {convert_datetime_to_string(self.last_date)}:\n\n\n'
        text += header_test
        text += header

        for filial in self.data:
            text += create_text_one_filial_data(filial)
        return text

    def _attack_message(self):
        part1 = MIMEText(self._create_message_text(), "plain")
        self.message.attach(part1)

    def _send_email(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.yandex.ru", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(
                self.sender_email, self.receiver_email, self.message.as_string()
            )

    def send_email(self):
        self._set_subject()
        self._set_from_to_mail()
        self._attack_message()
        self._send_email()


def convert_datetime_to_string(date):
    return date.strftime('%d.%m.%Y')


def create_text_one_filial_data(filial):
    text = f"Название филиала: {filial['filial_name']}\n" \
           f"Кол-во телефонных номеров: {filial['count_phone_numbers']}\n" \
           f"Кол-во оцененных факторов: {filial['count_factors']}\n" \
           f"Всего оценок: {filial['all_scores']}\n" \
           f"Оценок 1: {filial['score_1']}\n" \
           f"Оценок 2: {filial['score_2']}\n" \
           f"Оценок 3: {filial['score_3']}\n" \
           f"Оценок 4: {filial['score_4']}\n" \
           f"Оценок 5: {filial['score_5']}\n" \
           f"Удовлетворенность: {filial['rating']}\n\n"
    return text
