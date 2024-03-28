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
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
    }
line_count = 0


def print_statistics():
    print(f"File size: {total_file_size}")
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")
    print()


def handle_interrupt(sig, frame):
    print_statistics()
    sys.exit(0)


# Register signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, handle_interrupt)

# Read input from stdin
for line in sys.stdin:
    try:
        # Parse the line
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()

    except (IndexError, ValueError):
        # Skip lines that do not match the specified input format
        continue

# Print final statistics when the input ends
print_statistics()
