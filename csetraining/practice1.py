'''name=['thrisha','sanay']
for i in name:
    print(i)'''
'''age=17
price=19.9
print(age)
print(price)'''
'''name=input("whats is your name")
print(name)'''

#add
'''a=30
b=40
c=a+b
print(c)
'''
#square root of given numbers
'''num=int(input("enter a number:"))
squareroots=num**(1/2)
print("the square root of given number is",squareroots)
'''
'''import math
num=int(input("enter a number:"))
squreroot=math.sqrt(num)
print("",squreroot)'''
#Area of triangle
'''height=float(input("enter height:"))
base=float(input("enter base:"))
area=(0.5)*base*height
print("tthe area is:",area)'''
#even or odd
'''num=int(input("enter a number:"))
if num % 2 ==0:
    print("even")
else:
   print("odd")'''
'''def reverse_number(n, reversed_number=0):
    if n == 0:  # Base case
        return reversed_number
    else:
        last_digit = n % 10
        reversed_number = reversed_number * 10 + last_digit
        return reverse_number(n // 10, reversed_number)  # Recursive case

# Example usage:
reversed_num = reverse_number(123)  # Should return 321
print(f"Reversed number: {reversed_num}")'''


'''def sum_of_digits_and_reverse(n, reversed_number=0):
    if n == 0:  # Base case
        print(f"Reversed number: {reversed_number}")
        return 0
    else:
        last_digit = n % 10
        reversed_number = reversed_number * 10 + last_digit
        return last_digit + sum_of_digits_and_reverse(n // 10, reversed_number)  # Recursive case

# Example usage:
result = sum_of_digits_and_reverse(123)  # Output: Reversed number: 321
print(f"Sum of digits: {result}") ''' # Output: Sum of digits: 6
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value,end='')
        in_order_traversal(root.right)
root=TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("inorder:",end='')
in_order_traversal(root)
print()
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=' ')


print("Post-order Traversal: ", end='')
post_order_traversal(root)
print()  
