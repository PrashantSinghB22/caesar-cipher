# Build a Caesar Cipher in Python: A Step-by-Step Learning Guide

## 1. Introduction

This guide explains how to build a Caesar cipher encoder and decoder from scratch using Python.

It is designed for beginners who want to understand how a small Python application is planned, implemented, tested, documented, and published on GitHub.

The objective is not merely to obtain working code. The objective is to understand the purpose of each component, learn how the implementation works, and develop the ability to recreate the project independently.

Throughout this guide, we will build the application incrementally, starting with the underlying encryption algorithm and gradually developing a complete command-line program.

## 2. What Are We Building?

A Caesar cipher is a substitution cipher that encrypts a message by shifting letters through the English alphabet.

For example, with a shift of 3:

| Original | Encrypted |
| -------- | --------- |
| A        | D         |
| B        | E         |
| C        | F         |
| H        | K         |
| Z        | C         |

The alphabet wraps around at the end. Therefore, shifting Z forward by three positions produces C.

The application will support both encryption and decryption.

For example:

* Original message: `Hello World`
* Shift value: `3`
* Encrypted message: `Khoor Zruog`
* Decrypted message: `Hello World`

The application will preserve uppercase and lowercase letters, spaces, punctuation, and numbers.

**Security note:** The Caesar cipher is a learning exercise, not a secure encryption method. Its small key space and predictable substitution pattern make it easy to break.

## 3. Project Goals

By completing this project, the learner should understand how to:

* Break a programming problem into manageable steps.
* Represent messages using Python strings.
* Store and manipulate values using variables.
* Process characters using loops.
* Make decisions using conditional statements.
* Organize logic into reusable functions.
* Convert characters to numerical code points using `ord()`.
* Convert numerical code points back into characters using `chr()`.
* Apply modular arithmetic to wrap around the alphabet.
* Implement encryption and decryption.
* Collect and validate user input.
* Handle invalid input with exception handling.
* Write automated tests using pytest.
* Track changes using Git.
* Publish a repository on GitHub.
* Write documentation that helps another person reproduce the project.

## 4. Prerequisites

Before beginning the implementation, make sure you have:

* Python installed.
* Visual Studio Code or another Python-compatible editor.
* Git installed.
* A GitHub account if you intend to publish the repository.
* A terminal for running commands.

You should be comfortable opening a project folder, creating files, saving code, and running a Python script.

The Python concepts required for the project will be explained as they are introduced. Advanced Python knowledge is not required.

## 5. Development Approach

We will develop the project in small, testable stages.

Each stage introduces a specific capability or improvement.

The general workflow is:

1. Understand the requirement.
2. Learn the necessary concepts.
3. Design the solution.
4. Implement the feature.
5. Run the application and inspect the results.
6. Test expected behavior and edge cases.
7. Record meaningful changes with Git.
8. Update the documentation.

The completed project should be understandable both as a working application and as a learning resource.

## 6. Project Status

The project is being developed incrementally.

Implemented capabilities include:

* Single-letter encryption.
* Whole-message encryption.
* Uppercase and lowercase support.
* Preservation of non-letter characters.
* Single-letter and whole-message decryption.
* An interactive command-line menu.
* Basic validation of menu choices and shift values.
* Automated tests using pytest.

Additional improvements, tests, and documentation will be recorded as development continues.

## 7. Implementation Walkthrough

The following sections will document the actual implementation in chronological order.

### Stage 1: Project setup

Document the creation of the project directory, Git repository, `.gitignore`, and initial README.

### Stage 2: Understanding the cipher

Explain how alphabet shifts work, why the alphabet must wrap around, and how encryption differs from decryption.

### Stage 3: Encrypting one character

Explain character encoding, `ord()`, `chr()`, zero-based alphabet positions, modular arithmetic, and the `encrypt_letter()` function.

### Stage 4: Encrypting an entire message

Explain the `encrypt_message()` function, iteration over strings, the construction of the output string, and preservation of non-letter characters.

### Stage 5: Adding decryption

Explain why a negative shift reverses the encryption operation and document the decryption functions.

### Stage 6: Building the command-line interface

Explain `input()`, menu selection, the `main()` function, and the application's entry-point condition.

### Stage 7: Input validation

Explain exception handling, `try`, `except`, `ValueError`, and validation of user input.

