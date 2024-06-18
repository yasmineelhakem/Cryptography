from Crypto.Util.number import *

integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
#from long to bytes
octets = long_to_bytes(integer)
#from bytes to a message
print(octets.decode('utf-8'))
