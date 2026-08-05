'''Generators'''
'''Напишіть генератор, який повертає послідовність парних чисел від 0 до N.'''
def even_numbers(n):
    for k in range(0, n + 1, 2):
        yield k

print(list(even_numbers(10)))  # [0, 2, 4, 6, 8, 10]

'''Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.'''
def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

print(list(fibonacci_generator(100)))

'''Iterators'''
'''Реалізуйте ітератор для зворотного виведення елементів списку.'''
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


list_of_numbers = [11, 12, 13, 14, 15]

for num in ReverseIterator(list_of_numbers):
    print(num)   # 15, 14, 13, 12, 11

'''Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.'''
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


for num in EvenIterator(8):
    print(num)   # 0, 2, 4, 6, 8


'''Decorators'''
'''Напишіть декоратор, який логує аргументи та результати викликаної функції.'''
def log_sum_of_two_num(function):
    def wrapper(*args, **kwargs):
        print(f"Aргументи: {args}")
        result = function(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@log_sum_of_two_num
def sum_two_numbers(a, b):
    return a + b

print(sum_two_numbers(1, 2))

'''Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.'''
def catch_exceptions(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            print(f"Перехоплено виняток — {e}")
            return None
    return wrapper


@catch_exceptions
def check_value(k):
    if k is None:
        raise ValueError("значення не може бути None")
    return k


print(check_value("Test success"))
print(check_value(None))