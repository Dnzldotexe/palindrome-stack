from SimpleStack import Stack
import string

# A man, a plan, a canal, Panama.

def is_palindrome():

    alphabet_lower = string.ascii_lowercase

    word = input("Please Enter String: ")

    stack = Stack(len(word))

    for letter in word:         # Loop over letters in word
        if not stack.isFull() and letter.lower() in alphabet_lower:   # Push letters on stack if not full
            stack.push(letter)

    reverse = ''                # Build the reversed version
    while not stack.isEmpty():  # by popping the stack until empty
        reverse += stack.pop()

    if word == reverse:
        print(f"'{word}' is Palindrome")

    else:
        print(f"'{word}' is not Palindrome")


is_palindrome()


# references:
# https://tutorial.eyehunts.com/python/python-list-of-letters-a-z-how-to-make-and-print-example/