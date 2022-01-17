# practical functions related to pandas that may use several times
from typing import List
import pandas as pd
import numpy as np


def row_insert(df, i, df_add):
    # insert data at row i, return the new list, with old lists not changed
    df1 = df.iloc[:i, :]
    df2 = df.iloc[i:, :]
    df_new = pd.concat([df1, df_add, df2], ignore_index=True)
    return df_new


def str2date(str_date: str):
    # change "yy-mm-dd" to [yy,mm,dd]
    return list(map(int, str_date.split('-')))


def search_date(dates: List[str], tar: str) -> int:
    # search tar from dates, assume dates is sorted. If there's such element, return its index.
    # If not, return the index of the smallest element that is bigger then tar
    # if tar is biggest, return the size of the dates
    list_tar = str2date(tar)
    list_dates = list(map(str2date, dates))

    begin = 0
    end = len(dates) - 1
    while begin <= end:
        mid = begin + (end - begin) // 2
        if list_dates[mid] == list_tar:
            return mid
        elif list_dates[mid] < list_tar:
            begin = mid + 1
        else:
            end = mid - 1

    return begin


def save_prompt(rec: pd.DataFrame, fileName: str) -> bool:
    is_save = input("Save this change?(Y/N): ")
    if is_save == 'Y':
        rec.to_csv('account.csv', index=None, header=None)
        print("save successfully")
        print(rec.to_string())
        return True
    else:
        print("The change is not saved.")
        rec = pd.read_csv('account.csv', names=['item', 'price', 'date', 'method', 'note'])
        print(rec.to_string())
        return False
