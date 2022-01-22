# practical functions related to matplotlib that may use several times

import matplotlib.pyplot as plt
import pandas as pd


def plotPartInAll(part_rec: pd.DataFrame, all_rec: pd.DataFrame, label=None):
    # draw a pie diagram with 2 part: part_rec and the rest. With respect to price
    # suppose all_rec contains part_rec, otherwise ub
    part_price = round(sum(part_rec['price'].tolist()), 2)
    all_price = round(sum(all_rec['price'].tolist()), 2)
    plt.pie([part_price, all_price - part_price], labels=label, explode=(0.2, 0))
    plt.show()


def plotPartsInAll(parts_rec: list[pd.DataFrame], all_rec: pd.DataFrame, label=None):
    # draw a pie diagram with many parts: parts_rec(with many part) and the rest. With respect to price
    # suppose all_rec contains part_rec, otherwise ub
    prices = []
    for part in parts_rec:
        prices.append(round(sum(part['price'].tolist()), 2))
    rest = round(sum(all_rec['price'].tolist()) - sum(prices), 2)
    prices.append(rest)
    plt.pie(prices, labels=label, explode=tuple([0.0] * len(parts_rec) + [0.2]))
    plt.show()
