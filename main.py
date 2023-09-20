def create_cook_book(text):
    cook_book = {}
    recipes = text.strip().split("\n\n")
    for recipe in recipes:
        lines = recipe.split("\n")
        name = lines[0]
        count_ingredients = int(lines[1])
        ingredients = []
        for i in range(2, count_ingredients + 2):
            ingredient_line = lines[i].split("|")
            ingredient_name = ingredient_line[0].strip()
            quantity = int(ingredient_line[1])
            measure = ingredient_line[2].strip()
            ingredient = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
            ingredients.append(ingredient)
        cook_book[name] = ingredients
    return cook_book

def create_products(dishes, person_count, cook_book):
    products = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name in products:
                    products[ingredient_name]['quantity'] += quantity
                else:
                    products[ingredient_name] = {'quantity': quantity, 'measure': measure}
        else:
            print(f'Не найдено блюдо: {dish}')
    return products


with open("recipes.txt", encoding="utf-8") as f:
    text = f.read()

cook_book = create_cook_book(text)
dishes = ['Омлет', 'Фахитос']
person_count = 2
print(create_products(dishes, person_count, cook_book))







