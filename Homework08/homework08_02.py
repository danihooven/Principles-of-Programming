""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 08 - 02

Please write a class BankAccount for depositing and withdrawing money.
There should be two methods.
The method for withdrawing money should give warning message if the balance is not enough.
Do not update the balance if insufficient money in the bank account.
In addition, write a method to display the account balance.
You can overwrite the __str__ method to display the bank balance.

Note: Please write the whole program from scratch yourself, without looking at any examples.
This exercise it intentionally kept simple for that reason.


@author: Dani Hooven
@version: 10/27/2020

-------------------------------------------------------------------------------------------------------------------- """


# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# CLASSES
# ----------------------------------------------------------------------------------------------------------------------

class BankAccount:
    """BankAccount class for depositing and withdrawing money"""

    def __init__(self):
        self.balance = 0

    def __str__(self):
        """Return string representation"""
        return "Account Balance: " + str(self.balance)

    def deposit(self, amount):
        """Add amount to balance"""
        self.balance = self.balance + amount
        print("Amount Deposited: ", amount)

    def withdraw(self, amount):
        """Subtract amount from balance"""
        if (self.balance - amount) < 0:
            print("Insufficient Funds")
        else:
            self.balance = self.balance - amount
            print("Withdraw Amount: ", amount)


# ----------------------------------------------------------------------------------------------------------------------
# VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

my_account = BankAccount()

# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM
# ----------------------------------------------------------------------------------------------------------------------

print(my_account)

my_account.deposit(100)
print(my_account)

my_account.withdraw(120)
print(my_account)

my_account.withdraw(100)
print(my_account)


