## ATM Interface using Python

**Overview**

- This is a simple ATM interface implemented in Python.
- The program allows customers to verify their Pin_no, check their balance, deposit money, and withdraw money.

## Features 

**Verify Customer:** Verify the customer's Pin_no to allow further transactions.

**Check Balance:** Check the current balance of the verified customer.

**Deposit Money:** Deposit a specified amount of money into the verified customer's account.

**Withdraw Money:** Withdraw a specified amount of money from the verified customer's account, if sufficient balance is available.

## Requirements

- **Python 3.x**

## Code Structure

**Customer:**
- A class representing a customer with attributes for Pin_no and Balance.

**ATM:**
- A class representing the ATM with methods to add customers, verify customers, check balance, deposit money, withdraw money, and display the main menu.

**Main Methods**

*add_customer(self, Pin_no, Balance=0):* 
- Adds a new customer with the specified Pin_no and Balance.

*verify(self, Pin_no):*
- verifies the user by checking the entered Pin_no.

*check_balance(self):*
- Displays the current balance of the verified user.

*deposit(self, amount):*
- Deposits the specified amount into the verified customer's account.

*withdraw(self, amount):*
- Withdraws the specified amount from the verified customer's account.

*main_menu(self):*
- Displays the main menu and handles customer choices.

## Usage

- Run the script to start the ATM interface:

- Upon running the script, you will be presented with a main menu to perform various operations:

        Welcome to the ATM
        1. Verification
        2. Check Balance
        3. Deposit Money
        4. Withdraw Money
        5. Exit
        Enter your choice:

## Example

- Here is an example of how to use the ATM interface:

        Welcome to the ATM
        1. Verification
        2. Check Balance
        3. Deposit Money
        4. Withdraw Money
        5. Exit
        Enter your choice: 1
        Enter your Pin_no.: 1357
        Verification successful!

        Welcome to the ATM
        1. Verification
        2. Check Balance
        3. Deposit Money
        4. Withdraw Money
        5. Exit
        Enter your choice: 2
        Your Bank Balance is: ₹3000

        Welcome to the ATM
        1. Verification
        2. Check Balance
        3. Deposit Money
        4. Withdraw Money
        5. Exit
        Enter your choice: 3
        Enter amount to deposit: 2500
        Successfully deposited ₹2500.0.

        Welcome to the ATM
        1. Verification
        2. Check Balance
        3. Deposit Money
        4. Withdraw Money
        5. Exit
        Enter your choice: 2
        Your Bank Balance is: ₹5500.0

        Welcome to the ATM
        1. Verification
        2. Check Balance
        3. Deposit Money
        4. Withdraw Money
        5. Exit
        Enter your choice: 4
        Enter amount to withdraw: 1500
        Successfully withdrawn ₹1500.0.

        Welcome to the ATM
        1. Verification
        2. Check Balance
        3. Deposit Money
        4. Withdraw Money
        5. Exit
        Enter your choice: 2
        Your Bank Balance is: ₹4000.0

        Welcome to the ATM
        1. Verification
        2. Check Balance
        3. Deposit Money
        4. Withdraw Money
        5. Exit
        Enter your choice: 5
        Thank you for using the ATM. Have a Great Day!

## Notes

- Ensure Python 3.x is installed.
- The example adds a customer with Pin_no 1357 and a Balance of ₹3000 for testing purposes.
- Modify the add_customer method call to add more customers as needed.

## Contributing

- Contributions are welcome! Please create a pull request or submit an issue for any bugs or feature requests.

## Contact

- For any questions or suggestions, please contact [nbkreddy472@gmail.com].
