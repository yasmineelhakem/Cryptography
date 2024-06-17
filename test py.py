#Ramadan ctf spark isetcom
# 3tani l n w c wel e 

from Crypto.Util.number import inverse, long_to_bytes
import math
import binascii
from sympy import factorint


n = 121080445189254887821047481617272094153208569924958182521896839941311452630044209191499973207170433956960742750205418444592838153424139044247728464430924089527510320460272909
factors = factorint(n)
print(factors)
p, q = factors.keys()

print("p =", p)
print("q =", q)



c = 44145136431253793742491428137490587414262556125620813004495217809419012897281805438781227523289509785252752996008970820036817646182253051040769395807091065441590671235281645

e = 65537

n = q*p
phi = (q-1)*(p-1)
d = inverse( e, phi )
m = pow( c, d, n )
print(long_to_bytes(m))

# https://www.alpertron.com.ar/ECM.HTM  hedha site yfactorizi
# fama zeda factordb