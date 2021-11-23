from math import sqrt

# my_arr = [1, 5, 2, 4, 6, 1, 3, 5, 7]
my_arr = [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]
n = len(my_arr)

blk_sz = int(sqrt(n))
blocks = [0] * (n // blk_sz + 1)


# print(blk_sz, blocks)


def preprocess(arr: list, n: int, blk_sz: int) -> None:
    blk_idx = -1

    for i in range(n):
        if i % blk_sz == 0:
            blk_idx += 1

        blocks[blk_idx] += arr[i]


def print_sum(l: int, r: int) -> None:
    sum = 0

    while l < r and l % blk_sz != 0 and l != 0:
        sum += my_arr[l]
        l += 1

    while l + blk_sz <= r:
        sum += blocks[l // blk_sz]
        l += blk_sz

    while l <= r:
        sum += my_arr[l]
        l += 1

    print(sum)


def update(i: int, val: int) -> None:
    blocks[i // blk_sz] += val - my_arr[i]
    my_arr[i] = val


preprocess(my_arr, n, blk_sz)
print(blocks)

print_sum(1, 7)

