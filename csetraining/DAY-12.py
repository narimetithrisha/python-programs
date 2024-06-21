#BFS:
'''def bfs():
    while q:
        for key,values in d.items():
            for i in d[key]:
               if i not in vislis and i not in q:
                 q.append(i)
            x=q.pop(0)
            vislis.append(x)
            
    print(vislis)
q=[5]
vislis=[]
d={
        5:[7,3],
        7:[5,4,3],
        4:[7,8,2],
        8:[3,4,2],
        3:[5,7,8],
        2:[4,8]
    }
key=5
print(bfs())'''

#Dijikistras algorithm:
'''def dijkstras():
    while queue:
        for i in dic[queue[0]]:
            if i[0] not in visited:
                queue.append(i[0])
                c=cost[queue[0]]+i[1]
                if cost[i[0]]>c:
                    cost[i[0]]=c
        x=queue.pop(0)
        visited.append(x)
    print(cost)                

visited=[]
queue=[2]
dic={
          5:[(8,2),(3,2),(2,2)],
          2:[(5,2),(3,1)],
          8:[(5,2),(3,3),(6,4)],
          3:[(5,2),(2,1),(8,3),(7,3)],
          7:[(3,3),(9,1)],
          6:[(8,4),(9,2)],
          9:[(6,2),(7,1),(4,2)],
          4:[(9,2)]
         }
cost=     {
           5:999999,
           2:999999,
           8:999999,
           3:999999,
           7:999999,
           6:999999,
           9:999999,
           4:999999,
           }
cost[5]=0
dijkstras()'''
'''
given 2 lists
2 list have even and odd numbers

[6,3,2,9,4,7]
[8,9,5,3,6,9]

size of both list are same

generate another list such that an even form 1st list is mappend to all odd numbsers in 2nd list

op:
[6+9,6+5,6+3,6+9,  .. . . . . ..  . .. . . .]=[13,11,9,15 .. .... . . . .. ]
[13,11,9,15,9,7,5,11,11,9,7,13]
'''

def fun(i,j,res,length):
    if i==length:
        return res
    if j==length :
        return fun(i+1,0,res,length)
        
    
    if l1[i]%2==0 and l2[j]%2!=0:
        res.append(l1[i]+l2[j])
    return fun(i,j+1,res,length)
    return res
def fun1(i,j,res,length,s):
    if i==length:
        return res
    if j==length :
        if s:
            res.append(sum(s))
            s=[]
        return fun1(i+1,0,res,length,[])
    if l1[i]%2==0 and l2[j]%2!=0:
        s.append(l1[i]+l2[j])
    return fun1(i,j+1,res,length,s)
    return res
l1=[6,3,2,9,4,7]
l2=[8,9,5,3,6,9]
le1,le2=len(l1),len(l2)
i,j=0,0
res=[]
while le1:
    le2=len(l2)
    j=0
    while le2:
        if l1[i]%2==0 and l2[j]%2!=0:
            res.append(l1[i]+l2[j])
        j+=1
        le2-=1
    i+=1
    le1-=1
print(fun(0,0,[],le1))
print(fun1(0,0,[],le1,[]))