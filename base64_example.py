"""
  * binary-to-text
  *commonly used to encode binary data, such as images, audio files, or other binary content, into a text format
  *every three bytes of binary data are represented as four ASCII characters
  * ala kol 6 bits mel binary  charactere 
  *The Base64 character set consists of 64 characters: a combination of uppercase and lowercase letters, digits (0-9),
  and two additional characters (usually '+', and '/'). The character '=' is used as padding
  *The length of the Base64-encoded string is always a multiple of 4 characters.

"""
import base64

#from hex to bytes
hex = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
octets = bytes.fromhex(hex)

#from bytes to base64
res=base64.b64encode(octets)
print(res)