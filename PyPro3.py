# Homework 3 (10.11.2022)

# 1. Модифікуйте Перше домашнє завдання так, щоб при спробі встановити від'ємну або нульову вартість товару викликалася
# виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати).

# 2. Модифікуйте Друге домашнє завдання так, щоб при спробі додавання до групи більше 10-ти студентів, викликалася
# виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати).

# Подію додавання нового студента до групи необхідно фіксувати у лог-файлі.
#######################################################################################################################

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

# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')


class GroupLimitError(Exception):
    def __init__(self, max_limit):
        self.max_limit = max_limit

    def __str__(self):
        return f'In group we already have  {self.max_limit} students.'


class DublicateStudentError(Exception):
    def __init__(self, student, group_title):
        self.student = student
        self.group_title = group_title

    def __str__(self):
        return f'The {self.student} registered in group {self.group_title}.'


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


class Group:

    def __init__(self, title: str, max_students: int = 10):
        if not isinstance(max_students, int):
            logger.warning(TypeError())
            raise TypeError()
        if max_students <= 0:
            logger.warning(ValueError())
            raise ValueError()

        self.title = title
        self.__students = []
        self.max_student = max_students

    def add_student(self, student: Student):
        """

        :param student:
        :return:
        """
        if student in self.__students:
            logger.warning(DublicateStudentError(student, self.title))
            raise DublicateStudentError(student, self.title)
        if len(self.__students) >= self.max_student:
            logger.warning(GroupLimitError(self.max_student))
            raise GroupLimitError(self.max_student)

        self.__students.append(student)

    def remove_student(self, student: Student):
        """

        :param student:
        :return:
        """
        if student in self.__students:
            self.__students.remove(student)

    def search_surname(self, surname: str):
        """

        :param surname:
        :return:
        """
        res = []
        for student in self.__students:
            if student.surname == surname:
                res.append(student)
        return res



    def __str__(self):
        return f'{self.title}\n\n' + '\n'.join(map(str, self.__students))


try:
    x = Group('Python', max_students=2)

    x.add_student(Student('Ivan', 'Ivanov3', 20))
    x.add_student(Student('Petro', 'Ivanov4', 20))
    x.add_student(Student('Ivan1', 'Ivanov5', 20))
    x.add_student(Student('Ivan1', 'Ivanov6', 20))
    x.add_student(Student('Ivan1', 'Ivanov7', 20))
    x.add_student(Student('Ivan1', 'Ivanov8', 20))
    x.add_student(Student('Ivan1', 'Ivanov9', 20))
    x.add_student(Student('Ivan1', 'Ivanov10', 20))
    x.add_student(Student('Ivan1', 'Ivanov11', 20))
    x.add_student(Student('Ivan1', 'Ivanov12', 20))

    res = x.search_surname('Ivanov12')

    if res:
        print(list(map(str, res)))

except Exception as error:
    print(error)