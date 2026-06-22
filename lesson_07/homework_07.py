# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_two_numbers(first, second):
    return first + second
print(sum_two_numbers(1, 2))



# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
list_of_numbers = [1,2,3,4,5,6]

def sum_two_numbers(list_of_numbers):
    return sum(list_of_numbers) / len(list_of_numbers)
print(sum_two_numbers(list_of_numbers))


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
string_line = "Hello World"

def reverse_string(string_line):
    return string_line[::-1]

print(reverse_string(string_line))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
list_of_words = ["One", "Two", "Three", "Four", "Five"]

def longest_word(list_of_words):
    return max(list_of_words, key=len)
print(longest_word(list_of_words))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1




# # task 7
# task 04
black_sea = 436402
azov_sea = 37800

def sum_area(black_sea, azov_sea):
    """Повертає сумарну площу двох морів у км²."""
    return black_sea + azov_sea

print("Площа Чорного та Азовського моря дорівнює:", sum_area(black_sea, azov_sea), "км2")

# # task 8
total_products = 375291
first_second_storage = 250449
second_third_storage = 222950

def find_products(total_products, first_second_storage, second_third_storage):
    '''Шукає кількість товарів на кожному складі.'''
    third_storage = total_products - first_second_storage
    first_storage = total_products - second_third_storage
    second_storage = total_products - third_storage - first_storage
    return first_storage, second_storage, third_storage   # ← first, second, third

first_storage, second_storage, third_storage = find_products(
    total_products, first_second_storage, second_third_storage)

print("Товарів на першому складі:", first_storage)
print("Товарів на другому складі:", second_storage)
print("Товарів на третьому складі:", third_storage)
print("Всього товарів на складі:", total_products)

# # task 9
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
total_month = 18

def full_computer_price(monthly_payment, total_month):
    """Повертає загальну вартість компʼютера."""
    return monthly_payment * total_month

print("Загальна вартість компʼютера:", full_computer_price(monthly_payment, total_month), "грн.")

# # task 10
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
max_photo_per_page = 8

def pages_total(all_photos, max_photo_per_page):
    """Повертає загальну кількість сторінок потрібних для
    вклеєння фотографій."""
    return all_photos / max_photo_per_page

print("Загальна кількість сторінок:", int(pages_total(all_photos, max_photo_per_page)))

# """  Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.
# """