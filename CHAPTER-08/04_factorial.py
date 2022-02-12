
'''n = 0
product = 1
for i in range(n):
    product = product * (i+1)
print(product)
'''
def factorial_iter(n):
    product = 1 
    for i in range(n):
      product = product * (i+1)
    return product
def factorial_recursive(n)
   if n == i or n == 1:
      return 1
    return n * factorial_recursive(n-1)
  #f = fractorial_iter(5)
   f = factorial_recursive(5)
print(f)