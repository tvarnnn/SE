from savings import SavingsAcc
from checking import CheckingAcc


class RayBank:
    bank_name = "RayBank"

    def __init__(self,customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    
    def deposit(self,deposit):
        if isinstance(deposit, (int,float)):
            self.current_balance += deposit
            print("Your current balance is: ", self.current_balance)
        else:
            print("Please enter a number.")
    
    def withdraw(self, deposit):
        if self.current_balance - deposit < self.minimum_balance:
            print("You have a balance of",self.current_balance,". This is an insufficient amount of funds. Please deposit more") 
        else:
            self.current_balance -= deposit
            print("Withdrawal succesful, Current balance so far: ", self.current_balance)
    

    def print_customer_information(self):
        print(f"Welcome to: {RayBank.bank_name}")
        print("Welcome", self.customer_name)

        print("Current Balance:", self.current_balance)
        print("-----------------------------------")

        print("As a reminder the minimum balance for withdrawals is: ", self.minimum_balance)
        






# Example usage
check_acc = CheckingAcc("Bob", 200, 50, overdraft_limit=150)

check_acc.print_customer_information()
check_acc.withdraw(220)   # allowed with overdraft
check_acc.apply_fee()     # balance below minimum -> fee applied
check_acc.withdraw(300)   # exceeds overdraft -> denied






customer1 = RayBank("Jane", 500, 100)
customer2 = RayBank("Maxwell", 1000, 200)

customer1.deposit(200)
customer1.withdraw(700)  
customer1.print_customer_information()

customer2.withdraw(850) 
customer2.print_customer_information()
            