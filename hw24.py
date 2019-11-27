import os
from pprint import pprint

# Чтение из файла
def read_file(path_to_file):
    cook_book = {}
    with open(path_to_file, 'r', encoding = "utf-8") as f:
        for line in f:
            if line.strip().isdigit():
                quantity = int(line)
            elif line.strip().find("|") == -1 and line.strip():
                name = line.strip().lower()
                cook_book[name] = []
            elif line.strip().find("|") != -1:
                ingredients = line.strip().split("|")
                list_ingredients = {"ingredient_name": ingredients[0], "quantity": int(ingredients[1]),
                                    "measure": ingredients[2]}
                cook_book[name].append(list_ingredients)
    return cook_book


# Создание списка
def get_shop_list_by_dishes(dishes_list, count):
    path_to_file = "./recipes.txt"
    cook_book = read_file(path_to_file)
    shopping_list = {}
    for dish in dishes_list:
        if dish not in cook_book:
            pass
        else:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shopping_list:
                    shopping_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                    'quantity': ingredient['quantity'] * count}
                else:
                    all_amount = shopping_list[ingredient['ingredient_name']]['quantity'] + ingredient['quantity'] * count
                    shopping_list[ingredient['ingredient_name']]['quantity'] = all_amount
    if shopping_list:
        pprint(shopping_list)
        return shopping_list
    else:
        print("Введенного блюда нет в списке")


# Получение данных для программы
def start_program():
    dishes_list = []
    while True:
        dish = input("Введите название блюда или ENTER для завершения ввода блюд: ")
        if not dish:
            person_count = int(input("Введите количество персон: "))
            get_shop_list_by_dishes(dishes_list, person_count)
            break
        else:
            dishes_list.append(dish.lower())


start_program()