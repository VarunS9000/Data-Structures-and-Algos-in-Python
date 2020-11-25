data=[3,4,2,1,8]

def insertionSort(data):

   for i in range(1,len(data)):
      k=i
      while(data[k]<data[k-1] and k>0):
          data[k],data[k-1]=data[k-1],data[k]
          k=k-1
   print(data)


insertionSort(data)
