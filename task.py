#  «Дай задачу на Python уровня Junior+ / Middle на списки и словари»


things = ["палатка", "нож", "спальник", "котел", "спички", "еда", "карта"]
backpack = []
for i in things :
    if len (i) <= 3:
        backpack.append(i)
print (f"В рюкзаке {len(backpack)} предметов: {backpack}")