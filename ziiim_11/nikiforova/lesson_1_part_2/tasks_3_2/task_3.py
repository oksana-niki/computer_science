"""
### 3.2.3 Задача 3: “Ресторан”

Напишите приложение, представляющее собой меню ресторана,
состоящее из 10 блюд, которые:  
1) собраны в словарь, где содержится информация о названии в виде строки,
    цене в виде числа и составе блюда в виде списка ингредиентов;  
2) название блюда является ключом к переменной, содержащей ингредиенты и
    цену блюда: каждому из блюд присваивается словарь,  
3) этот словарь с меню должен находиться в классе как одна из его переменных;  
4) у этого класса есть функции:  
- функцию, выводящую все блюда с их ценами и составом в виде таблички в консоли;  
- функцию, выводящую по названию блюда его состав и цену и если блюда нет, то;  
- функцию, выводящую только вегетарианские блюда;  
- функцию, вычисляющую сумму к оплате по списку названий блюд.
"""

# -*- coding: utf-8 -*-

class RestaurantMenu:
    def __init__(self):
        self.menu = {
            "Салат Овощной": {"price": 200, "ingredients": ["помидор", "огурец", "масло", "зелень"]},
            "Борщ": {"price": 300, "ingredients": ["свекла", "картофель", "мясо", "лук"]},
            "Пюре с котлетой": {"price": 350, "ingredients": ["картофель", "масло", "котлета (мясо)"]},
            "Плов": {"price": 320, "ingredients": ["рис", "морковь", "лук", "говядина"]},
            "Овощное рагу": {"price": 280, "ingredients": ["кабачки", "баклажан", "перец", "масло"]},
            "Каша гречневая": {"price": 150, "ingredients": ["гречка", "масло"]},
            "Омлет": {"price": 180, "ingredients": ["яйца", "молоко", "масло"]},
            "Куриный суп": {"price": 250, "ingredients": ["курица", "морковь", "картофель"]},
            "Фрукты": {"price": 120, "ingredients": ["яблоко", "груша", "банан"]},
            "Макароны по-флотски": {"price": 290, "ingredients": ["макароны", "фарш", "масло"]}
        }

    def show_all_dishes(self):
        print(f"{'Блюдо':<25} | {'Цена':<6} | Состав")
        print("-" * 60)
        for name, info in self.menu.items():
            ingredients = ", ".join(info["ingredients"])
            print(f"{name:<25} | {info['price']:<6} | {ingredients}")

    def show_dish(self, dish_name):
        dish = self.menu.get(dish_name)
        if dish:
            ingredients = ", ".join(dish["ingredients"])
            print(f"Блюдо: {dish_name}\nЦена: {dish['price']}\nСостав: {ingredients}")
        else:
            print(f"Блюдо '{dish_name}' не найдено в меню.")

    def show_vegetarian(self):
        print("Вегетарианские блюда:")
        non_veg = ["мясо", "курица", "котлета", "фарш"]
        for name, info in self.menu.items():
            if all(not any(nv in ingr for nv in non_veg) for ingr in info["ingredients"]):
                print(f" - {name}")


    def calculate_total(self, selected_dishes):
        total = 0
        for dish in selected_dishes:
            if dish in self.menu:
                total += self.menu[dish]["price"]
            else:
                print(f"Блюдо '{dish}' не найдено, пропущено.")
        print(f"Общая сумма к оплате: {total} руб.")


restaurant = RestaurantMenu()
restaurant.show_all_dishes()
print("\n--- Информация о блюде ---")
restaurant.show_dish("Борщ")
print("\n--- Вегетарианские блюда ---")
restaurant.show_vegetarian()
print("\n--- Итог по заказу ---")
restaurant.calculate_total(["Борщ", "Каша гречневая", "Фрукты", "Пельмени"])
