#!/usr/bin/python3
"""
script that reads stdin line by line
and computes metrics
"""
import re
import signal
import sys


codes = [200, 301, 400, 401, 403, 404, 405, 500]
stats = {}


def main():
    """
    code entry point, run the main code
    """
    pattern = r'((\d{1,3}\.){3}\d{1,3}) \- \[(.*?)\]'
    pattern += r' "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)'
    count = 0

    for line in sys.stdin:
        match = re.fullmatch(pattern, line.strip())
        if match:
            file_size = match.group(5)
            code = int(match.group(4))
            stats['file_size'] = stats.get('file_size', 0) + int(file_size)
            if code in codes:
                stats[code] = stats.get(code, 0) + 1
            count += 1

        if count >= 10:
            count = 0
            print_stats(stats)


def print_stats(stats: dict):
    """
    prints the parsed stats
    """
    print("File size: {}".format(stats.get('file_size', 0)))
    for code in codes:
        val = stats.get(code, None)
        if val:
            print("{}: {}".format(code, val))


def interupt_handler(sig_num, frame):
    """
    handle the CTRL+C interuption
    """
    print_stats(stats)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, interupt_handler)
    try:
        main()
    except KeyboardInterrupt:
        print_stats(stats)
        signal.siginterrupt(signal.SIGINT, True)
