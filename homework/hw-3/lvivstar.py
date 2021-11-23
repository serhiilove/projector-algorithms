from math import sqrt

# getting input data

# n = int(input())
# c = list(map(int, input().split()))
# q = int(input())
#
# queries = list()
#
# for qi in range(q):
#     query = input()
#     queries.append(query)


# test data input

n = 5
c = [2, 0, 2, 3, 1]
q = 9

queries = [
    'COUNT 2 4',
    'ENTER 2',
    'LEAVE 1',
    'COUNT 2 4',
    'LEAVE 5',
    'COUNT 4 5',
    'COUNT 1 2',
    'ENTER 2',
    'COUNT 1 2'
]

# preprocess data
blk_sz = int(sqrt(n))
blocks = [0] * (n // blk_sz + 1)


def preprocess(arr: list, n: int) -> None:
    blk_idx = -1

    for i in range(n):
        if i % blk_sz == 0:
            blk_idx += 1

        blocks[blk_idx] += arr[i]


def print_sum(l: int, r: int) -> None:
    sum = 0

    while l < r and l % blk_sz != 0 and l != 0:
        sum += c[l]
        l += 1

    while l + blk_sz <= r:
        sum += blocks[l // blk_sz]
        l += blk_sz

    while l <= r:
        sum += c[l]
        l += 1

    print(sum)


# def update(i: int, val: int) -> None:
#     blocks[i // blk_sz] += val - c[i]
#     c[i] = val


def parse_queries(queries_list: list) -> list:
    splited_values = list(map(lambda s: s.split(), queries_list))

    def format_query(a: list) -> list:
        if a[0] == 'COUNT':
            return [a[0], int(a[1]), int(a[2])]

        return [a[0], int(a[1])]

    return list(map(format_query, splited_values))


def process_queries(clients: list, events: list) -> None:
    for evt in events:
        if evt[0] == 'COUNT':
            print_sum(evt[1] - 1, evt[2] - 1)
            continue

        d = 1 if evt[0] == 'ENTER' else -1
        new_value = clients[evt[1] - 1] + d

        # update(evt[1] - 1, new_value)

        blocks[(evt[1] - 1) // blk_sz] += d
        c[evt[1] - 1] = new_value



preprocess(c, n)
parsed_queries = parse_queries(queries)
process_queries(c, parsed_queries)



