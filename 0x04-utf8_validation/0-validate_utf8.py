#!/usr/bin/python3
"""
Validate integers as utf-8(single byte
"""

def validUTF8(data):
    """
    validate integers if fall between the
    unicode code point for a singel byte in utf-8
    """
    for num in data:
        if num >= 32 and num < 128:
            continue
        else:
            return False
    return True
