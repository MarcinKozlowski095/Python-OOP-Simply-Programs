"""
Zadanie 3: Klasa BankAccount
Stwórz klasę BankAccount, która przechowuje numer konta i saldo.
Dodaj metody do wpłacania, wypłacania pieniędzy oraz sprawdzania salda.
Zaimplementuj również metodę do przelewu środków między dwoma kontami.
"""
class BankAccount():
    def __init__(self, acc_number, saldo):
        self.nr_konta = acc_number
        self.saldo = saldo

    def withdraw(self, amount):
        if self.saldo > amount:
            self.saldo -= amount
            return f'Withdraw: {amount}. Balance: {self.saldo}'
        else:
            return 'Insufficient funds'

    def deposit(self, amount):
        self.saldo += amount
        return f'Deposit {amount}. Balance: {self.saldo}'

    def display_saldo(self):
        return  self.saldo

    def transfer(self, amount, other_acc):
        if amount <= self.saldo:
            self.saldo -= amount
            other_acc.deposit(amount)
            return 'Transfer done.'
        else:
            return 'Insufficient funds'

ba = BankAccount(11111, 5000)
ba1 = BankAccount(22222, 1000)
print(ba.display_saldo())
print(ba1.display_saldo())
print(ba.withdraw(100))
print(ba.deposit(200))
print(ba.transfer(200, ba1))
print(ba.display_saldo())
print(ba1.display_saldo())
