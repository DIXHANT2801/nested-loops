i = input("enter your own word")
c = input("choose your own character")
e = 0
t = 0
while(e<len(i)):
    if(i[e]==c):
        t=t+1

    e=e+1

print("the total number of your word is",t)