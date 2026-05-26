#  «Дай задачу на Python уровня Junior+ / Middle на списки и словари»


menu = {
    "cola" : 50,
    "chips" : 60,
    "chocolate" : 40
}

print("Добро пожаловать в магазин! Выберите товар:")
for product, price in menu.items():
    print(f"- {product}: {price} руб.")
user_product = input("\nВведите название товара: ").lower().strip() 
user_money = int(input("Введите количество денег: "))
if user_product in menu: 
     if user_money >= menu[user_product]:
        change = user_money - menu[user_product]
        print(f"Вы купили {user_product} за {menu[user_product]} руб. Ваша сдача: {change} руб.")
     else:
        print("Недостаточно денег")
else:
    print("Товар не найден")