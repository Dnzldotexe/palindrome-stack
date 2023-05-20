'''
Check if a string input is a palindrome or not
    Test case:
    A man, a plan, a canal, Panama.
'''

from SimpleStack import Stack                               # Imports the necessary python module

# Time Complexity: O()
# Space Complexity: O()
def is_palindrome(word):

    lowercase = "abcdefghijklmnopqrstuvwxyz"                # Creates a string of lowercase letters

    original_stack = Stack(len(word))                       # Creates two ojects of the Stack
    copy_stack = Stack(len(word))                           # based on length of the word

    for letter in word:                                     # Loops over each letters in word
        if letter.lower() in lowercase:                     # if the letter is in lowercase
            original_stack.push(letter.lower())
            copy_stack.push(letter.lower())

    if original_stack.isEmpty():                            # Returns if the stack has no letters
        print("No letters were found.")
        return False

    original_word, reverse = '',''                          # Build the orginal and reversed version
    while not original_stack.isEmpty():                     # by popping the stack until empty
        reverse += original_stack.pop()
        original_word = copy_stack.pop() + original_word    # Adding each character after the other

    if original_word != reverse:                            # Returns False if not palindrome
        return False

    return True                                             # Returns True if palindrome


def main():

    word = input("\nPlease Enter a String: ").strip()       # Asks the user for input

    while not word:                                         # Loops until string is not empty
        print("String is Empty.")
        word = input("\nPlease Enter a String: ").strip()

    result = is_palindrome(word)                            # Stores the result of the function call

    print(f"Result: {result}.")                             # Prints the result


main()                                                      # Runs the function