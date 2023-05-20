'''
Check if a string input is a palindrome or not
    Test case:
    A man, a plan, a canal, Panama.
'''

from SimpleStack import Stack                               # Imports the necessary python module

# Time Complexity: O()
# Space Complexity: O()
def is_palindrome(words):

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
        reverse += original_stack.pop()
        original_word = copy_stack.pop() + original_word    # Prefixing each character

    return original_word == reverse                         # Returns True if palindrome


def main():

    words = input("\nPlease Enter a String: ").strip()      # Asks the user for input

    while not words:                                        # Loops until input is not empty
        print("String is Empty.")
        words = input("\nPlease Enter a String: ").strip()

    result = is_palindrome(words)                           # Stores the result of the function call

    print(f"Result: {result}.")                             # Prints the result


main()                                                      # Runs the function