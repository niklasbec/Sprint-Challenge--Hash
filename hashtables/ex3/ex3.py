def intersection(arrays):
    hashTable = {}
    doubles = {}

    for array in arrays:
        for el in array:
            if el not in hashTable:
                hashTable[el] = None
            else:
                doubles[el] = None
    result = []
    for key in doubles.keys():
        result.append(key)
    return result
            


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
