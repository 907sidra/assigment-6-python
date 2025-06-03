class Bank:
    
    Bank_name = "state"

    @classmethod
    
    def change_bank(cls,name):
       cls.bank_name = name

b1=Bank()

print(f"my old bank name is {b1.Bank_name}")

Bank.change_bank="new bank"

print(f"my new bank name is {b1.change_bank}")


