
class Shanon:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preprocess(contents):
    freq={}
    
    for i in contents:
        try:
            freq[i]+=1

        except:
            freq[i]=1

    tupleList=sorted(freq.items(),key=lambda x:x[1])

    newFreq={}
    for t in tupleList:
        newFreq[t[0]]=t[1]

    return newFreq


def splitText(text):
    t=len(text)
    leftString=text[0]
    leftSum=frequency[text[0]]
    leftCount=1
    rightString=text[t-1]
    rightSum=frequency[text[t-1]]
    rightCount=t-2
    if(len(text)>2):
        for i in text:
            if(leftCount==rightCount):
                leftString=leftString+text[leftCount]
                break
            if(leftSum<=rightSum):
                
                leftSum=leftSum+frequency[text[leftCount]]
                leftString=leftString+text[leftCount]
                leftCount+=1
                

            else:
                rightSum=rightSum+frequency[text[rightCount]]
                rightString=rightString+text[rightCount]
                rightCount-=1

    elif(len(text)==2):
        leftString=text[0]
        rightString=text[1]
                

    return leftString,rightString
            


def constructTree(root,val):

        

        if len(root.val)==1:
            #print(Shanon(val).val)
            return Shanon(val)

        else:
            #print(splitText(root.val))
            leftString,rightString=splitText(root.val)


            root.left=constructTree(Shanon(leftString),leftString)
            root.right=constructTree(Shanon(rightString),rightString)

            

       
        
        return root


def shannonCode(root,character,binaryCode):
    
    if(root.left is not None):
        if character in root.left.val:
            binaryCode=binaryCode+'0'
            shannonCode(root.left,character,binaryCode)
            
            
            
        elif character in root.right.val:
             binaryCode=binaryCode+'1'
             shannonCode(root.right,character,binaryCode)
             
             
             
        else:
            print('Not Found')

    else:
        print(binaryCode,end="")


def displayShannonCodedFile(root,fileContents):
    
    for x in fileContents:
        shannonCode(root,x,'')

def binaryCodedFile(fileContents):
    for x in fileContents:
        print(bin(ord(x)).replace('0b',""),end="")

   
f=open('DeepBlue.txt','r')
fc=f.read()
frequency=preprocess(fc)
print(frequency)
string=''
text=string.join(list(frequency.keys()))

Root=Shanon(text)

constructTree(Root,text)
print('Inorder traversal of Shannon Tree')
inorder(Root)
while True:
    print('\n1.Get shannon code for a particular character in file\n2.Get shannon code for the entire file\n3.Get binary code for the entire file\n4.Press 4 to exit')
    option=int(input('Enter option'))
    if(option==1):
        charac=input('Enter character ')
        shannonCode(Root,charac,'')

    elif(option==2):
        displayShannonCodedFile(Root,fc)

    elif(option==3):
        binaryCodedFile(fc)

    elif(option==4):
        break
    

    





        
            
            
