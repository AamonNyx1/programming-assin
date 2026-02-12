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
