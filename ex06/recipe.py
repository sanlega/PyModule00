# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 15:18:11 by slegaris          #+#    #+#              #
#    Updated: 2023/05/10 15:53:05 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {
    'Sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'Cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'Salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}

def print_recipe_names():
    print("Recipes:")
    for recipe in cookbook:
        print(recipe)

def print_recipe_details(recipe_name):
    if recipe_name in cookbook:
        recipe = cookbook[recipe_name]
        print(f"Recipe for {recipe_name}:")
        print(f"Ingredients list: {recipe['ingredients']}")
        print(f"To be eaten for {recipe['meal']}.")
        print(f"Takes {recipe['prep_time']} minutes of cooking.")
    else:
        print(f"{recipe_name} not found in the cookbook.")

def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print(f"{recipe_name} has been deleted.")
    else:
        print(f"{recipe_name} not found in the cookbook.")

def add_recipe(recipe_name, ingredients, meal_type, prep_time):
    cookbook[recipe_name] = {
        'ingredients': ingredients,
        'meal': meal_type,
        'prep_time': prep_time
    }

def main():
    print("Welcome to the Python Cookbook!")
    while True:
        print("List of available options:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        print("Please select an option:")
        option = input(">> ")

        if option == "1":
            recipe_name = input("Enter a name:\n>> ")
            ingredients = input("Enter ingredients (comma-separated):\n>> ").split(',')
            meal_type = input("Enter a meal type:\n>> ")
            prep_time = int(input("Enter a preparation time:\n>> "))
            add_recipe(recipe_name, ingredients, meal_type, prep_time)
        elif option == "2":
            recipe_name = input("Enter a recipe name to delete:\n>> ")
            delete_recipe(recipe_name)
        elif option == "3":
            recipe_name = input("Enter a recipe name to get its details:\n>> ")
            print_recipe_details(recipe_name)
        elif option == "4":
            print_recipe_names()
        elif option == "5":
            print("Cookbook closed. Goodbye!")
            break
        else:
            print("Sorry, this option does not exist.")

if __name__ == "__main__":
    main()
