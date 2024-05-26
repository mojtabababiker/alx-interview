#!/usr/bin/python3
"""
validate utf-8 module
"""


def validUTF8(data):
    """
    Validate if the data is a valid utf-8 encoding by
    1. checking the leading bytes and validate them
    2. checking the continuation bytes for mutli-bytes

    Parameters:
    -----------
    data: list of integers

    Return:
    -----------
    result: boolean
    """
    if not data or not isinstance(data, list):
        return True

    msp = 1 << 7  # 1000 0000
    smsp = 1 << 6  # 0100 0000
    bytes_number = 0  # counter for the number of bytes for a single char
    # loop on data and check each int (byte) is it single byte or
    # multi-byte character and validate the multi-byte ones
    # [65] ==> 0010 0001
    for chunk in data:
        # the first byte on the data or a start of a new byte
        if bytes_number == 0:
            # count the number of leading bytes
            mask = 1 << 7
            while mask & chunk:
                bytes_number += 1
                mask >>= 1

            # single byte char [ASCI] no need to go farther
            if bytes_number == 0:
                continue
            # invalid leading bytes number, inidcate invalide utf-8
            if bytes_number == 1 or bytes_number > 4:
                return False
        # the current byte is continuation byte
        elif not (msp & chunk and not (smsp & chunk)):
            # invalide utf-8
            return False
        bytes_number -= 1

    return bytes_number == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111,
            110, 32, 105, 115, 32,
            99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
