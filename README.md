# Python CLI Projects

Three command line applications written in Python, built as university and internship projects. They run in the terminal, need no external libraries and show core programming ideas: classes, functions, input validation, file storage and menu-driven design.

## Requirements and how to run

Python 3.8 or newer is needed. Nothing else has to be installed. Download or clone this repository, open a terminal in its folder and run any project with Python:

```
python ATM\_Simulation.py
python To\_Do\_List.py
python Cafe\_Menu\_System.py
```

On some systems the command is `python3` instead of `python`.

## 1\. ATM Simulation

File: `ATM\_Simulation.py`

A simulation of an ATM machine written with two classes. The `ATM` class holds the account logic (PIN check, balance, deposits, withdrawals and the transaction list) and the `ATMController` class handles the menu and user input.

The user must enter the correct 4-digit PIN before anything else works. After three wrong attempts the card is blocked and the program ends. Once logged in, the user can check the balance, deposit money, withdraw money and view a time-stamped transaction history that shows the balance after every transaction. Withdrawals larger than the balance are refused, invalid amounts are rejected, and typing letters instead of a number does not crash the program.

This is a demo, so the PIN is stored in the code. The default PIN is `1234` and the starting balance is 1000.

```
Enter your 4-digit PIN: 1234
PIN verified. Welcome!

===== ATM Menu =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit
```

## 2\. To-Do List

File: `To\_Do\_List.py`

A task manager that keeps its data in a JSON file, so tasks are still there the next time the program runs. Every task has a title and a category such as Work or Personal.

The menu lets the user add several tasks in one go, view pending tasks, update the title or category of a task, delete one or more tasks, mark one or more tasks as completed, view the completed list, remove completed tasks and filter pending tasks by category. Several tasks can be chosen at once by typing numbers separated by commas, for example `1, 3, 4`. Numbers that do not match a task are skipped and the user is told. If the saved file is missing or damaged, the program starts with an empty list instead of crashing.

The data is saved in `todo\_list.json`, which is created next to the script (or in the current folder) when the program runs. It is listed in `.gitignore` because it is personal data and does not belong in the repository.

## 3\. Cafe Menu System

File: `Cafe\_Menu\_System.py`

A cafe ordering and billing program. It shows a menu with three categories (Fast Food, Rice and Drinks) and prices in rupees, asks for the customer's name, and takes the order as free text such as `pizza 2, cold, burger`. When the customer types `exit` or `end`, it prints a receipt with the customer name, the order time, every item with quantity and price, and the total bill.

Item names are flexible. Each menu item has alternative spellings and names (for example `chips` for fries or `cola` for a cold drink), so the order does not have to match the menu exactly. Typing a category name such as `drinks` or `rice` shows the items in that category. Unknown items and invalid quantities are reported without stopping the order, and ordering the same item twice adds to its quantity.

```
Your order: pizza 2, cold

\[OK] 2 PIZZA added. Subtotal: Rs 1040
\[OK] 1 COLD DRINK added. Subtotal: Rs 100
```

This was a team semester project. I wrote all of the code for it.

## What I learned

These projects strengthened my understanding of Python fundamentals: object-oriented design with classes, splitting a program into small functions, handling wrong input safely, reading and writing JSON files, working with dates and times, and building clear menu-driven interfaces.

## Author

Abdul Rehman, BS Computer Science, Allama Iqbal Open University.
Email: abdul.rehman.edu9@gmail.com
Portfolio: https://abdulrehmanedu9-maker.github.io

