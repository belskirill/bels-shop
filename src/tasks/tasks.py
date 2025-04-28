import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src.config import settigns
from src.tasks.celery_app import celery_instance


@celery_instance.task
def change_password(receiver_email):
    sender_email = settigns.EMAIL
    receiver_email = receiver_email
    sender_password = settigns.SENDER_PASSWORD
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    message = MIMEMultipart("alternative")
    message["Subject"] = "Подтверждение смены пароля"
    message["From"] = sender_email
    message["To"] = receiver_email

    html = """\
    <html>
      <body>
        <p>Здравствуйте!<br><br>
           Вы изменили свой пароль на сайте bels-shop.<br>
           <b>Если это были не вы</b>, пожалуйста, обратитесь в тех.поддержку.<br><br>
           С уважением, команда bels-shop.
        </p>
      </body>
    </html>
    """

    part2 = MIMEText(html, "html")

    message.attach(part2)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Письмо отправлено!")