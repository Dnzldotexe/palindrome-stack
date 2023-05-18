# Check if a string input is a palindrome or not
    # Test case:
    # A man, a plan, a canal, Panama.

from SimpleStack import Stack                                                   # Imports the necessary python module


def is_palindrome():

    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"                               # Creates a string of lowercase letters

    word = input("\nPlease Enter a String: ").strip()                           # Asks the user for input

    while not word and word not in alphabet_lower:                              # Validates input
        print("String Invalid")
        word = input("\nPlease Enter a String: ").strip()
    
    original_stack = Stack(len(word))                                           # Creates two ojects of the Stack
    copy_stack = Stack(len(word))                                               # based on length

    for letter in word:                                                         # Loops over each letters in word
        if not original_stack.isFull() and letter.lower() in alphabet_lower:    # Push letters on both stacks if not full
            original_stack.push(letter.lower())                                 # and if letters are in alphabet_lower
            copy_stack.push(letter.lower())
    
    original_word = ''                                                          # Creates an empty string
    reverse = ''                                                                # Build the reversed version
    while not original_stack.isEmpty():                                         # by popping the original_stack until empty
        reverse += original_stack.pop()
        original_word = copy_stack.pop() + original_word                        # Adding each character after the other

    if original_word != reverse:                                                # Checks if both string are not the same
        print(f"'{word}' is not a Palindrome")                                  # prints not a palindrome if not

    else:                                                                       # prints palindrome if both are identical
        print(f"'{word}' is a Palindrome")                                      


is_palindrome()                                                                 # runs the function