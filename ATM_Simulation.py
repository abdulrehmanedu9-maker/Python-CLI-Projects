import datetime  # Used to time-stamp every transaction


# ATM class - handles the account logic: PIN, balance and transactions
class ATM:
    MAX_PIN_ATTEMPTS = 3  # The card is blocked after this many wrong PINs

    def __init__(self, pin="1234", initial_balance=1000):
        # Demo values: the default PIN is 1234 and the starting balance is 1000
        self._pin = pin
        self.balance = initial_balance
        self.history = []  # Every successful transaction is stored here

    def verify_pin(self, entered_pin):
        # Return True only when the entered PIN matches the stored one
        return entered_pin == self._pin

    def _record(self, kind, amount):
        # Store one transaction with its time and the balance after it
        self.history.append({
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": kind,
            "amount": amount,
            "balance": self.balance,
        })

    def check_balance(self):
        # Return the current balance
        return self.balance

    def deposit(self, amount):
        # Add money to the account
        if amount <= 0:
            return "Invalid deposit amount."
        self.balance += amount
        self._record("Deposit", amount)
        return f"Deposit successful! New balance: {self.balance:.2f}"

    def withdraw(self, amount):
        # Take money out of the account if the balance allows it
        if amount <= 0:
            return "Invalid withdrawal amount."
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        self._record("Withdrawal", amount)
        return f"Withdrawal successful! New balance: {self.balance:.2f}"

    def get_history(self):
        # Return the list of transactions made in this session
        return self.history


# ATMController class - handles the menu and user interaction
class ATMController:
    def __init__(self):
        self.atm = ATM()

    def login(self):
        # Ask for the PIN; block the card after too many wrong attempts
        for attempt in range(1, ATM.MAX_PIN_ATTEMPTS + 1):
            pin = input("Enter your 4-digit PIN: ").strip()
            if self.atm.verify_pin(pin):
                print("PIN verified. Welcome!")
                return True
            remaining = ATM.MAX_PIN_ATTEMPTS - attempt
            if remaining > 0:
                print(f"Wrong PIN. {remaining} attempt(s) left.")
        print("Too many wrong attempts. Your card is blocked.")
        return False

    def read_amount(self, prompt):
        # Read a number from the user without crashing on bad input
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            return None

    def show_history(self):
        # Print all transactions of this session
        history = self.atm.get_history()
        if not history:
            print("No transactions yet.")
            return
        print("\n----- Transaction History -----")
        for item in history:
            print(f"{item['time']}  {item['type']:<10}  "
                  f"{item['amount']:>10.2f}  Balance: {item['balance']:.2f}")

    def run(self):
        # Start only if the PIN is correct, then keep the menu running
        if not self.login():
            return
        while True:
            print("\n===== ATM Menu =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transaction History")
            print("5. Exit")
            choice = input("Select an option: ").strip()

            if choice == "1":
                print(f"Your balance: {self.atm.check_balance():.2f}")
            elif choice == "2":
                amount = self.read_amount("Enter deposit amount: ")
                if amount is not None:
                    print(self.atm.deposit(amount))
            elif choice == "3":
                amount = self.read_amount("Enter withdrawal amount: ")
                if amount is not None:
                    print(self.atm.withdraw(amount))
            elif choice == "4":
                self.show_history()
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option! Please try again.")


# Start the ATM Simulation
if __name__ == "__main__":
    ATMController().run()
