"""
1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії із зазначеним множником.
 Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу,
 або при передачі команди на завершення.
2. Реалізуйте свій аналог генераторної функції range().
3. Напишіть функцію-генератор, яка повертатиме прості числа. Верхня межа діапазону повинна бути задана
параметром цієї функції.
4. Напишіть генераторний вираз для заповнення списку. Список повинен бути заповнений кубами чисел
від 2 до вказаної вами величини.
"""


# geometric progression
def geometric_gen(start: int, stop: int, n: int):
    while start < stop:
        yield start
        start *= n


# prime number generator
def prime_gen(stop: int):
    for n in range(2, stop + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n



# range
def m_range(*args):
    start, stop, step = 1, None, 1
    if len(args) == 1:
        stop = args
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError('Invalid data')

    if not isinstance(start, int):
        raise TypeError('my_range() args must be int')
    if not isinstance(stop, int):
        raise TypeError('my_range() args must be int')
    if not isinstance(step, int):
        raise TypeError('my_range() args must be int')
    if not step:
        raise ValueError('Step arg must be > 0')
    if step < 0 and stop > start:
        return
    if step > 0 and stop < start:
        return
    while abs(start) < abs(stop):
        yield start
        start += step
