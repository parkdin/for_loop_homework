def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    string = ""
    for i in range(n):
        string += "," + str(i)
    return string[1:]
print(main(5))