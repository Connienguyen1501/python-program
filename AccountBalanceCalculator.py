class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
      
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance += amount
        return self.balance
        
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.balance -= amount
        self.balance < 0 
        get_fees = 5
        return self.balance
        
    def get_balance(self):
        """Returns the current balance in the account."""
        get_balance = self.balance
        return get_balance
    
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        self.balance < 0
        get_fees = 5
        return get_fees

my_account = BankAccount(10)
my_account.withdraw(15)
my_account.deposit(20)
print my_account.get_balance(), my_account.get_fees()
