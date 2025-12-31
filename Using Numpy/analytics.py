import numpy as np

def dailybasis(expenses_arr):
    return expenses_arr.sum(axis=1)
def categorywise(expenses_arr):
    return expenses_arr.sum(axis=0)
def mean_daily(expenses_arr):
    pass
def stats(expenses_arr):
    nzero = expenses_arr[expenses_arr > 0]
    return{
        'total' : expenses_arr.sum(),
        'mean' : expenses_arr.mean(),
        'std_dev' : expenses_arr.std(),
        'variance' : expenses_arr.var(),
        'max' : expenses_arr.max(),
        'min' : nzero.min() if len(nzero) > 0 else 0

    }
def cat_percent(expenses_arr):
    '''i need to calculate percentage of each category 
    that is :
    sum of each all categories expenses 
    and sum of each category expense '''
    cat_totals = categorywise(expenses_arr)
    total = expenses_arr.sum()
    return (cat_totals / total)*100
def maxday(expenses_arr):
    '''i want to return the index of whatever way possible in which i can get the date on which maximum expenses are there'''

def cat_by_range(expenses_arr, dates, sdate, edate):
    
    region = [(sdate <= date <= edate) for date in dates]

    filtered_expenses = expenses_arr[region]
    filtered_dates = [dates[i] for i,j in enumerate(region) if j]
    return filtered_expenses,filtered_dates
def monthly(expenses_arr,dates):
    '''
    output is dictionary -
    mmonth : total'''
    monthspend ={}
    for i, j in enumerate(dates):
        month = j[:7]
        dayt = expenses_arr[i].sum()
        if month not in monthspend:
            monthspend[month]=0
            monthspend[month] += dayt
    return monthspend
    
