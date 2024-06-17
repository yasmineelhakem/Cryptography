from sympy.ntheory.modular import crt  
import gmpy2 as g
from Crypto.Util.number import *


cc=[ct0,ct1,ct2,ct3,ct4,ct5,ct6,ct7,ct8,ct9]
nn=[N0,N1,N2,N3,N4,N5,N6,N7,N8,N9]

"""

mel function eli 3ana : ct=m**e mod(n) => m**e=ct mod(n)
m**e=ct1 mod(n1)
m**e=ct2 mod(n2)
m**e=ct3 mod(n3)
......
donc on va utiliser Chinese Remaining Theorem CRT  solution c=m**e

"""

#crt takhou en parametre 2 liste: lista mtaa ai w lista mtaa les modulo
#trajaa tuple fih solution wel modulo lkol fel kol
c=crt(nn,cc)[0]
#bel irrot ntay7ou fel puissance bech nkharjou  l m

#m**2=c
print(long_to_bytes(g.iroot(c,10)[0]).decode())

"""

le type de retour de irrot est toujours un tuple
Si la racine entière est un entier, le tuple contient:
        l'entier racine et un booléen qui est vrai.
Si la racine entière est un flottant (non entier), le tuple contient:
        la partie entière de la racine et un booléen qui est faux.

"""