def fibbonaci(n):
 if n==1 or n==2:
  return 1
 return fibbonaci(n-1)+fibbonaci(n-2)
print (fibbonaci(7))
