
class Huffman:
    def __init__(self,val,freq):
        self.val=val
        self.freq=freq
        self.left=None
        self.right=None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def pseudoSort(objList):
    for i in range(len(objList)-1):
        if(objList[i].freq>objList[i+1].freq):
            objList[i],objList[i+1]= objList[i+1],objList[i]

        else:
            break

       
    return objList

def preprocess(contents):
    freq={}
    
    for i in contents:
        try:
            freq[i]+=1

        except:
            freq[i]=1

    print(freq)

    tupleList=sorted(freq.items(),key=lambda x:x[1])

    huffmanObjects=[]
    for t in tupleList:
        huffmanObjects.append(Huffman(t[0],t[1]))

    return huffmanObjects

    
            


def huffmanTree(objectList):
    
    if len(objectList)==1:
       return objectList[0]
    leftNode=objectList[0]
    rightNode=objectList[1]
    parentval=objectList[0].val+objectList[1].val
    parentFreq=objectList[0].freq+objectList[1].freq
    parentNode=Huffman(parentval,parentFreq)
    parentNode.left=objectList[0]
    parentNode.right=objectList[1]
    objectList.pop(0)
    objectList[0]=parentNode
    objectList=pseudoSort(objectList)
    huffmanTree(objectList)
    return objectList[0]

def huffmanCode(root,character,binaryCode):
    
    if(root.left is not None):
        if character in root.left.val:
            binaryCode=binaryCode+'0'
            huffmanCode(root.left,character,binaryCode)
            
            
            
        elif character in root.right.val:
             binaryCode=binaryCode+'1'
             huffmanCode(root.right,character,binaryCode)
             
             
             
        else:
            print('Not Found')

    else:
        print(binaryCode,end="")

def displayHuffmanCodedFile(root,fileContents):
    
    for x in fileContents:
        huffmanCode(root,x,'')

def binaryCodedFile(fileContents):
    for x in fileContents:
        print(bin(ord(x)).replace('0b',""),end="")



f=open('DeepBlue.txt','r')
fc=f.read()
huffmanObjects=preprocess(fc)
Root=huffmanTree(huffmanObjects)
print('Inorder Traversal')
inorder(Root)

while True:
    print('\n1.Get huffman code for a particular character in file\n2.Get huffman code for the entire file\n3.Get binary code for the entire file\n4.Press 4 to exit')
    option=int(input('Enter option'))
    if(option==1):
        charac=input('Enter character ')
        huffmanCode(Root,charac,'')

    elif(option==2):
        displayHuffmanCodedFile(Root,fc)

    elif(option==3):
        binaryCodedFile(fc)

    elif(option==4):
        break



    
        
