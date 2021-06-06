MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
is_On = True

def compare_cost():
    global profit
    drink = MENU[choice]
    mrp = drink['cost']
    change = round(payment - mrp,2)
    if mrp > payment:
        print(f"Not enough Money. You are short of ${change}")
        return False
    elif mrp == payment:
        profit += payment
        return True
    elif mrp<payment:
        profit += mrp
        print(f"Here's your extra ${change} change.")
        return change


def deduct_resources():
    drink = MENU[choice]
    drink_ingredient = drink['ingredients']
    for item in drink_ingredient:
        resources[item] =  resources[item] - drink_ingredient[item]

    return resources[item]





def is_resources_suffcient(order_indegrient):
    for item in order_indegrient:
        if order_indegrient[item]>resources[item]:
            print(f"Sorry there is not enough{item}.")
            return False
    return True

def process_coins():
    print("Please enter the coins")
    total = int(input("How many quater? :")) * 0.25
    total += int(input("How many dimes? :")) * 0.1
    total += int(input("How many nikal? :")) * 0.05
    total += int(input("How many pennies? :")) * 0.01
    return total

while is_On:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice =="off":
        is_On = False
    elif choice =="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_suffcient(drink['ingredients']):
            payment = process_coins()
            if compare_cost():
                print("Here your Drink. Enjoy!!")
                deduct_resources()
