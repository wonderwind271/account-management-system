from typing import List, Tuple
import pandas as pd
from pdlibs import *
import numpy as np


def update(record: pd.DataFrame, args: List[str], fileName: str) -> Tuple[bool, pd.DataFrame]:
    if args[0] == 'del':
        del_lines = list(map(int, args[1:]))
        # Todo: check if it's num, check boundary
        record = record.drop(del_lines).reset_index(drop=True)
        save_prompt(record, fileName)
        return (True, record)
    elif args[0] == 'l' or args[0] == 'list':
        list_lines = list(map(int, args[1:]))

        print(record.loc[list_lines].to_string())
        return (True, record)
    elif args[0] == 'sum':
        # arg[1]: index, item, price, date, method, note
        if args[1] == 'index':
            sum_lines = list(map(int, args[2:]))
            sum_all = round(sum(record.loc[sum_lines]['price'].tolist()), 2)
            print(sum_all)
        elif args[1] == 'item':
            sum_lines = []
            sum_feature = args[2:]
            # "_" -> " "
            for i in range(len(sum_feature)):
                sum_feature[i] = sum_feature[i].replace('_', ' ')
            sum_lines = find_require(record, 'item', sum_feature)
            sum_all = round(sum(record.loc[sum_lines]['price'].tolist()), 2)
            print(sum_all)

        return (True, record)

    else:
        return (False, record)