### Stage 8: Automated testing

Explain test functions, assertions, pytest, test discovery, expected results, and the interpretation of failed tests.

### Stage 9: Final review and publication

Document the final project structure, test commands, Git workflow, installation and usage instructions, and the process of publishing updates to GitHub.

## 8. Independent Reconstruction

After completing the guided implementation, attempt to recreate the core application without copying the original code.

The goal is to demonstrate understanding of:

* The encryption algorithm.
* Alphabet wraparound.
* Message processing.
* Decryption.
* Input validation.
* Testing.

Use the requirements and explanations as guidance, but try to write the implementation independently before consulting the finished version.


# 9. Detailed Implementation Walkthrough

This section explains how to implement the Caesar cipher from the beginning.

Follow the stages in order. Each stage builds on concepts introduced in the previous stage.

## Stage 1: Create the Project

Create a folder named `caesar-cipher` to store the application.

Inside the folder, create the following files and directories:

```text
caesar-cipher/
├── caesar_cipher.py
├── README.md
├── .gitignore
├── docs/
│   └── LEARNING_GUIDE.md
└── tests/
    └── test_caesar_cipher.py
```

The application code belongs in `caesar_cipher.py`. Automated tests belong in `tests/test_caesar_cipher.py`. Project instructions belong in `README.md`, while the detailed tutorial is stored in `docs/LEARNING_GUIDE.md`.

Initialize Git in the project directory:

```powershell
git init
```

Check the repository status:

```powershell
git status
```

Create an initial commit after adding the initial project files.

During development, commit meaningful changes and push them to the GitHub repository.

## Stage 2: Understand Character Representation

Python strings contain characters. To perform the Caesar cipher calculation, we need a way to represent English letters numerically.

Python provides two useful built-in functions.

`ord()` returns the Unicode code point of a single character:

```python
print(ord("A"))  # 65
print(ord("B"))  # 66
print(ord("C"))  # 67
```

`chr()` converts a Unicode code point back into its corresponding character:

```python
print(chr(65))  # A
print(chr(66))  # B
print(chr(67))  # C
```

The numerical code points of uppercase English letters are consecutive. The same is true of lowercase English letters.

This means that we can use arithmetic to move between letters.

However, the code point itself is not the same as the letter's zero-based alphabet position.

For example:

* The code point of `A` is 65.
* The alphabet position of `A` is 0.
* The code point of `D` is 68.
* The alphabet position of `D` is 3.

For uppercase letters, we calculate the alphabet position by subtracting the code point of `A`:

```python
position = ord(letter) - ord("A")
```

For lowercase letters, we subtract the code point of `a`:

```python
position = ord(letter) - ord("a")
```

Both calculations give us an alphabet position between 0 and 25 for the corresponding English letters.

## Stage 3: Implement Single-Letter Encryption

Start with a simple requirement:

Given an uppercase English letter and a shift value, return the encrypted letter.

For example:

```text
Input letter: A
Shift: 3
Expected result: D
```

### Step 3.1: Calculate the alphabet position

For uppercase `A`:

```python
position = ord("A") - ord("A")
```

This produces:

```text
65 - 65 = 0
```

Therefore, `A` has position 0.

### Step 3.2: Add the shift

If we shift `A` forward three positions:

```text
0 + 3 = 3
```

Position 3 represents `D`.

But simply adding the shift does not handle letters that pass the end of the alphabet.

For example, the position of `Z` is 25. Adding 3 produces 28, which is outside the valid range of 0 through 25.

We need modular arithmetic to wrap around the alphabet.

### Step 3.3: Use modulo

The expression:

```python
new_position = (position + shift) % 26
```

keeps the resulting position within the alphabet's range when using a positive divisor of 26.

For `Z` with a shift of 3:

```text
(25 + 3) % 26
= 28 % 26
= 2
```

Position 2 corresponds to `C`.

### Step 3.4: Convert the position back into a character

Once we have the new position, we can reconstruct the uppercase letter:

```python
encrypted_letter = chr(new_position + ord("A"))
```

For position 2:

```text
2 + 65 = 67
chr(67) = C
```

### Step 3.5: Combine the calculation into a function

Our first working function can be written as:

```python
def encrypt_letter(letter, shift):
    position = ord(letter) - ord("A")

    new_position = (position + shift) % 26

    encrypted_letter = chr(new_position + ord("A"))

    return encrypted_letter
```

