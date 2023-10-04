MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

dollars=0

def insert_coins():
    pennies=int(input("How many pennies would you like to insert? "))
    quarters=int(input("How many quarters would you like to insert? "))
    dimes=int(input("How many dimes would you like to insert? "))
    nickels=int(input("How many nickels would you like to insert? "))
    return pennies/100+quarters/4+dimes/10+nickels/20

def refill_needed(flavour):
    needed=[]
    if resources["water"]<MENU[flavour]["ingredients"]["water"]:
        needed.append("water")
    elif resources["milk"]<MENU[flavour]["ingredients"]["milk"]:
        needed.append("milk")
    elif resources["coffee"]<MENU[flavour]["ingredients"]["coffee"]:
        needed.append("coffee")
    return needed

def check_resources(flavour):
    if resources["water"]<MENU[flavour]["ingredients"]["water"] or resources["milk"]<MENU[flavour]["ingredients"][
            "milk"] or resources["coffee"]<MENU[flavour]["ingredients"]["coffee"]:
            return False
    else:
        return True
def make_coffee(flavour):
    resources["water"]-=MENU[flavour]["ingredients"]["water"]
    resources["milk"]-=MENU[flavour]["ingredients"]["milk"]
    resources["coffee"]-=MENU[flavour]["ingredients"]["coffee"]
    print(f"Here's you coffee. Your change is ${round(MENU[flavour]['cost'], 2)}")

should_continue=True
while should_continue==True:
    prompt=input("What would you like? (espresso/latte/cappuccino): ")

    if prompt=="report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")
    elif prompt in MENU:
        if check_resources(prompt):
            while dollars<MENU[prompt]["cost"]:
                print(f"You need {MENU[prompt]['cost']-dollars} more dollars.")
                dollars=dollars+insert_coins()
            make_coffee(prompt)
            dollars-=round(MENU[prompt]["cost"], 2)
            decision=input("Would you like to order again? (yes/no): ").lower()
            if decision=="no":
                 should_continue=False
                 print("Goodbye!")
        else:
            needed=refill_needed(prompt)
            needed_ingredients=", ".join(needed)
            print(f"Sorry, the coffee machine needs more {needed_ingredients}.")
    else:
        print("Please enter a valid option")
