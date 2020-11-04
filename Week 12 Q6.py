l1= []
l2 = []

for a in range (0,11):
    a = input()
    if (a[0]=='1'):
        l1.append(a[-1])
    elif (a[0]=='2'):
        l2.append(a[-1])
    elif (a[0] == '6'):
        for b in range (0,len(l1)):
            print (l1[b], end = "")
        print()
    elif (a[0] == '7'):
        for b in range (0,len(l2)):
            print (l2[b], end = "")
        print()

for j in range (0, len(l1)):
    if (l1[j]!=l2[j]):
        print ("Not Identical")
        print ("Mismatch at {}th element".format(j+1))
    
