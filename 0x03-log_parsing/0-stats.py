#!/usr/bin/python3
"""
Parse logging files
"""
import signal
import sys
import re


def handler(signum, frame):
    """
    Handler for a SIGINT (ctrl-c) signals
    """
    print('File size: {:d}'.format(file_size))
    codes_sorted = sorted(codes.keys(), key=lambda k: int(k))
    for cd in codes_sorted:
        print('{}: {:d}'.format(cd, codes.get(cd)))


signal.signal(signal.SIGINT, handler)

file_size = 0
codes = {}
count = 0
# matches 117.254.206.229 - [2024-03-28 10:10:52.224640]\
# "GET /projects/260 HTTP/1.1" 405 829
# and groups the last two numbers
p = r'^[\d+.]*\s-\s\[[\d+-:.\s]*\]\s[\\"\w.\s/]*\s(\d+)\s(\d+)'
pattern = re.compile(p)

# readline from stdout
for line in sys.stdin:
    if count % 10 == 0 and count != 0:
        print('File size: {:d}'.format(file_size))
        codes_sorted = sorted(codes.keys(), key=lambda k: int(k))
        for cd in codes_sorted:
            print('{}: {:d}'.format(cd, codes.get(cd)))
    try:
        code, size = pattern.search(line).groups()
        codes[code] = codes.get(code, 0) + 1
        file_size += int(size)
    except Exception:
        pass

    count += 1
