#xor teste l égalité

#Given the string label, XOR each character with the integer 13. Convert these integers back to a string
#b xor taatik toul resultat
from pwn import xor

ch = "label"
x = 13

res = xor(ch, x)

print(res)

"""
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0

"""

"""
Enoncé:
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

"""
#il faut convertir mel hex lel bytes
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
k2xork1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
k2xork3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
res = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

key2 = xor(k2xork1, key1)
key3 = xor(k2xork3, key2)
flag = xor(res, key1, key2, key3)
print(flag)

""" 
       Single Byte XOR
**each byte of the plaintext is XORed with a single byte key
**Choose a single byte key which can range from 0 to 255 (in decimal) or 0x00 to 0xFF (in hexadecimal)
**ala heka tnajam tbruteforci w tala3 l key w ciphertext

"""
#Favourite Byte (CryptoHack)

val = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
valBytes = bytes.fromhex(val)
print(valBytes)
def find_crypto(valBytes):
    key = 0
    while True:
        flag = xor(valBytes, key)
        if b'crypto' in flag:
            return flag
        key += 1

print(find_crypto(valBytes))