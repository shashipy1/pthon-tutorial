def percent(marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100 
    return p
marks1 = [45,46,67,56]
percentage1 = percent(marks1)
#percentage1 = (sum(marks)/400)*100

marks2 = [67,76,86,45]
#percentage2 = (sum(marks)/400)*100
percentage2 = percent(marks2) 

print(percentage1)
print(percentage2)
