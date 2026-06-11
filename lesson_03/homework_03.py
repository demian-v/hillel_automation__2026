# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to." said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800

sum_area = black_sea + azov_sea

print("Площа Чорного та Азовського моря дорівнює:", sum_area, "км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_products = 375291
first_second_storage = 250449
second_third_storage = 222950

third_storage = total_products - first_second_storage
first_storage = total_products - second_third_storage
second_storage = total_products - third_storage - first_storage

print("Товарів на першому складі:", first_storage)
print("Товарів на другому складі:", second_storage)
print("Товарів на третьому складі:", third_storage)
print("Всього товарів на складі:", total_products)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
total_month = 18
full_computer_price = monthly_payment * total_month

print("Загальна вартість компʼютера:", full_computer_price, "грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
example_a = 8019 % 8
example_b = 9907 % 9
example_c = 2789 % 5
example_d = 7248 % 6
example_e = 7128 % 5
example_f = 19224 % 9

print(f"Варіант а: {example_a} \nВаріант b: {example_b} \nВаріант c: {example_c} \n"
      f"Варіант d: {example_d} \nВаріант e: {example_e} \nВаріант f: {example_f}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza = 274 * 4
medium_pizza = 218 * 2
juice = 35 * 4
cake = 350
water = 21 * 3

order_sum_total = big_pizza + medium_pizza + juice + cake + water

print("Загальна сума замовлення:", order_sum_total, "грн.")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
max_photo_per_page = 8

pages_total = all_photos / max_photo_per_page

print("Загальна кількість сторінок:", int(pages_total))

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

total_distance = 1600
fuel_consumption_per_100 = 9
car_tank = 48

total_fuel_consumption = (total_distance / 100) * fuel_consumption_per_100
min_number_refueling = total_fuel_consumption / car_tank

print("Загальна кількість літрів бензину:", int(total_fuel_consumption))
print("Мінімальна кількість заправок:", int(min_number_refueling))

