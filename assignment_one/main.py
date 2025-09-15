### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input."""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        return quarters + dimes + nickels + pennies

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if (coins >= cost):
            change = round(coins - cost, 2)
            if (change > 0):
                print(f"Here is ${change} in change.")
            print("Payment accepted.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"Here is your {sandwich_size} sandwich! Enjoy!")



### Running the machine ###
machine = SandwichMachine(resources)

is_on = True
while is_on:
    choice = input("What would you like? (small/medium/large/off): ").lower()
    if (choice == "off"):
        is_on = False
    elif (choice in recipes):
        sandwich = recipes[choice]
        if (machine.check_resources(sandwich["ingredients"])):
            payment = machine.process_coins()
            if (machine.transaction_result(payment, sandwich["cost"])):
                machine.make_sandwich(choice, sandwich["ingredients"])
    else:
        print("Invalid option. Please choose small, medium, or large.")
