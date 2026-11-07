# Unit 11 — a bank account
# Run this with the Run button in your editor.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("A deposit must be more than zero")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("A withdrawal must be more than zero")
        if amount > self.balance:
            raise ValueError(f"Not enough money, the balance is {self.balance}")
        self.balance -= amount

    def __str__(self):
        return f"{self.owner} has {self.balance}"


account = BankAccount("Ada", 100)
print(account)               # Ada has 100

account.deposit(50)
print(account)               # Ada has 150

account.withdraw(30)
print(account)               # Ada has 120

print()

# ---------------------------------------------------------------
# withdraw raises a ValueError instead of printing. The caller decides
# what to do about it, with try and except from unit 05.
# "as error" gives the error a name, so you can print its message.

try:
    account.withdraw(500)
except ValueError as error:
    print(f"Could not withdraw: {error}")

print(account)               # Ada has 120, nothing changed

print()

# ---------------------------------------------------------------
# Several attempts in a loop. The good ones go through and the bad
# ones are reported, and the program keeps going.

for amount in [20, -5, 1000, 50]:
    try:
        account.withdraw(amount)
        print(f"Took out {amount}")
    except ValueError as error:
        print(f"Refused {amount}: {error}")

print(account)               # Ada has 50

print()

# Two accounts are two separate objects with their own balance.
grace = BankAccount("Grace")
grace.deposit(10)
print(grace)                 # Grace has 10
print(account)               # Ada has 50

# ---------------------------------------------------------------
# Break it on purpose. Uncomment one block at a time.

# Forgetting the brackets. This is the class, not an account.
# broken = BankAccount
# print(broken)              # <class '__main__.BankAccount'>
# broken.deposit(50)
#   TypeError: BankAccount.deposit() missing 1 required positional argument: 'amount'
#   The 50 went into self, so amount got nothing.

# Withdrawing too much without try and except.
# account.withdraw(1000)
#   ValueError: Not enough money, the balance is 50
