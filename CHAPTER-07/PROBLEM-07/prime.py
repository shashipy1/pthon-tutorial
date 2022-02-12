 num = int(input("Enter the number:"))
 prime = True
 for i in range(2,num):
     if(n%i==0):
     prime=False
     break
 if prime:
     print("number is prime")
 else:
     print("number is not prime")