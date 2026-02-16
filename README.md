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

  python
# Simple Message Encryption and Decryption Tool
# Caesar Cipher
#create a encryption function
     
      def encrypt(text, key):
    result = ""
    shift = key % 26

    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            new_char = (ord(char) - base + shift) % 26 + base
            result += chr(new_char)
        else:
            result += char

    return result
#
```


  
