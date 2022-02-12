age = int(input("enter the age"))
if(age>34 and age<57):
#both are true.
    print("you are selected")
else:
    print("you are not selected")
print("OK")    
marks = int(input("enter the marks"))
if(marks>30 or marks<30):
      print("pass")
else:
    print("fail")
print("GOOD")
#IMPORTANT POINT:-None
a = None
if(a is None):
    print("yes")
else:
    print("no")

#In it means no is present in the list so output is true and not present o/p is false
a= [34,55,4,32]
print("55 in a")#true
#print("45 in a") result- false
    
    