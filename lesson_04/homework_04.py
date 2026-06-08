adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

#   ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3

# task 01
"""Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer_one = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer_one)

# task 02
""" Замініть .... на пробіл"""
adwentures_of_tom_sawer_two = adwentures_of_tom_sawer_one.replace("....", " ")
print(adwentures_of_tom_sawer_two)

# task 03
"""Зробіть так, щоб у тексті було не більше одного пробілу між словами."""
adwentures_of_tom_sawer_three_total = " ".join(adwentures_of_tom_sawer_two.split())
print(adwentures_of_tom_sawer_three_total)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h" """
adwentures_of_tom_sawer_four = adwentures_of_tom_sawer.count("h")
print(adwentures_of_tom_sawer_four)

# task 05
"""Виведіть, скільки слів у тексті починається з Великої літери?"""
count_capital = 0
for word in adwentures_of_tom_sawer.split():
    word = word.strip('".,;:!?')
    if word and word[0].isupper():
        count_capital += 1
print(count_capital)

# # task 06
"""Виведіть позицію, на якій слово Tom зустрічається вдруге"""
first_tom = adwentures_of_tom_sawer.find("Tom")
second_tom = adwentures_of_tom_sawer.find("Tom", first_tom + 1)
print("Слово том зустрічажться вдруге:", second_tom)

# task 07
"""Розділіть змінну adwentures_of_tom_sawer по кінцю речення. Збережіть результат у змінній adwentures_of_tom_sawer_sentences"""
adwentures_of_tom_sawer_replace = adwentures_of_tom_sawer.replace("....", "")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_replace.split(".")
print(adwentures_of_tom_sawer_sentences)

# task 08
"""Виведіть четверте речення з adwentures_of_tom_sawer_sentences.Перетворіть рядок у нижній регістр."""
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
"""Перевірте чи починається якесь речення з "By the time"."""
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print(True)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences."""
adwentures_of_tom_sawer_last = adwentures_of_tom_sawer.replace("....", " ")
adwentures_of_tom_sawer_last_sentence = adwentures_of_tom_sawer_last.split(".")
word_count = (adwentures_of_tom_sawer_last_sentence[-2].split())
print("Кількість слів останнього речення:", len(word_count))