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

Money = 0


def money(coffee):
    global Money
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    budget = quarters + dimes + nickels + pennies
    if budget >= MENU[coffee]["cost"]:
        change = budget - MENU[coffee]["cost"]
        Money += MENU[coffee]["cost"]
        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {coffee}. Enjoy!")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def is_enough_resources(coffee):
    enough = []
    if coffee == "espresso":
        if not MENU[coffee]["ingredients"]["water"] <= resources["water"]:
            enough.append("water")
        if not MENU[coffee]["ingredients"]["coffee"] <= resources["coffee"]:
            enough.append("coffee")
    elif coffee == "latte" or coffee == "cappuccino":
        if not MENU[coffee]["ingredients"]["water"] <= resources["water"]:
            enough.append("water")
        if not MENU[coffee]["ingredients"]["coffee"] <= resources["coffee"]:
            enough.append("coffee")
        if not MENU[coffee]["ingredients"]["milk"] <= resources["milk"]:
            enough.append("milk")

    if enough:
        print(f"Sorry, there is not enough {', '.join(enough)}.")
        return False
    else:
        return True


def coffee_report():
    global keep_going
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    keep_going = is_enough_resources(coffee)
    if coffee == "report":
        report()
    elif keep_going and [coffee == "espresso" and coffee == "latte" and coffee == "cappuccino"]:
        keep_going = money(coffee)
        if coffee == "espresso" and keep_going:
            resources["water"] -= MENU[coffee]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
        elif coffee == "latte" and keep_going:
            resources["water"] -= MENU[coffee]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
            resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
        elif coffee == "cappuccino" and keep_going:
            resources["water"] -= MENU[coffee]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
            resources["milk"] -= MENU[coffee]["ingredients"]["milk"]

    coffee_report()


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${Money}")


# Programı başlat
coffee_report()
