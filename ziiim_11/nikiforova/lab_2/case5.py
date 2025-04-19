"""
### 3.2.5. Задача 5: "Графический интерфейс для задачи 3 с PyQt5"

Напишите простейший графический интерфейс, который выводит меню блюд
в поле <QPlainTextEdit>, позволяет просматривать простое и вегетарианское меню,
цену и состав блюд, подсчитывать стоимость заказа.
"""
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem
from PyQt5 import uic

class RestaurantApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("restaurant.ui", self)

        # Меню
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

        self.total = 0

        # Сигналы
        self.pushButtonAll.clicked.connect(self.show_all_dishes)
        self.pushButtonVeg.clicked.connect(self.show_vegetarian)
        self.pushButtonAdd.clicked.connect(self.add_to_order)
        self.listWidgetMenu.itemClicked.connect(self.show_ingredients)

        # Показать всё меню при запуске
        self.show_all_dishes()

    def show_all_dishes(self):
        self.listWidgetMenu.clear()
        for dish in self.menu:
            self.listWidgetMenu.addItem(dish)

    def show_vegetarian(self):
        self.listWidgetMenu.clear()
        non_veg = ["мясо", "курица", "котлета", "фарш"]
        for name, info in self.menu.items():
            if all(not any(nv in ingr for nv in non_veg) for ingr in info["ingredients"]):
                self.listWidgetMenu.addItem(name)

    def show_ingredients(self, item):
        dish_name = item.text()
        info = self.menu[dish_name]
        self.listWidgetIngredients.clear()
        self.listWidgetIngredients.addItems(info["ingredients"])
        self.labelPrice.setText(f"{info['price']} руб.")

    def add_to_order(self):
        item = self.listWidgetMenu.currentItem()
        if item:
            dish = item.text()
            self.listWidgetOrder.addItem(dish)
            self.total += self.menu[dish]["price"]
            self.labelTotal.setText(f"{self.total} руб.")

def main():
    app = QApplication(sys.argv)
    window = RestaurantApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
