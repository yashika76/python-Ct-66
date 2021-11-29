
n = int(input("Enter a number: "))

def armstrong(num):
  sum = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
  return sum

summ=armstrong(n)
if n == summ:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")