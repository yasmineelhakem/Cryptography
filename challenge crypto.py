#mini ctf securinets insat 2024
"""
Created on Sat Jan 27 22:37:53 2024

@author: yasmi
"""

"""
flag1+flag2+3*flag3==583601198217999802821640273
3*flag1+2*flag2+2*flag3==787432535105101541361772353
-flag2-2*flag3+2*flag4== -119883660368948934388465829
-flag1+flag3-flag4==-102047525517112400806626497

"""
#mini ctf l enoncé
flag=b"Securinets{REDIRECT}"
flag1=bytes_to_long(flag[0: 11])
flag2=bytes_to_long(flag[11:22])
flag3=bytes_to_long(flag[22:33])
flag4=bytes_to_long(flag[33:44])

assert flag1+flag2+3*flag3==583601198217999802821640273
assert 3*flag1+2*flag2+2*flag3==787432535105101541361772353
assert -flag2-2*flag3+2*flag4== -119883660368948934388465829
assert -flag1+flag3-flag4==-102047525517112400806626497


import sys
sys.path.append(r'C:\Users\yasmi\AppData\Roaming\Python\Python311\site-packages')

from Crypto.Util import number
"""
def long_to_bytes(n):
    byte_list = []
    while n:
        byte_list.append(n & 0xFF)
        n >>= 8
    return bytes(reversed(byte_list))
"""
flag1=100819636733389925564838779
flag2=122339437936393884872041265
flag3=120147374516071997461586743
flag4=121375263299794472703374461

ch=number.long_to_bytes(flag1)
print(ch)

"""
non_negative_integer = 16909060
result_bytes = number.long_to_bytes(non_negative_integer)
print(result_bytes)
"""
ph=ch.decode('utf-8')
print(ph)


ch2=number.long_to_bytes(flag2)
print(ch2)

ph2=ch2.decode('utf-8')
print(ph2)


ch3=number.long_to_bytes(flag3)
print(ch3)

ph3=ch3.decode('utf-8')
print(ph3)


ch4=number.long_to_bytes(flag4)
print(ch4)

ph4=ch4.decode('utf-8')
print(ph4)

print(ph+ph2+ph3+ph4)


from sympy import symbols, Eq, solve

# Define variables
flag1,flag2,flag3,flag4 = symbols('flag1 flag2 flag3 flag4')

# Define equations
eq1 = Eq(flag1+flag2+3*flag3,583601198217999802821640273 )
eq2 = Eq(3*flag1+2*flag2+2*flag3,787432535105101541361772353)
eq3 = Eq(-flag2-2*flag3+2*flag4,-119883660368948934388465829)
eq4 = Eq(-flag1+flag3-flag4,-102047525517112400806626497)

# Solve the system of equations symbolically
solution = solve((eq1, eq2,eq3,eq4), (flag1,flag2,flag3,flag4))

print("Symbolic Solution:", solution)
