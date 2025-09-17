class RayBank:
    bank_name = "RayBank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

        # Protected member | Tristan
        self._account_number = account_number  

        # Private member | Tristan
        self.__routing_number = routing_number  

    def deposit(self, deposit):
        if isinstance(deposit, (int, float)):
            self.current_balance += deposit
            print("Your current balance is: ", self.current_balance)
        else:
            print("Please enter a number.")
    
    def withdraw(self, deposit):
        if self.current_balance - deposit < self.minimum_balance:
            print("You have a balance of", self.current_balance, 
                  ". This is an insufficient amount of funds. Please deposit more") 
        else:
            self.current_balance -= deposit
            print("Withdrawal successful, Current balance so far: ", self.current_balance)
    
    def print_customer_information(self):
        print(f"Welcome to: {RayBank.bank_name}")
        print("Welcome", self.customer_name)
        print("Current Balance:", self.current_balance)
        print("Account Number (protected):", self._account_number)
        print("Routing Number (private):", self.__routing_number)
        print("-----------------------------------")
        print("As a reminder the minimum balance for withdrawals is: ", self.minimum_balance)


# Example usage
customer1 = RayBank("Jane", 500, 100, "12345678", "111000025")
customer2 = RayBank("Maxwell", 1000, 200, "87654321", "222000111")

customer1.deposit(200)
customer1.withdraw(700)  
customer1.print_customer_information()

customer2.withdraw(850) 
customer2.print_customer_information()
