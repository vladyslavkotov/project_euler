# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome():
    pal=0
    for a in range(900,1000):
        for b in range(900,1000):
            if str(a*b)==str(a*b)[::-1] and a*b>pal:
                pal=a*b
    return pal

print(palindrome())

