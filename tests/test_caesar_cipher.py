from caesar_cipher import (
    encrypt_letter,
    encrypt_message,
    decrypt_letter,
    decrypt_message,
)


def test_encrypt_uppercase_letter():
    assert encrypt_letter("A", 3) == "D"


def test_encrypt_uppercase_wraparound():
    assert encrypt_letter("Z", 3) == "C"


def test_encrypt_lowercase_letter():
    assert encrypt_letter("a", 3) == "d"


def test_non_letters_unchanged():
    assert encrypt_letter("!", 3) == "!"
    assert encrypt_letter("5", 3) == "5"
    assert encrypt_letter(" ", 3) == " "


def test_encrypt_message_preserves_other_characters():
    message = "Hello, World! 123"

    result = encrypt_message(message, 3)

    assert result == "Khoor, Zruog! 123"


def test_decrypt_uppercase_letter():
    assert decrypt_letter("D", 3) == "A"


def test_decrypt_lowercase_letter():
    assert decrypt_letter("d", 3) == "a"


def test_decrypt_message():
    message = "Khoor, Zruog! 123"

    result = decrypt_message(message, 3)

    assert result == "Hello, World! 123"


def test_encrypt_then_decrypt_returns_original():
    message = "Hello, World! 123"
    shift = 3

    encrypted = encrypt_message(message, shift)
    decrypted = decrypt_message(encrypted, shift)

    assert decrypted == message







def test_zero_shift_keeps_message_unchanged():
    message = "Hello, World!"

    assert encrypt_message(message, 0) == message


def test_shift_of_26_keeps_message_unchanged():
    message = "Hello, World!"

    assert encrypt_message(message, 26) == message


def test_shift_larger_than_alphabet():
    assert encrypt_message("ABC", 29) == "DEF"


def test_negative_shift_moves_letters_backward():
    assert encrypt_message("DEF", -3) == "ABC"


def test_lowercase_wraparound():
    assert encrypt_message("xyz", 3) == "abc"


def test_empty_message():
    assert encrypt_message("", 3) == ""
    assert decrypt_message("", 3) == ""


def test_non_english_letters_are_preserved():
    assert encrypt_message("café!", 3) == "fdié!"