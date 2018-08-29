from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    a_lines = a.splitlines()
    a_set = set(a_lines)
    b_lines = b.splitlines()
    b_set = set(b_lines)
    return a_set & b_set


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    a_lines = sent_tokenize(a)
    a_set = set(a_lines)
    b_lines = sent_tokenize(b)
    b_set = set(b_lines)
    return a_set & b_set


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    if len(a) < n or len(b) < n:
        return []

    a_len = len(a)
    a_set = set()
    for i in range(a_len - n + 1):
        a_set.add(a[i:i+n])
        #print(a_set)

    b_len = len(b)
    b_set = set()
    for i in range(b_len - n + 1):
        b_set.add(b[i:i+n])

    return a_set & b_set
