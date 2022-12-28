# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def prime_sum():
    i=1
    cum_sum1=5

    while True:
        nums=[6*i-1,6*i+1]
        if nums[1]>=2_000_000:
            break
        for n in nums:
            flag=0
            for div in range(5, int(n**0.5)+1,6):
                if n%div==0 or n%(div+2)==0:
                    flag=1
                    break
            if flag==0:
                cum_sum1+=n
        i+=1

    return cum_sum1

print(prime_sum())