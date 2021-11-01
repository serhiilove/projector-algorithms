# arr = [1, 2, 2, 2, 2, 2, 2, 8, 9, 10]
arr = [5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 5, 3, 3, 5, 3]

def find_maj_el(arr: arr) -> int:
    counter = 0
    candidate = None
    for el in arr:
        if counter == 0:
            candidate = el
            counter = 1
        elif candidate == el:
            counter += 1
        else:
            counter -= 1
    return candidate

def find_maj_el_2(arr: arr) -> int:
    list_of_pairs = []
    maj_pair = [None, 0]
    for el in arr:
        pair = [item for item in list_of_pairs if item[0] == el]
        if len(pair) != 0:
            pair[0][1] += 1
        else:
            list_of_pairs.append([el, 1])

    for pair in list_of_pairs:
        if pair[1] > maj_pair[1]:
            maj_pair = pair
    return maj_pair[0]

print('Majority element 1: ', find_maj_el(arr))
print('Majority element 2: ', find_maj_el_2(arr))