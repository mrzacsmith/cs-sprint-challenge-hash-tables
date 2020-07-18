def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    # cache = dict()
    cache = {}

    for i in range(length):
        if weights[i] in cache:
            index_location = cache[weights[i]]
            return (i, index_location)

        cache[limit - weights[i]] = i

    return None
