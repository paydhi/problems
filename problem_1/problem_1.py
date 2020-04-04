# Created by: Paydhi
x = 0
i = 1
while i < 1000:
    i = i + 1
    if i % 3 == 0 or i % 5 == 0:
        # print('in progress...')
        x = x + i

print(x)
