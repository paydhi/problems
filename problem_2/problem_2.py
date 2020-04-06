def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


fibonacci_list = []
j = 1
while fibonacci(j) <= 4000000:
    fibonacci_list.append(fibonacci(j))
    j = j + 1
print(sum(fibonacci_list))
