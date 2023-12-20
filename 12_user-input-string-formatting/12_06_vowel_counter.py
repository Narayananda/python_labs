# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

str_ = input("white somtihng here: ")

a,e,i,o,u = 0,0,0,0,0

for y in range(len(str_)):
    if str_[y]=="a":
        a+=1
    elif str_[y]=="e":
        e+=1
    elif str_[y]=="i":
        i+=1
    elif str_[y]=="o":
        o+=1
    elif str_[y]=="u":
        u+=1
    else:
        None

print("a =",a,"\ne =",e,"\ni =",i,"\no =",o,"\nu =",u)
