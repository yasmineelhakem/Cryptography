print(pow(11, 1, 6))
print(pow(8146798528947, 1, 17))
print(pow(273246787654, 65536, 65537))

"""  The modular multiplicative inverse of an integer 
For all elements g in the field, there exists a unique integer d such that g * d ≡ 1 mod p
                                                                              g=d^-1 mod p """
# What is the inverse element: 3 * d ≡ 1 mod 13?
from Crypto.Util.number import inverse
d = inverse(3, 13)
print(d)

"""          Quadratic Residu
We say that an integer x is a Quadratic Residue if there exists an a such that a^2 = x mod p. 
If there is no such solution, then the integer is a Quadratic Non-Residue.
wel a yetsama square root 
"""
from sympy.ntheory import is_quad_residue, sqrt_mod
print(is_quad_residue(14, 29))
print(is_quad_residue(6, 29))
print(is_quad_residue(11, 29))

#taw naarfou eli 6 houwa quadratic residu bech ntal3ou square root
print(sqrt_mod(6, 29))
