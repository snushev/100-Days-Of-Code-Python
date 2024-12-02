from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
is_on = True

while is_on:
    print(f"\nPlease select your drink ({menu.get_items()})")
    choice = input()
    if choice == "off":
        is_on = False
        print("Goodbye!")
        break
    elif choice == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            money_machine.report()
