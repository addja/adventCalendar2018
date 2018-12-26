import sys
import numpy

d = 3339 # depth
x, y = 10, 715 # target coordinates

x += 1 # indexes from 0 to x (included) -.-
y += 1 # indexes from 0 to x (included) -.-
geoIdx = numpy.zeros( [ x, y ] )

erosion = lambda x: ( x + d ) % 20183

# set the geological indexes and erosion levels of the edges
for i in range( 1, x ):
    geoIdx[ i, 0 ] = i * 16807

for j in range( 1, y ):
    geoIdx[ 0, j ] = j * 48271

# compute erosion levels and indexes for the rest
for i in range( 1, x ):
    for j in range( 1, y ):
        geoIdx[ i, j ] = erosion( geoIdx[ i - 1, j ]) * erosion( geoIdx[ i, j - 1 ] )

geoIdx[ x - 1, y - 1 ] = 0; # target

risk = 0.0

# compute the riks
for i in range( 0, x ):
    for j in range( 0, y ):
        risk +=  erosion( geoIdx[ i, j ] ) % 3

print( risk )
