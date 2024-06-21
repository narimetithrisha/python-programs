def com(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr + [l[i]] , i+1)
    fun([],0)
a=[3,2,5,4,1,6,8]
k=3
com(a,k)

'''
ip:
    school
    3
    l=2 hoosc
    r=3 oolsch
    l=1 chools
op:
    yes
hoc
sch,cho,hoo,ool'''
'''a=input()
n=int(input())
str=[]
for i in range(n):
    b=input()
    if(b[0]=='L'):
        str.append(a[int(b[2])])
    else:
        str.append([-int(b[2])])

#str=lis(str)
str.sort()
b=[]
for i in range(len(a)-n+1):
    t=sorted(a[i:n+i])
    
    b.append(t)
print(b)
print(str)
for i in b:
    if(i==str):
        print("yes")
        break
else:
    print("No")'''
        


'''IP:
    12
    print yes if we can show as sum of two primes
    1--->prime'''
'''def prime(n):
    for i in range(2, (n//2)+1):
        if n%i==0:
            return False
    return True
def sumofprime(nums):
    for i in range(2,nums):
        if prime(i) and prime(nums-i):
            return True
    return False
    if prime(i)+print(nums-i)==nums:
        return "yes"
num=int(input("enter number"))
print(sumofprime(num))'''

'''a=int(input())
for i in range(a):
  list=input()#"qwryupcsfoghjkldezxvbintma"
  str=input()#ativedoc
  for i in list:
     if j in str:
        if j==i:
           print(j,end="")'''
'''
ip:
    [3,9,4,1,5,7]    Gold in each house
     0 1 2 3 4 5

    if theif stole gold in one house he cant steal in next consecutive house

    find the maxinum amount theif can steal'''

def findmax(l):
    if len(l)==0:
        return 0
    if len(l)==1:
        return l[0]
    if len(l)==2:
        return max(l)
    left=l[0]+findmax( l[2:])
    right=l[1]+findmax(l[3:])
    return max(left,right)
l=[13,9,4,10,5,7]
print(findmax(l))