'''Оберіть від 3 до 5 різних домашніх завдань
- перетворюєте їх у функції (якщо це потрібно)
- створіть в папці файл homeworks.py куди вставте ваші функції з дз
- та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
- імпорт та самі тести помістіть в окремому файлі - test_homeworks08.py
На оцінку впливає як якість тестів так і розмір тестового покриття. Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію. '''


"""  Написати функцію, яка обчислює суму двох чисел."""
def sum_two_numbers(first, second):
    return first + second
print(sum_two_numbers(1, 2))


""" Виведіть, скількі разів у тексті зустрічається літера "h" """
def count_letter(text, letter):
    """
    :param text: text for searching
    :param letter: letter for searching
    :return: count of letter in text
    """
    return text.count(letter)


""" Замініть .... на пробіл"""
def replace_dots(text):
    """
    :param text: text for task
    :return:  replacing dots by spaces
    """
    return text.replace("....", " ")


"""Зробіть так, щоб у тексті було не більше одного пробілу між словами."""
def clean_text(text):
    """
    :param text: text for task
    :return: text with no more than one space
    """
    return " ".join(text.split())






