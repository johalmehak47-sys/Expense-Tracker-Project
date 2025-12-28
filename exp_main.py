
import exp_ops
import expfile_handler
with open("expenses.txt","r") as f:
    for line in f:
        data = line.strip().split('|')
        print(int(data[0]))
        print(data[1])
        print(data[2])
        print(float(data[3]))
        print(data[4])
# def menu():
#     print("1. ADD NEW EXPENSE RECORD.")
#     print("2. DELETE AN EXPENSE RECORD.")
#     print("3. UPDATE AN EXPENSE RECORD.")
#     print("4. VIEW ALL EXPENSES.")
#     print("5. FILTER EXPENSES BY CATEGORY.")
#     print("6. FILTER EXPENSES BY DATE.")
#     print("7. CALCULATE TOTAL EXPENSES.")
#     print("8. EXIT.")
    

# def main():
#     exp_ops.expenses = expfile_handler.load_expenses()

#     while True :

#         menu()

#         try:
#             inp = int(input("Enter choice : "))

#             if inp==1:
#                 exp_ops.add_expense()


#             elif inp==2:
#                 exp_ops.delete_expense()
            
#             elif inp ==3 :
#                 exp_ops.update_expense()

#             elif inp ==4 :
#                 exp_ops.view_all_expenses()
            
#             elif inp == 5:
#                 exp_ops.filter_by_category()
#             elif inp == 6:
#                 exp_ops.filter_by_date()
#             elif inp == 7:
#                 exp_ops.calculate_total_expenses()
#             elif inp == 8:
#                 print("EXITING....")
#                 break
#             else :
#                 print("Enter valid number ! ")
#         except ValueError:
#             print("Invalid choice ! ")

#         except Exception as e:
#             print(f"An error occured {e}.")

# if __name__ == "__main__":
#     main()