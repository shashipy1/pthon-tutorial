story='''python is simple language
  and easly to understand.python is a 
  language just like raed a simple book'''
#STRING FUNCTION:-
print(len(story))
print(story[0:5])
print(story[3:9])
print(story.endswith("dhdhfjehf"))
print(story.count("P"))#it is use for 'P' counting
print(story.count("Python"))#this is count word
print(story.count("u"))#it is count any letter as like u
print(story.capitalize())#it convert 1st letter into capital lette
print(story.find("python"))#in a sentance only say about strating of 1st
print(story.find("ptyon"))#-1 it means not present 
print(story.find("python"))
print(story.replace("python","java"))#python=java