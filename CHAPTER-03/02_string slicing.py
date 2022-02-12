greeting='Good morning, '
#name="Shashi"
#print(type(name))
#print(greeting + name)
#WE CAN  ALSO WRITE 
'''c=greeting + name
#Concantenating two string
#print(c)'''
name="SHASHI"
#Indexing of string
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
#IndexError: string index out of range
#print(name[6])
#name[5]="f"-->does not access
#TypeError: 'str' object does not support item assignment
print(name[0:5])
print(name[2:5])
print(name[4:6])
#last is including in first
print(name[:3])#is same as name[0:3]
print(name[0:])#is same as name[0:5]
c=name [-4:-1]#is same as name[1:4]
print(c)
name='SKRANJHA'
d=(name[1:4:1])
print(d)
g=(name[0:6:2])
print(g)
h=(name[0::2])
print(h) 
K=(name[0::3])
print(K)
p=(name[0::4])
print(p)

