#  «Дай задачу на Python уровня Junior+ / Middle на списки и словари»


text = input("Введите текст: ")
leght = len(text)
count_a = 0 
for letter in text:
    if letter.lower() == 'а':
        count_a += 1

text = text.replace(" ","").lower()
if text == text[::-1]:
    result = "Палиндром"
else:
    result = "Не палиндром"

print(f"""Количество символов: {leght}
Количество букв 'а': {count_a}
Результат проверки: {result}""")



