# N - кількість базових станцій
# C [ c1, ... , cn] - кількість клієнтів базових станцій
# Q - кількість запитів

test_1 = '5\n2 0 2 3 1\n9\nCOUNT 2 4\nENTER 2\nLEAVE 1\nCOUNT 2 4\nLEAVE 5\nCOUNT 4 5\nCOUNT 1 2\nENTER 2\nCOUNT 1 2'

def parseInput(input: str) -> list:
    lines = input.splitlines()
    data = [None] * 4
    data[0] = int(lines[0])
    data[1] = list(map(int, lines[1].split()))
    data[2] = int(lines[2])
    data[3] = lines[3:len(lines)]

    return data

def parseEvent(e: str) -> tuple:
    pass


def countClients(input: str) -> None:
    data = parseInput(input)
    print(data)


countClients(test_1)