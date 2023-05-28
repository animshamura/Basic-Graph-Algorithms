#Solve of Target Sum 

#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
 
def Postorder(root):
    if(root!=None): 
        return Postorder(root.left)+Postorder(root.right)+root.data
    else: return 0;  
    
    
#Node Creating 
n1 =  Node(1000)
n2 =  Node(800)
n3 =  Node(700)
n4 =  Node(600)
n5 =  Node(400)
n6 =  Node(270)
n7 =  Node(100)
n8 =  Node(300)
n9 =  Node(210)
n10 = Node(170)


#Linking nodes 
n1.left=n2
n1.right=n3
n2.left=n4
n4.left=n8
n3.left=n5
n3.right=n6
n6.left=n9
n9.right=n10

pos = ["CEO","Manager","Finance","Accounts","Sales"]
cost = [1000,2500,3770,4280,4450]
inp = input()
print((Postorder(n1)-cost[pos.index(inp)])*1000)
