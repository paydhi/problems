def sum_of_squares_untill(n):
    x = 0
    for i in range(n + 1):
        x = x + i ** 2
    return x


def square_of_sum_untill(n):
    y = 0
    for i in range(n + 1):
        y = y + i
    return y ** 2


print(sum_of_squares_untill(100) + square_of_sum_untill(100))
