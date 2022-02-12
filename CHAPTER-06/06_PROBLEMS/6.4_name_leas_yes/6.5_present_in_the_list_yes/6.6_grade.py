marks = int(input("Enter Your Marks"))

#if(marks>90 or marks<=100):
 # print("Exelent")
  
#if(marks>80 or marks<=90):
 # print("A")
  
#if(marks>70 or marks<=80):
 # print("B")
  
#if(marks>60 or marks<=70):
 # print("C")  
  
#if(marks>50 or marks<=60):
#  print("D")  
  
#else:
   # print("fail")
if marks > 90:
    grade = "Exelent"
elif marks > 80:
    grade = "A"
elif marks > 70:
    grade = "B"
elif marks > 60:
    grade = "C"
elif marks > 50:
    grade = "D"
else:
    grade = "F"
    print("Your grade is", + grade)