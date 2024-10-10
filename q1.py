# Question 1: Palindromic Numbers
# A palindromic number is one that is the same when its digits are reversed.
# For example:
# • 98789 is a palindrome;
# • 12344321 is a palindrome;
# • 12345 is not a palindrome as it becomes 54321 when reversed.
# Except for 0, a palindromic number’s leftmost digit must be non-zero.
# 1(a) [ 25 marks ]
# Write a program that reads in a positive integer of up to 20 digits.
# You should output the smallest palindromic number that is higher than the input.

# Sample run 1
# 17
# 22
# Sample run 2
# 343
# 353

# thought process: count digits in input number.
# split number into array of digits
# split in half 
# if first half reversed is greater than second half, set equal to first half +first half reversed 
# if not ...


num = input("enter a positive integer: ")
digits = []
for digit in num:
    digits.append(digit)

print("digits: ", digits)

def better_split(digits):
    halfway = int(len(digits)/2)
    print("halfway: ", halfway)
    firsthalf = []
    secondhalf = []
    for i in range(halfway):
        firsthalf.append(digits[i]) 
        secondhalf.append(digits[halfway+i+1])

    print(firsthalf, secondhalf)

better_split(digits)

# # split number in half
# def split_in_half(num):
#     halfway = int(len(digits)/2)
#     print("halfway: ", halfway)

#     secondhalf = []
#     for i in range(halfway):
#         secondhalf.append(digits.pop())

#     secondhalf.reverse()
#     return digits, secondhalf



# firsthalf, secondhalf = split_in_half(num)
# print("first: ", firsthalf)
# print("second ", secondhalf)

# # if firsthalf reversed is greater than secondhalf then palindrome = firsthalf + firsthalf reversed
# firsthalf.reverse()
# if int(''.join(map(str, firsthalf))) > int(''.join(map(str, secondhalf))):
#     firsthalf.reverse()
#     palindrome = ''.join(map(str, firsthalf)) 
#     firsthalf.reverse()
#     palindrome = palindrome + ''.join(map(str, firsthalf))
#     print(palindrome)
# else: 
#     print("not greater")