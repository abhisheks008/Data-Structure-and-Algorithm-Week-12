l = []
i = int(input()) #enter the query
for a in range (0,i):
    a = input()
    if (a[0]=='1'):
        l.append(a[-1])
    elif (a[0]=='3'):
        for b in range (0,i-1):
            print (l[b], end = " ")
print ()
print (len(l))
