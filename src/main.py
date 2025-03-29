from getinput import *
from saveload import *
from display import *


# Load the file if the data available or initialize the list    
try:
    expenseDetails = loadExpenses("Personalexpenses.csv")
except FileNotFoundError:
    print("File not found. Initializing an empty expense list.")
    expenseDetails = []
except Exception as e:
    print(f"An error occurred: {e}")
    expenseDetails = []

budget_limit = 10000

# Options to personal expenses tracker

while True:
    options = int(input("Enter 1 to add expense,\n 2 to view expense,\n 3 to Track Budget, 4 to Save expenses, 5 to exit: "))
    
    if options == 1:

        while True:
            expenseDetails.append(getinput())
            
            option = input("Do you want to continue  N - No, any other key should continue")
            if option == 'N' or option == 'n':
                break

        print(expenseDetails)
        
    elif options == 2: # Code to view expense
        display_all_expenses(expenseDetails)
        
    elif options == 3: # Code to track budget
        budget_limit = Monthly_Budget_limit()
        budget_status = Validate_monthly_budget_limit(budget_limit, expenseDetails)

              
    elif options == 4: # Code to save expenses
        saveExpenses(expenseDetails)
        
    elif options == 5:
        #saveExpenses(expenseDetails)
        break
    else:
        print("Invalid options\n")
    