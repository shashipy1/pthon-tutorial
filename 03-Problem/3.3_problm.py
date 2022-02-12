letter='''Dear </name/>
Your are selected!

date:</date/>
'''
name=input("Enter your name")
date=input("Enter date")
letter=letter.replace("</name/>",name)
letter=letter.replace("</date/>",date)
print(letter)  