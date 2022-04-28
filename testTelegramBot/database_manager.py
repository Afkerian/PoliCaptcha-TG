import psycopg2


def get_connection() -> psycopg2.connect:
    """
    Realiza la conexión con la base de datos "Policaptcha"
    :return:
    """
    global connection
    try:
        connection = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="password",
            database="Policaptcha"
        )
        #print("Conexión exitosa")

    except Exception as ex:
        print(ex)

    return connection

