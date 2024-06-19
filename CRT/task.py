from secret import FLAG
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
from sympy import gcd
flag = FLAG


def encrypting(p,q):
    N=p*q
    e=10
    m=bytes_to_long(flag)
    ct=pow(m,e,N)
    return ct,N,e


primes = [getPrime(256) for _ in range(20)]
Ns = [(primes[i],primes[i+10]) for i in range(10)]

ciphertexts = [encrypting(Ns[i][0] , Ns[i][1]) for i in range(10)]


with open("output.txt" , "w") as f :
    for i in range(10):
        f.write(f"ct{i} = {ciphertexts[i][0]}\n")
        f.write(f"N{i} = {ciphertexts[i][1]}\n")
        f.write(f"e{i} = {ciphertexts[i][2]}\n")
        f.write("\n")
