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
        
    class SavingsAcc(Person):
        def interest(RayBank):
            if self.current_balance

    print("TEST TO SEE IF PULL REQUEST WILL WORK")

class SavingsAcc(RayBank):
    def interest(self):
        if self.current_balance > 200:
            print("You are due to gain some interest on your crash if you keep", self.current_balance,"in the bank over time we will give you interest at a small rate into your account")
        else:
            print("Not enough money, need at least 200 to maintain balance without harm of fees or limitation of services.")
        



class SavingsAcc(RayBank):
    def interest(self):
        if self.current_balance > 200:
            print("You are due to gain some interest on your crash if you keep", self.current_balance,"in the bank over time we will give you interest at a small rate into your account")
        else:
            print("Not enough money, need at least 200 to maintain balance without harm of fees or limitation of services.")


class checking_limitation(RayBank):
    def checking(self):
        if 





customer1 = RayBank("Jane", 500, 100)
customer2 = RayBank("Maxwell", 1000, 200)

customer1.deposit(200)
customer1.withdraw(700)  
customer1.print_customer_information()

customer2.withdraw(850) 
customer2.print_customer_information()
            