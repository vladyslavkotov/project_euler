# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def nth_prime():

    primes=[2,3]
    i=1
    count=2

    while count!=10_001:
        nums=[6*i-1,6*i+1] # every prime except 2 and 3 is 6n+1 or 6n-1
        for n in nums: #a is possible prime
            flag=0
            for div in range(5, int(n**0.5)+1,6): #b is possible divisor
                if n%div==0 or n%(div+2)==0:
                    flag=1
                    break
            if flag==0:
                primes.append(n)
                count+=1
        i+=1

    return primes[-1]

print(nth_prime())