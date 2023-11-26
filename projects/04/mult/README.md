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
