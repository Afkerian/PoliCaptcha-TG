import database_manager


class NewStudent:

    code = 0
    email = ""
    name = ""
    group = ""
    id = 0

    def __init__(self) -> None:
        self.code = 0
        self.email = ""
        self.name = ""
        self.group = ""
        self.id = 0

    def upload_student(self):
        """
        Carga al estudiante en la base de datos "telegram"
        :return:
        """
        db = database_manager.get_connection()
        cursor = db.cursor()
        """cursor.execute("INSERT INTO telegram ('idUser', 'userName', 'EstudiantesCodigoUnico') VALUES ('%s', %s, %s)",
                       (str(self.id), self.name, str(self.code)))"""

        sql = f"INSERT INTO telegram (\"idUser\",\"userName\",\"EstudiantesCodigoUnico\") VALUES (\'{str(self.id)}\', \'{self.name}\', \'{str(self.code)}\')"
        print(sql)
        # cursor.execute("INSERT INTO telegram ('idUser', 'userName', 'EstudiantesCodigoUnico') VALUES ('a', 'b', 'c')")
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()

    def check_student(self) -> bool:
        """
        Valida que el estudiante se encuentre dentro de la Tabla estudiantes. Actualmente solo toma en cuenta el correo
        :return:
        """
        db = database_manager.get_connection()
        cursor = db.cursor()
        sql = f"SELECT  \"codigoUnico\" FROM estudiantes WHERE \"codigoUnico\" = \'{self.code}\' "
        cursor.execute(sql)
        x = cursor.fetchone()
        db.commit()
        cursor.close()
        db.close()
        return x is not None

    # ,                 (str(self.id), self.name, str(self.code))
