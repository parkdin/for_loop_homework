def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    list = []
    i = 0
    for i in range(n):
        list.append(k)
    return list
