# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.
# What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

def lcm():
    start=20*11
    l1=[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
    remainder=1
    while remainder!=0:
        remainder=sum([start%x for x in l1])
        if remainder==0:
            return start
        start+=20*11

print(lcm())




