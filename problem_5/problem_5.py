def if_divides_all(num):
  for i in range(2, 21):
    if num % i != 0:
      return False
  return True


x = 20
while True:
  if if_divides_all(x):
    break
  else:
    x = x + 1
print(x)
