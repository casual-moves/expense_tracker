import csv
import os


def saveExpenses(expenses):
    
    file_name = "Personalexpenses.csv"

    # Check if the file exists, Clear the file by opening it in write mode 
    if os.path.exists(file_name):
        
        with open(file_name, 'w', newline='') as expensesFile:
            pass  # This clears the file

    # Write the expenses to the file
    with open(file_name, 'w', newline='') as expensesFile:
        if len(expenses) > 0:
            # Use the keys of the first dictionary as the header
            fieldnames = expenses[0].keys()
            writer = csv.DictWriter(expensesFile, fieldnames=fieldnames)

            # Write the header
            writer.writeheader()

            # Write the rows
            print(expenses)
            writer.writerows(expenses)
        else:
            print("No expenses to save.")


def loadExpenses(filename):
    
    expenses = []

    try:
        with open(filename, 'r') as expensesFile:
            reader = csv.DictReader(expensesFile)
            for row in reader:
                # Convert the 'amount' field to a float if it exists
                if 'amount' in row:
                    row['amount'] = float(row['amount'])
                expenses.append(row)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Returning an empty list.")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")

    return expenses

