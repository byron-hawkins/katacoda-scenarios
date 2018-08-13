#!/usr/bin/env python
"""
A simple script for making random passwords, WITHOUT 1,l,O,0.  Because
those characters are visually identical in some fonts. Usage:

<this-script.py> [length] ["easy"]

Example:

<this-script.py>
 * generates a random password of 8 characters

<this-script.py> 12
 * generates a random password of 12 characters

<this-script.py> 12 easy
 * generates a random password of 12 characters that is easy to type
"""

import sys
from random import Random

random = Random()

lDigits = unicode('2345')
rDigits = unicode('789')
lLowers = unicode('qwertasdfgzxcvb')
rLowers = unicode('uiophjknm')
lUppers = unicode('!$%QWERTASDFGZXCVB')
rUppers = unicode('&*{}[]-_UIPHJKLNM')

if (len(sys.argv) > 1):
    arg1 = unicode(sys.argv[1])
    if (arg1.isnumeric()):
        passwordLength = int(arg1)
    else:
        print "USAGE:"
        print sys.argv[0], "[length of password]",
        print "[easy (if you want the password to be easy to type)]"
else:
    passwordLength = 8 # default

if (len(sys.argv) > 2):
    easy = (sys.argv[2] == 'easy')
    if easy:
        lDigits += lDigits
        rDigits += rDigits
        lLowers += lLowers + lLowers
        rLowers += rLowers + rLowers
else:
    easy = False

allDigits = lDigits + rDigits
allLowers = lLowers + rLowers
allUppers = lUppers + rUppers

lGroup = lDigits + lLowers + lUppers
rGroup = rDigits + rLowers + rUppers
allGroup = allDigits + allLowers + allUppers

flip = 0
hasLower = hasUpper = hasDigit = hasSpecial = False
for i in range(passwordLength):
    while True:
        if easy:
            if (i + flip) % 2 == 0:
                group = lGroup
            else:
                group = rGroup
        else:
            group = allGroup

        letter = random.choice(group)
        if easy and (letter.isupper() or not letter.isalnum()):
            flip = (flip + 1) % 2
            if group == lGroup:
                letter = random.choice(rUppers)
            else:
                letter = random.choice(lUppers)

        if letter.islower():
            hasLower = True
        elif letter.isupper():
            hasUpper = True
        elif letter.isnumeric():
            hasDigit = True
        else:
            hasSpecial = True

        missing = 0
        if not hasLower:
            missing += 1
        if not hasUpper:
            missing += 1
        if not hasDigit:
            missing += 1
        if not hasSpecial:
            missing += 1

        if i < (passwordLength - missing):
            sys.stdout.write( letter )
            break

sys.stdout.write("\n")

