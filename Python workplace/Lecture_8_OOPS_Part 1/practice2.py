# Create Account class with 2 attributes - balance & account no. 
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self, deb_bal):
        self.balance -= deb_bal
        print("From", self.account_no," this account",deb_bal,"tk was debited.")
        print("The total balace = ", self.get_balance())

    def credit(self, cred_bal):
        self.balance += cred_bal
        print("In", self.account_no," this account",cred_bal,"tk was debited.")
        print("The total balace = ", self.get_balance())
    
    def get_balance(self):
        return self.balance
    
    
acc1 = Account(10000, 12345)

acc1.debit(500)
# acc1.credit(500)