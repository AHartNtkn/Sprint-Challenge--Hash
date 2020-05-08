def get_indices_of_item_weights(weights, length, limit):
    dict = {}

    for i, w in enumerate(weights):
        dict[w] = i

    for i, w in enumerate(weights):
        r = dict.get(limit - w, None)
        if r:
            return [ r, i ]

    return None
