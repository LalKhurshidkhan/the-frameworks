class Bankaccount:
    def __init__(self,onwer,balance):
        self.onwer = onwer
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficent Balance!!!!!!")

acc = Bankaccount("lal" ,5000)
acc.deposit(2000)
acc.withdraw(6000)
print(acc.balance)  
    


# method method are function inside a class
# class methods are function inside a class that can be called without creating an object of the class
# they describe what an obj can do and how to be done 

class WashingMachine:
    def wash(self):
        print("Washing started...")

    def dry(self):
        print("Drying clothes...")

# here wash and dry are method