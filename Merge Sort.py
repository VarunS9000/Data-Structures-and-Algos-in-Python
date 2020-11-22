#Merge Sort

data=[5,4,3,2,1]

def merge(data,l,m,r):
    n1=m-l+1
    n2=r-m

    L=[0]*n1
    R=[0]*n2

    for i in range(n1):
        L[i]=data[l+i]

    for j in range(n2):
        R[j]=data[m+1+j]


    i=0
    j=0
    k=l

    while(i<n1 and j<n2):
        if(L[i]<=R[j]):
            data[k]=L[i]
            i=i+1

        elif(R[j]<=L[i]):
            data[k]=R[j]
            j=j+1

        k=k+1

    while(i<n1):
        data[k]=L[i]
        i=i+1
        k=k+1

    while(j<n2):
        data[k]=R[j]
        j=j+1
        k=k+1


def mergeSort(data,l,r):
    if(l<r):
        m=(l+r-1)//2

        mergeSort(data,l,m)
        mergeSort(data,m+1,r)
        merge(data,l,m,r)

mergeSort(data,0,len(data)-1)

print(data)

        
        
        
           
            
