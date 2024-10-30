

import matplotlib.pyplot as plt
from functools import cache
from fractions import Fraction


@cache
def P(a, b, c, k, n):
    if k < 0 or a < 0 or b < 0 or c < 0:
        return Fraction(0)
    if k == 0 and a == 0 and b == 0 and c == 0:
        return Fraction(1)
    return  P(a - 1, b, c, k - 1, n) * Fraction(6 - a, n + 1 - k) + \
            P(a, b - 1, c, k - 1, n) * Fraction(6 - b, n + 1 - k) + \
            P(a, b, c - 1, k - 1, n) * Fraction(6 - c, n + 1 - k) + \
            P(a, b, c, k - 1, n) * Fraction(n - k - 14 + a + b + c, n + 1 - k)

@cache
def getRowProb():
    probs = []
    n = 90
    for i in range(91):
        currentProb = 0
        for a in range(6):
            for b in range(6):
                for c in range(6):
                    if a == 5 or b == 5 or c == 5:
                        currentProb += P(a, b, c, i, n)
        probs.append(currentProb)
    return probs

@cache
def getTwoRowProb():
    probs = []
    n = 90
    for i in range(91):
        currentProb = 0
        for a in range(6):
            for b in range(6):
                for c in range(6):
                    if a == 5 == b or b == 5 == c or c == 5 == a:
                        currentProb += P(a, b, c, i, n)
        probs.append(currentProb)
    return probs

@cache
def getFullSheetProb():
    probs = []
    n = 90
    for i in range(91):
        currentProb = P(5, 5, 5, i, n)
        probs.append(currentProb)
    return probs

def plotProbabilities(data):
    for probabilities in data:
        if len(probabilities) == 91:
            plt.plot(range(91), probabilities)
        else:
            plt.plot(range(1, 91), probabilities)
    plt.show()


def computeStats(probabilities):
    pmf = cdfToPmf(probabilities)
    mean = sum([i * p for i, p in enumerate(pmf)])
    variance = sum([i**2 * p for i, p in enumerate(pmf)]) - mean**2
    standardDeviation = variance**0.5
    median = min(range(91), key=lambda i: abs(probabilities[i] - 0.5))
    return mean, variance, standardDeviation, median

def cdfToPmf(probabilities):
    individualProbabilies = [0] * 91
    for i in range(90):
        individualProbabilies[i+1] = probabilities[i+1] - probabilities[i]
    return individualProbabilies

def pmfToCdf(probabilities):
    cumulativeProbabilities = [0] * 91
    cumulativeProbabilities[0] = probabilities[0]
    for i in range(1, 91):
        cumulativeProbabilities[i] = cumulativeProbabilities[i-1] + probabilities[i]
    return cumulativeProbabilities

def nIndependentSheets(n):
    nSheetResults = []
    for result in [getRowProb(), getTwoRowProb(), getFullSheetProb()]:
        nSheetResults.append([1 - (1 - p) ** n for p in result])
    return nSheetResults

if __name__ == "__main__":
    #plotProbabilities([getRowProb(), getTwoRowProb(), getFullSheetProb()])
    #for i, (p1, p2, p3) in enumerate(zip(getRowProb(), getTwoRowProb(), getFullSheetProb())):
    #    print(f"{i:2d}: {p1:.20f} - {p2:.20f} - {p3:.20f}")
    #print(*computeStats(getRowProb()))
    #print(*computeStats(getTwoRowProb()))
    #print(*computeStats(getFullSheetProb()))
    n = 10
    for i, (p1, p2, p3) in enumerate(zip(*nIndependentSheets(n))):
        print(f"{i:2d}: {p1:.20f} - {p2:.20f} - {p3:.20f}")