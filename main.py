from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
m = Menu()
amt = MoneyMachine()




isOn = True
while isOn:
    # TODO: 1. Prompt user by asking "what would you like? (espresso/latte/cappuccino): "
    option = input(f"What would you like? ({m.get_items()}): ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
    if option == "off":
        isOn = False

    # TODO: 3. Print report.
    elif option == "report":
        coffee.report()
        amt.report()
    else:
        order = m.find_drink(option)
        # TODO: 4 Check if resources are sufficient.
        sufficient = coffee.is_resource_sufficient(order)
        if sufficient:
            # TODO: 5. Process coins.
            # TODO: 6. Check if transaction is successful.
            successful = amt.make_payment(order.cost)
            if successful:
                # TODO: 7. Make coffee.
                coffee.make_coffee(order)
