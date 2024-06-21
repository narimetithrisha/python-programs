'''[(1,3)(2,5)(4,6)(6,7)(5,8)(7,9)] from 1'o clock to 3 'o clock 5rupees as salary  like that do rest of them
[5,6,5,4,11,2]
op:add maximum times 6+11=17'''

'''j=[(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
pr=[5, 6, 5, 4, 11, 2]
cp=pr.copy()
for i in range(1,len(job)):
    for j in range(0,i):
        if j[1]<=i[0]:
            if(b[j]+a[i]>b[i]):
                b[i]=b[j]+a[i]
print(pr)'''
'''print the subsequence for given input
ip=abcd
a ab ac ad abc abd acd abcd
b bc bd bcd
c cd
d'''
'''s1="abcd"
s2="axbd"
m=[]
for i in range(len(s1)+1):
    l=[0]*(len(s1)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if(s1[i-1]==s2[j-1]):
           m[i][j]=m[i-1][j]+1
        else:
           m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])'''


'''s1="abcd"
s2="axbd"
m=[]
for i in range(len(s1)+1):
    l=[0]*(len(s1)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1], m[i-1][j])
print("The Longest Common Subsequence is: ", m[len(s1)][len(s2)])

a=len(s1)
b=len(s2)
s=""
while a!=0 and b!=0:
    if s1[a-1]==s2[b-1]:
        s=s+s1[a-1]
        a=a-1
        b=b-1
    else:
        if m[a][b]==m[a][b-1]:
            b=b-1
        elif m[a][b]==m[a-1][b]:
            a=a-1
print("The Longest Subsequence string is : ", s[::-1])'''

'''l=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
n=len(l)
count=0
c=0
def fun(l,i,j,n,c):
    if l[i][j]==0:
        return c
    
    if l[i][j]==1:
        l[i][j]=0
        c=c+1
    
    if i>0:
        c=fun(l,i-1,j,n,c) 
    if i<n-1:
        c=fun(l,i+1,j,n,c)   
    if j>0:
        c=fun(l,i,j-1,n,c) 
    if j<n-1:
        c=fun(l,i,j+1,n,c)
    return c
res=[]

for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count=count+1
            res.append(fun(l,i,j,n,0))
print(max(res))
print(count)'''
'''ip:7662 sec
op:2hr 1min 2sec'''

def time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600)//60
    seconds = seconds % 60
    print(hours,"hours:",minutes,"minutes:",seconds,"seconds:")
   
input = 7662
time(input)