Test it:

```python
print(encrypt_letter("A", 3))  # D
print(encrypt_letter("Z", 3))  # C
```

At this stage, the function works for uppercase English letters. It does not yet correctly handle lowercase letters or non-letter characters.

## Stage 4: Support Uppercase, Lowercase, and Other Characters

We want the application to preserve capitalization.

For example:

```text
Hello -> Khoor
```

Uppercase and lowercase English letters have different code points. Therefore, we need to use the correct starting point for each case.

We also want spaces, punctuation, and digits to remain unchanged.

Update the function:

```python
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
```

The function now checks three possibilities.

**Uppercase English letter:** Use `A` as the starting point.

**Lowercase English letter:** Use `a` as the starting point.

**Anything else:** Return the original character unchanged.

For example:

```python
print(encrypt_letter("A", 3))  # D
print(encrypt_letter("a", 3))  # d
print(encrypt_letter("Z", 3))  # C
print(encrypt_letter("z", 3))  # c
print(encrypt_letter("!", 3))  # !
print(encrypt_letter("5", 3))  # 5
```

The function expects a single character. Passing an entire message directly to `encrypt_letter()` is outside its intended use.

## Stage 5: Encrypt an Entire Message

The previous function handles one character. We now need to process every character in a message.

Python's `for` loop allows us to examine a string one character at a time.

For example:

```python
message = "HELLO"

for character in message:
    print(character)
```

This prints each letter on a separate line.

To encrypt the entire message, we create an empty string and gradually add each encrypted character to it.

```python
def encrypt_message(message, shift):
    encrypted_message = ""

    for character in message:
        encrypted_character = encrypt_letter(character, shift)

        encrypted_message += encrypted_character

    return encrypted_message
```

Here's how it works.

First, we create an empty string:

```python
encrypted_message = ""
```

Next, the loop takes one character at a time:

```python
for character in message:
```

We pass the character to our single-letter function:

```python
encrypted_character = encrypt_letter(character, shift)
```

We add the result to the growing output string:

```python
encrypted_message += encrypted_character
```

After the loop finishes, we return the complete message:

```python
return encrypted_message
```

Because `encrypt_letter()` returns non-letter characters unchanged, the larger function automatically preserves spaces, punctuation, and digits.

Test the function:

```python
print(encrypt_message("HELLO", 3))
print(encrypt_message("Hello World", 3))
print(encrypt_message("Hello, World! 123", 3))
```

Expected output:

```text
KHOOR
Khoor Zruog
Khoor, Zruog! 123
```

## Stage 6: Implement Decryption

Decryption reverses the encryption operation.

If encryption moves a letter forward three places, decryption moves it backward three places.

Our existing encryption formula supports negative shifts.

For example:

```python
print(encrypt_letter("D", -3))  # A
print(encrypt_letter("A", -3))  # X
```

Python's modulo operation with a positive divisor handles negative shifts by producing a result in the range 0 through 25.

We can therefore reuse our existing function.

### Step 6.1: Decrypt one character

```python
def decrypt_letter(letter, shift):
    return encrypt_letter(letter, -shift)
```

Passing a negative shift reverses the direction of the transformation.

### Step 6.2: Decrypt an entire message

Similarly, we can reuse `encrypt_message()`:

```python
def decrypt_message(message, shift):
    return encrypt_message(message, -shift)
```

This works because `encrypt_message()` processes every character using `encrypt_letter()`, which supports negative shifts.

Test decryption:

```python
print(decrypt_letter("D", 3))  # A
print(decrypt_message("KHOOR", 3))  # HELLO
print(decrypt_message("Khoor Zruog", 3))  # Hello World
```

An important property of the cipher is that decrypting a message with the same shift used to encrypt it restores the original message.

## Stage 7: Build the Interactive Command-Line Interface

Our functions now perform the encryption and decryption. The next requirement is to let users operate the application through the terminal.

The `input()` function collects user input:

```python
message = input("Enter your message: ")
```

It always returns a string.

If we need a whole number, we must convert the input:

```python
shift = int(input("Enter shift value: "))
```

We use conditional statements to determine which operation to execute.

The `main()` function coordinates the application:

