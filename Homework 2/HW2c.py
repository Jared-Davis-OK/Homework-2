# region imports
from copy import deepcopy
from NumericalMethods import GaussSeidel
from Gauss_Elim import AugmentMatrix
# endregion
def main():
    # ----- system 1
    A = [[3, 1, -1],
         [1, 4, 1],
         [2, 1, 2]]

    b = [2, 12, 10]

    Aaug = AugmentMatrix(A, b)
    x0 = [0, 0, 0]

    sol1 = GaussSeidel(deepcopy(Aaug), x0, 15)

    print("Solution set 1:", sol1)

    # ----- system 2
    A2 = [[1, -10, 2, 4],
          [3, 1, 4, 12],
          [9, 2, 3, 4],
          [-1, 2, 7, 3]]

    b2 = [2, 12, 21, 37]

    Aaug2 = AugmentMatrix(A2, b2)
    x02 = [0, 0, 0, 0]

    sol2 = GaussSeidel(deepcopy(Aaug2), x02, 15)

    print("Solution set 2:", sol2)

    pass


if __name__=="__main__":
    main()