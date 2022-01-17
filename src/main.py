import pandas as pd
import numpy as np
from pdlibs import *
from update import *
import os

if not os.path.exists('account.csv'):
    print("Account not exist, creating a new account... ")
    f = open('account.csv', 'w')
    f.close()

records = pd.read_csv('account.csv', names=['item', 'price', 'date', 'method', 'note'])
records.iloc[:, 1] = records.iloc[:, 1].map(float)
# print(records.loc[0])
records_data = np.array(records)
# print(records_data)

print("successfully read data, please input commands. Input \"help\" to get a manual for the commands")

help_list = pd.read_csv('helpmanual.csv', names=['command', 'usage'])
cmd = ""
print(records.to_string())

while cmd != 'q':
    cmd = input("> ")
    # start processing
    if cmd == 'help':
        print(help_list)
    elif cmd == 'l' or cmd == 'list':
        print(records.to_string())
    elif cmd == 'add':
        print('creating new record...')
        new_item = input("item name: ")
        new_price = input("item price: ")
        new_date = input("purchase date in syntax yy-mm-dd: ")
        # todo: check and fix the date syntax
        new_method = input("payment method: ")
        new_note = input("other notation: ")
        if new_note == '':
            new_note = '-'
        newline = pd.DataFrame(
            {'item': [new_item], 'price': [new_price], 'date': [new_date], 'method': [new_method], 'note': [new_note]})
        # find proper place
        sz = len(records)

        # print(records)
        dates = records['date'].tolist()
        # print(dates)

        ins_place = search_date(dates, new_date)
        records = row_insert(records, ins_place, newline)
        if not save_prompt(records, 'account.csv'):
            records = pd.read_csv('account.csv', names=['item', 'price', 'date', 'method', 'note'])
            records.iloc[:, 1] = records.iloc[:, 1].map(float)  # turn str to float
        records_data = np.array(records)

    elif cmd == 'del':
        print(records.to_string())
        del_line = int(input('please input the line you want to delete: '))
        records = records.drop(del_line).reset_index(drop=True)

        if not save_prompt(records, 'account.csv'):
            records = pd.read_csv('account.csv', names=['item', 'price', 'date', 'method', 'note'])
            records.iloc[:, 1] = records.iloc[:, 1].map(float)  # turn str to float
        records_data = np.array(records)

    elif cmd == 'sum':
        sum_all = round(sum(records['price'].tolist()), 2)
        print(sum_all)

    else:
        args = cmd.split(' ')
        success, records = update(records, args, "account.csv")
