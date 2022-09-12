# Q: given k, get x such that k ≥ Σƒ(x)
# ƒ(x) – count of set bits at odd positions, where LSB is position 1


# ƒ(x):
# set bit count for k = prev_sum && set bit count for k+1 = curr_sum
def set_bit_count(k):
    prev_sum, curr_sum = 0, 0
    curr_value, iter_var = 1, 1
    while (curr_value <= k+1):
        prev_sum = curr_sum
        iter_var = curr_value
        while (iter_var != 0):
            if (iter_var & 1 == 1):
                curr_sum += 1
            iter_var = iter_var >> 2
        curr_value += 1
    return prev_sum, curr_sum


# given k, returns x such that k ≥ Σƒ(x)
def number_finder(k):
    x = k // 2
    while (True):
        x_bit_set = set_bit_count(x)
        if (k >= x_bit_set[0] and k < x_bit_set[1]):
            return x
        elif (k > x_bit_set[0] and k > x_bit_set[1]):
            x += 1
        elif (k == x_bit_set[1]):
            return x+1
        else:
            x -= 1


print(number_finder(7))
# expected output: 6
