import datetime
from validations import *


def getinput():
    

    exp_date = input("Input Date format YYYY-MM-DD:")
    category_input = input("Expense category \n F - Food \n T - Travel \n G - Grocery \n M - Medicine \n V - vegetables \n :")
    amount_spent = float(input("enter the expense amount"))
    exp_description = input("Expense description")
    if category_input == 'F' or category_input == 'f':
        category = 'Food'
    elif category_input == 'T' or category_input == 't':
        category = 'Travel'
    else:
        category = 'Others'

    expense_dict = {'date': exp_date, 'category': category, 'amount': amount_spent, 'description': exp_description}
        
    return expense_dict


def Monthly_Budget_limit():
    budget_limit = float(input("Enter the budget limit for the month"))
    return budget_limit

