m=int(input("Enter Start number:"))
n=int(input("Enter End number:"))
print("List of prime numbers from m till n:-")
count=0
for t in range(m,n+1):
    
    i=2
    while (i<t):
        if(t%i==0): 
        
    
            break
            
        else:
            i=i+1
            continue
   
    if(i==t):
        print(f"{t}")
        count=count+1

      
print("Total no. of primes =",count)