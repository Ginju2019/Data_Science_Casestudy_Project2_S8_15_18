import math

class PiggyBank:
    #Pigg Bank

    def __init__(self):
        # initialize Piggy Bank current balance to zero
        self.balance_amt = 0        
    
    def addMoney(self, deposit_amount):        
        """ Add the user deposited amount with current balance
        
        Parameters:
        deposit_amount (float): User deposited amount
        """
        self.balance_amt = self.balance_amt + deposit_amount

    def withdrawMoney(self, withdraw_amount):
        """ Subtract the user withdrawal amount from current balance
        
        Parameters:
        withdraw_amount (float): User withdrawal amount
        """
        self.balance_amt = self.balance_amt - withdraw_amount
        
    def getCurrentBalance(self):
        """ Return the Piggy Bank current balance
        
        Returns:
        float:balance_amt
        """
        return self.balance_amt
    
    
class Error(Exception):
   """Base class for other exceptions"""
   pass

class WithdrawError(Error):
   """Raised when the withdrawal amount is more than account balance"""
   pass

class NewPiggyBank(PiggyBank):
    
    def withdrawMoney(self, withdraw_amount):
        """ Overridden method - Subtract the user withdrawal amount from current balance 
         with check for sufficient balance
        
        Parameters:
        withdraw_amount (float): User withdrawal amount
        """
        if (self.balance_amt - withdraw_amount) > 0:
            self.balance_amt = self.balance_amt - withdraw_amount
        else:
            raise WithdrawError #Exception('Overdraft withdrawal Error. Cannot withdraw more than amount in account balance: {}'.format(self.balance_amt))
        

# main code
print(" ")
print("--------------------Start-------------------")
piggyBankObj = NewPiggyBank()
while True:
    print(" ")
    app_init = input("Start or End : ")
    if app_init.strip().lower() == "start":
        user_action = input("Add, Withdraw or Check : ")
        if user_action.strip() == "Add":
            print(" ")
            deposit = float(input("Add amount : "))
            print(" ")
            piggyBankObj.addMoney(deposit)
            print("After adding, your updated balance is " + str(piggyBankObj.getCurrentBalance()) + " rupees")
            print("None")
            continue
        elif user_action.strip() == "Withdraw":
            print(" ")
            withdraw = float(input("withdraw amount: "))
            print(" ")
            try:
                piggyBankObj.withdrawMoney(withdraw)
                print("After withdrawing, balance amount is " + str(piggyBankObj.getCurrentBalance()) + " rupees")
                print("None")            
            except WithdrawError:
                print("Overdraft Withdrawal Error. Cannot withdraw amount that is more than your account balance amount")
                print("Your withdrawal amount is " + str(withdraw) + " rupees")
                print("Your current balance is   " + str(piggyBankObj.getCurrentBalance()) + " rupees")
                print(" ")
                continue
        elif user_action.strip() == "Check":
            print(" ")
            print("Your current balance is " + str(piggyBankObj.getCurrentBalance()) + " rupees")
            print("None")
            continue
        else :
            print(" ")
            print("Invalid Input.Try again")
            continue
    elif app_init.strip() == "End" :
        print(" ")
        print("------------Program Ended-----------")
        print(" ")
        break
    else :
        print(" ")
        print("Invalid Input. Try again")
        continue        
        
