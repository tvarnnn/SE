from raybank import RayBank

class SavingsAcc(RayBank):
    def interest(self):
        if self.current_balance > 200:
            print("You are due to gain some interest on your crash if you keep", self.current_balance,"in the bank over time we will give you interest at a small rate into your account")
        else:
            print("Not enough money, need at least 200 to maintain balance without harm of fees or limitation of services.")
