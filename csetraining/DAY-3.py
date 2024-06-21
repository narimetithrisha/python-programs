'''ip:   
      khoor
      3
op:
    hello
---------
ip:
    bcdmnwc
    9
    
op:student
-------------
ip:
 bvec
4
op:
Xray
'''
'''str=input()
key=3
decrypt=[]
for s in str:
    decrypt.append(chr((ord(s)-key-97)%26+97))
n="".join(decrypt)
print(n)'''

'''a='bvec'
b=30
c=b%26
d=''
for i in a:
    if((ord(i)-c)>=97:
       d=d+char(ord(i)-c)
    else:
       d=d+char(ord(i)-c)+26)
print(d)'''
#len of longest substring
'''def longsubstring(s):
    maxlen = 0
    curlen = 1 

    #for i in range(1,len(s)):
    for i in range(len(s)-1):
        if ord(s[i]) == ord(s[i+1])-1:
            curlen += 1
        else:
            if curlen > maxlen:
                maxlen = curlen
                
            curlen = 1

    if curlen > maxlen:
        maxlen= curlen

    return maxlen
s = "abcde"
print("longest sub string len is:", longsubstring(s))
'''
'''
ip:
    3
    
     x y z
     p q r
     a b c

    "xpaypb"
op:
    yes
'''

'''def m(matrix,s):
    for i in range(len(s)):
        if s[i] not in matrix[i%n]:
            return 'no'
        matrix[i]=s[i].replace(s[i],'.')
        
    return 'yes'
n=int(input("enter a number"))
matrix = []
s=input("enter string")
s1=list(s)
for i in range(n): 
    l =[] 
    for j in range(n):
         l.append(input())
    matrix.append(l)
print("the matrix is:",matrix)
print(m(matrix,s))'''


'''n=int(input())
m=[]
for i in range(n):
    m.append(input())
s=input()
for i in range(len(s)):
    if(s[i] not in m[i%n]):
        print("no")
        break
else:
    print("yes")'''
#print reverse 12321 using recursion

'''def reverse(n):
    if n < 10:
        return n
    else:
        last = n % 10
        remaining = n // 10
        return int(str(last) + str(reverse(remaining)))
number = 12321
print(reverse(number))'''
'''def fun(x,re):
    if(x==0):
        return re
    re=re*10+(x%10)
    return fun(x//10,re)
n=int(input("enter the number"))

if(n==fun(n,0)):
   print("pal")
else:
    print("not pal")'''
'''ip:
    15 3 2 7 8 4
    m t  w t f s
op:
 6
------------
ip:
    5 3 2 7 8 4
op:
    6
-----------'''
'''l=[15,3,2,7,8,4]
max=0
profit=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]<l[j]:
         profit=l[j]-l[i]
         
        if max<profit:
         max=profit
print(max)'''

'''
ip:5
op:
    * * * * *
    * 1 2 3 *
    * 4 5 6 *
    * 7 8 9 *
    * * * * *
'''
'''n=5
x=1
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(x,end="")
            x=x+1
    print()
'''
'''
ip=4
op=
  ----a----
  ---aba---
  --abcba--
  -abcdcba-
  '''
def pattern(n):
     for i in range(n):
    
        dashcount = n - i - 1
        dashes = '-' * dashcount
       
        increase = ''.join(chr(97 + j)
        for j in range(i + 1))
        decrease = ''.join(chr(97 + j)
        for j in range(i - 1, -1, -1))
       
        pattern = dashes + increase + decrease + dashes
        
        print(pattern)
n=4
pattern(n)


    
    

    
