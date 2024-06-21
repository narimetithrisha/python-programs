'''ip:[4,8,14,22,37,68]
#7 13 19 31 67
all the elements are non primes find largest prime number between 2 consecutive numbers find sum of all these numbers'''
'''l=[14,16,20,22]
def prime(j):
    for i in range(2, (j//2)+1):
        if j%i==0:
            return 0
    return j
new=[]
for i in range(len(l)-1):
    n=0
    for j in range(l[i],l[i+1]):
        n=max(prime(j),n)
    new.append(n)
print(new)
print(sum(new))'''

'''
ip:
    [4,9,8,2,14,3,5,6]
    take first three elements
    unsorted array

    4 8 9 2 14 3 5 6
       2 8 9 14 3 5 6
          8 9 14 3 5 6
            3 9 14 5 6
                 5 9 14 6
                     6 9 14

   op: 4 2 8 3 5 6 9 14           
    (4,8,9)  (2,14,22)............
'''
'''a= list(map(int,input().split()))
for i in range(len(a)-2):
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
    if(a[i+1]>a[i+2]):
        a[i+1],a[i+2]=a[i+2],a[i+1]
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i] 
print(a)'''
'''ip:
    "hello:5348,car:214,book:8799,apple:2187"
    op:
        oaxp'''
'''

ip:
    "hello:5438,car:214,book:8799,apple:2187"
op:

    oaxp
'''

l = dict(item.split(':') for item in input().split(','))
for key,value in l.items():
    length=len(key)
    f=0
    if str(length) in value:
        print(key[length-1],end="")
        f=1
        continue
    for i in range(length-1,0,-1):
        if str(i) in value:
            print(key[i-1],end="")
            f=1
            break
    if f==0:
        print("x",end="")
        continue



    
