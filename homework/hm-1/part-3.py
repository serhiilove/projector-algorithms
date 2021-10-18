arr = [1, 2, 2, 2, 2, 2, 2, 8, 9, 10]

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

print('Majority element: ', find_maj_el(arr))