import pandas as pd
import database_manager


def load_csv():
    """
    Carga el archivo CSV y lo retorna
    :return:
    """
    try:
        df1 = pd.read_csv("Path to Data2.csv",
                  delimiter=";")
        return df1
    except Exception as ex:
        print(ex)

def add_update_students():
    """
    Permite borrar toda la base de datos de estudiantes
    :return:
    """
    df1 = load_csv()
    db = database_manager.get_connection()
    cursor = db.cursor()
    for i in range(0, len(df1["codigoUnico"])):
        cod = df1["codigoUnico"][i]
        cor = df1["correo"][i]
        est = df1["estado"][i]
        rol = df1["rol"][i]

        sql = f"SELECT  \"codigoUnico\" FROM estudiantes WHERE \"codigoUnico\" = \'{cod}\' "
        cursor.execute(sql)
        aux = cursor.fetchone()
        if aux == None:
            sql = f"INSERT INTO estudiantes (\"codigoUnico\",\"correo\",\"estado\",\"rol\") VALUES " \
                  f"(\'{cod}\', \'{cor}\', \'{est}\', \'{rol}\')"
            cursor.execute(sql)
        else:
            sql = f"UPDATE estudiantes SET \"correo\"=\'{cor}\',\"estado\"=\'{est}\',\"rol\"=\'{rol}\'" \
                  f" WHERE \"codigoUnico\" = \'{cod}\' "
            cursor.execute(sql)

    cursor.close()
    db.commit()
    db.close()



def get_deleted_students() -> list:
    """
    Permite obtener los estudiantes que fueron borrados del csv de estudiantes, retorna la lista de ids de estos manes
    :return:
    """
    df1 = load_csv()
    db = database_manager.get_connection()
    cursor = db.cursor()
    sql = f"SELECT  \"codigoUnico\" FROM estudiantes WHERE "
    sql1 = ""
    for i in range(0, len(df1["codigoUnico"])):
        cod = df1["codigoUnico"][i]

        if i == 0:
            sql1 = f"\"codigoUnico\" != \'{cod}\' "
        else:
            sql1 += f"AND \"codigoUnico\" != \'{cod}\' "

    cursor.execute(sql+" ( "+sql1+" )")
    students = cursor.fetchall()
    cursor.close()
    db.commit()
    db.close()
    return students


def delete_students(students_id:list):
    """
    Borra de la base de datos a los estudiantes que no se encuentran en el archivo csv
    :param students_id: lista de tuplas que contienen a los ids de los estudiantes borrados
    :return:
    """
    for student_id in students_id:
        db = database_manager.get_connection()
        cursor = db.cursor()
        sql = f"DELETE FROM estudiantes WHERE  \"codigoUnico\" = \'{student_id[0]}\' "
        cursor.execute(sql)
        cursor.close()
        db.commit()
        db.close()


def total_update_estudiantes():
    """
    Realiza la actualización de la base de datos tal y como se encuentra el archivo csv
    :return:
    """
    add_update_students()
    delete_students(get_deleted_students())






