# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True,
# інакше - False. Строку отримати за допомогою функції input()

unique = input("Enter some value: ")

unique = set(unique)

if len(unique) > 10:
    print(True)
else:
    print(False)