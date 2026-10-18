def encrypt_letter(letter, shift):
  position = ord(letter) - ord("A")

  new_position = (position + shift) % 26

  encrypt_letter = chr(new_position + ord("A"))

  return encrypt_letter

def encrypt_message(message, shift):
    encrypted_message = ""

    for character in message:
        if "A" <= character <= "Z":
            encrypted_character = encrypt_letter(character, shift)
        else:
            encrypted_character = character

        encrypted_message += encrypted_character

    return encrypted_message

print(encrypt_message("HELLO", 3))
print(encrypt_message("HELLO WORLD", 3))
print(encrypt_message("HELLO, WORLD! 123", 3))