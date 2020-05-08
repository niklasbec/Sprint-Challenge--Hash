def get_indices_of_item_weights(weights, length, limit):
    hashTable = {}

    for i in range(length):
        req = limit - weights[i]
        if req in hashTable.values():
            return [i, weights.index(req)]
        else:
            hashTable[i] = weights[i]
            i += 1
    return None

testingWeights = [1, 2, 3, 4, 5]
limit = 9
result = get_indices_of_item_weights(testingWeights, len(testingWeights), limit)
print(result)