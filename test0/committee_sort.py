#! /usr/bin/python3
import sys

f = open(sys.argv[1], 'r')
lines = f.read().split('\n')
f = open(sys.argv[2], 'w')
for line in lines:
    words = line.split(',')
    print(words)
    if not(len(words) == 1 or (len(words) == 2 and words[1] == '')):
        f.write(words[0])
        f.write(',')
        words.pop(0)
        words.sort()
        s = ','.join(words)
        f.write(s)
        f.write('\n')
f.close()
