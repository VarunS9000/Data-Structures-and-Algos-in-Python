data=[1,2,3,4,5,7,9]

def binarySearch(data,start,end,element):
    if end>=start:
        mid=(end+start-1)//2

        if(data[mid]==element):
            print("element found at position",mid+1)
            

        elif(element<data[mid]):
            binarySearch(data,start,mid-1,element)
            
        elif(element>data[mid]):
            binarySearch(data,mid+1,end,element)

    else:
        print("Not found")

   
        

n=int(input("enter number to be searched"))
binarySearch(data,0,len(data)-1,n)
        
           
            
