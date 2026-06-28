# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

lst2 = []
for item in lst1:
    if item % 2 == 0 and item != 0:
        lst2.append(item)

print(sum(lst2))