# HackerRank: Raskin Bobbins

# m - dollars

# n - flavors
# c - flavors cost

# t - trips

test_1 = '2\n4\n5\n1 4 5 3 2\n4\n4\n2 2 4 3'


def raskin_bobbins(lines: str) -> None:
    list_of_lines = lines.splitlines()
    t = list_of_lines[0]

    for i in range(1, len(list_of_lines), 3):
        m = list_of_lines[i]
        n = list_of_lines[i + 1]
        c = list_of_lines[i + 2].split()

        print(m, n, c)

    # print('\n')  # n[i] n[j] - ice cream ids, n[i] < n[j]


raskin_bobbins(test_1)
