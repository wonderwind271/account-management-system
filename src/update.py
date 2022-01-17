from typing import List, Tuple
import pandas as pd
import numpy as np


def update(record: pd.DataFrame, args: List[str], fileName: str) -> Tuple[bool, pd.DataFrame]:
    if args[0] == 'del':
        del_lines = list(map(int, args[1:]))



    return False, record
