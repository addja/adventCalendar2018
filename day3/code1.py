import sys
import numpy

fabric = numpy.zeros([1000,1000])

for line in sys.stdin:
    # parse input
    data = line.split( '@ ')[ 1 ].split( ' ' )
    pos = str( data[0] ).split( ',' )
    pos[1] = str(pos[1])[:-1]
    size = str( data[1] ).split( 'x' )
    size[1] = str(size[1])[:-1]
    pos = list ( map( int, pos ) )
    size = list( map( int, size ) )

    # update fabric
    for i in range( pos[0], pos[0] + size[0] ):
        for j in range( pos[1], pos[1] + size[1] ):
            fabric[i][j] += 1

# output overlapping positions
count = 0
for i in numpy.nditer( fabric ):
    if i > 1: count += 1
print ( count )
