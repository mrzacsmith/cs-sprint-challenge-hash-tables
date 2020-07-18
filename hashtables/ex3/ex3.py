def intersection(arrays):
    """
    YOUR CODE HERE
    """

    intersect = {}
    # result = []

    for array in arrays:
        for num in array:
            if num in intersect:
                intersect[num] += 1
            else:
                intersect[num] = 1

            # for num in intersect:
                # result.append(num)

    # return result
    return [key for key, value in intersect.items() if value == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
