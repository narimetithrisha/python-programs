'''def backtrack(r,col,posdig,negdig,res,board):
    if r>=n-1:
        l=["".join(i) for i in board]
        res.append(l)
        return res
    for c in range(n):
        if c in col or (r+c) in posdig or (r-c) in negdig:
            continue
        board[r][c]="Q"
        col.append(c)
        posdig.append(r+c)
        negdig.append(r-c)

        backtrack(r+1,col,posdig,negdig,res,board)

        board[r][c]="_ "
                
        col.remove(c)
        posdig.remove(r+c)
        negdig.remove(r-c)
res=[]
col=[]
row=[]
posdig=[]
negdig=[]
n=int(input("Enter the no of queens:"))
board=[["_  "]*n for i in range(n)]
board[0][5]="R"
col=[5]
row=[0]
posdig=[0+5]
negdig=[0-5]
backtrack(1,col,posdig,negdig,res,board)
for i in res:
    for j in i:
        print(j)
    print()
    print()'''
    

    
'''def backtrack(r,col,posdig,negdig,res,board,flag,x,m):
    m=max(len(x),m)
    if r>n-1:
        l=["".join(i) for i in board]
        res.append(l)
        flag+=1
        return res,flag,m
    if r in row:
        res,flag,m=backtrack(r+1,col,posdig,negdig,res,board,flag,x,m)
    for c in range(n):
        if c in col or (r+c) in posdig or (r-c) in negdig:
            continue
        board[r][c]="  Q  "
        x.append(1)
        col.append(c)
        posdig.append(r+c)
        negdig.append(r-c)

        res,flag,m=backtrack(r+1,col,posdig,negdig,res,board,flag,x,m)
        x.pop()
        board[r][c]="  _  "
                
        col.remove(c)
        posdig.remove(r+c)
        negdig.remove(r-c)
    return res,flag,m
x=[]
col=[]
row=[]
posdig=[]
negdig=[]
n=6
a=int(input("enter row coordinates of rook"))
b=int(input("enter col coordinates of rook"))
board=[["_"]*n for i in range(n)]
board[a][b]="  R  "
col=[b]
row=[a]
res,flag,x=backtrack(0,col,posdig,negdig,[],board,0,x,0)
print("maximum number of queens :", x)'''
'''if flag==0:
    print("no solution")
else:
    for i in res:
        for j in i:
            print(j)
            print()
        print()
'''
'''
ip:[3,5,9,6,8,10]
sun at 6am will be at left side and count the number of buildings the sunraise will fall
sun at 6pm will be at right side and count the number of buildings the sunraise will fall

'''
'''l=[3,5,9,6,8,10]
left=0
lc,rc=1,1
right=len(l)-1
lm=l[left]
rm=l[right]
while left<=len(l) and right>=0:
    if lm<l[left]:
       lm=l[left]
       lc+=1
    if rm<l[right]:
       rm=l[right]
       rc+=1
    left+=1
    right-=1
print(rc,lc)'''

'''ip:
    tu5g2k1h8
    g5g8gd6h3
op:
    865312
    exact the largest even number from the given ip'''
'''ip:
    122
    op:
        131
        if its not palindrome then print next largest palindrome
----------------
ip:
    1234
    op:
        1331
----------------
      ip:
          24
          op:33
---------------------   '''
'''def palin(num):
    return str(num) == str(num)[::-1]

def nextpalin(num):
    num += 1  
    while not palin(num):
        num += 1
    return num


n = int(input("enter number:"))
output = nextpalin(n)
print(output)  '''

'''ip:abdbsdabca
print the longest palindromic substring
op:bdb
else print -1
'''