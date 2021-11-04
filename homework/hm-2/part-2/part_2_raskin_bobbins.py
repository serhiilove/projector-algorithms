# HackerRank: Raskin Bobbins

# t - trips
# m - dollars
# n - flavors
# c - flavors cost []

test_1 = '2\n4\n5\n1 4 5 3 2\n4\n4\n2 2 4 3'


def raskin_bobbins(lines: str) -> None:
    list_of_lines = lines.splitlines()
    t = list_of_lines[0]

    for k in range(1, len(list_of_lines), 3):
        m = int(list_of_lines[k])
        n = int(list_of_lines[k + 1])
        c = list_of_lines[k + 2].split()

        print(m, n, c)

        c_sorted = c
        c_sorted.sort()
        id_i = 0
        id_j = n - 1

        for j, cj in reversed(list(enumerate(c_sorted))):
            if int(cj) + int(c_sorted[id_i]) == m:
                id_j = j
                break
            if int(cj) < m - int(c_sorted[id_i]):
                id_i += 1

        print('ids | values in sorted array: ', id_i, id_j, '|', c_sorted[id_i], c_sorted[id_j])


raskin_bobbins(test_1)
