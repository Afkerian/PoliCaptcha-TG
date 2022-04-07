from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class mensaje_Bot():

    # Creacion del mensaje
    mensaje = MIMEMultipart("alternative")  # standar

    def __init__(self, username, destinatario, subject) -> None:
        self.mensaje["From"] = username
        self.mensaje["To"] = destinatario
        self.mensaje["Subject"] = subject

    def set_html(self, html) -> None:
        self.mensaje.attach(MIMEText(html, "html"))

    def get_msg(self) -> MIMEMultipart:
        return self.mensaje
