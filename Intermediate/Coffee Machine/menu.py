# menu.py

# Defines menu of drinks and their ingredients and prices
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

def display_menu():
    print("-" *24)
    print("          Menu          ")
    print(f"{'Drink':<15}{'Cost ($)':<10}")
    print("-" * 24)
    for drink, details in MENU.items():
        print(f"{drink:<15}{details['cost']:<10.2f}")
    print("-" * 24)
