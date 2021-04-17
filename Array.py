
from array import Array
import random

# The constructor is called to create the array.      
valueList = Array( 100 )

for i in range(len(valueList ) ):
    valueList[ i ] = random.random()
# Print the values, one per line

for value in valueList:
    print( value)    
