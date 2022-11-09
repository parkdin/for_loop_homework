def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    sum = 0
    for i in range(0, N):
        if i%2!=0:
            sum += i
    return sum
print(main(12))