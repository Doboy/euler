from utils import pqSearch
from ast import literal_eval

dist = {}

for i, line in enumerate( open( "txt/p081" ) ):
    for j, number in enumerate( line.split( ',' ) ):
        dist[ i, j ] = literal_eval( number )

fringe = [ ( dist[ 0, 0 ], ( 0, 0 ) ) ]

def successorFn( state ):
    i, j = state
    if i < 79:
        yield i + 1, j
    if j < 79:
        yield i, j + 1

def goalStateFn( state ):
    i, j = state
    return ( i, j ) == ( 79, 79 )

def distFn( from_, to_ ):
    return dist[ to_ ]

print pqSearch( fringe=fringe,
                successorFn=successorFn,
                goalStateFn=goalStateFn,
                distFn=distFn ).search()
