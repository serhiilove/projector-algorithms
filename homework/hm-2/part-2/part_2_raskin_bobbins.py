# HackerRank: Raskin Bobbins

# t - trips
# m - dollars
# n - flavors
# c - flavors cost []

test_1 = '2\n4\n5\n1 4 5 3 2\n4\n4\n2 2 4 3'


def raskin_bobbins(lines: str) -> None:
    list_of_lines = lines.splitlines()

    for k in range(1, len(list_of_lines), 3):
        m = int(list_of_lines[k])
        n = int(list_of_lines[k + 1])
        c = list(map(int, (list_of_lines[k + 2].split())))

        c_sorted = sorted(enumerate(c), key=lambda i: i[1])
        id_i = 0
        id_j = n - 1

        for j, cj in reversed(list(enumerate(c_sorted))):
            if cj[1] + c_sorted[id_i][1] == m:
                id_j = j
                break
            if cj[1] < m - c_sorted[id_i][1]:
                id_i += 1

        print(c_sorted[id_i][0] + 1, c_sorted[id_j][0] + 1)


raskin_bobbins(test_1)
