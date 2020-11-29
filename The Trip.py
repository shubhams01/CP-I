while(True):
    n = int(input())#("Enter Number of Students:"))
    #print("Enter Amount they Spend:")
    Total,pd,nd,avg = 0,0,0,0
    M = [10,20,30]
    for i in range(0,n):
        m = float(input())
        M.append(m)
        Total = sum(M)
        avg = Total/n
#print("Total:",Total)
#print("avg:",avg)

    for i in range(0,n):
        E = M[i]-avg #-10,0,10
        if(E > 0):
            pd += E #10
        else:
            nd += E #-10
    nd = -(nd)#10
    if(nd > pd):
        print("${:.2f}".format(nd))
    else:
        print("${:.2f}".format(pd))
    print()

