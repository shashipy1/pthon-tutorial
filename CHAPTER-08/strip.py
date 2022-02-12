#strip - it means remove the space  
this = "           HELLO S.K. RANJHA      "
print(this)
print(this.strip())

# WAP function to remove a given word from a 
# list and strip at same time.
def remove_and_split(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()
this = "           HELLO S.K. RANJHA      "
n = remove_and_split(this,"HELLO")
print(n)
