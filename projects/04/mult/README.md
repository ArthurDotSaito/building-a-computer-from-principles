# Mult code

The general purpose of this program is simply multiply two values. Here, we multiply the R0 and R1 values, storing the result on R2. The program do this summing R1 to R2, R0 times. If R0 or R1 were zero, the program end.

The pseudo-code is something like:

```
// Init R2 with zero.
R2 = 0

// Load the entry value R0 into D.
D = R0

// If D (or R0) was zero, jump to END.
If D == 0, goto END

// Load the entry value R1 into D.
D = R1

// If D (or R1) was zero, jump to END.

LOOP:
    // Load the entry value R1 into D.
    D = R1

    //Add the value D (R1) to the R2 value.
    R2 = R2 + D

    //Decrement R0
    R0 = R0 -1

    //If R0 was zero, jump to END:
    If RO == 0, goto END

    //Loop again
    goto LOOP

END;

```

The first lines of code just load variables into memory slots.

the LOOP is the part of the code which do the multiplitication, in fact. The loop performs addition of the value in R1 to the value in R2 a number of times equal to the value in R0. Essentially, you are performing multiplication through successive additions.
Example: 4 x 4 is nothing more than perform 4 + 4 + 4. And is equal 16.

So, how the loop works:

- Load and Add: First, the loop loads the value of R1 into the temporary variable D and then adds this value to R2. This action is equivalent to R2 = R2 + R1.

- Decrement and Exit Condition: After each addition, the value in R0 (which determines how many times the loop should be executed) is decremented by 1 (R0 = R0 - 1). Then, it is checked whether R0 has reached zero, which would indicate that the loop must be terminated. If R0 is zero, the program jumps to the END label, exiting the loop.

- Repetition: If R0 is not zero, the program jumps back to the beginning of the loop (LOOP), repeating the addition and decrement process.
