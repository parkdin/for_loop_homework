def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    list =[]
    i = 0
    for i in range(A , B + 1):
        list.append(i)
    list = list[::-1]
    return list
