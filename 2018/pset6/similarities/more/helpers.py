from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""
    # Set up 2D list
    h = len(a) + 1
    w = len(b) + 1
    m = [[0 for x in range(w)] for y in range(h)]

    # Add values for base cases(first row and first column)
    m[0][0] = (0, 0)
    for i in range(1, h):
        m[i][0] = (i ,Operation.DELETED)
    for j in range(1, w):
        m[0][j] = (j ,Operation.INSERTED)

    # Fill in the other entries in the table
    calculate(a, b, m)
    return m

def calculate(a, b, matrix):
    if len(a) == 0 or len(b) == 0:
        return matrix[len(a)][len(b)][0]

    # Deletion: cost[i - 1][j] + 1
    # Insertion: cost[i][j - 1] + 1
    # Substitution: cost[i -1][j - 1] if ith char of a is jth char of b
    #               cost[i -1][j - 1] + 1 otherwise
    matrix[len(a)][len(b)] = (calculate(a[:len(a) - 1],b, matrix) + 1, Operation.DELETED)
    ins = calculate(a,b[:len(b) - 1],matrix)
    if matrix[len(a)][len(b)][0] > ins + 1:
        matrix[len(a)][len(b)] = (ins + 1, Operation.INSERTED)

    subs = calculate(a[:len(a) - 1],b[:len(b) - 1], matrix)
    if matrix[len(a)][len(b)][0] > subs and a[len(a) - 1] == b[len(b) - 1]:
        matrix[len(a)][len(b)] = (subs, Operation.SUBSTITUTED)
    elif matrix[len(a)][len(b)][0] > subs + 1:
        matrix[len(a)][len(b)] = (subs + 1, Operation.SUBSTITUTED)

    return matrix[len(a)][len(b)][0]