# PSet 6 of Harvard's CS50 Week 06: Python
This is the problem set assigned for week six of Harvard's CS50 class in python. I'm using it as a study tool. The problems I did are described below.

## Mario

- Write, in a file called mario.py in ~/workspace/pset6/mario/more/, a program that recreates these half-pyramids using hashes (#) for blocks, exactly as you did in Problem Set 1, except that your program this time should be written (a) in Python ~~and (b) in CS50 IDE~~.
- To make things more interesting, first prompt the user for the half-pyramids' heights, a positive integer between 1 and 8, inclusive. (The height of the half-pyramids pictured above happens to be 4, the width of each half-pyramid 4, with a gap of size 2 separating them.)
- If the user fails to provide a positive integer no greater than 8, you should re-prompt for the same again.
- Then, generate (with the help of print and one or more loops) the desired half-pyramids.
- Take care to left-align the bottom-left corner of the left-hand half-pyramid with the left-hand edge of your terminal window.

## Cash

- Write, in a file called cash.py in ~/workspace/pset6/cash/, a program that first asks the user how much change is owed and then spits out the minimum number of coins with which said change can be made, exactly as you did in Problem Set 1, except that your program this time should be written (a) in Python ~~and (b) in CS50 IDE~~.
- Use get_float from the CS50 Library to get the user’s input and print to output your answer. Assume that the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).
- We ask that you use get_float so that you can handle dollars and cents, albeit sans dollar sign. In other words, if some customer is owed $9.75 (as in the case where a newspaper costs 25¢ but the customer pays with a $10 bill), assume that your program’s input will be 9.75 and not $9.75 or 975. However, if some customer is owed $9 exactly, assume that your program’s input will be 9.00 or just 9 but, again, not $9 or 900. Of course, by nature of floating-point values, your program will likely work with inputs like 9.0 and 9.000 as well; you need not worry about checking whether the user’s input is "formatted" like money should be.
- If the user fails to provide a non-negative value, your program should re-prompt the user for a valid amount again and again until the user complies.
- Incidentally, so that we can automate some tests of your code, we ask that your program’s last line of output be only the minimum number of coins possible: an integer followed by ```\n```.

## Caesar-Cipher

- Implement a program that encrypts messages using Caesar’s cipher, per the below.
    - plaintext:  HELLO  
    - ciphertext: URYYB
    - Design and implement a program, caesar, that encrypts messages using Caesar’s cipher, exactly as you did in Problem Set 2, except that your program this time should be written (a) in Python ~~and (b) in CS50 IDE~~.

-Implement your program in a file called caesar.py in your ~/workspace/pset6/caesar directory (if it doesn’t already exist, create it now!).

- Your program must accept a single command-line argument, a non-negative integer. Let’s call it k for the sake of discussion.

- If your program is executed without any command-line arguments or with more than one command-line argument, your program should print an error message of your choice (with print) and exit immediately with a status code of 1.

- You can assume that, if a user does provide a command-line argument, it will be a non-negative integer (e.g., 1). No need to check that it’s indeed numeric.

- Do not assume that k will be less than or equal to 26. Your program should work for all non-negative integral values of k less than 231 - 26. In other words, you don’t need to worry if your program eventually breaks if the user chooses a value for k that’s too big or almost too big to fit in an int. (Recall that an int can overflow.) But, even if k is greater than 26, alphabetical characters in your program’s input should remain alphabetical characters in your program’s output. For instance, if k is 27, A should not become [ even though [ is 27 positions away from A in ASCII, per asciichart.com; A should become B, since B is 27 positions away from A, provided you wrap around from Z to A.

- Your program must output plaintext: (without a newline) and then prompt the user for a string of plaintext (using get_string).

- Your program must output ciphertext: (without a newline) followed by the plaintext’s corresponding ciphertext, with each alphabetical character in the plaintext "rotated" by k positions; non-alphabetical characters should be outputted unchanged.

- Your program must preserve case: capitalized letters, though rotated, must remain capitalized letters; lowercase letters, though rotated, must remain lowercase letters.

- After outputting ciphertext, you should print a newline.
[Back](../README.md#harvard)
