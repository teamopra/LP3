#Python program to display the fibonnaci Sequence
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
nterms=7
#check if the number of terms is valid
if nterms<=0:
    print("Please enter a positive number")
else:
    print("Fibonacci Sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
