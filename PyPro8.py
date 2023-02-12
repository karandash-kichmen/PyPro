import timeit



# generator
def get_item(item):
    return item ** 2


def get_function(start, count, predicate):
    index = 0
    while index < count:
        yield predicate(start)
        start += 1
        index += 1


# for i in get_function(1, 20, get_item):
    # print(i)

# Memorization
stmt_1= """
def rec_fibonachi(m):
    if m <= 1:
        return m
    else:
        return (rec_fibonachi(m - 1) + rec_fibonachi(m - 2))
rec_fibonachi(30)
"""


stmt_2= """
def fibonachi():
    buf = [0, 1]

    def get_next(m):
        if m < len(buf):
            return buf[m]
        curr, next = buf[-2], buf[-1]
        index = len(buf)
        while index <= m:
            curr, next = next, curr + next
            buf.append(next)
            index += 1
        return next

    return get_next
f = fibonachi()
f(30)
"""
print(timeit.timeit(stmt_1, number=20))
print(timeit.timeit(stmt_2, number=20))
# 3



def func(seq, predicate):
    return sum(predicate(item) for item in seq)


x = [1, 2, 3, 4, 5, 6]
print(func(x, lambda item: item ** 2))
