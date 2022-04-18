import datetime
from typing import Optional, Union

import telegram
from telegram import Update, Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQueryResult, \
    InputMessageContent, InputTextMessageContent
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    DispatcherHandlerStop,
    Filters,
    CallbackContext, MessageFilter, ConversationHandler, CallbackQueryHandler,
)
import yaml
import logging
from modified_filters import NewFilter

from enviocorreos import correo_bot

logger = logging.getLogger(__name__)


def callback_query_handler(update: Update, context: CallbackContext):
    update.callback_query.message.reply_text("Has presionado el boton: "+update.callback_query.data)


def inline_buttons_test(update: Update, context: CallbackContext):
    msg = update.message.text.upper()
    keyboard = [[InlineKeyboardButton(text="Text1", callback_data="but1"),InlineKeyboardButton(text="Text2", callback_data="but2")],
                [InlineKeyboardButton(text="Text3", callback_data="but3"),InlineKeyboardButton(text="Text4", callback_data="but4")]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please select the judge or select all for showing all', reply_markup=reply_markup)




def handler_generate_link_command(update: Update, context: CallbackContext) -> None:
    """
    Handler para el comando /link, que generará un link para un grupo y se lo enviará al usuario,
    por el momento requiere de más estudio y personalización, respecto a los grupos que se genera y la validación.
    :param update: Update de la librería.
    :param context:Contexto de la librería.
    :return:
    """
    with open("token.yml") as token_f:
        service = yaml.safe_load(token_f)
        group_id = service["group_id"]

    with open("users.yml") as users:
        enabled_users = yaml.safe_load(users)["enabled_users"]

    created_link = create_one_user_invite_link(update, context, group_id)
    update.message.reply_text(f'Hello your link is {created_link}')
    enabled_users.append(update.effective_user.id)

    dict_file = {'enabled_users': enabled_users}
    with open("users.yml", 'w') as users:
        yaml.dump(dict_file, users)


def start(update: Update, context: CallbackContext) -> None:
  """
  Handler que se encarga de solicitar información al usuario como su correo.
  :param update: Update de la librería.
  :param context: Contexto de la librería.
  :return: None
  """


def save_email_users(update: Update, context: CallbackContext) -> None:
    """
    Handler que se encarga de solicitar información al usuario como su correo
    :param update: Update de la librería.
    :param context:Contexto de la librería.
    :return: None
    """
    print(update.message)


def handler_new_member_joined(update: Update, context: CallbackContext) -> None:
    """
        Handler que se encarga de escuchar cuando un usuario se une al chat y comprueba si este esta permitido
        PD: Es necesario setearlo con Filters.status_update.new_chat_members para que escuche al usuario que se une
        :param update: Update de la librería.
        :param context:Contexto de la librería.
        :return: None
        """
    with open("users.yml") as users:
        n_service = yaml.safe_load(users)
        enabled_users = n_service["enabled_users"]
    joined_member_id = update.message.new_chat_members[0].id

    print(check_new_chat_member_joined(enabled_users, joined_member_id))


def check_new_chat_member_joined(enabled_users: [int], joined_member_id: int) -> bool:
    """
    Verifica si un id de usuario pertenece a los usuarios permitidos.
    :param enabled_users: Lista de usuarios permitidos que debería ser creado luego de que el proceso de solicitud se ha validado.
    :param joined_member_id: ID del nuevo miembro que se ha unido al grupo y que debería pertenecer a la lista.
    :return: True si el usuario pertenece a la lista.
    """

    flag = False
    for enabled_user in enabled_users:
        if joined_member_id == enabled_user:
            flag = True

    return flag


def create_one_user_invite_link(update: Update, context: CallbackContext, group_id: str) -> str:
    """
    Crea un link para un solo usuario para un grupo específico basado en el id del grupo.
    :param update: Update de la librería.
    :param context: Contexto de la librería.
    :param group_id: ID del grupo del cual se requiere generar un link de invitación.
    :return: El link de la invitación al grupo especificado a través de su group_id
    """

    new_personal_link = update.message.bot.create_chat_invite_link(group_id, member_limit=1)
    return new_personal_link.invite_link


def send_links_to_emails(update: Update, context: CallbackContext) -> None:
    """
    Se encarga de enviar correos electrónicos con links unicos para cada estudiante
    :param update: Update de la librería.
    :param context: Contexto de la librería.
    :return: None

    """

    # Parametros para el envio de datos
    username = "correo@gmail.com"
    password = "password"
    lista_destinatarios = ["correo1@gmail.com"] #luis.andrade03@epn.edu.ec
    # Leer en la base de datos todos los correos, para realizar esta tarea
    subject = "Intento de envio de link de telegram"

    for destinatario in lista_destinatarios:

        created_link = create_one_user_invite_link(update, context, "-1001597618720")
        # print(created_link)
        correo1 = correo_bot(username, password, destinatario, subject)
        html = f"""
        <p> Hola {destinatario}, como estas Por favor accede a este link:
        <a href={created_link}>{created_link}</a>
        </p>
        """
        print(f"El destinatario es: "+destinatario)

        correo1.mensaje.set_html(html)
        correo1.enviar_correo()


def create_main_invite_link(update: Update, context: CallbackContext) -> str:
    """
    Este método debería ejecutarse por primera vez en cada grupo del cual
    se requiera generar links, por el momento depende de que el usuario previamente
    envie un mensaje desde el grupo
    :return: El link principal de invitación al grupo requerido para poder crear los otros tipos de links
    """
    return update.message.chat.export_invite_link()


def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


with open("token.yml") as token:
    prime_service = yaml.safe_load(token)
    token_str = prime_service["token"]

updater = Updater(token_str)

# Get the dispatcher to register handlers
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('link', handler_generate_link_command))
dp.add_handler(CommandHandler('send_links', send_links_to_emails))
#dp.add_handler(MessageHandler(Filters.update,inline_buttons_test))
dp.add_handler(CallbackQueryHandler(callback_query_handler))


# log all errors
dp.add_error_handler(error)

# Start the Bot
updater.start_polling()
updater.idle()
