
"""
Example

s = '12:01:00PM'
Return '12:01:00'.

s = '12:01:00AM'
Return '00:01:00'.

"""

# timeConversion: str -> str
def timeConversion(s):
    """
        :type s: string in 12h AM/PM format
        :rtype:  string in 24h format
    """

    # logic to check if AM/PM
    # logic to convert the hour
    # minutes and seconds stay same
    # drop the AM/PM in output
    h = int(s[:2])
    suffix = s[-2:]

    h = h % 12 if suffix == 'AM' else h % 12 + 12

    output = '{:02}{}'.format(
        h,
        s[2:-2]
    )
    return output
if __name__ == "__main__":
    
    a = timeConversion('12:01:00PM')
    print(a)

"""
    12:00AM     00:00
    01:00AM     01:00
    02:00AM     02:00
    .
    .
    .
    12:00PM     12:00
    01:00PM     13:00
    02:00PM     14:00
    03:00PM     15:00
    .           
    .
    .
    .         
    08:00PM     20:00
    09:00PM     21:00
    10:00PM     22:00
    11:00PM     23:00
    11:59:59PM  23:59:59
"""
