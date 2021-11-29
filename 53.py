
def num1(x,y,z):
  def num2(a,b,c):
    return a+b+c
  outer=num2(x,y,z)+5
  return outer

print(num1(5,4,5))