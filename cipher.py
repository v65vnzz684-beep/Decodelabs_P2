def encrypt(text, shift):
    encrypted_text = ""
    shift_amount = shift % 26

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(encrypted_text, shift):
    decrypted_text = ""
    shift_amount = shift % 26

    for char in encrypted_text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            decrypted_text += chr((ord(char) - base - shift_amount) % 26 + base)
        else:
            decrypted_text += char

    return decrypted_text


text = input("Enter text to encrypt: ")
shift = int(input("Enter shift amount (1-25): "))

if shift < 1 or shift > 25:
    print("Invalid shift! Please enter a number between 1 and 25.")
    exit()

print(f"Original: {text}")

encrypted = encrypt(text, shift)
print(f"Encrypted: {encrypted}")

decrypted = decrypt(encrypted, shift)
print(f"Decrypted: {decrypted}")