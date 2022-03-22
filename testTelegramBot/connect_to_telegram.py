from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    InlineQueryHandler,
)
import yaml


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
    created_link = create_one_user_invite_link(update,context,group_id)
    update.message.reply_text(f'Hello your link is {created_link}')


def hello(update: Update, context: CallbackContext) -> None:
    """
    Handler que se encarga de manejar el comando hello util para pruebas por el momento
    :param update: Update de la librería.
    :param context:Contexto de la librería.
    :return: None
    """
    print(update.message.chat.id)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def handler_new_member_joined(update: Update, context: CallbackContext) -> None:
    """
        Handler que se encarga de escuchar cuando un usuario se une al chat y comprueba si este esta permitido
        PD: Es necesario setearlo con Filters.status_update.new_chat_members para que escuche al usuario que se une
        :param update: Update de la librería.
        :param context:Contexto de la librería.
        :return: None
        """
    with open("token.yml") as n_token:
        n_service = yaml.safe_load(n_token)
        enabled_users = n_service["enabled_users"]
    print(check_new_chat_member_joined(enabled_users, update.message.new_chat_members))


def check_new_chat_member_joined(enabled_users: [str], joined_member_id: str) -> bool:
    """
    Verifica si un id de usuario pertenece a los usuarios permitidos.
    :param enabled_users: Lista de usuarios permitidos que debería ser creado luego de que el proceso de
                            solicitud se ha validado.
    :param joined_member_id: ID del nuevo miembro que se ha unido al grupo y que debería pertenecer a la lista.
    :return: True si el usuario pertenece a la lista.
    """
    for enabled_user in enabled_users:
        if joined_member_id == enabled_user :
            return True
    return False


def create_one_user_invite_link(update: Update, context: CallbackContext, group_id:str) -> str:
    """
    Crea un link para un solo usuario para un grupo específico basado en el id del grupo.
    :param update: Update de la librería.
    :param context: Contexto de la librería.
    :param group_id: ID del grupo del cual se requiere generar un link de invitación.
    :return: El link de la invitación al grupo especificado a través de su group_id
    """
    return update.message.bot.create_chat_invite_link(group_id, member_limit=1)


def create_main_invite_link(update: Update, context: CallbackContext) -> str:
    """
    Este método debería ejecutarse por primera vez en cada grupo del cual
    se requiera generar links, por el momento depende de que el usuario previamente
    envie un mensaje desde el grupo
    :return: El link principal de invitación al grupo requerido para poder crear los otros tipos de links
    """
    return update.message.chat.export_invite_link()

token_str = ""

with open("token.yml") as token:
    prime_service = yaml.safe_load(token)
    token_str = prime_service["token"]

updater = Updater(token_str)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('link', handler_generate_link_command))
updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, handler_new_member_joined))

updater.start_polling()
updater.idle()
