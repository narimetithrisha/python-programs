#DFS
'''
def fun(dic,key,last):
    l.append(key)
    if(key==last):
       print(l)
       l.pop()
       return
    for i in dic[key]:
        if i not in l:
            fun(dic,i,last)
    l.pop()
def cost1(dic,key,last,cost,s):
    l.append(key)
    s+=cost
    if(key==last):
       print(l," ",s)
       l.pop()
       return
    for i in dic[key]:
        if i[0] not in l:
            cost1(dic,i[0],last,i[1],s)
    l.pop() 
dic={5:[(7,1),(3,2)],7:[(5,1),(4,2),(3,4)],4:[(7,1),(8,3),(2,4)],8:[(3,2),(4,1),(2,4)],3:[(5,1),(7,2),(8,5)],2:[(4,7),(8,6)]}
l=[]
cost1(dic,5,2,0,0)
print()

'''
def dfs(key,l):
    print(key,end=" ")
    l.append(key)
    for i in d[key]:
        if i not in l:
            dfs(i,l)
def allPaths(key,end,l):
    l.append(key)
    if key==end:
        print(l)
        l.pop()
        return 
    for i in d[key]:
        if i not in l:
            allPaths(i,end,l)
    l.pop()
def weightgraph(d,key,end,s,cost,l):
    l.append(key)
    s+=cost
    if key==end:
        print(l," ",s)
        l.pop()
        return 
    for i in d[key]:
        if i[0] not in l:
            weightgraph(d,i[0],end,s,i[1],l)
    l.pop()
def leastCost(d,key,end,s,cost,l,m):
    l.append(key)
    s+=cost
    if key==end:
        if s<m:
            m=s
        l.pop()
        return m 
    for i in d[key]:
        if i[0] not in l:
            m=leastCost(d,i[0],end,s,i[1],l,m)
    l.pop()
    return m
res={}
def lowCostpath(d,key,end,s,cost,l,m,l1):
    l.append(key)
    s+=cost
    if key==end:
        if s<m:
            m=s
            l1=l.copy()
        l.pop()
        return m,l1 
    for i in d[key]:
        if i[0] not in l:
            m,l1=lowCostpath(d,i[0],end,s,i[1],l,m,l1)
    l.pop()
    return m,l1
 #unweighted graph       

d={
        5:[7,3],
        7:[5,4,3],
        4:[7,8,2],
        8:[3,4,2],
        3:[5,7,8],
        2:[4,8]
    }
'''
#weighted graph
d={
        5:[(7,1),(3,3)],
        7:[(5,1),(4,3),(3,2)],
        4:[(7,3),(8,2),(2,1)],
        8:[(3,5),(4,2),(2,4)],
        3:[(5,3),(7,2),(8,5)],
        2:[(4,1),(8,4)]
    }'''
l=[]
#dfs(5,l)
for i in d:
    allPaths(5,i,l)
#allPaths(5,2,l)
key=5
end=2
s=0
cost=0
#weightgraph(d,key,end,s,cost,l)
#lowCost(d,key,end,s,cost,l)
#print(leastCost(d,key,end,s,cost,l,99999999999))
#print(lowCostpath(d,key,end,s,cost,l,99999999999,[]))
#print(res)
'''for i in sorted(res):
    print(i,"------>",res[i])
    
    break
'''