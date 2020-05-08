def get_indices_of_item_weights(weights, length, limit):
    ht = {}

    for i, w in enumerate(weights):
        ht[w] = i

    for i, w in enumerate(weights):
        r = ht.get(limit - w, None)
        if r:
            return [ r, i ]

    return None
