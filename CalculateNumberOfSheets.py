from functools import cache
from math import comb, factorial, prod
import random
from time import time

import numpy as np

def possibleNumbersInColumn(column):
    if column == 1:
        return 11
    elif column == 9:
        return 9
    else:
        return 10

@cache
def getNumberOfSheets(top_row = 5, middle_row = 5, bottom_row = 5, coloumns_left = 9):
    if top_row == 0 and middle_row == 0 and bottom_row == 0 and coloumns_left == 0:
        return 1
    if coloumns_left == 0 or top_row < 0 or middle_row < 0 or bottom_row < 0:
        return 0
    total = 0
    total += getNumberOfSheets(top_row - 1, middle_row, bottom_row, coloumns_left - 1)# * possibleNumbersInColumn(coloumns_left)
    total += getNumberOfSheets(top_row, middle_row - 1, bottom_row, coloumns_left - 1)# * possibleNumbersInColumn(coloumns_left)
    total += getNumberOfSheets(top_row, middle_row, bottom_row - 1, coloumns_left - 1)# * possibleNumbersInColumn(coloumns_left)
    total += getNumberOfSheets(top_row - 1, middle_row - 1, bottom_row, coloumns_left - 1)# * comb(possibleNumbersInColumn(coloumns_left), 2)
    total += getNumberOfSheets(top_row - 1, middle_row, bottom_row - 1, coloumns_left - 1)# * comb(possibleNumbersInColumn(coloumns_left), 2)
    total += getNumberOfSheets(top_row, middle_row - 1, bottom_row - 1, coloumns_left - 1)# * comb(possibleNumbersInColumn(coloumns_left), 2)
    total += getNumberOfSheets(top_row - 1, middle_row - 1, bottom_row - 1, coloumns_left - 1)# * comb(possibleNumbersInColumn(coloumns_left), 3)
    return total


if __name__ == "__main__":
    start = time()
    print(getNumberOfSheets())
    print(f"Time: {time() - start}")
# Number of sheets: 3669688706217187500
# Number of sheets without placing any numbers (i.e just placements of numbers): 735210