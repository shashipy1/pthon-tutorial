
sub1 = int(input("Enter 1st subject marks"))
sub2 = int(input("Enter 2nd subject marks"))
sub3 = int(input("Enter 3rd subject marks"))
if(sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("Fail,bacuse you marks is less than 33 percent")

if(sub1+sub2+sub3)/3<40:
    print("Your percent is less than 40,Fail")
else:
    print("Conguatulation!,You are passed in the exam 2021")
    
    