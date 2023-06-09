'''
Check if a string input is a palindrome or not
    Test case:
    A man, a plan, a canal, Panama.
'''

from SimpleStack import Stack                               # Imports the necessary python module

# Time Complexity: O(n)
# Space Complexity: O(n)

def is_palindrome(words):
    '''Determines if input is palindrome or not 
    
    Args: 
        string (str) text

    Returns:
        boolean (bool)

    '''
    letters = "abcdefghijklmnopqrstuvwxyz"                  # Creates a string of lowercase alphabet

    original_stack = Stack(len(words))                      # Creates two objects of the Stack
    copy_stack = Stack(len(words))                          # based on length of the word

    for item in words:                                      # Loops over each item in words
        if item.lower() in letters:                         # if the item is in letters
            original_stack.push(item.lower())
            copy_stack.push(item.lower())

    if original_stack.isEmpty():                            # Returns if the stack has no letters
        print("No letters were found.")
        return False

    original_word, reverse = '',''                          # Build the orginal and reversed version
    while not original_stack.isEmpty():                     # by popping the stack until empty
        reverse += original_stack.pop()                     # cba
        original_word = copy_stack.pop() + original_word    # Prefixing each character abc

    return original_word == reverse                         # Returns True if palindrome


def main():
    '''Demonstrates the is_palindrome() function
    
    Prints: 
        string (str) text

    '''
    while True:                                             # Loops until input is empty
        words = input("\nIs it a palindrome: ").strip()

        if not words:                                       # Returns when input is empty
            return

        result = is_palindrome(words)                       # Stores the result of the function call

        print(f"Result: {result}.")                         # Prints the result


main()                                                      # Runs the function
