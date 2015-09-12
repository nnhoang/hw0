#!/usr/bin/python

""" Write a python script that reads the file and computes the number of
records (in this file, each line is a record) that contain the exact case
insensitive phrase "single malt scotch". Ignore upper and lower casing, so
"Single Malt Scotch", and "SINGLE Malt Scotch" all match, whereas "Single's
Malty Scootch" does not.
"""


def main():
    count = 0
    my_file = open("iowa-liquor-sample.csv", 'r')
    for line in my_file:
        line = line.lower()
        if line.find("single malt scotch") > 0:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
