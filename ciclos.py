# # while
# i = 0

# while i < 100:
#   print(i)
#   i += 1

# # for
# for i in range(20):
#   print(i)


# break
for n in range(2, 10):
  # print(n)
  for x in range(2, n):
    if n % x == 0:
      # print (n, x, "modulo", n % x)
      print(n, "es igual a", x, "*", n//x)
      break
  else:
    print("Es primo")

# continue
# for num in range(2, 10):
#   if num % 2 == 0:
#     print('Found an even number', num)
#     continue
#   print('Found an odd number', num)