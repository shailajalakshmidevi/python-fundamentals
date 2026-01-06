class BankAccount:
    INTEREST_RATE = 0.03

    def __init__(self, name, balance):
        http://self.name = name
        self.balance = balance
        self.transactions = []
        self.transactions.append(f'The initial amount deposited in {balance}')


## create the method deposite
## check amount less than o equal to 0, if satisified raise error else add amt to balnce
## and transaction to list

b1 = BankAccount('Steve', 20000)
print(http://b1.name, b1.balance, b1.transactions)
 

class BankAccount:
    INTEREST_RATE = 0.03

    def __init__(self, name, balance):
        http://self.name = name
        self.balance = balance
        self.transactions = []
        self.transactions.append(f'The initial amount deposited in {balance}')

    def deposit(self, amount):
        if amount <= 0:
            raise Exception(f"You can't deposit amount {amount}")
        self.balance += amount
        self.transactions.append(f'The amount deposited is {amount}')

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("you don't have enough money")
        self.balance -= amount
        self.transactions.append(f'The amount withdrawn is {amount}')

    def statement(self):
        for transaction in self.transactions:
            print(transaction)

    def roi(self):
        interest_amount = self.balance * self.INTEREST_RATE
        self.balance += interest_amount
        self.transactions.append(f'The amount credited as interest is {interest_amount}')

b1 = BankAccount('Steve', 20000)
# print(http://b1.name, b1.balance, b1.transactions)
# b1.deposit(0)
# b1.deposit(10000)
# print(b1.balance, b1.transactions)
# b1.withdraw(50000)
# b1.withdraw(10000)
# print(b1.balance, b1.transactions)
# b1.statement()
# b1.roi()
# print(b1.balance, b1.transactions)

class SavingsAccount(BankAccount):
    INTEREST_RATE = 0.04

    def withdraw(self, amount):
        if amount > 10000:
            raise Exception("the maximum limit to withdraw the amount is 10000")
        super().withdraw(amount)            ## method chaining

s1 = SavingsAccount('John', 30000)
# print(s1.balance, s1.transactions)
# s1.deposit(0)
# s1.deposit(40000)
# print(s1.balance, s1.transactions)
# s1.withdraw(15000)
# s1.withdraw(10000)
# print(s1.balance, s1.transactions)
# s1.statement()
# s1.roi()
# print(s1.balance, s1.transactions)

## create the class by name senior citizen account inherit it with savings account change the interest rate

## create the class salary account inherit it with senior citizen account
## chnage the intereset rate and overide the method deposit
## if amount is less than 20k raise error else have the same implemenation of parent class
 


def __init__(self, face, pin):
        self.face = face
        http://self.pin = pin

    def Unlock_Face(self, FACE_ID):
        if self.face == FACE_ID:
            print('Unlocked')
        else:
            print('Face not matching')

    def Unlock_Pin(self, PIN_NO):
          if http://self.pin == PIN_NO:
print('Unlocked')
else:
print('Pin not matching')
 




class Unlock:
    def __init__(self, face, pin):
        self.face = face
        http://self.pin = pin

    def Unlock_Face(self, FACE_ID):
        if self.face == FACE_ID:
            print('Unlocked')
        else:
            print('Face not matching')

    def Unlock_Pin(self, PIN_NO):
        if http://self.pin == PIN_NO:
        print('Unlocked')
        else:
        print('Pin not matching')