#use for open a file contant and read
#f =  open('sample.txt', "r")
f =  open('sample.txt')#by default the mode is r
data = f.read()#read file
#data = f.read(10)#read only 10 charater 
print(data)#print data
f.close()#close file                            