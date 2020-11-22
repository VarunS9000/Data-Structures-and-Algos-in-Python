data=[1,2,3,4,5,6]

def binarySearch(data,start,end,element):
    mid=(end+start-1)//2

    if(data[mid]==element):
        print("element found")
        

    elif(element<data[mid]):
        end=mid-1
        start=0
        binarySearch(data,start,end,element)
        
    elif(element>data[mid]):
        end=len(data)-1
        start=mid+1
        binarySearch(data,start,end,element)
        

n=int(input("enter number to be searched"))
binarySearch(data,0,len(data)-1,n)
        
           
            
