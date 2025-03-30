# Expense Tracker

## Overview
The Expense Tracker is a Python-based application designed to help users manage their personal finances. It allows users to add, view, save, and load expenses, as well as track their monthly budget. The application uses a CSV file to store expense data persistently.

---

## Features
- **Add Expenses**: Input details such as date, category, amount, and description.
- **View Expenses**: Display all recorded expenses in a structured format.
- **Track Monthly Budget**: Validate expenses against a user-defined monthly budget limit.
- **Save and Load Data**: Save expenses to a CSV file and load them back when needed.

---

## Project Structure
```
expense_tracker/
├── Personalexpenses.csv       # CSV file to store expense data
├── README.md                  # Project documentation
├── .vscode/
│   └── settings.json          # VSCode settings for testing
└── src/
    ├── display.py             # Module to display expenses
    ├── getinput.py            # Module to handle user input
    ├── main.py                # Main application entry point
    ├── saveload.py            # Module to save/load expenses
    ├── validations.py         # Module for input validation
    └── __pycache__/           # Compiled Python files
```

---

## Setup Instructions

### Prerequisites
- Python 3.10 or later installed on your system.
- A terminal or command prompt to run the application.

### Steps
1. Clone the repository or download the project files:
   ```bash
   git clone https://github.com/your-username/expense_tracker.git
   cd expense_tracker
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python src/main.py
   ```

---

## Usage Instructions

### Adding an Expense
1. Select option `1` from the menu.
2. Enter the following details:
   - **Date**: Format `YYYY-MM-DD` (e.g., `2023-10-01`).
   - **Category**: Choose from `F` (Food), `T` (Travel), or others.
   - **Amount**: Enter the expense amount (e.g., `500.0`).
   - **Description**: Provide a brief description of the expense.

**Example Input**:
```
Input Date format YYYY-MM-DD: 2023-10-01
Expense category 
 F - Food 
 T - Travel 
 G - Grocery 
 M - Medicine 
 V - vegetables 
 : F
enter the expense amount: 500.0
Expense description: Dinner at a restaurant
```

### Viewing Expenses
1. Select option `2` from the menu.
2. The application will display all recorded expenses in a structured format.

**Example Output**:
```
------------------------
 date : 2023-10-01
 category : Food
 amount : 500.0
 description : Dinner at a restaurant
------------------------
```

### Tracking Monthly Budget
1. Select option `3` from the menu.
2. Enter the monthly budget limit (e.g., `1000.0`).
3. The application will calculate and display whether the budget is exceeded or remaining for each month.

**Example Output**:
```
Enter the budget limit for the month: 1000.0
 For the year-month 2023-10, you have left 500.0
```

### Saving Expenses
1. Select option `4` from the menu.
2. The application will save all recorded expenses to `Personalexpenses.csv`.

**Example Output**:
```
Expenses saved successfully to Personalexpenses.csv.
```

### Exiting the Application
1. Select option `5` from the menu to exit.

---

## Examples

### Example CSV File
After saving expenses, the `Personalexpenses.csv` file will look like this:
```csv
date,category,amount,description
2023-10-01,Food,500.0,Dinner at a restaurant
2023-10-02,Travel,200.0,Taxi fare
```

### Example Code Snippets
#### Adding an Expense Programmatically
You can use the `getinput` function from [`src/getinput.py`](src/getinput.py) to add an expense:
```python
from getinput import getinput

expense = getinput()
print(expense)
```

#### Validating a Budget
Use the `Validate_monthly_budget_limit` function from [`src/validations.py`](src/validations.py) to check the budget:
```python
from validations import Validate_monthly_budget_limit

expenses = [
    {'date': '2023-10-01', 'category': 'Food', 'amount': 500.0, 'description': 'Dinner'},
    {'date': '2023-10-02', 'category': 'Travel', 'amount': 200.0, 'description': 'Taxi'}
]
budget_limit = 1000.0
Validate_monthly_budget_limit(budget_limit, expenses)
```

---

## Testing
This project uses Python's built-in `unittest` framework. To run tests:
1. Ensure the `.vscode/settings.json` file is configured for `unittest`.
2. Run the following command:
   ```bash
   python -m unittest discover -s src -p "test*.py"
   ```

---

## License
This project is open-source and available for use and modification under the MIT License.