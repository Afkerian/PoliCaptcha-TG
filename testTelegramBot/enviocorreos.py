import smtplib, ssl
from mensaje_bot import mensaje_Bot
#import getpass  Esto permite el ingreso de datos de forma segura
#getpass.getpass("Ingresa x dato: ")
class correo_bot():

    def __init__(self, username, password, destinatario, subject) -> None:
        self.username = username
        self.password = password
        self.destinatario = destinatario
        self.mensaje = mensaje_Bot(username, destinatario, subject)


    def enviar_correo(self) -> bool:
        """
        #Código para enviar correos a través de office365
        mailserver = smtplib.SMTP('smtp.office365.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login(self.username,self.password)
        print("Inicio sesión")
        # Adding a newline before the body text fixes the missing message body
        mailserver.sendmail(self.username,self.destinatario,self.mensaje.mensaje.as_string())
        print(f"Mensaje enviado a {self.destinatario}")
        mailserver.quit()"""


        #Código paraenviar correos en gmail
        context= ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
            server.login(self.username,self.password)
            print("Inicio sesión")
            server.sendmail(self.username,self.destinatario,self.mensaje.mensaje.as_string())
            print(f"Mensaje enviado a {self.destinatario}")


