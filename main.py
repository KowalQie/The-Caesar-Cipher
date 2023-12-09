alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Encrypting message
def encrypt (text, shift):
  cipher_text=''
  for index, character in enumerate(text):
      base_number=alphabet.index(character)
      new_base_number=alphabet[base_number+shift]
      cipher_text+=new_base_number
  print(cipher_text)

#Decrypting message
def decrypt (text, shift):
  cipher_text=''
  for index, character in enumerate(text):
      base_number=alphabet.index(character)
      new_base_number=alphabet[base_number-shift]
      cipher_text+=new_base_number
  print(cipher_text)

if direction == 'encode':
  encrypt(text, shift)
elif direction == 'decode':
  decrypt(text, shift)