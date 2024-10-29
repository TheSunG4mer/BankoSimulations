from functools import cache
from math import comb, factorial, prod
import random
from time import time

import numpy as np



# Not all placements have same number of sheets, however, we will generate placements uniformly
# and then randomly select a placement to generate a sheet

def numberOfSheetsWithListType(top_row, middle_row, bottom_row, listType):
    if not listType and top_row == 0 and middle_row == 0 and bottom_row == 0:
        return 1
    if top_row < 0 or middle_row < 0 or bottom_row < 0:
        return 0
    if not listType:
        return 0
    total = 0
    if listType[0] == 1:
        total += numberOfSheetsWithListType(top_row - 1, middle_row, bottom_row, listType[1:])
        total += numberOfSheetsWithListType(top_row, middle_row - 1, bottom_row, listType[1:])
        total += numberOfSheetsWithListType(top_row, middle_row, bottom_row - 1, listType[1:])
        return total
    if listType[0] == 2:
        total += numberOfSheetsWithListType(top_row - 1, middle_row - 1, bottom_row, listType[1:])
        total += numberOfSheetsWithListType(top_row - 1, middle_row, bottom_row - 1, listType[1:])
        total += numberOfSheetsWithListType(top_row, middle_row - 1, bottom_row - 1, listType[1:])
        return total
    if listType[0] == 3:
        return numberOfSheetsWithListType(top_row - 1, middle_row - 1, bottom_row - 1, listType[1:])

@cache
def numberOfSheetsWithType(one_coloumns, two_coloumns, three_coloumns, number_of_coloumns = 9):
    waysOfDistribution = factorial(number_of_coloumns) // (factorial(one_coloumns) * factorial(two_coloumns) * factorial(three_coloumns))
    return waysOfDistribution * numberOfSheetsWithListType(5, 5, 5, tuple([1] * one_coloumns + [2] * two_coloumns + [3] * three_coloumns))

#print(numberOfSheetsWithType(6, 0, 3) + numberOfSheetsWithType(5, 2, 2) + numberOfSheetsWithType(4, 4, 1) + numberOfSheetsWithType(3, 6, 0))

## we encode a sheets coloumns into a list of seven entries. First three are coloumns with one number (above, middle, below), 
## next three are coloumns with two numbers, and last one is coloumn with three numbers. We simply conut the number of each type of 
## coloumn on a sheet. We list all possible type of sheet, and calculate their probablility of occuring:

@cache
def multinomial(L):
    """
    Calculate the multinomial coefficient for a given list of integers.

    The multinomial coefficient is a generalization of the binomial coefficient.
    It is used to find the number of ways to partition a set of objects into
    several groups of specified sizes.

    Args:
        L (list of int): A list of integers representing the sizes of the groups.

    Returns:
        int: The multinomial coefficient.

    Example:
        >>> multinomial([2, 3, 4])
        1260
    """
    return factorial(sum(L)) // (prod([factorial(x) for x in L]))

