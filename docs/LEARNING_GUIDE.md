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
