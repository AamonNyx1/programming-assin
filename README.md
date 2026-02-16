# Simple message encrypton and decryption Tool

## Overwiew
This project is about a simple tool that allows user to encrypt and decrypt message that 
is written by the user. This code allows the user to input the message and number key and then 
either to encrypt or decrypt the message. Similar number keys are used in both encrypt and decrypt.
And it is an example of cipher txt.

## Feature 
- use shift keys to encrypt alphabetic text
- decrypts text back to its original form
- keeps non alphabetic characters unchanged
- use command line interface

  ```python
# Simple Message Encryption and Decryption Tool
# Caesar Cipher

def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = key % 26

            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            new_char = (ord(char) - base + shift) % 26 + base
            result = result + chr(new_char)
        else:
            result = result + char

    return result


def decrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = key % 26

            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            new_char = (ord(char) - base - shift) % 26 + base
            result = result + chr(new_char)
        else:
            result = result + char

    return result


print("=== Simple Encryption Tool ===")

choice = input("Do you want to Encrypt (E) or Decrypt (D)? ").upper()
message = input("Enter your message: ")
key = int(input("Enter your key (number): "))

if choice == "E":
    encrypted_text = encrypt(message, key)
    print("Encrypted Message:", encrypted_text)

elif choice == "D":
    decrypted_text = decrypt(message, key)
    print("Decrypted Message:", decrypted_text)

else:
    print("Invalid choice! Please enter E or D.")
```


  
