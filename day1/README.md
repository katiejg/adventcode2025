## Day 1 of Advent of Code

Important lessons learned:
- Just use Python since I'm gonna have to deal with strings and arrays and all the stuff that gets messy in C
- Test on the smaller data set since you already know the expected output of it (duh)
- But don't assume that all numbers are two digits just because they are in the smaller data set -_- (also duh, but I guess I'm too hopeful)

## Part 1
**Key realization: Number of clicks can be more than two digits**
Basics:
If I turn left, subtract. If I turn right, add. Dial is cyclic from 0-99.

## Part 2
Small cases to think about:
If the dial starts at 50, and I rotate it 50 times (either way), it will end on 0.
If I rotate it 100 times (either way), it will end on 50 and pass 0 once.
If I rotate it 150 times (either way), it will pass 0 once and end on 0. 
If I rotate it 200 times, it will end on 50 and pass 0 twice. 