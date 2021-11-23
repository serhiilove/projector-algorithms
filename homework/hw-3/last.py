from math import sqrt

# input data

n = int(input())
c = list(map(int, input().split()))
q = int(input())

queries = list()

for qi in range(q):
    query = input()
    queries.append(query)

# preprocess data

blk_sz = int(sqrt(n))
blocks = [0] * (n // blk_sz + 1)


def preprocess(arr: list, n: int) -> None:
    blk_idx = -1

    for i in range(n):
        if i % blk_sz == 0:
            blk_idx += 1

        blocks[blk_idx] += arr[i]


preprocess(c, n)


# main part

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


def update(i: int, val: int) -> None:
    blocks[i // blk_sz] += val - c[i]
    c[i] = val


def process_queries(clients: list, queries_list: list) -> None:
    for q_str in queries_list:
        parsed_query = q_str.split()
        event = parsed_query[0]

        if event == 'COUNT':
            start = int(parsed_query[1]) - 1
            end = int(parsed_query[2]) - 1

            print_sum(start, end)

            continue

        tower = int(parsed_query[1]) - 1
        d = 1 if event == 'ENTER' else -1
        new_value = clients[tower] + d

        update(tower, new_value)


process_queries(c, queries)





