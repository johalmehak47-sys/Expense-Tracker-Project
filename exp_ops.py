from expense import Expense
from datetime import datetime
import expfile_handler
expenses =  expfile_handler.load_expenses()
def generate_id():
    if(len(expenses)==0):
        return 1
    
    max_id = max(exp.exp_id for exp in expenses)
    return max_id+1

def add_expense():

    exp = Expense()
    exp.exp_id = generate_id()

    while True :
        exp.date = input("Enter date (YYYY-MM-DD) OR press ENTER for today : ").strip()
        
        # if user entered enter 
        if exp.date == "":
            exp.date = datetime.now().strftime("%Y-%m-%d")
            break

        # manual date 
        elif len(exp.date)==10 and exp.date[4] == '-' and exp.date[7] =='-':
            try :
                datetime.strptime(exp.date,"%Y-%m-%d")
                break
            except ValueError :
                print("Invalid date ! ")
 
        # timepass 
        else :
            print("Invalid date format ! ")

    
    while True :

        exp.category = input("Enter category of the expense : ").strip()

        if exp.category!="":
            break
        print("category cannot be left blank ! ")


    while True :

        try :
            exp.amount = float(input("Enter amount of expense : "))

            if exp.amount > 0:
                break
            print("Amount should be greater than zero ! ")
            # pass
        except ValueError:
            print("Invalid input ! enter valid amount ! ")

    exp.optional_note = input("Enter note ( optional ). Press ENTER to skip.").strip()


    expenses.append(exp)
    expfile_handler.save_expenses(expenses) 
    print("Expense input successfull !!")
    print(f"Expense {exp.exp_id} added to the expense list.")

def view_all_expenses():

    if(len(expenses)==0):
        print("Expense record is empty ! ")
        print("Nothing to display.")
        return

    for exp in expenses :
        print(f"expense id :- {exp.exp_id}| expense date :- {exp.date} | expense category :- {exp.category} | expense amount :- ${exp.amount} | note :- {exp.optional_note}.")

def filter_by_category():

    if(len(expenses)==0):
        print("Expense record empty ! ")
        return
    
    try:
        choice = input("Enter the category : ").strip()
        if choice =="":
            print("Category choice cannot be left blank ! ")
            return
        
        found = False
        for exp in expenses :
            if exp.category.lower() == choice.lower():
                print(f"expense id :- {exp.exp_id}| expense date :- {exp.date} | expense category :- {exp.category} | expense amount :- ${exp.amount} | note :- {exp.optional_note}.")
                found = True

        if not found :
            print(f"No record found in category {choice}! ")
    except Exception as e:
        print(f"An error occured {e} ! ")

def filter_by_date():
    if(len(expenses)==0):
        print("Expense record empty ! ")
        return
    
    try :
        choice = input("enter date (YYYY-MM-DD) format : ")

        if choice=="":
            print("Date cannot be empty ! ")
            return
        
        from datetime import datetime
        if len(choice) != 10 or choice[4] != '-' or choice[7] != '-':
            print("Error: Invalid date format! Use YYYY-MM-DD")
            return
        
        try:
            datetime.strptime(choice, "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid date! Please enter a real date.")
            return
        
        found = False
        for exp in expenses :
            if exp.date == choice :
                print(f"expense id :- {exp.exp_id}| expense date :- {exp.date} | expense category :- {exp.category} | expense amount :- ${exp.amount} | note :- {exp.optional_note}.")
                found = True

        if not found :
            print(f"No expense found for date {choice}.")
            return
                
    except Exception as e:
        print(f"Error occured {e}.")

def calculate_total_expenses():
    if(len(expenses)==0):
        print("Expense record empty ! ")
        return
    
    total = 0
    for exp in expenses :
        total = total + exp.amount
    
    print(f"Total expenses are : ${total}")

def delete_expense():
    if(len(expenses)==0):
        print("Expense record empty ! ")
        return
    
    try :
        choice = int(input("Enter expense ID which is to be deleted : "))

        found = False 
        for exp in expenses :
            if exp.exp_id == choice :
                expenses.remove(exp)
                found=True
                expfile_handler.save_expenses(expenses)
                break
        if not found :
            print(f"No record found with expense id {choice}.")
    except Exception as e:
        print(f"An error arised {e}.")

def update_expense():
    if(len(expenses)==0):
        print("Expense record empty ! ")
        return
    
    try :
        choice = int(input("Enter expense ID for updation : "))

        found = False
        
        for exp in expenses :

            if exp.exp_id == choice :
                found = True
                print("What needs to be updated ? ")
                print("1. Date.")
                print("2. Category.")
                print("3. Amount.")
                print("4. Note.")
                print("5.None")

                second_choice = int(input("ENTER : "))

                if second_choice==1:

                    while True :
                        exp.date = input("Enter date (YYYY-MM-DD) OR press ENTER for today : ").strip()
        
                    # if user entered enter 
                        if exp.date == "":
                            exp.date = datetime.now().strftime("%Y-%m-%d")
                            expfile_handler.save_expenses(expenses)
                            break

                    # manual date 
                        elif len(exp.date)==10 and exp.date[4] == '-' and exp.date[7] =='-':
                            try :
                                datetime.strptime(exp.date,"%Y-%m-%d")
                                expfile_handler.save_expenses(expenses)
                                break
                            except ValueError :
                                print("Invalid date ! ")
 
                    # timepass 
                        else :
                            print("Invalid date format ! ")


                elif second_choice ==2: #for category

                    while True:
                        exp.category = input("Enter new category : ").strip()

                        if exp.category !="":
                            expfile_handler.save_expenses(expenses)
                            break
                        else :
                            print("Category cannot be left blank ! ")

                elif second_choice ==3:  #for amount

                    while True :
                        try:
                            exp.amount = float(input("Enter new amount : "))
                            if exp.amount > 0:
                                expfile_handler.save_expenses(expenses)
                                break

                            print("Amount must be greater than zero ! ")

                        except ValueError:
                            print("Enter numeric value only ! ")
                elif second_choice ==4: #note
                    while True:
                        exp.optional_note = input("Enter optional note : ").strip()
                        expfile_handler.save_expenses(expenses)
                        break
                elif second_choice ==5:
                    print("No updation done ! ")
                    expfile_handler.save_expenses(expenses)
                    return
                else :
                    print("Invalid choice ! ")
        if not found:
            print("No record found with given expense ID ! ")
    except Exception as e:
        print(f"An error arised {e}.")