'''ht=[2,7,2,3,6,7,1,0,5,7]
l=0
r=len(ht)-1
lm,rm=ht[l],ht[r]
w=0
while l<r:
    if lm<rm:
       l+=1
       if lm<ht[l]:
          lm=ht[l]
       w=w+abs(lm-ht[l])
       
    else:
      r-=1
      if rm<ht[r]:
        rm=ht[r]
      w=w+abs(rm-ht[r])
    
print(w)'''

'''#coin exchange
#ip=[1,3,4,5]
#op=17
coins=[1,3,4,5]
val=17
m=[]
for i in range(len(coins)):
    l=[0]*(val+1)
    m.append(l)
for i in range(len(coins)):
    for j in range(val+1):
       if coins[i]==j:
           m[i][j]=1
       if j>coins[i]:
           x=j-coins[i]
           m[i][j]=m[i][x]+1 
       if coins[i]>j:
           m[i][j]=m[i-1][j]
           
#for i in range(len(m)):
    print(m[i])
    '''
#possible paths:
'''def fun(i,j,m,cnt,vi,a,b):
    if i==a and j==b:
        return cnt
    if (i,j) in vi:
        return cnt
    else:
        vi.append((i,j))
    if i==r-1 and j==c-1:
        cnt+=1
        print(vi)
        vi.pop()
        return cnt
    if i<r-1:
        cnt=fun(i+1,j,m,cnt,vi,a,b)
    if i> 0:
        cnt=fun(i-1,j,m,cnt,vi,a,b)
    if j<c-1:
        cnt=fun(i,j+1,m,cnt,vi,a,b)
    if j>0:
        cnt=fun(i,j-1,m,cnt,vi,a,b)
    vi.pop()
    return cnt
r=int(input())
c=int(input())
#obstrucle coordinates:
a=int(input())
b=int(input())
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        l.append("-")
    m.append(l)
print(m)
print(fun(0,0,m,0,[],a,b))'''
def solveNQueens():
        res=[]
        col=[]
        posdig=[]
        negdig=[]
        res=[]
        board=[["."]*n for i in range(n)]
        def backtrack(r):
            if r>=n:
                 l=["".join(i) for i in board]
                 res.append(l)
                return
            for c in range(n):
                if c in col or (r+c) in posdig or (r-c) in negdig:
                    continue
                board[r][c]="Q"
                col.append(c)
                posdig.append(r+c)
                negdig.append(r-c)

                backtrack(r+1)

                board[r][c]="."
                
                col.remove(c)
                posdig.remove(r+c)
                negdig.remove(r-c)
        backtrack(0)
        return res