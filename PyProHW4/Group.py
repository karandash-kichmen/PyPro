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

# Exceptions
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