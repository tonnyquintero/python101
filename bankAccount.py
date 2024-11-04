#Programammos la función
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposite(self, account_holder, amount) :
        if self.is_active:
            self.account_holder = account_holder
            self.balance += amount
            print(f"{account_holder} ha depositado {amount} pesos. Saldo actual {self.balance} pesos")
        else:
            print("No se puede depositar, cuenta inactiva")
    
    def withdraw(self, account_holder, amount) :
        if self.is_active:
            self.account_holder = account_holder
            if amount <= self.balance:
                self.balance -= amount
                print(f"{account_holder} ha retirado {amount} pesos, Saldo actual {self.balance} pesos")

    def deactivate_account(self):
        self.is_active = False
        print(f"La cuenta ha sido desactivada")

    def activate_account(self):
        self.is_active = True
        print(f"La cuenta ha sido activada")

#Declaramos los objetos
account1 = BankAccount("Anthony", 500)
account2 = BankAccount("Ana", 1000)

#Llamada a los metodos
account1.deposite("Anthony", 200)
account2.deposite("Ana", 100)
account1.deactivate_account()
account1.deposite("Anthony", 50)
account2.withdraw("Ana", 700)
