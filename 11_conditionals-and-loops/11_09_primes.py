# Print out every prime number between 1 and 1000.
for i in range(3,1000+1):
    for y in range(2,i):
        if i%y==0:
            break
    else: #no break
        print(i)