```python
def main():
    print("================================")
    print("       CAESAR CIPHER TOOL")
    print("================================")

    while True:
        print("\nChoose an operation:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")

        choice = input("\nEnter your choice: ")

        if choice == "1" or choice == "2":
            break

        print("Invalid choice. Please select 1 or 2.")

    message = input("Enter your message: ")

    while True:
        try:
            shift = int(input("Enter shift value: "))
            break

        except ValueError:
            print("Invalid shift value. Please enter a whole number.")

    if choice == "1":
        result = encrypt_message(message, shift)
        print("Encrypted message:", result)

    else:
        result = decrypt_message(message, shift)
        print("Decrypted message:", result)
```

The first `while` loop repeats the menu until the user selects a valid operation.

The second loop keeps asking for a shift value until Python can convert the input into an integer.

The `try` block attempts the conversion, while `except ValueError` handles input that cannot be converted.

The program then calls either `encrypt_message()` or `decrypt_message()`.

The application does not need a separate encryption algorithm inside `main()`. It reuses the functions we implemented earlier.

## Stage 8: Add the Application Entry Point

At the end of `caesar_cipher.py`, add:

```python
if __name__ == "__main__":
    main()
```

When Python executes this file directly, `__name__` is set to `"__main__"`, and the interactive application starts.

When another file imports the functions, the interactive menu does not start automatically.

This makes the functions easier to reuse and test.

## Stage 9: Test the Application Manually

Run the application from the project directory:

```powershell
python caesar_cipher.py
```

Alternatively, if Python is available through the Windows launcher:

```powershell
py caesar_cipher.py
```

Test encryption using:

```text
Choice: 1
Message: Hello World
Shift: 3
```

Expected result:

```text
Encrypted message: Khoor Zruog
```

Test decryption using:

```text
Choice: 2
Message: Khoor Zruog
Shift: 3
```

Expected result:

```text
Decrypted message: Hello World
```

Also test invalid menu choices and invalid shift values.

The application should display helpful error messages rather than crash when the user enters an unsupported menu choice or a non-numeric shift.

## Stage 10: Keep the Implementation Organized

The finished `caesar_cipher.py` file should contain these functions in order:

1. `encrypt_letter()`
2. `encrypt_message()`
3. `decrypt_letter()`
4. `decrypt_message()`
5. `main()`

The final entry-point condition belongs at the bottom:

```python
if __name__ == "__main__":
    main()
```

The encryption and decryption functions contain the transformation logic. The `main()` function manages user interaction.

Separating these responsibilities makes the implementation easier to test, understand, and modify.

## Stage 11: Run Automated Tests

The project uses pytest to test the encryption and decryption functions.

Install pytest in the project's virtual environment if it is not already installed.

On Windows PowerShell, run:

```powershell
.\.venv\Scripts\python.exe -m pip install pytest
```

Run the tests:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

The tests check uppercase and lowercase encryption, alphabet wraparound, preservation of non-letter characters, message encryption, decryption, and the property that encryption followed by decryption restores the original message.

A passing test suite provides evidence that the tested behaviors work as expected. It does not prove that every possible input or scenario is correct.

## Stage 12: Record Changes With Git

After making a meaningful change, inspect the repository:

```powershell
git status
```

Review changes to tracked files:

```powershell
git diff
```

Stage the relevant files:

```powershell
git add caesar_cipher.py
```

For a new or updated test file, stage that file as well.

Commit the changes with a descriptive message:

```powershell
git commit -m "Describe the change"
```

Push the commits to GitHub:

```powershell
git push
```

Use commit messages that describe the change you actually made. Avoid committing broken code or claiming that tests pass without running them.

## 13. Final Learning Check

After completing the project, try to implement the core functionality independently.

You should be able to explain:

* Why alphabet positions start at zero.
* How `ord()` and `chr()` are used.
* Why modulo 26 is necessary.
* How the program handles uppercase and lowercase letters.
* Why spaces and punctuation remain unchanged.
* Why a negative shift reverses encryption.
* Why encryption and decryption are separate functions.
* How the interactive interface calls those functions.
* How exceptions prevent invalid numerical input from crashing the program.
* How automated tests verify expected behavior.

If you cannot explain a particular stage, revisit that section and reproduce its examples before moving on.

The goal is not to memorize every line. The goal is to understand the reasoning well enough to build the program again.
