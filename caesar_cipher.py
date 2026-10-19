def encrypt_message(message, shift):
    encrypted_message = ""

    for character in message:
        encrypted_character = encrypt_letter(character, shift)

        encrypted_message += encrypted_character

    return encrypted_message

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

print(encrypt_message("HELLO", 3))
print(encrypt_message("Hello World", 3))
print(encrypt_message("Hello, World! 123", 3))
print(encrypt_message("xyz XYZ", 3))