# Find the difference between the sum of the squares of the first one hundred natural
# numbers and the square of the sum.

# n(n+1)2
# (n(n+1)(2n+1))/6

def difference():
    return int((((100*(101))/2)**2)-((100*101*201)/6))

print(difference())





