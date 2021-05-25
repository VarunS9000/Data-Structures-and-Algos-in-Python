#Binary Search Tree in Python

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def insert(root,value):
        if root is None:
            return Node(value)
        else:
            if value<=root.value:
                root.left=insert(root.left,value)

            elif value>root.value:
                root.right=insert(root.right,value)

        return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

def search(root,x):
    if root:
        if root.value==x:
            print("found")

        elif x<root.value:
            search(root.left,x)

        elif x>root.value:
            search(root.right,x)

    else:
        print("element does not exist")


def maxDepth(root):
    if(root is None):
        return
    else:
        ld=maxDepth(root.left)
        rd=maxDepth(root.right)

        if(ld>=rd):
            return ld+1

        else:
            return rd+1


def invert(root):
    if(root is None):
        return
    else:
        temp=root
        invert(root.left)
        invert(root.right)

        temp=root.left
        root.left=root.right
        root.right=temp
        

y=int(input("enter tree root value"))

Root=Node(y)
              

print("1.Insert Node\n2.Inorder\n3.Preorder\n4.Postorder\n5.Search")
while True:
    x=int(input("Enter choice"))

    if(x==1):
        n=int(input("Enter value"))
        Root=insert(Root,n)

    if(x==2):
        inorder(Root)

    elif(x==3):
        preorder(Root)

    elif(x==4):
        postorder(Root)

    elif(x==5):
        m=int(input("enter element to be searched"))
        search(Root,m)

    elif(x==0):
        break
            
        
