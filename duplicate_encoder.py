#Duplicate Encoder
# The goal of this exercise is to convert a string to a new 
# string where each character in the new string is
# "(" if that character appears only once in the original string, or ")" 
# if that character appears more than once in the original string.
# #  Ignore capitalization when determining if a character is a duplicate.

# str="Success"
# newstr=str.lower()
# encoded=""
# print(newstr)
# for i in newstr:
#     if newstr.count(i)>1:
#         encoded=encoded+")"
#     else:
#         encoded=encoded+"("
# print(encoded)
num="8 j 8   mBliB8g  imjB8B8  jl  B"
new_num=num.replace(" ","")
print(new_num)