@cache
def getCummulativeFrequenciesForSheetTypes():
    """
    Calculate the cumulative frequencies for different sheet types.
    This function defines a list of sheet types, each represented by a list of integers.
    It calculates the probability of each sheet type occurring using a multinomial distribution.
    The function then computes the cumulative frequencies of these probabilities.
    Returns:
        tuple: A tuple containing:
            - cummulative_frequencies (list): A list of cumulative frequencies for the sheet types.
            - sheet_types (list): The original list of sheet types.
    """
    sheet_types = [
        [2, 2, 2, 0, 0, 0, 3],


        [1, 1, 3, 2, 0, 0, 2],
        [1, 3, 1, 0, 2, 0, 2],
        [3, 1, 1, 0, 0, 2, 2],
        [1, 2, 2, 1, 1, 0, 2],
        [2, 1, 2, 1, 0, 1, 2],
        [2, 2, 1, 0, 1, 1, 2],


        [0, 0, 4, 4, 0, 0, 1],
        [0, 4, 0, 0, 4, 0, 1],
        [4, 0, 0, 0, 0, 4, 1],

        [0, 2, 2, 2, 2, 0, 1],
        [2, 0, 2, 2, 0, 2, 1],
        [2, 2, 0, 0, 2, 2, 1],
        [2, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 1, 2, 1, 1],
        [1, 1, 2, 2, 1, 1, 1],

        [0, 1, 3, 3, 1, 0, 1],
        [0, 3, 1, 1, 3, 0, 1],
        [1, 0, 3, 3, 0, 1, 1],
        [3, 0, 1, 1, 0, 3, 1],
        [1, 3, 0, 0, 3, 1, 1],
        [3, 1, 0, 0, 1, 3, 1],


        [1, 1, 1, 2, 2, 2, 0],

        [3, 0, 0, 1, 1, 4, 0],
        [0, 3, 0, 1, 4, 1, 0],
        [0, 0, 3, 4, 1, 1, 0],

        [2, 1, 0, 1, 2, 3, 0],
        [1, 2, 0, 1, 3, 2, 0],
        [2, 0, 1, 2, 1, 3, 0],
        [1, 0, 2, 3, 1, 2, 0],
        [0, 2, 1, 2, 3, 1, 0],
        [0, 1, 2, 3, 2, 1, 0]
    ]

    ## we calculate the probability of each sheet type occuring
    frequency = []

    for sheet_type in sheet_types:
        frequency.append(multinomial(tuple(sheet_type)))

    assert all([sum(l) == 9 for l in sheet_types])
    #print(sum(frequency)) # check if all sheet types are covered
    #print(len(frequency)) # check if all sheet types are covered
    cummulative_frequencies = [frequency[0]]
    for i in range(1, len(frequency)):
        cummulative_frequencies.append(cummulative_frequencies[-1] + frequency[i])
    return cummulative_frequencies, sheet_types

def getRandomSheetType():
    """
    Selects a random sheet type based on cumulative frequencies.

    This function retrieves cumulative frequencies and corresponding sheet types,
    generates a random integer within the range of the cumulative frequencies,
    and returns the sheet type that corresponds to the generated random integer.

    Returns:
        list: The selected sheet type.
    """
    cummulative_frequencies, sheet_types = getCummulativeFrequenciesForSheetTypes()
    r = np.random.randint(0, cummulative_frequencies[-1])
    for i, cf in enumerate(cummulative_frequencies):
        if r < cf:
            return sheet_types[i]

@cache
def getInterval(coloumn_number):
    if coloumn_number == 1:
        return 1, 10
    if coloumn_number == 9:
        return 80, 91
    else:
        return 10 * (coloumn_number - 1), 10 * coloumn_number

@cache
def convertTypeToIndecies(sheet_type):
    if sheet_type < 4:
        return [sheet_type - 1]
    elif sheet_type < 7:
        return sorted([(1 - sheet_type) % 3, (2 - sheet_type) % 3])
    else:
        return [0, 1, 2]

def getSheetFromType(sheet_type):
    """
    Generates a bingo sheet based on the provided sheet type.
    Args:
        sheet_type (list of int): A list where each element represents the count of a specific type of number.
    Returns:
        numpy.ndarray: A 3x3 numpy array representing the bingo sheet.
    Raises:
        ValueError: If the input sheet_type is not valid.
    Note:
        - The function uses random sampling to generate the numbers for the bingo sheet.
        - The function assumes that `getInterval` and `convertTypeToIndecies` are defined elsewhere in the code.
    """
    types = []
    for i, count in enumerate(sheet_type):
        types.extend([i + 1] * count)
    #print(types)
    random.shuffle(types)
    
    A = np.zeros((3, 3), dtype=np.int32)
    #L = [[0 for _ in range(9)] for _ in range(3)]

    for i, type in enumerate(types):
        numbers_to_use = sorted(list(random.sample(range(*getInterval(i + 1)), (type + 2) // 3)))
        for j, index in enumerate(convertTypeToIndecies(type)): #Should probably use zip here
            x = numbers_to_use[j]
            d, r = divmod(x - 1, 30)
            A[index, d] += 1 << r
            #L[index][i] = x
    return A#, L

def getRandomSheet():
    """
    Generates a random banko sheet.

    Returns:
        Numpy Array: A list representing the banko sheet generated from the selected type. Dimensions: 3x3
    """
    sheet_type = getRandomSheetType()
    return getSheetFromType(sheet_type)

if __name__ == "__main__":
    for _ in range(10):
        sheet_type = getRandomSheetType()
        print(sheet_type)
        A, L = getSheetFromType(sheet_type)
        print(A)
        for l in L:
            print(" ".join([f"{x:2d}" for x in l]))