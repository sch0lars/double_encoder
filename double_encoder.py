# # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                 #
#   A url double encoder for XSS attacks.         #
#                                                 #
#   Author: Tyler Hooks                           #
#                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # #


import urllib

def encode(string):
    encoded_string = ""
    for s in string:
        char = hex(ord(s)).replace("0x", "")
        char = char.upper()
        encoded_string += ("%25" + char)
    return encoded_string

# Write code to be encoded here.
code = ""
encoded = encode(code)
print(encoded)
