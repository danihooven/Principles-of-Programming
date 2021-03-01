""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Lab 04

Please update the following Python program to include additional methods:

a.	deposit(500) 		#Adds $500 to the account
b.	withdraw(500) 	#Takes $500 from the account
c.	transfer (b, 500) 	#Transfers $500 from the account to account b. Account b is bank account object.
d.	transactions() 		#Prints all the transactions line by line.
e.	overdraft_fees() 	#Prints the sum of overdraft fees. Assume $35 per one.
f.	another_method() 	#Create another method that you think necessary and change the name appropriately

Test each method comprehensively before submission.
For example, you cannot transfer $300 to another account, if your account has only $100.
If there is insufficient funds, do not update the balance.
Treat the overdraft fee as a separate fee.
Do not deduct the overdraft fee from the balance.

Hint: You will need to add more object properties.

@author: Dani Hooven
@version: 11/12/2020

-------------------------------------------------------------------------------------------------------------------- """


# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# CLASSES
# ----------------------------------------------------------------------------------------------------------------------

class BankAccount():

    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.overdraft = 0
        self.overdraft_amount = 35
        self.transaction_history = []
        self.interest_rate = float(.06)
        self.interest_amount = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append('deposit: {:.2f}'.format(amount))

    def withdraw(self, amount):
        """Subtract amount from balance"""
        if (self.balance - amount) < 0:
            print("Insufficient Funds")
            self.overdraft += self.overdraft_amount
            self.transaction_history.append('nsf overdraft fee: {:.2f}'.format(self.overdraft_amount))
        else:
            self.balance -= amount
            self.transaction_history.append('withdraw: {:.2f}'.format(amount))

    def transfer(self, trans_account, amount):
        if (self.balance - amount) < 0:
            print("Insufficient Funds")
            self.overdraft += self.overdraft_amount
        else:
            self.balance -= amount
            trans_account.deposit(amount)
            self.transaction_history.append('transfer: {:.2f}'.format(amount))

    def transactions(self):
        for each in self.transaction_history:
            print(each)

    def overdraft_fees(self):
        s = 'overdraft fees: {:.2f}'.format(self.overdraft)
        print(s)

    def status(self):
        s = '{}, {}, balance: {:.2f}'.format(self.name, self.no, self.balance)
        print(s)

    def interest(self): # new method
        self.interest_amount = self.balance * self.interest_rate
        self.balance += self.interest_amount
        self.transaction_history.append('interest: {:.2f}'.format(self.interest_amount))


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

account_a = BankAccount("Jack Skellington", 18594673, 0)
account_b = BankAccount("Sally Stein", 28495320, 0)

# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM
# ----------------------------------------------------------------------------------------------------------------------

account_a.status()
account_a.deposit(500)
account_a.deposit(200)
account_a.withdraw(200)
account_a.withdraw(600)
account_a.transfer(account_b, 500)
account_a.deposit(100)
account_a.interest()
account_a.status()
account_a.transactions()
account_b.interest()
account_b.status()
account_b.transactions()


