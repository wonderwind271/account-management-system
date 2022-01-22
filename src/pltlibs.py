# practical functions related to matplotlib that may use several times

import matplotlib.pyplot as plt
import pandas as pd


def plotPartInAll(part_rec: pd.DataFrame, all_rec: pd.DataFrame):
    # draw a pie diagram with 2 part: part_rec and the rest. With respect to price
    # suppose all_rec contains part_rec, otherwise ub
    part_price = round(sum(part_rec['price'].tolist()), 2)
    all_price = round(sum(all_rec['price'].tolist()), 2)
    plt.pie([part_price, all_price - part_price], explode=(0.2, 0))
    plt.show()
