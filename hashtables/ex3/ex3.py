def intersection(arrays):
    """
    YOUR CODE HERE
    """

    intersect = {}
    result = []

    for i in arrays:
        for num in i:
            if num in intersect:
                intersect[num] += 1
            else:
                intersect[num] = 1

            for num in intersect:
                result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
