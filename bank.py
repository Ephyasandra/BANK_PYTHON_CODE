class BankAccount:
    def __init__(self, name, currency, intial_deposit):
        self.__account_holder_name__ = name
        self.currency__ = currency
        self.__balance__ = intial_deposit

    def deposit(self, amount):
        self.__balance__ += amount

    def withdraw(self, amount):
        if (self.__balance - amount < 0):
            raise Exception('Insufficient funds')
        self.__balance__ -= amount

    def check_balance(self):
        return self.__balance__
    
    def get_account_holder_name(self):
        return self.__account_holder_name__
    
def driver():
    while True:
        option = int(input("\nPress 1 to create an account.\nPress 2 to exit.\n\n "))
        

        if option == 1:
            account_name = input("Enter account name: ")
            account_currency = input("Enter currency: ")
            account_intitial_amount = float(input("Enter initial amount: "))

            new_account = BankAccount(account_name, account_currency, account_intitial_amount)
            print("\nBalance after creating account:", new_account.check_balance())

            new_account.deposit(0)   #1000
            print("Balance after deposit:", new_account.check_balance())

            new_account.withdraw(0)   #500
            print("Balance after withdraw:", new_account.check_balance())
            print("Account holder name is:", new_account.get_account_holder_name())

            print(new_account.currency)

            while True:
                option3_4_5= str(input("Press 3 to check your account balance.\n\nPress 4 to Withdraw money from your account.\n\n Press 5 to deposit money into your account.\n"))
                if option3_4_5 == "3":
                    print(f"Dear {account_name}, your account balance is: {account_currency}{account_intitial_amount}")
                    
                elif option3_4_5== "4":
                    withdrawal = int(input("Enter the amount you want to withdraw.\n"))
                    account_intitial_amount -= withdrawal
                    print(f"Dear {account_name}, the amount{account_currency}{withdrawal} has succesfully been withdraw from you account.")
                    print(f"Your current balance is: {account_currency}{account_intitial_amount}")
                    

                elif option3_4_5=="5":
                    dep = float(input("Enter the amount you want to deposit.\n"))
                    account_intitial_amount += dep
                    print(f"The amount of {account_currency}{dep} has been deposited into your account successfully.")
                    print(f"Dear {account_name}, your current balance is: {account_currency}{account_intitial_amount}")
                    
                else:
                    raise Exception("Your input is incorrect")
                continue
            

        elif option == 2:
            break
        else:
            print("Invalid option")
    
            

if __name__ == '__main__':
    print("######## WELCOME TO OUR BANK ##########")
    driver()


driver()