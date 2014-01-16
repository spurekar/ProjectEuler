def Euler3(n=49):  #600851475143):
    for i in range(2,100000):
        while n % i == 0:
            n //= i
            print("We found %d is a factor, lets test %d" % (i, n))
            if n == 1 or n == i:
                return i

Euler3()
