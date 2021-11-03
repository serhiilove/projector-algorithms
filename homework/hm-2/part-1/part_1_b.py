a = [1, 3, 0, 2]
x = 2

def eval_polynomial(a: list, x: int) -> int:
    k = len(a) - 1
    b_prev = a[k]

    for i in range(k, 0, -1):
        b = a[i - 1] + b_prev * x
        b_prev = b

    return b


sum = eval_polynomial(a, x)
print(sum)
