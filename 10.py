count=0
for x1 in range(1,10):
    for x2 in range(0,10):
        for x3 in range(0,10):
            for x4 in range(0,10):
                for x5 in range(0,10):
                    for x6 in range(0,10):
                        if x1!=x2 and x1!=x3 and x1!=x4 and x1!=x5 and x1!=x6 and x2!=3 and x2!=x4 and x2!=x5 and x2!=x6 and x3!=x4 and x3!=x5 and x3!=x6 and x4!=x5 and x4!=x6 and x5!=x6:
                            if x6==5:
                                if (x1%2==0 and x2%2!=0 and x3%2==0 and x4%2!=0 and x5%2==0 and x6%2!=0) or (x1%2!=0 and x2%2==0 and x3%2!=0 and x4%2==0 and x5%2!=0 and x6%2==0):
                                    count+=1
                                    print(x1,x2,x3,x4,x5,x6)
print(count)
    
