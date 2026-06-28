# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

while True:
    unique = input("Enter some value with letter 'h' or 'H': ")
    print(unique)

    if 'h' in unique or 'H' in unique:
        break