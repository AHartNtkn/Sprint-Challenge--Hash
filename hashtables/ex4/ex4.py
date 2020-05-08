def has_negatives(a):
    ht = {}
    result = []

    for i in a:
        if i != 0:
            ht[i] = True
            if ht.get(-i, None) is not None:
                result.append(abs(i))

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
