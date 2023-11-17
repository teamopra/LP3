#Program to display the fibonacci sequenceup to n th term
nterms=int(input("How many Terms?"))

#First Two Number
n1=0
n2=1
count=0

#check if the number of terms is valid
if nterms<=0:

    print("Please enter a positive number")

#if there is only one term, return nl
elif nterms==1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)

#Generate Fibonacci sequence
else:
    print("Fibonacci Sequence:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        #update values
        n1=n2
        n2=nth
        count+=1
