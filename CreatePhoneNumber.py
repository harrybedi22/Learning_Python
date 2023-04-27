# Python program
#Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
#create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_number(n):
    phone_number=""
    for i in range(len(n)):
        phone_number=phone_number+str(n[i])
    formatted_phonenumber=f'({phone_number[0:3]}) {phone_number[3:6]}-{phone_number[6:]}'
    return formatted_phonenumber
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
