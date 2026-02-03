from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposite(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

class BankAccount(Account):
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance

    def deposite(self, amount):
        if(amount<=0):
            raise ValueError("Amount must be greater than 0")
        self.__balance += amount
        print(f"Deposited {amount} into account {self.acc_no}")

    def withdraw(self, amount):
        if (amount> self.__balance):
            raise ValueError("Withdrawal amount exceeds balance")
        self.__balance -= amount
        print(f"Withdrew {amount} from account {self.acc_no}")

    def get_balance(self):
        return self.__balance

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.acc_no}")
        print(f"Balance: {self.__balance}")

class SavingAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.get_balance():
            raise ValueError("Withdrawal amount exceeds balance")
        print("Saving Account Withdrawal")
        super().withdraw(amount)

try:
    acc1 = SavingAccount('Smith', 101, 10000)

    acc1.deposite(5000)
    acc1.withdraw(10000)
    acc1.show_details()

except ValueError as e:
    print("Error", e)