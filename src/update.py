from typing import List, Tuple
import pandas as pd
from pdlibs import save_prompt
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

        print(record.iloc[list_lines].to_string())
        return (True, record)

    else:
        return (False, record)
