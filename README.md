# Caesar Cipher Encoder/Decoder

A command-line Caesar cipher implementation built with Python. Encrypt and decrypt messages using a configurable shift value while preserving uppercase and lowercase letters, spaces, numbers, and punctuation.

This project is part of a 10-project Python learning journey focused on understanding software by building it from scratch.

## Features

* **Message encryption:** Encrypt complete messages using a configurable shift.
* **Message decryption:** Recover the original message using the corresponding shift.
* **Case preservation:** Keep uppercase and lowercase letters in their original case.
* **Character preservation:** Leave spaces, numbers, and punctuation unchanged.
* **Alphabet wraparound:** Correctly handle shifts that pass the end of the alphabet.
* **Interactive CLI:** Choose an operation and enter a message directly in the terminal.
* **Input validation:** Handle invalid menu choices and non-numeric shift values.
* **Automated testing:** Use pytest to verify encryption and decryption behavior.

## Example

With a shift value of `3`:

| Operation | Input               | Output              |
| --------- | ------------------- | ------------------- |
| Encrypt   | `Hello World`       | `Khoor Zruog`       |
| Decrypt   | `Khoor Zruog`       | `Hello World`       |
| Encrypt   | `Hello, World! 123` | `Khoor, Zruog! 123` |

## How the Caesar Cipher Works

The Caesar cipher encrypts a message by shifting each English letter through the alphabet.

For example, with a shift of 3:

```text
Original:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Encrypted: DEFGHIJKLMNOPQRSTUVWXYZABC
```

The alphabet wraps around at the end, so `X`, `Y`, and `Z` become `A`, `B`, and `C`, respectively.

The implementation uses Python's `ord()` and `chr()` functions to work with character code points and modular arithmetic to handle alphabet wraparound.

**Security note:** The Caesar cipher is a historical substitution cipher and is not suitable for protecting sensitive information.

## Requirements

* Python 3
* Git, if you want to clone the repository
* pytest, for running the automated tests

The application itself uses Python's standard library. Pytest is needed only for the test suite.

## Getting Started

### 1. Clone the repository

Replace `YOUR-USERNAME` with the GitHub username that owns this repository.

```bash
git clone https://github.com/YOUR-USERNAME/caesar-cipher.git
cd caesar-cipher
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### 2. Create a virtual environment

A virtual environment keeps project-specific Python packages separate from other projects.

**Windows PowerShell:**

```powershell
python -m venv .venv
```

**macOS or Linux:**

```bash
python3 -m venv .venv
```

### 3. Install pytest

**Windows PowerShell:**

```powershell
.\.venv\Scripts\python.exe -m pip install pytest
```

**macOS or Linux:**

```bash
./.venv/bin/python -m pip install pytest
```

### 4. Run the application

**Windows PowerShell:**

```powershell
.\.venv\Scripts\python.exe caesar_cipher.py
```

**macOS or Linux:**

```bash
./.venv/bin/python caesar_cipher.py
```

Follow the menu instructions to encrypt or decrypt a message.

Choose `1` to encrypt or `2` to decrypt, enter the message, and provide the shift value.

### 5. Run the automated tests

**Windows PowerShell:**

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

**macOS or Linux:**

```bash
./.venv/bin/python -m pytest -v
```

The test suite checks important encryption and decryption behavior, including alphabet wraparound, lowercase letters, and preservation of non-letter characters.

## Project Structure

```text
caesar-cipher/
│
├── caesar_cipher.py
├── tests/
│   └── test_caesar_cipher.py
├── docs/
│   └── LEARNING_GUIDE.md
├── .gitignore
└── README.md
```

The `.venv` and `.git` directories are omitted from this overview because they are local environment and version-control directories, respectively.

### Main files

* `caesar_cipher.py`: Contains the encryption and decryption functions and the command-line interface.
* `tests/test_caesar_cipher.py`: Contains automated tests for the cipher operations.
* `docs/LEARNING_GUIDE.md`: Documents the project-building process and the concepts needed to understand it.
* `.gitignore`: Identifies files that Git should ignore.

## Learning Guide

Want to understand how the application was built?

Read the [Step-by-Step Learning Guide](docs/LEARNING_GUIDE.md).

The guide explains the project requirements, Python concepts, character shifting, modular arithmetic, encryption, decryption, input validation, testing, and independent reconstruction.

It will be expanded as the project progresses.

## Learning Objectives

This project provides practical experience with:

* Python strings and character manipulation.
* Variables, data types, loops, and conditional statements.
* Functions, parameters, and return values.
* Character conversion using `ord()` and `chr()`.
* Modular arithmetic.
* Exception handling and input validation.
* Automated testing with pytest.
* Git and GitHub workflows.
* Technical documentation.

## Current Status

The initial encryption, decryption, interactive interface, and automated tests have been implemented.

The project is being developed incrementally, with further improvements to testing, code organization, and documentation planned.

## Future Improvements

Potential extensions include:

* A clearer separation between application logic and user interaction.
* Additional automated tests for edge cases and invalid input.
* Improved command-line options.
* More comprehensive troubleshooting documentation.
* A complete guide for independently rebuilding the project.

## License

No license has been added yet. A license will be selected before the project is finalized for publication.
