def encrypt_letter(letter, shift):
    if "A" <= letter <= "Z":
        alphabet_start = ord("A")
    elif "a" <= letter <= "z":
        alphabet_start = ord("a")
    else:
        return letter

    position = ord(letter) - alphabet_start

    new_position = (position + shift) % 26

    encrypted_letter = chr(new_position + alphabet_start)

    return encrypted_letter


def encrypt_message(message, shift):
    encrypted_message = ""

    for character in message:
        encrypted_character = encrypt_letter(character, shift)

        encrypted_message += encrypted_character

    return encrypted_message



def decrypt_letter(letter, shift):
    return encrypt_letter(letter, -shift)


def decrypt_message(message, shift):
    return encrypt_message(message, -shift)


message = "Hello, World! 123"
shift = 3

encrypted = encrypt_message(message, shift)
decrypted = decrypt_message(encrypted, shift)

print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
print(decrypt_message("KHOOR", 3))
print(decrypt_message("Khoor Zruog!", 3))
print(decrypt_message("abc XYZ", 3))