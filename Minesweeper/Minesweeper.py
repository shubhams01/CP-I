r = int(input())
c = int(input())

a = list()

for i in range(0,r):
    a.append(list(input()))
    
for i in range(0,r): 
    for j in range(0,c): 
        count=0
        if(a[i][j]=='*'):
            continue
        else:
            for n in range(i-1,i+2):
                for m in range(j-1,j+2):
                    if(n<0 or m<0 or n>=r or m>=c):
                        continue
                    else:
                        if(a[n][m]=='*'):
                            count+=1
        a[i][j]=str(count)
print()
        
print("Field")
for i in range(0,r):
    for j in range(0,c):
        print(a[i][j],end="")
    print()
