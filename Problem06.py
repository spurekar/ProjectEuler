
def sumSquares():
    added = 0
    for i in range(1,101):
        added += i**2
    return added

def squaresSum():
    added = sum(range(1,101))
    return (added**2)


print ( squaresSum() - sumSquares() )
