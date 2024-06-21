''' 1.)ip:    2 5 7 9
    1 3 6 7 10 13
op:
1 2 3 5 6 7 7 9 10 13'''
'''l1=[2,5,7,9]
l2=[1,3,6,7,10,13]
res=l1+l2
res.sort()
print(res)'''

'''l1=[2,5,7,9]
l2=[1,3,6,7,10,13] 
res=[]
i=0
j=0
while(i<len(a) and j<len(b)):

 if(l1[i]<l2[j]):
    res.append(l1[i])
    i=i+1
 else:
     res.append(l2[j])
     j=j+1
if(j<len(l2)):
    res.extend(l2[j:])
if(i<len(l1)):
    res.extend(l1[i:])'''

''' no of alphabets in string
ip:
aaabbaaaaddd
  op:
a3b2a4d3 '''

#program'''
s = "aaabbaaaaddd"
'''result = []
i = 0
while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i + 1]:
        i += 1
        count += 1
    result.append(s[i] + str(count))
    i += 1
print("".join(result))  '''

'''3.)ip:
    3 5 4 3 6 7 1 2 4 3 3 7 6
    op:
    3-4,5-1,4-3,6-2,7-2,1-1,2-1,8-2'''
'''
ip:
    3 5 4 3 6 7 1 2 4 3 3 7 6 8 8
op:
    3 - 4
    5 - 1
    4 - 2
    6 - 2
    7 - 2
    1 - 1
    2 - 1
    8 - 2

a=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
b=[]
for i in a:
    if(i not in b):
        b.append(i)
for i in b:
    print(i ,'-',a.count(i))'''

'''4.)ip:
       f46feLk9y56u#@&56hIjbn6kJhA
   
a="f46feLk9y56u#@&56hIjbn6kJhA"
lv=0
uv=0
lc=0
uc=0
d=0
s=0
for i in a:
    
    if(i.islower()):
        if(i in 'aeiou'):
            
           lv=lv+1
        else:
           lc=lc+1
    elif i.isupper():
        if(i in 'AEIOU'):
        
           uv=uv+1
        else:
           uc=uc+1
    elif i.isdigit():
        d=d+1
    
    elif(not i.isalnum()):
        s=s+1
print("lv -",lv)
print("uv -",uv)
print("lc -",lc)
print("uc -",uc)
print("d -",d)
print("s -",s)'''

'''
5.)ip:
  placements
op:
  plAcEmEnts'''
'''
s="placements"
res=""
for i in s:
   if i in 'aeiouAEIOU':
       res=res+i.upper()
   else:
      res=res+i.lower()
print(res)'''

'''6.)ip:" 5 38 7 5.6 4 2 3"
      op:
      15 6 9.4
'''
'''
ip:
    5,3.8,7,5.6,4,2,3
op:

    decimal_sum:9.4
    evenSum:6
    oddSum:15
'''
'''
ip:
    5,3.8,7,5.6,4,2,3
op:

    decimal_sum:9.4
    evenSum:6
    oddSum:15
'''
'''
l=[]
num=[]
decimal=[]
es=0
s=0
for i in range(7):
    l.append(input())
print(l)
for i in l:
    if '.' in i:
        decimal.append(float(i))
    else:
        num.append(int(i))
        s=sum(num)
        for i in num:
            if i%2==0:
                es=es+i
            
            
print(sum(decimal))
print("even sum",es)
print("odd sum",s-es)'''

'''
count of numbers divisible by 7
ip:
300
400
op:
'''
'''count=0
for i in range(300,400):
   if i%7==0:
       print(i)
       count=count+1
print("div by 7:",count)'''
'''prime means print prime number
else if
ip: 14
op: 17
If the number is prime then print prime number else print next nearest prime"""
'''
"""
def prime(n):
    for i in range(2, (n//2)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if prime(n) is True:
    print(n)
else:
    while 1:
        if prime(n+1):
            print(n+1)
            break
        else:
            n=n+1"""
'''
n=int(input())
while 1:
    c=0
    for i in range(2,n//2+1):
        if(n%i==0):
            c=c+1
            break
    if c==0:
        print(n)
        break
    else:
        n=n+1'''
'''ip:7856(no ofprime digits)
op:2'''

'''n=467765
count=0
while(n):
    if(n%10 in [2,3,5,7]):
        count=count+1
    n=n//10
print(count)'''

'''
ip: asd123!@#
op:1

ip:A1234B
op:2

ip:a123456
op:2

ip:123456789
oP:3

ip:A1234a@4
op:-1

ip:abcdef127
op:2
'''
'''
inp:
    asd8728#*^A
op:
    if valid then -1

------------------------
ip:
123456789

op:
    3
-----------------------------
ip:
    ab

op:
    6
----------------------'''

'''s=input("enter a password")
caps=[]
smalls=[]
nums=[]
special=[]
char=-1

for i in s:
    if i.isupper():
        caps.append(i)
    elif i.islower():
        smalls.append(i)
    elif i.isdigit():
        nums.append(i)
    else:
        special.append(i)

if len(s)==8 and len(caps)!=0 and len(smalls)!=0 and len(nums)!=0 and len(special)!=0:
    print(char)
elif len(s)>8:
    char+=1
    if len(caps)==0:
        char+=1
    if len(smalls)==0:
        char+=1    
    if len(nums)==0:
        char+=1
    if len(special)==0:
        char+=1
elif len(s)<8:
    char+=1
    if len(caps)==0:
        char+=1
    if len(smalls)==0:
        char+=1    
    if len(nums)==0:
        char+=1
    if len(special)==0:
        char+=1
    if char+len(s)<8:
        char=char+(8-len(s)-char)
    
print(char)    
print(caps, smalls,nums,special)'''

        

        