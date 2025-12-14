// Advent of Code 2025 Day 1
// 0-99
// L = left, R = right
// Circle (right from 99 -> 0, left from 0 -> 99)

// To get password:
// Follow all input instructions OR
// Count # times dial is left pointing at 0 after any rotation

// Local use: gcc -o day1 "main.c"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
      // variables
      int dial = 0; // number that dial points to
      char line[4]; // current line
      // file handling
      FILE* input;
      input = fopen("input.txt", "r"); // open file in read mode

      while (input != NULL) {
            fgets(line, sizeof(line), input);
            // TO FIX: Currently gets an instruction then subsequently a new line
            if (fgets(line, sizeof(line), input) == EOF) {
                  break; // leave loop
            }
            printf("Instruction: %s\n", line); // debugging
            fseek(input, sizeof(line) - 4, SEEK_CUR);
      }
      fclose(input); // close file
      return 0;
}