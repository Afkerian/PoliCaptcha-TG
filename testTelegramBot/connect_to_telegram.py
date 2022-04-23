from telegram import Update, Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext, CallbackQueryHandler, MessageFilter, ConversationHandler,
)
import yaml
import logging
# Para enviar los correos
from enviocorreos import correo_bot
# Enable logging
from testTelegramBot.EstudiantesNuevos import NewStudent

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

GROUP, EMAIL, CODE = range(3)


def get_group_id() -> str:
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

    return group_id

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

""""""
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
    # print(joined_member_id)
    print(check_new_chat_member_joined(enabled_users, joined_member_id))


def check_new_chat_member_joined(enabled_users: [int], joined_member_id: int) -> bool:
    """
    Verifica si un id de usuario pertenece a los usuarios permitidos.
    :param enabled_users: Lista de usuarios permitidos que debería ser creado luego de que el proceso de
                            solicitud se ha validado.
    :param joined_member_id: ID del nuevo miembro que se ha unido al grupo y que debería pertenecer a la lista.
    :return: True si el usuario pertenece a la lista.
    """

    flag = False
    for enabled_user in enabled_users:
        if joined_member_id == enabled_user:
            flag = True

    return flag


def send_links_to_emails(update: Update, context: CallbackContext, destinatario:str) -> None:
    """
    :param update: Update de la librería.
    :param context: Contexto de la librería.
    :return: None
    Se encarga de enviar correos electrónicos con links unicos para cada estudiante, no se pudo realizar la verificación
    planeada inicialmente, pues no se puede acceder a los numeros de los miembros del grupo mediante el bot y ademas, no
    se tiene en la base de datos la información de los IDs de lso estudiantes.
    """

    # Parametros para el envio de datos
    username = "example@epn.edu.ec"
    password = ""
    # Leer en la base de datos todos los correos, para realizar esta tarea
    subject = "Enlace de invitacion al grupo de Telegram"
    created_link = create_one_user_invite_link(update, context, get_group_id())
    # print(created_link)
    correo1 = correo_bot(username, password, destinatario, subject)
    html = generate_email_template(created_link, created_link)
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


def generate_email_template(join_faculty_link: str, join_fepon_link: str):
    """
    Este método lee la plantilla de correo y reemplaza los links donde pertenecen.
    :param join_faculty_link: Enlace de union a grupo de la facultad correspondiente
    :param join_fepon_link: Enlace de union a Grupo de fepon
    :return: String con la plantilla de correo preparada para el envío
    """
    with open("join_email.html", 'r', encoding='utf8') as html:
        body = html.read().replace("[GROUP_JOIN_FACULTY_LINK]", join_faculty_link)
        body = body.replace("[GROUP_JOIN_FEPON_LINK]", join_fepon_link)
        return body


logging_students = []
new_student = NewStudent()

def start(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about their gender."""
    reply_keyboard = [['AEIS', 'FEPON']]
    update.message.reply_text(
        'Bienvenido a Policaptcha\n'
        'A través de este bot podrás unirte a los grupos de telegram de la AEIS o de la FEPON 🤓',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='AEIS o FEPON?'
        ),
    )

    return GROUP


def group(update: Update, context: CallbackContext) -> int:
    """Stores the selected gender and asks for a photo."""
    user = update.message.from_user
    grupo = update.message.text

    new_student.name = user.first_name
    new_student.group = grupo
    new_student.id = user.id
    logger.info("Group of %s: %s", user.first_name, grupo)
    update.message.reply_text(
        'Listo\n'
        'Ingresa tu correo institucional para validar que seas parte de la EPN',
        reply_markup=ReplyKeyboardRemove(),
    )

    return EMAIL


def email(update: Update, context: CallbackContext) -> int:
    """Stores the photo and asks for a location."""
    user = update.message.from_user
    email1 = update.message.text
    new_student.email = email1
    logger.info("Email of %s: %s", user.first_name, email1)
    update.message.reply_text(
        'Perfecto, por último ingresa tu código único'
    )

    return CODE


def code(update: Update, context: CallbackContext) -> int:
    """Stores the location and asks for some info about the user."""
    user = update.message.from_user
    # user_location = update.message.location
    codigo_unico = update.message.text
    new_student.code = codigo_unico

    logger.info(
        "Code of %s: %s", user.first_name, codigo_unico
    )
    update.message.reply_text(
        'Listo, tu número único se ha validado\n'
        'Gracias por tu colaboración'
    )
    print(f"Nombre:" + new_student.name +"ID: " + str(new_student.id) + " Grupo:" + new_student.group + " Email:" + new_student.email + " Codigo: " + new_student.code)
    modify_users(new_student)
    send_links_to_emails(update,context,new_student.email)

    return ConversationHandler.END



def modify_users(student: NewStudent):
    with open("users.yml") as users:
        enabled_users = yaml.unsafe_load(users)["enabled_users"]

        enabled_users.append(student)

    dict_file = {'enabled_users': enabled_users}
    with open("users.yml", 'w') as users:
        yaml.dump(dict_file, users)


def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Chao! Te puedes unir a cualquiera de los grupos cuando desees', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


with open("token.yml") as token:
    prime_service = yaml.safe_load(token)
    token_str = prime_service["token"]

updater = Updater(token_str)

# Get the dispatcher to register handlers
dp = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        GROUP: [MessageHandler(Filters.regex('^(AEIS|FEPON)$') & ~Filters.command & Filters.text, group)],
        EMAIL: [MessageHandler(Filters.regex('^[a-zA-Z0-9.]+@epn.edu.ec') & ~Filters.command & Filters.text, email)],
        CODE: [MessageHandler(Filters.regex('^[0-9.]+') & ~Filters.command & Filters.text, code)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

dp.add_handler(conv_handler)
#dp.add_handler(CommandHandler('link', handler_generate_link_command))
dp.add_handler(CommandHandler('send_links', send_links_to_emails))
dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, handler_new_member_joined))

# dp.add_handler(CallbackQueryHandler())
# log all errors
dp.add_error_handler(error)

# Start the Bot
updater.start_polling()
updater.idle()
