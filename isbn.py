'''
This code determines whether an ISBN code is valid or not.
This code was made by Julian
'''

# This assigns the sum to 0 so that the program can later add it.
sumOfIsbn = 0

# The program asks the user for their ISBN number. 
isbn = str(input("Please enter your ISBN: "))

'''
This block of code takes the ISBN number and numbers it
from 0 - 9. Still making it 10 digits for every number in the ISBN number.
The program then multiplies the value by its nummber (0-9)
'''
for i in range(len(isbn)):
    digit = isbn[i]
    multiply_value = 10 - i

'''
Here we take the sum and assign it to the multiplication that the
program did previously
'''
    sumOfIsbn = sumOfIsbn + int(digit) * multiply_value

'''
Here we take the sum and modulus by 11.
If there is a remainder, the ISBN is invalid.
If the remainder is equal to 0, the ISBN is valid.
'''
if sumOfIsbn % 11 == 0:
    print("ISBN is Valid")
else:
    print("ISBN is Invalid")
