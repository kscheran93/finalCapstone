# ************ Cypher Project Task **************

# References:
# https://www.youtube.com/watch?v=JtbKh_12ctg&t=643s
# created a variable and taking user_input value from user
user_input = input('Please enter the text')
# As per the task requirement in alphabets 'a' letter should be encrypted with 'p' letter and clock wise rotation in total 26 alphabets
# I have created a variable shift and assigned 15 values because the task requirement need 15th letter
# example 'a' letter should be encrypted with 'p' letter and 'p' letter encrypted with 'e'
shift = 15


# created a function and used for in loop inside function to iterate the character with user_input
# for ASCII Table reference: https://www.geeksforgeeks.org/ascii-table/
# created logic
def encrpted_alphabet(text, s):
    text = text.lower()
    encrypted_text = ''
    for char in text:
        if char.islower():
            encrypted_text += chr((ord(char) + s - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text


# The final output
print(
    f'The final encrypted code of users input: {encrpted_alphabet(user_input, shift)}')
