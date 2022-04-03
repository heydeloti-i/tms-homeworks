class Data():

    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
        self._clear_whitespaces(name, age)

    def _clear_whitespaces(self, name, age):
        self.name = name.strip()
        self.age = age.strip()
        self.age = int(age)

class DataWithDate(Data):

    def __init__(self, name: str, age: str):
        self.current_time = datetime.utcnow

class Validator:

    def __init__(self, data_history):
        self.data_history: list[Data] = []

    def _validate_name(self, data_history):
        """Проверка введенного имени"""
        if not self.data_history[-1].name:
            raise Exception('Вы не ввели имя.')

        elif len(self.data_history[-1].name) < 3:
            raise Exception('Минимальная длина имени - 3 символа.')

        elif self.data_history[-1].name.count(' ') > 1:
            raise Exception('Максимальное количество пробелов - 1 символ.')


    def _validate_age(self, data_history):
        """Проверка введенного возраста"""
        if self.data_history[-1].age <= 0:
            raise Exception('Вам не может быть 0 лет или меньше.')

        elif self.data_history[-1].age < 14:
            raise Exception('Программой запрещено пользоваться, если вам меньше 14 лет.')

    def validate(self, data: Data):
        self.data_history.append(data)
        self._validate_age(data_history[-1].age)
        self._validate_name(data_history[-1].name)
