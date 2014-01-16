
def checkPalindrome(n):
    if ( str(n) == str(n)[::-1]):
        return True
    return False

def makeProduct(bot,top):
    largest = 0;
    for x in range(top,bot,-1):
        for y in range(top,bot,-1):
            if checkPalindrome(x*y):
                if (x*y) > largest:
                    largest = x*y
    return largest

print(makeProduct(100,999))
