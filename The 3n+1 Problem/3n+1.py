i=int(input())
j=int(input())
def Cycle(i, j):
    max_length = 0
    if i>j:
        i,j=j,i
    for n in range(i, j+1):
        cycle = []
        while(True):
            cycle.append(n)
            if(n==1):
                break
            if(n%2==0):
                n = n/2
            else:
                n = 3*n+1
        if(len(cycle) > max_length):
            max_length = len(cycle)
    return max_length
cycle_length = Cycle(i, j)
print(i,j,cycle_length,end=" ")
