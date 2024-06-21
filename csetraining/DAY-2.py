#Add all the digits of the number and check the sum value if prime print the n value if not increment and check   
'''def check(n):
    x=sum(n)
    while x>10:
        x=sum(x)
    if x in [2,3,5,7]:
        print(n)
    else:
        n=n+1
        check(n)    
def sum(n):
    rem=0
    s=0
    while n:
        rem=n%10
        s=s+rem
        n=n//10
    return s
n=int(input())
check(n)
'''
'''def fun(x):
   if (x==6):
       return
   print(x)
   fun(x+1)
   print(x)
fun(1)
print('hi')'''
'''a=[3,8,5,4,3]
b=[5,0,9,3,2]
op:(12,17)'''
'''def fun1(x,a,b,os,es):
    if x==len(a):
        return(es,os)
    if a[x]%2==0:
        es=es+a[x]
    if b[x]%2!==0:
        os=os+b[x]
    return fun1(x+1,b,es,os)
a=[3,8,5,4,3]
b=[5,0,9,3,2]
es=0
os=0
print(fun1(0,a,b,es,os))'''
#print 1 to 10 even numbers
'''def even(x):
    if x > 10:
        return
    if x % 2 == 0:
        print(x)
    even(x + 1)
even(2)'''
#print yes if len is even no if len is odd

#
'''nums=[4,7,5,2,3]
s=sum(nums)
x=0
j=0
for i in nums:
    nums[j]=abs((x)-(s-i-x))
    x=x+i
    j=j+1
print(nums)'''
#
'''s=input()
cm=0
cf=0
for i in s:
    if i=='m':
        cm=cm+1
    else:
        cf=cf+1
if cm==cf:
    print("its nothing")
if cm>cf:
    print("its male")
if cm<cf:
    print("its female")'''
'''s="leet**cod*e"
t=[]
for i in s:
    if i=='*':
        t.pop()
    else:
        t.append(i)

print(''.join(t))'''
#
'''ip="is2 sentence4 This1 a3"
op="This is a sentence"'''
s="is2 sentence4 This1 a3"
s=input().split()
re=[0]*len(a)
for i in a:
    re[int(i[-1])-1]=i[:-1]
    




        




     
    


