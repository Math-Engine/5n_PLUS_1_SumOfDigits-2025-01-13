import sys
sys.set_int_max_str_digits(2147483647)

param = int(sys.argv[1])

def SumOfDigits(n):
  result = 0
  for i in range(len(str(n))):
    result = result + int(str(n)[i])
  return result

temp = 2
SODs = 0 # Sum Of Digits
for i in range(1, param + 1):
  temp = (temp * 5) + 1
  SODs = SumOfDigits(temp)
  while (len(str(SODs)) != 1):
    SODs = SumOfDigits(SODs)
  if (SODs != 2):
    print(f"반례 ( i : {i} )")
