data=[1,3,5,7,9,11,13,15,17,19,20,21,23,25,27,29]
def interpolationSearch(data,low,high,val):
    print(data[low:high+1])
    mid=low+(high-low)*((val-data[low])/(data[high]-data[low]))
    mid=int(mid)
    if(val==data[mid]):
        print('Value found in position',mid+1)

    elif(val<data[mid]):
        interpolationSearch(data,low,mid-1,val)

    elif(val>data[mid]):
        interpolationSearch(data,mid+1,high,val)

x=int(input('Enter number to search from data'))
interpolationSearch(data,0,len(data)-1,x)
        
    
