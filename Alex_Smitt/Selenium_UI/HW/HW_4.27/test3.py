
print("Приветствую тебя в нашем интернет - магазине")

d = {1: "Sauce Labs Backpack", 2: "Sauce Labs Bike Light", 3: "Sauce Labs Bolt T-Shirt", 4: "Sauce Labs Fleece Jacket", 5: "Sauce Labs Onesie", 6: "Test.allTheThings() T-Shirt (Red)"}

print(f"Выбери один из товаров и укажи его номер: {d}")


while True:
    try:
        product = int(input())
        if product in list(d.keys()):
            print("Товар добавлен в корзину")
            break
        else:
            print("Такого продукта нет в наличии. Попробуйте еще раз")
    except ValueError:
        print("Вы ввели некорректное значение. Попробуйте еще раз")