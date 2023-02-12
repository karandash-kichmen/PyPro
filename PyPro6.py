"""
1. Доповніть клас Група (завдання Лекції 2) можливістю підтримки ітераційного протоколу.
2. Модифікуєте клас Замовлення (завдання Лекції 1), додавши реалізацію протоколу послідовностей
та ітераційного протоколу.
"""

from dataclasses import dataclass


@dataclass
class Students:
    name: str
    surname: str


class Group:
    def __int__(self, title, max_student=10):
        self.title = title
        self.max_student = max_student
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.students[item]
        raise TypeError

    def __iter__(self):
        return GroupIter(self, self.students)

    def __str__(self):
        return '\n'.join(map(str, self.students))


class GroupIter:
    def __init__(self, students):
        self.items = students
        self.index = 0

    def __next__(self):
        if self.index < len(self.items):
            self.index += 1
            return self.items[self.index - 1]

    raise StopIteration


x1 = Students("Ivan1", "Ivanov1")
x2 = Students("Ivan2", "Ivanov2")
x3 = Students("Ivan3", "Ivanov3")
x4 = Students("Ivan4", "Ivanov4")

group = Group('Python')
group.add_student(x1)
group.add_student(x2)
group.add_student(x3)
group.add_student(x4)
