def lcs(x,y,m,n): # Time complexity = O(2^n)
    if m==0 or n==0:
        return 0
    elif x[m-1]==y[n-1]:
        return 1+lcs(x,y,m-1,n-1)

    else:
        return max(lcs(x,y,m,n-1),lcs(x,y,m-1,n))

def lcs2(x,y,m,n): # Time complexity = O(m*n)
    table=[[0]*(n+1) for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                table[i][j]=0

            elif x[m-1]==y[n-1]:
                table[i][j]=1+table[i-1][j-1]

            else:
                table[i][j]=max(table[i][j-1],table[i-1][j])

    return table[m][n]

 


print(lcs('abcd','bd',len('abcd'),len('bd')))
print(lcs2('abcd','bd',len('abcd'),len('bd')))


                
            
