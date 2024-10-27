import numpy as np
from ConstructBankoSheet import getRandomSheet
from BankoGame import incodeNumberInArray, incodeSheetIntoMatrix

list_of_sheets = [getRandomSheet() for _ in range(10)]
arrayOfSheets = np.array(list_of_sheets)

#print(arrayOfSheets)
A = incodeSheetIntoMatrix([[1, 24, 51, 79, 81], [5, 11, 30, 54, 66], [7, 15, 29, 35, 45]])
B = incodeSheetIntoMatrix([[3, 21, 53, 75, 85], [8, 12, 31, 59, 69], [9, 15, 28, 32, 49]])
arrayOfSheets = np.array([A, B])
print(A)
print(A & np.bitwise_not(incodeNumberInArray(11)))
print(f"All sheets:\n{arrayOfSheets}\n")
print(f"Minus 11:\n{arrayOfSheets & np.bitwise_not(incodeNumberInArray(11))}\n")