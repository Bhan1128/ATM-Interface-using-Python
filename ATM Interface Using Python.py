class Customer:
    def __init__(self, Pin_no, Balance=0):
        self.Pin_no = Pin_no
        self.Balance = Balance

class ATM:
    def __init__(self):
        self.customers = {}
        self.current_customer = None

    def add_customer(self, Pin_no, Balance=0):
        customer = Customer(Pin_no, Balance)
        self.customers[Pin_no] = customer

    def verify(self, Pin_no):
        customer = self.customers.get(Pin_no)
        if customer:
            self.current_customer = customer
            print("Verification successful!")
            return True
        else:
            print("Verification failed. Wrong PIN_No..")
            return False

    def check_balance(self):
        if self.current_customer:
            print(f"Your Bank Balance is: ₹{self.current_customer.Balance}")
        else:
            print("Please verify first.")

    def deposit(self, amount):
        if self.current_customer:
            if amount > 0:
                self.current_customer.Balance += amount
                print(f"Successfully deposited ₹{amount}.")
            else:
                print("not a valid amount. Please enter a positive number.")
        else:
            print("Please verify first.")

    def withdraw(self, amount):
        if self.current_customer:
            if 0 < amount <= self.current_customer.Balance:
                self.current_customer.Balance -= amount
                print(f"Successfully withdrawn ₹{amount}.")
            else:
                print("Insufficient Balance.")
        else:
            print("Please verify first.")

    def main_menu(self):
        while True:
            print("\nWelcome to the ATM")
            print("1. Verification")
            print("2. Check Balance")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                Pin_no = input("Enter your PIN_No.: ")
                self.verify(Pin_no)
            elif choice == '2':
                self.check_balance()
            elif choice == '3':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == '4':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '5':
                print("Thank you for using the ATM. Have a Great Day!")
                break
            else:
                print("Incorrect choice. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    
    # Adding a customer with PIN_No. and Balance
    atm.add_customer("1234", 1000)
    atm.add_customer("5678", 2000)
    atm.add_customer("1357", 3000)
    atm.add_customer("2468", 4000)
    
    atm.main_menu()
