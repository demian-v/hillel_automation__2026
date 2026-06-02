# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була завжди в чотири рази більша, ніж яблук
apples = 2
bananas = apples * 4
print("Кількість яблук:", apples)
print(f"Кількість бананів: {bananas}")

#task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05 та виведіть його для користувача
perimetry = storona_1 + storona_2 + storona_3 + storona_4
print("Периметр дорівнює:", perimetry)

"""
    Задачі 07 -10:
    Переведіть задачі з книги "Математика, 2 клас"
    на мову пітон і виведіть відповідь, так, щоб було
    зрозуміло дитині, що навчається в другому класі
"""


# task 07
"""
    У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
    Скільки всього дерев посадили в саду?
"""
apples = 4
pears = apples + 5
plums = apples - 2
trees_total = apples + pears + plums
print("Яблук:", apples, end="\n")
print("Груш:", pears, end="\n")
print("Слив:", plums, end="\n")
print("Всього дерев:", trees_total)

# task 08
"""
    До обіда температура повітря була на 5 градусів вище нуля.
    Після обіду температура опустилася на 10 градусів.
    Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
zero_temperature = 0
before_lunch_temperature = zero_temperature + 5
after_lunch_temperature = before_lunch_temperature - 10
evening_temperature = after_lunch_temperature + 4
print("Температура повітря до обіду:", before_lunch_temperature, end="\n")
print("Температура повітря після обіду:", after_lunch_temperature, end="\n")
print("Температура повітря надвечір:", evening_temperature)

# task 09
"""
    Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
    1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
    Скількі сьогодні дітей у театральному гуртку?
"""
boys_in_theater_group = 24
girls_in_theater_group = boys_in_theater_group / 2
boys_in_theater_group_today = boys_in_theater_group - 1
girls_in_theater_group_today = girls_in_theater_group - 2
total_boys_and_girls_today = boys_in_theater_group_today + girls_in_theater_group_today
print("Кількість дітей у театральному гуртку сьогодні:", int(total_boys_and_girls_today))

# task 10
"""
    Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
    а третя - як половина вартості першої та другої разом.
    Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) / 2
total_books = first_book + second_book + third_book
print("Перша книга:", first_book)
print("Друга книга:", second_book)
print("Третя книга:", int(third_book))
print (f"Вартість всіх книг: {int(total_books)}")