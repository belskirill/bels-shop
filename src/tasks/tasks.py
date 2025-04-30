import asyncio
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src.config import settigns
from src.database import async_session_maker_null_pool
from src.tasks.celery_app import celery_instance
from src.utils.db_manager import DBManager


@celery_instance.task
def info_update_password(receiver_email):
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
           Подтвердите смену пароля на сайте bels-shop.<br>
           <b>Нажмите на кнопку ниже!</b>
            <button onclick="alert('Кнопка нажата!')">Нажми меня</button>

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


async def check_change_password_not_used_start():
    print("i start")
    async with DBManager(session_factory=async_session_maker_null_pool) as db:
        await db.password_change.delete_not_confirm()


@celery_instance.task(name="chech_not_used_change_password")
def check_not_used_where_change_password():
    asyncio.run(check_change_password_not_used_start())