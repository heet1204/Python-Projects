from data import MENU


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] = resources[item] - order_ingredients[item]
    print(f"Here is your {drink_name}, ENJOY!!")


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True


def process_coins():
    print("\nInsert Coins.")
    total = int(input("How many Rs 10 coins : ")) * 10
    total += int(input("How many Rs 5 coins : ")) * 5
    total += int(input("How many Rs 2 coins : ")) * 2
    total += int(input("How many Rs 1 coins : ")) * 1
    return total


def is_transaction_successful(received_money, drink_cost):
    if received_money >= drink_cost:
        change = received_money - drink_cost
        print(f"\nHere is Rs {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"\nTotal money inserted = {received_money}")
        print("SORRY THAT'S NOT ENOUGH MONEY, MONEY REFUNDED.")
        return False


resources = {"water": 500,
             "milk": 500,
             "coffee": 100,
             }
is_continue = True

wd = True
profit = 0

while is_continue:
    admin_logout = True
    choice = input("\nType 'a' for Admin and 'c' to buy Coffee : ").lower()
    check_pwd = True
    if choice == "a":
        while check_pwd:
            password = input("Enter the password : ")
            if password == "password":
                print("Hello Sir!")
                while admin_logout:
                    user_choice = input("\nType 'report' to check the resources or 'off' to turn of the machine : ")
                    if user_choice == "report":
                        print(f"\nWater: {resources["water"]} ml\nMilk: {resources["milk"]} ml")
                        print(f"Coffee: {resources["coffee"]} gm\nProfit: {profit} Rs")
                    elif user_choice == "off":
                        print("The coffee machine is turned off!!")
                        is_continue = False
                        admin_logout = False
                        check_pwd = False
                    elif user_choice == "end":
                        admin_logout = False
                        check_pwd = False
                    else:
                        print("Invalid Selection")
            else:
                print("Password Wrong, Try Again")

    elif choice == "c":
        user_choice = input("\nWhat would you like?\n1. Espresso | Cost: Rs 65/-\n"
                            "2. Latte | Cost: 152/-\n3. Cappuccino | Cost: Rs 109/-)\nInput: ").lower()
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
    else:
        print("Invalid Selection")
