# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

"""  67 + 3 = 70
a  b c d e f g h i j k l m n o p q r s t u v w x y z
61 62 63 64 65 66 67 67 68 69 70 

"""


def caesarCipher(s, k):
    # Write your code here

    encrypted = ''
    modk = k % 26

    # captial    65 <= ascii <= 65 + 25 more letters = 90
    # lowercase  97 <= ascii <= 97 + 25 more letters  = 122
    # any other characters should be returned as-is

    for i, char in enumerate(s):
        curr = ord(char)
        # check if upper case letter
        if curr >= 65 and curr <= 90:
            curr = (curr + modk - 65) % 26
            curr = chr(curr + 65)
            encrypted += curr
        # check if lower case letter
        elif curr >= 97 and curr <= 97 + 25:
            curr = (curr + modk - 97) % 26
            curr = chr(curr + 97)
            encrypted += curr
        # or anything else
        else:
            encrypted += char

    return encrypted
