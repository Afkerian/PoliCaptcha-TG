class NewStudents:
    code = 0
    email = ""
    name = ""
    group = ""

    def __init__(self) -> None:
        self.code = 0
        self.email = ""
        self.name = ""
        self.group = ""

    def set_code(self, code: int):
        self.code = code

    def set_email(self, email: str):
        self.email = email

    def set_name(self, name: str):
        self.name = name

    def set_group(self, group: str):
        self.group = group


