from unitconversion import *

message = 'i went to the shop'
converted_message = process(message)

print(message)
print(type(converted_message))


if type(converted_message) is str:
    print("if Passed")
