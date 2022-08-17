from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while coffee_maker.is_on:
    options = menu.get_items()
    answer = input(f'What would you like? ({options}): ')
    if answer == 'off':
        coffee_maker.is_on = False
        print('The machine is now turned off.')
    elif answer == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        if answer in options:
            drink = menu.find_drink(answer)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print('This menu item does not exist.')
