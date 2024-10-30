from backend import MENU, resources

profit = 0

def generate_report():
    """
    This function is used to generate a report of the coffee machine resources
    :return:
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}kg")
    print(f"Money: ${profit}")


def sufficient_resources(drink):
    """
    This function is used to determine if sufficient resources exist to make the requested drink
    :param drink:
    :return:
    """
    # make drink
    drink_ingredients = MENU[drink]['ingredients']
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True


def process_coins(drink):
    """
    This function is used to attempt to charge for an ordered drink
    :param drink:
    :return:
    """
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    money_deposited = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    cost_of_drink = MENU[drink]['cost']

    print(f"Money deposited: ${money_deposited:.2f}")
    print(f"Cost of the drink ordered: ${cost_of_drink:.2f}")

    change = money_deposited - cost_of_drink

    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${change:.2f} in change.")
        global profit
        profit += cost_of_drink
        return True


def adjust_resources(drink):
    """
    This function is used to adjust the machine resources after a drink has been sold
    :param drink:
    :return:
    """
    drink_ingredients = MENU[drink]['ingredients']
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]

def make_drink(drink):
    """
    This function is used to process a transaction request to make a drink
    :param drink:
    :return:
    """
    if sufficient_resources(drink) and process_coins(drink):
        print(f"Here is your {drink}. Enjoy")
        adjust_resources(drink)


is_on = True

while is_on:
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ")

    match drink_choice:
        case "report":
            generate_report()
        case "off":
            exit(0)
        case _:
            make_drink(drink_choice)
