import smtplib
import ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from jinja2 import Environment, FileSystemLoader


class SendEmail:
    def __init__(self, data, config, first_date, last_date, xlsx_object):
        sender_file = open('sender.txt', 'r')
        login_password = sender_file.read().split(' ')
        self.sender_email = login_password[0]
        self.password = login_password[1]
        self.receiver_emails = config.get_emails()

        self.first_date = first_date
        self.last_date = last_date

        self.data = data

        self.message = MIMEMultipart()

        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)
        self.template = env.get_template('message.html')

        self.xlsx_object = xlsx_object

    def _set_subject(self):
        first_date_string = convert_datetime_to_string(self.first_date)
        last_date_string = convert_datetime_to_string(self.last_date)
        subject = f'МКГУ за период с {first_date_string} по {last_date_string}'
        self.message["Subject"] = subject

    def _set_from_to_mail(self):
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_emails

    def _create_message_text(self):
        text = ''
        header = f'Данные из МКГУ за период с {convert_datetime_to_string(self.first_date)} ' \
                 f'по {convert_datetime_to_string(self.last_date)}:\n\n\n'
        text += header

        for filial in self.data:
            text += create_text_one_filial_data(filial)
        return text

    def _create_message_html(self):
        render_message = self.template.render(first_date=convert_datetime_to_string(self.first_date),
                                              last_date=convert_datetime_to_string(self.last_date),
                                              filials=self.data)
        return render_message

    def _create_xlsx_file(self):
        filename = self.xlsx_object.get_all_path()
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            'attachment', filename=f'{self.xlsx_object.get_file_name()}.xlsx'
        )
        return part

    def _attack_message(self):
        # part1 = MIMEText(self._create_message_text(), "plain")
        part2 = MIMEText(self._create_message_html(), "html")
        # self.message.attach(part1)
        self.message.attach(part2)
        self.message.attach(self._create_xlsx_file())

    def _send_email(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.yandex.ru", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            for email in self.receiver_emails.split(', '):
                try:
                    server.sendmail(self.sender_email, email, self.message.as_string())
                    print(f'Данные успешно отправлены по адресу {email}')
                except Exception as _ex:
                    print(_ex)

    def send_email(self):
        self._set_subject()
        self._set_from_to_mail()
        self._attack_message()
        self._send_email()


def convert_datetime_to_string(date):
    return date.strftime('%d.%m.%Y')


def create_text_one_filial_data(filial):
    text = f"{filial['filial_name']}\n" \
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
