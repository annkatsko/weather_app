#a = [4, 1, 3, 11, 22]
#s=0
#for i in a:
    #if a[i] %2 == 0:
       # s=s+1
#print(s)

a = [1,1,2,3,2,4,5,3,3,4,7,7]
z = 1
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i]==a[j]:
            z=z+1
            print(str(i)+'-'+str(z))
        else:
            print(str(i))
