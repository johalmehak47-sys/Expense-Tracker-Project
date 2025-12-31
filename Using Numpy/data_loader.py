# this will load the data and convert it into a numpy array 

import numpy as np

def load_from_file(filename):
    expenses_dict ={}
    all_categories = set()

    try : 
        with open(filename,'r') as f:
            for line in f:
                date, category, amount = line.strip().split(',')

                amount = float(amount)
                all_categories.add(category)

                if date not in expenses_dict:
                    expenses_dict[date]={}
                expenses_dict[date][category]=amount
        
        dates = sorted(expenses_dict.keys())
        categories = sorted(all_categories)

        len_days = len(dates)
        len_categories = len(categories)

        expenses_arr = np.zeros((len_days,len_categories))

        for dayid, date in enumerate(dates):
            for catid, cat in enumerate(categories):
                if cat in expenses_dict[date]:
                    expenses_arr[dayid,catid] = expenses_dict[date][cat]
        
        return expenses_arr, dates, categories
    except FileNotFoundError:
        print("File not found ! ")
        raise
    except Exception as e:
        print(f"An error occured {e}.")
        raise