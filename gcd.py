import math
print(math.gcd(26513, 32321))

#extended gcd   egcd
# au + bv =gcd(a,b)  if au+bv=1 (gcd(a,b)=1) identité de Bezout 

# Python program to demonstrate working of extended 
# Euclidean Algorithm 
	
# function for extended Euclidean Algorithm

def extended_euclidean(a, b):
  if b == 0:
    gcd, s, t = a, 1, 0
    return (gcd, s, t)
  else:
    s2, t2, s1, t1 = 1, 0, 0, 1
    while b > 0:
      q= a // b
      r, s, t = (a - b * q),(s2 - q * s1),( t2 - q * t1)
      a,b,s2,t2,s1,t1=b,r,s1,t1,s,t
    gcd,s,t=a,s2,t2
    return (gcd,s,t)

a=26513
b=32321
x, y = a, b  # Store temporarily
result=extended_euclidean(a,b)

print(f"gcd({x},{y})={result[0]}")
print(f"Linear combination gcd(a,b)=sa+tb:\n {result[0]}={result[1]}*{x}+{result[2]}*{y}")