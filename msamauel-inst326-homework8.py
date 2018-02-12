#Mihrete Samuel
#11/19/17
#Homework 8
#Question 1

class BankAccount():
    def __init__(self, owner= "None", checking= 0, savings=0 ):
        self.owner= owner
        self.checking = checking
        self.savings = savings

    def displayBalance(self):   #Method that displays current balance of a person
        print(self.owner, self.checking, self.savings)    #Prints out self version of variables for abstraction

    def deposit(self, toChecking=0, toSavings=0):  #Method that makes deposits into checking and savings
        self.checking += toChecking  #add to checking
        self.savings += toSavings    #add to savings

    def checking2savings(self, transfer=0):
        self.checking -= transfer
        self.savings += transfer

    def __add__(self, other):  #Overload method that helps concatenate 2 bank objects together
        return self.owner + "+" + other.owner, self.checking + other.checking, self.savings + other.savings



b1 = BankAccount("M", 5,5)
b2 = BankAccount("A", 1, 1)
print(b1 + b2)


