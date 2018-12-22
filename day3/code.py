import sys
import numpy

def parseLine( line ):
    numId = str( line.split( '@ ')[ 0 ] )[1:]
    data = line.split( '@ ')[ 1 ].split( ' ' )
    pos = str( data[0] ).split( ',' )
    pos[1] = str(pos[1])[:-1]
    size = str( data[1] ).split( 'x' )
    size[1] = str(size[1])[:-1]
    pos = list ( map( int, pos ) )
    size = list( map( int, size ) )
    return size, pos, numId

def found ( line ):
    size, pos, numId = parseLine( line )

    # look for complete pattern
    for i in range( pos[0], pos[0] + size[0] ):
        for j in range( pos[1], pos[1] + size[1] ):
            if fabric[i][j] != 1: return False

    print( numId )
    return True

fabric = numpy.zeros([1000,1000])

for line in sys.stdin:
    # parse input
    size, pos, _ = parseLine( line )

    # update fabric
    for i in range( pos[0], pos[0] + size[0] ):
        for j in range( pos[1], pos[1] + size[1] ):
            fabric[i][j] += 1

# output overlapping positions
count = 0
for i in numpy.nditer( fabric ):
    if i > 1: count += 1
print ( count )

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        if ( found ( line ) ): break
