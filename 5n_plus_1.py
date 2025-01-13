import sys
sys.set_int_max_str_digits(2147483647)

param = int(sys.argv[1])

temp = 2
for i in range(1, param + 1):
  temp = (temp * 5) + 1
  print(temp)
