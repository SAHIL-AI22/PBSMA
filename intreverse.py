def intreverse(n):
  a=""
  while n>0:
    b=str(n%10)
    a=a+b
    n=n//10
  return int(a)
print(intreverse(783))
print(intreverse(242789))
print(intreverse(3))