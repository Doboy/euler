from utils import isPrime, baseGen

from math import log10

s = set()

def isTrunc( n ):
    f = n
    while f:
        if not isPrime( f ):
            return False
        f //= 10

    m = int( log10( n ) + 1 )
    while m:
        if not isPrime( n % ( 10 ** m ) ):
            return False
        m -= 1
    return True

for x in baseGen( goods=( 0, 1, 2, 3, 5, 7, 9 ),
                  start=10 ):
    if isTrunc( x ):
        s.add( x )
        if len( s ) >= 11:
            break

print sum( s )

