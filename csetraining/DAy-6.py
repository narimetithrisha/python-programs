#majority element which should be half the element
'''a=[6,6,6,6,7]
c=1
p=a[0]
for i in range(1,len(a)):
    if(a[i]==p):
        c=c+1
    else:
        if(c!=0):
           c=c-1
        if(c==0):
            p=a[i]
print(p)'''
'''ip:7
op:0536721
4'''
#leetcode:268
'''n=7
l=a=[0,5,3,6,7,2,1,9]
b=sum(l)
n=(n*(n+1))//2
print(n-b)'''
'''ip:12
factors of ip:1,2,3,4,6,12
op:print second largest factor i.e 6'''
'''def secondlargefactor(n):
    factors = []
    for i in range(1,n+1):
        if n%i==0:
            factors.append(i)
    return factors[-2]
n = 12
second_largest = secondlargefactor(n)
print(second_largest)'''
# check whether its coprime or not
'''def gcd(a, b):
    while b:
        a,b=b,a % b
    return a
def coprime(a, b):
    return gcd(a,b)== 1
a = 2
b = 3
if coprime(a, b):
    print("co-prime numbers")
else:
    print("not co-prime numbers")'''
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(data):
    return TreeNode(data)

# Creating the tree
root = insert(10)
root.left = insert(20)
root.right = insert(30)
root.left.left = insert(40)

# Printing the tree
print("\nThe tree is created")
print("\nThe tree values are:")
print("\nThe root:", root.data)
print("root.left =", root.left.data)
print("root.right =", root.right.data)
print("root.left.left =", root.left.left.data)

