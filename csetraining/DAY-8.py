'''L=[1,2,3,4,1,2,3,1,2]
op:
[[1 2 3 4],[1 2 3],[1,2]]'''
'''L=[1,2,3,4,1,2,3,1,2]
res=[]
r=[]
for i in range(len(L)):
    if L[i] not in r:
        r.append(L[i])
    else:
        res.append(r)
        r=[]
        r.append(L[i])
if r:
    res.append(r)
print(res)'''
'''ip:[2,3,1,3,4,3,2]
op:
    [[2 3 1 4],[3 2],[3]]'''
'''L=[2,3,1,3,4,3,2]
s=[]
res=[]
while L:
    for i in L:
        if i not in s:
         s.append(i)
    for i in s:
        L.remove(i)
    res.append(s)
    s=[]
print(res)'''
'''ip:"the 4quick br$%own foENDx j45umps o.ver the lazy dog"
op:yes
-----------------
ip:
    "qwweer yuoip asdfvgh JkL mnbvlkjcxz"
op:
    no'''
'''t="the 4quick br$%own foENDx j45umps o.ver the lazy dog"
d={}
for i in t:
    if i=="":
        continue
    if i not in d and i.islower():
        d[i]=1
if len(d)==26:
    print("yes")
else:
    print("no")'''
    
'''a=input()
b="qwertyuiopasdfghjklzxcvbnm"
for i in b:
    if(i not in a):
        print("no")
        break
else:
    print("yes")'''
'''a=input()
d=[0]*26
for i in a:
    if(i.islower()):
        d[ord(i)-97]+=1
print(all(d))'''
'''ip:"abfgresagtyuiofde"
7,9,12
length of longest substring with out repeating characters'''

'''s = "abfgresagtyuiofde"
a = set()
left = 0
maxlen = 0
for right in range(len(s)):    
    while s[right] in a:
    
       a.remove(s[left])
       left += 1
    a.add(s[right])    
    maxlen = max(maxlen, right-left + 1)
print(maxlen)'''

'''
Give a binary matrix with 1's and 0's
1's ----> trees
0's-----> land
l[r][c] is the starting index of fire

fire moves in top, down,left, right only
i/p:
[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]

r=0
c=0

o/p:
the output is 8

'''
l=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
n=len(l)
count=0
i=4
j=5
def fun(l,i,j,n):
    if l[i][j]==0:
        return
    
    if l[i][j]==1:
        l[i][j]=0    
    
    if i>0:
        fun(l,i-1,j,n) #t
    if i<n-1:
        fun(l,i+1,j,n) #b
    if j>0:
        fun(l,i,j-1,n) #l
    if j<n-1:
        fun(l,i,j+1,n)#r

if l[i][j]==1:
    fun(l,i,j,n)
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count=count+1
print(count)
        