#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (
if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""
import sys


def print_stats(total_size, status_codes):
    """
    Print the stats
    """
    print("File size: {}".format(total_size))
    for k, v in sorted(status_codes.items()):
        if v:
            print("{}: {}".format(k, v))
            total_size = 0

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
total_size = 0
counter = 0

try:

    for line in sys.stdin:
        counter += 1
        data = line.split()
        if len(data) > 2:
            if data[-2] in status_codes:
                status_codes[data[-2]] += 1
            total_size += int(data[-1])
        if counter == 10:
            print_stats(total_size, status_codes)
            counter = 0
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    #when the user hits ctrl+c
    print_stats(total_size, status_codes)
    raise

if __name__ == "__main__":
    print_stats(total_size, status_codes)

