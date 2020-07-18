def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for num in a:
        cache[num] = 0

        if num is not 0 and -num in cache:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
