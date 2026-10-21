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


def main():
    print("================================")
    print("       CAESAR CIPHER TOOL")
    print("================================")

    print("\nChoose an operation:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")

    choice = input("\nEnter your choice: ")

    if choice == "1" or choice == "2":
        message = input("Enter your message: ")

        try:
            shift = int(input("Enter shift value: "))

        except ValueError:
            print("Invalid shift value. Please enter a whole number.")
            return

        if choice == "1":
            result = encrypt_message(message, shift)
            print("Encrypted message:", result)
        else:
            result = decrypt_message(message, shift)
            print("Decrypted message:", result)

    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()