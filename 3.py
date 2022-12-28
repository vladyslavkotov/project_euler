# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def prime_factor():

    factors=[2,3]
    i=1
    target=600851475143

    while True:
        nums = [6 * i - 1, 6 * i + 1]
        if nums[1] >= (target**0.5)+1:
            break
        for n in nums:
            flag = 0
            for div in range(5, int(n ** 0.5) + 1, 6):
                if n % div == 0 or n % (div + 2) == 0:
                    flag = 1
                    break
            if flag == 0 and target%n==0:
                factors.append(n)
        i += 1

    return factors[-1]

print(prime_factor())