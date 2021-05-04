
def fibonacci(n,memo):
    if n==0:
        return 0
    elif n==1:
        return 1

    if n in memo:
        return memo[n]
   
    else:
        memo[n]=fibonacci(n-1,memo)+fibonacci(n-2,memo)
        return memo[n]

x=int(input("Enter number"))
memo=[0]*(x+1)
print(fibonacci(x,memo))
print(memo)
