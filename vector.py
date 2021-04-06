#!/usr/bin/env python3
import numpy as np
import argparse

# We can create vectors through this class
class rVector:

    def r2Vector(com1, com2):
        a = np.array([[com1], [com2]])
        return a

    def r3Vector(com1, com2, com3):
        a = np.array([[com1], [com2], [com3]])
        return a


# Sum vector spaces
class sumVectorSpaces:

    def sumR2Vector(vec1, vec2):
        sum_a = np.array([vec1 +  vec2])
        return sum_a

    def sumR3Vector(vec1, vec2):
        sum_a = np.array([vec1 + vec2])
        return sum_a

#defining classes
vec = rVector
sumvec = sumVectorSpaces

# Outputting vector additions
def r2VecOutput():
    print("-- R2-VECTOR ADDITION --")

    # Vector A
    vecInputAH = int(input("A-H Component: "))
    vecInputAV = int(input("A-V Compnent: "))
    vecA = vec.r2Vector(vecInputAH, vecInputAV)
    
    print()

    # Vector B
    vecInputBH = int(input("B-H Component: "))
    vecInputBV = int(input("B-V Component: "))
    vecB = vec.r2Vector(vecInputBH, vecInputBV)

    ABsum = sumvec.sumR2Vector(vecA, vecB)
    print(">> R2 SUM: ")
    print(ABsum)

def r3VecOutput():
    # Vector A
    vecInputAH = int(input("A-H Component: "))
    vecInputA2 = int(input("A-2 Component: "))
    vecInputAV = int(input("A-V Component: "))
    vecA = vec.r3Vector(vecInputAH, vecInputA2, vecInputAV)
    
    print()

    # Vector B
    vecInputBH = int(input("B-H Component: "))
    vecInputB2 = int(input("B-2 Component: "))
    vecInputBV = int(input("B-V Component: "))
    vecB = vec.r3Vector(vecInputBH, vecInputB2, vecInputBV)

    ABsum = sumvec.sumR3Vector(vecA, vecB)
    print(">> R3 SUM: ")
    print(ABsum)


def main():
    print("-- R2/3 - VECTOR ADDITION --")
    print("(1) R2 ")
    print("(2) R3")

    choice = int(input(">> "))

    if choice == 1:
        r2VecOutput()

    elif choice == 2:
        r3VecOutput()

main()
