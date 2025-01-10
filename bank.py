import random

class SavingsAccount:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __repr__(self):
        return f"Name: {self.name}\nPIN: {self.pin}\nBalance: {self.balance:.1f}"

# Sample account data with updated names
accounts = [
    SavingsAccount("Priam", 5468, 9500.0),
    SavingsAccount("Alexa", 1353, 6750.5),
    SavingsAccount("Mark", 7128, 1750.0),
    SavingsAccount("Rupert", 1864, 1800.0),
    SavingsAccount("Marco", 9331, 8000.0),
    SavingsAccount("Santiago", 3323, 1500.65),
    SavingsAccount("Matt", 5096, 6500.0),
    SavingsAccount("Milo", 1238, 2550.0),
    SavingsAccount("Alexa", 1872, 6875.0),
    SavingsAccount("Noah", 4253, 9000.0),
]

# Shuffle the list and print
random.shuffle(accounts)
for account in accounts:
    print(account)
