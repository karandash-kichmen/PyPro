# Homework 1 (03.11.2022)

# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару, опису товару
# габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.

# 2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище, ім'я, по батькові,
# мобільний телефон тощо.

# 3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості. Замовлення має містити дані
# про користувача, який його здійснив. Реалізуйте метод обчислення сумарної вартості замовлення. Визначте метод str()
# для коректного виведення інформації про це замовлення.

#######################################################################################################################
class Goods:
    def __init__(self, price, descr, size):
        self.price = price
        self.descr = descr
        self.size = size

    def __str__(self):
        return f'{self.descr} {self.price} '


class Customer:
    def __init__(self, name, sname, fname):
        self.name = name
        self.sname = sname
        self.fname = fname

    def __str__(self):
        return f'{self.sname} {self.name} {self.fname}'


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.goods = []
        self.quantities = []

    def add_product(self, product, quantity=1):
        if product in self.goods:
            index = self.goods.index(product)
            self.quantities[index] += quantity
        else:
            self.goods.append(product)
            self.quantities.append(quantity)

    def total(self):
        summa = 0
        for index, item in enumerate(self.goods):
            summa += item.price * self.quantities[index]
        return summa

    def __str__(self):
        res = ''
        for item, quantity in zip(self.goods, self.quantities):
            res += f'{item} x {quantity} = {item.price*quantity} UAH \n'
        return res


goods_1 = Goods(99, 'orange', 100)
goods_2 = Goods(120, 'apple', 150)

customer_1 = Customer('A', 'Denezh', 'V')
customer_2 = Customer('I', 'Ivanov', 'I')

order_1 = Order(customer_1)
order_1.add_product(goods_1, 3)
order_1.add_product(goods_2)

print(order_1)