class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
def Inorder(root):
    if(root!=None): 
        Inorder(root.left)
        print(root.data)
        Inorder(root.right)
def Preorder(root):
    if(root!=None): 
         print(root.data)
         Preorder(root.left)
         Preorder(root.right)
def Postorder(root):
    if(root!=None): 
        Postorder(root.left)
        Postorder(root.right)
        print(root.data)
        
    

#Node Creating 
n1 =  Node(77)
n2 =  Node(90)
n3 =  Node(102)
n4 =  Node(56)
n5 =  Node(12)
n6 =  Node(107)
n7 =  Node(100)
n8 =  Node(17)
n9 =  Node(98)
n10 =  Node(92)
n11 =  Node(109)
n12 =  Node(87)

#Linking 
n1.left=n2
n1.right=n7
n2.left=n3
n2.right=n6
n3.left=n4
n6.left=n5
n7.left=n8
n8.right=n9
n8.left=n12
n9.left=n10
n10.left = n11

print("Inorder :")
Inorder(n1)
print("Preorder :")
Preorder(n1)
print("Postorder :")
Postorder(n1)
