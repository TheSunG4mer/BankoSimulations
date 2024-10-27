import numpy as np
from ConstructBankoSheet import getRandomSheet

def mod_rest(x, m):
    return x // m, x % m

def incodeNumberInArray(x):
    A = np.zeros(3, dtype=np.int32)
    d, r = divmod(x - 1, 30)
    A[d] += 1 << r
    return A

def incodeSheetIntoMatrix(L):
    A = np.zeros((3, 3), dtype=np.int32)
    for i, l in enumerate(L):
        for x in l:
            d, r = divmod(x - 1, 30)
            A[i, d] += 1 << r
    return A


class BankoGame:
    def __init__(self, number_of_sheets):
        self.number_of_sheets = number_of_sheets
    

    def startNewGame(self):
        list_of_sheets = [getRandomSheet() for _ in range(self.number_of_sheets)]
        self.arrayOfSheets = np.array(list_of_sheets)
        self.number_of_announced_numbers = 0

    def announceNumber(self, number):
        self.number_of_announced_numbers += 1
        self.arrayOfSheets = self.arrayOfSheets & np.bitwise_not(incodeNumberInArray(number))
    
    