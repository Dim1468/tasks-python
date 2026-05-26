#  «Дай задачу на Python уровня Junior+ / Middle на списки и словари»


secret_number = 7
while True :
    number = int(input('Введите число: '))
    if number == secret_number:
        print ("Ура, ты угадал!")
        break
    elif number < secret_number:
        print ("Загаданное число больше")
    else:
         print ("Загаданное число меньше")
    