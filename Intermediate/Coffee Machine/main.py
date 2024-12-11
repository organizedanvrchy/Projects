# Coffee Machine OS Simulation
import os
import platform
import time
import menu
import resources

# Global variables
money_earned = 0

# Functions
def report():
    """Print current resources and money earned"""
    print(f"Water : {resources.resources['water']}ml")
    print(f"Milk  : {resources.resources['milk']}ml")
    print(f"Coffee: {resources.resources['coffee']}g")
    print(f"Money : ${money_earned}")

def check_resources(order_ingredients):
    """Return True if order can be made from current resources. 
    Otherwise this is False."""
    for i in order_ingredients:
        if order_ingredients[i] > resources.resources[i]:
            print(f"Sorry there is not enough {i} remaining.")
            return False
    return True

def process_coins():
    """Return total coin value calculated from coins inserted """
    print("\nPlease insert coins.")
    total =  int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? "))    * 0.10
    total += int(input("How many nickels? "))  * 0.05
    total += int(input("How many pennies? "))  * 0.01
    return total


def process_transaction(money_received, drink_cost):
    """Return True if payment is accepted, 
    or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money_earned
        money_earned += drink_cost
        return True
    else:
        print("\nSorry, that is not enough money. Money refunded.")
        print("\nRestarting...")
        time.sleep(3)
        clear_screen()
        return False

def process_order(drink_name, order_ingredients):
    """Deduct required ingredients from current resources"""
    for i in order_ingredients:
        resources.resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name} ☕! Enjoy!")

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")    # Clear command for Windows
    else:
        os.system("clear")  # Clear command for Unix/Linux/Mac

# Main
def main():
    machine_on = True
    while machine_on:
        menu.display_menu()
        choice = input ("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            print("\nShutting Down...")
            time.sleep(3)
            machine_on = False
        elif choice == "report":
            print("\nGenerating Report...")
            time.sleep(3)
            report()
            print("\nWould you like to exit to main menu?")
            print("WARNING: Entering 'N' will shut down machine!")
            exit = input("Y or N: ").upper()
            if exit == "Y":
                print("\nRestarting...")
                time.sleep(3)
                clear_screen()
            else:
                print("\nShutting Down...")
                time.sleep(3)
                machine_on = False
        else:
            try:
                drink = menu.MENU[choice]
                if check_resources(drink["ingredients"]):
                    try:
                        payment = process_coins()
                        print("\nProcessing order...")
                        time.sleep(3)
                    except ValueError:
                        print("\nInvalid entry. Please enter a valid coin amount.")
                        print("\nRestarting...")
                        time.sleep(3)
                        clear_screen()
                        continue
                    
                    if process_transaction(payment, drink["cost"]) == True:
                        print("\nMaking your drink...")
                        time.sleep(5)
                        process_order(choice, drink["ingredients"])
                        time.sleep(5)
                        clear_screen()
                else:
                    new_order = input("\nWould you like to purchase another drink? Y or N: ").upper()
                    if new_order == "Y":
                        clear_screen()
                        continue
                    else:
                        print("\nThank you. Goodbye...")
                        time.sleep(5)
                        machine_on = False
            except KeyError:
                print("\nInvalid choice. Please enter one of three drink names above.")
                print("\nRestarting...")
                time.sleep(3)
                clear_screen()
                
if __name__ == "__main__":
    main()
