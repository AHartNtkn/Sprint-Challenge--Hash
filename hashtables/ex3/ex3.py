def intersection(arrays):
    ht = {}

    for a in arrays:
        for i in a:
            if ht.get(i, None) is None:
                ht[i] = 0
            ht[i] += 1

    result = []

    for i, n in ht.items():
        if n == len(arrays):
            result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
