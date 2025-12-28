from expense import Expense




def save_expenses(expenses):
    with open("expenses.txt","w") as f:
        for exp in expenses:
            line=f"{exp.exp_id}|{exp.date}|{exp.category}|{exp.amount}|{exp.optional_note}\n"
            f.write(line)

def load_expenses():
    expenses=[]
    try :

        with open("expenses.txt","r") as f:
            for line in f:
                data = line.strip().split('|')
                exp = Expense()
                exp.exp_id = int(data[0])
                exp.date = data[1]
                exp.category = data[2]
                exp.amount = float(data[3])
                exp.optional_note = data[4]
                expenses.append(exp)
                print("Data loaded successfully ! ")
    except FileNotFoundError :
        print("File not found ! ")
    except Exception as e :
        print(f"Some error occured {e}.")

    return expenses

