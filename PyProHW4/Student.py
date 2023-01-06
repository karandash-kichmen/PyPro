import logging
# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
# 'application' code

class Human:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class Student(Human):

    def __init__(self, name: str, surname: str, age: int):
        if not isinstance(age, int):
            logger.warning(TypeError())
            raise TypeError()

        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'{super().__str__()}, {self.age}'