def enqueue (x,y):
    global k
    if (int(y)>int(k)):
        l.append(x)
        k = y
    elif (int(y)<int(k)):
        l.insert(0,x)
        k = y

def display():
    for j in range (0,len(l)):
        print ('{}|{}'.format(l[j],j+1),end = " ")
        if (j<(len(l)-1)):
            print ("->",end = " ")

i = 0
l = []
k = 0
count = int(input())
while (i<count):
    a = input()
    if (a[0]=='1'):
        enqueue (a[2],a[4])
    elif (a[0]=='3'):
        display()
    i = i+1
