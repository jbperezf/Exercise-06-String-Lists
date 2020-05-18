# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

word_to_check = str(input("Enter the word to check: ")).lower()
word_to_check_list = list(word_to_check)
word_reverse = list(word_to_check).copy()
word_reverse.reverse()

if word_to_check_list == word_reverse:
    print(word_to_check + " is a palindrome.")
else:
    print(word_to_check + " is not a palindrome.")
