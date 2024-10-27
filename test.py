import numpy as np

def mod_rest(x, m):
    return x // m, x % m

def incodeListInArray(L):
    A = np.array([0,0,0], dtype=np.int32)
    for x in L:
        d, r = mod_rest(x - 1, 30)
        #print(d, r)
        A[d] += 1 << r
        #print(A[d], type(A[d]))
    return A

def printBinaryArray(A):
    for x in A:
        print(bin(x), end = " ")
    print()

def incodeSheetIntoMatrix(L):
    A = np.zeros((3, 3), dtype=np.int32)
    for i, l in enumerate(L):
        for x in l:
            d, r = mod_rest(x - 1, 30)
            A[i, d] += 1 << r
    return A

L = [1, 5, 15, 25, 50]
M = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
N = range(1, 91)
#print(2 << 30)

print(1 << 1)

A = incodeListInArray(L)
B = incodeListInArray(M)

printBinaryArray(A)
printBinaryArray(B)

printBinaryArray(A & B)

printBinaryArray(incodeListInArray(N))

print(incodeSheetIntoMatrix([L, M, N]))