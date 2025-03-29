
def validate_date(date_str):
    """
    Validate the date format YYYY-MM-DD.

    Args:
    date_str (str): The date string to validate.

    Returns:
    bool: True if the date is valid, False otherwise.
    """
    try:
        year, month, day = date_str.split('-')
        if len(year) == 4 and len(month) == 2 and len(day) == 2:
            int(year)
            int(month)
            int(day)
            return True
        else:
            return False
    except ValueError:
        return False


def validate_category(category):
    category_list = ['Food','Travel', 'Others', 'Grocery', 'Medicine', 'vegetables']

    if category in category_list:
        return True
    else:
        return False
    


def validate_amount(expense_amount):
    if (expense_amount != 0.0):
        return True
    else:
        return False
    

def Validate_monthly_budget_limit(budget_limit, expenses):
    monthly_expenses = {}
    

    for expense in expenses:
        print (expense)

        
       # date_str = expense['date']
       # amount = expense['amount']
        date_str, category, amount, description = expense.values()

        print(date_str)
        year, month, day = date_str.split('-')
        month_key = f"{year}-{month}"
        
        if month_key not in monthly_expenses:
            monthly_expenses[month_key] = 0.0
        monthly_expenses[month_key] += amount
    
    for mon_key, amount in monthly_expenses.items():
        if amount > budget_limit:
            print(f' For the year-month {mon_key}, you have exceeded the budget by {amount - budget_limit}')

        else:
            print(f'For the year-month {mon_key},you have left {budget_limit - amount} ')
    return monthly_expenses



