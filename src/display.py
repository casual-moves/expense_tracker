from validations import *

def display_all_expenses(expense_list):

    for expense in expense_list:
        
        print('------------------------')

        for item in expense.items():


            if item[0] == 'date' and validate_date(item[1]):
                print(f' {item[0]} : {item[1]}')
            elif item[0] == 'category' and validate_category(item[1]) :
                print(f' {item[0]} : {item[1]}')
            elif item[0] == 'amount' and validate_amount(item[1]) :
                print(f' {item[0]} : {item[1]}')
            elif item[0] == 'description' and item[1] != '' :
                print(f' {item[0]} : {item[1]}')
            else:
                print(f" {item[0]} : {item[1]} - This data is incomplete")
        print('------------------------')

        








            
            
            
    