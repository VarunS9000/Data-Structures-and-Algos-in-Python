#Linked List in python



class Node:
    
    
    def __init__(self,value):
        self.value=value
        self.next=None

    def append(self,new_node):
        self.next=new_node    
    

def show(current,start):
    current=start
    while current:
        print(current.value,'->',end='')
        current=current.next

    print('NULL')

def insertEnd(value,current,start):
    current=start
    while current.next!=None:
        current=current.next
    new_node=Node(value)
    current.append(new_node)
    current=new_node
    show(current,start)

def insertAfter(afterVal,value,current,start):
    current=start
    while current.value!=afterVal:
        current=current.next

    alias=current.next

    new_node=Node(value)
    current.append(new_node)
    current=new_node
    current.next=alias
    show(current,start)

def delete(value,current,start):
    current=start
    while current.value!=value:
        precurrent=current
        current=current.next

    precurrent.next=current.next
    show(current,start)

def deleteEnd(current,start):
    current=start
    while(current.next!=None):
        precurrent=current
        current=current.next
    current=None
    precurrent.next=None
    show(current,start)
    

    

    
        
    


n=int(input("Enter initial value of node"))

start=Node(n)
current=start

print("1.Insert in End\n2.Insert After\n3.Delete Value\n4.Delete End")



while True:
    
    x=int(input("Enter option"))

    if(x==1):
        n=int(input("Enter number to be inserted in the end"))
        insertEnd(n,current,start)


    elif(x==2):
        m=int(input('Enter number'))
        n=int(input("Enter value to be inserted after {}".format(m)))
        insertAfter(m,n,current,start)

    elif(x==3):
        n=int(input("Enter number to be delete"))
        delete(n,current,start)

    elif(x==4):
        deleteEnd(current,start)

    elif(x==0):
        break
        
    
   
    



        
       
        
    



