#Fibonacci series
def fibonacci(n):
    a,b,c=2,1,3
    for i in range(n-1):
        a,b,c=b,c,a*b
    return a

n=int(input("Enter the number of terms: "))
result=fibonacci(n)
print(f"The {n}th term in the modified Fibonacci series is: {result}")