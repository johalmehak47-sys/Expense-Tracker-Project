import numpy as np
from data_loader import load_from_file
from analytics import *

def menu():
    print("     EXPENSE ANALYSIS WITH NUMPY.      ")
    print("1. Load Expense Data")
    print("2. View Spending Summary")
    print("3. Category-wise Analysis")
    print("4. Find Most Expensive Days")
    print("5. Exit")

def main():
    expenses = None
    dates = None
    categories = None
    
    while True:
        menu
        
        try:
            choice = int(input("\nEnter choice: "))
            
            if choice == 1:
                try:
                    expenses, dates, categories = load_from_file("/Users/mehakdeepsinghmac/ROADMP/numpyprojct/details.txt")
                    print("LOADING SUCCESSFULL ! ")
                except FileNotFoundError:
                    print("File not Found !")
            
            elif choice == 2:
                # Summary
                if expenses is None:
                    print("Load data first!")
                    continue
                
                statis = stats(expenses)
                print("\n--- SPENDING SUMMARY ---")
                print(f"Total spending: ${statis['total']:.2f}")
                print(f"Average daily: ${statis['mean']:.2f}")
                print(f"Std deviation: ${statis['std_dev']:.2f}")
                print(f"Max expense: ${statis['max']:.2f}")
                print(f"Min expense: ${statis['min']:.2f}")
            
            elif choice == 3:
                # Category analysis
                if expenses is None:
                    print("Load data first!")
                    continue
                
                cat_totals = categorywise(expenses)
                cat_percentages = cat_percent(expenses)
                
                print("\n--- CATEGORY ANALYSIS ---")
                for i, cat in enumerate(categories):
                    print(f"{cat:15s}: ${cat_totals[i]:8.2f} ({cat_percentages[i]:5.2f}%)")
            
            elif choice == 4:
                # Expensive days
                if expenses is None:
                    print("Load data first!")
                    continue
                
                print("5. MAXIMUM DAY : \n")
                daily = dailybasis(expenses)
                maxi = max(daily)
                i = 0
                while i < len(daily) :
                    if daily[i] == maxi:
                        print(f"{dates[i]} = ${maxi}")
                    i = i+1
            
            elif choice == 5:
                print(" Exiting... ")
                break
            
            else:
                print("Invalid choice!")
        
        except ValueError:
            print("Enter a valid number!")
        except Exception as e:
            print(f" Error occured: {e}")

if __name__ == "__main__":
    main()