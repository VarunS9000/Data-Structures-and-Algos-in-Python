data=[1,4,2,3,6,8,9,7]

def partition(data,l,h):
    i=l
    j=h
    pivot=data[l]

    while(i<j):
        while(data[i]<=pivot and i<=h-1):
            i=i+1
            

        while(data[j]>pivot and j>=l+1):

            j=j-1

            
            
        if(i<j):
            data[i],data[j]=data[j],data[i]


    data[l],data[j]=data[j],data[l]
    return j

def quickSort(data,l,h):
    if(l<h):
        divider=partition(data,l,h)
        quickSort(data,l,divider-1)
        quickSort(data,divider+1,h)

    


quickSort(data,0,len(data)-1)
print(data)
        
    

