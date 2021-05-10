def knapsack(W,n,p,wt):

    K=[[0 for x in range(W+1)] for y in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w]=0

            elif wt[i-1]<=w:
                K[i][w]=max(K[i-1][w],p[i-1]+K[i-1][w-wt[i-1]])

            else:
                K[i][w]=K[i-1][w]


    return K[n][w]


wt=[2,3,4,5]
p=[1,2,5,6]
print(knapsack(8,len(p),p,wt))
                
    
