#what is the string?
message = "hello_world"
print(message)
uppercase_message = message.upper()
print(uppercase_message)

#string operation

#return length of a string
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_length = len(alphabet)
print(alphabet_length)
print(alphabet_length - 2)

for letter in range(alphabet_length):
    print("this is printed same # times as the length alphabet")

#lowercase -> uppercase
alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabet = alphabet.upper()
print(uppercase_alphabet)
#ABCDEFGHIJKLMNOPQRSTUVWXYZ

#what is the ASCII?
#convert character to it's ASII code - ord()
english_a = "a"
ASCII_a = ord(english_a)
print(ASCII_a)
#97

ASCII_code_for_a = 97
a_z_letter = chr(97)
print(a_z_letter)
#a

ASCII_code_for_a_letter = 255
result = chr(ASCII_code_for_a_letter)
print(result)
#y

#add two strings together
string_one = "good morning"
string_two = "myneighbor"
combined = string_one + " " + string_two
print(combined)
#good morning something my neighbor

#return the possition of a specific letter
#01234567891011121314151617181920212223242526 (26total)
alphabet = "abcdefghijklmnopqrstuvwxyz"
position_of_letter_d = alphabet.index("d")
print(position_of_letter_d + 1)
#4


#string operation
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#write a line of code to find the length of this string
#print length on the screen
alphabet_length = len(alphabet)
print(alphabet_length)

#write code to find the index (position) of the letter "t"
#print the index on the screen 

position = alphabet.find('t')

print(position + 1)


#strings are objects in oythin
#using the dot operator (.) we can access an object's functions (methods)
message = "this is my message"
uppercase_message = message.capitalize()
print(uppercase_message)

#len function isn't a part of the string object it's more "general"
#that's why it's not called using the dot operator message.len()
print(len(message))