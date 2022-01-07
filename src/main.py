import pandas as pd
import numpy as np
from pdlibs import *


records=pd.read_csv('account.csv',names=['item','price','date','method','note'])
# print(records.loc[0])
records_data=np.array(records)
# print(records_data)

print("successfully read data, please input commands. Input help to get a manual for the commands")

help_list=[]
cmd=""
print(records)

while cmd!='q':
    cmd=input("> ")
    # start processing
    if cmd=='help':
        print(help_list)
    elif cmd=='l' or cmd=='list':
        print(records.to_string())
    elif cmd=='add':
        print('creating new record...')
        new_item=input("item name: ")
        new_price=input("item price: ")
        new_date=input("purchase date in syntax yy-mm-dd: ")
        # todo: check and fix the date syntax
        new_method=input("payment method: ")
        new_note=input("other notation: ")
        if new_note=='':
            new_note='-'
        newline=pd.DataFrame({'item':[new_item],'price':[new_price],'date':[new_date],'method':[new_method],'note':[new_note]})
        # find proper place
        sz=len(records)

        # print(records)
        dates=records['date'].tolist()
        # print(dates)
        

        ins_place=search_date(dates,new_date)
        records=row_insert(records,ins_place,newline)
        print(records.to_string())
        is_save=input("Save this change?(Y/N): ")
        if is_save=='Y':
            records.to_csv('account.csv',index=None,header=None)
            print("save successfully")
            records_data=np.array(records)
        else:
            print("The change is not saved.")
            records=pd.read_csv('account.csv',names=['item','price','date','method','note'])
            print(records.to_string())
        


