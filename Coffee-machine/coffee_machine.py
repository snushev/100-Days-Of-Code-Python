MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coins():
    quarters = int(input("How many quarters do you have? "))
    dimes = int(input("How many dimes do you have? "))
    nickels = int(input("How many nickels do you have? "))
    pennies = int(input("How many pennies do you have? "))

    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01


def check_resources(resources):
    for resource in resources:
        if resources[resource] < drink["ingredients"][resource]:
            print(f"Sorry, the machine does not have enough {resource}")
            return False
    return True


def make_drink(resources, profit):
    resources["water"] -= drink["ingredients"]["water"]
    resources["milk"] -= drink["ingredients"]["milk"]
    resources["coffee"] -= drink["ingredients"]["coffee"]
    profit += drink["cost"]

    return resources, profit


is_on = True
while is_on:
    command = input("What would you like? (espresso/latte/cappuccino): ")

    if command == "off":
        is_on = False
        print("The coffee machine is turning off...")
    elif command == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit:.2f}")
    elif command in MENU:
        drink = MENU[command]
        enough_resources = check_resources(resources)
        if enough_resources:
            coins_ = coins()
            if coins_ < drink["cost"]:
                print("Insufficient funds. Here is your change.")
            else:
                resources, profit = make_drink(resources, profit)
                print(f"Here's your change: {coins_ - drink["cost"]:.2f}")
                print(f"Here's your {command}. Enjoy!")

