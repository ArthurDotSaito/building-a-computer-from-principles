// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

@color
M=0

@SCREEN
D=A

@pointer
M=D

@8192
D=A+D

@maxaddress
M=D

(LOOP)
    @SCREEN
    D=A

    @pointer
    M=D

    @KBD
    D=M

    @BLACK
    D;JGT

    @WHITE
    0;JMP

    (BLACK)
        @color
        M=-1

        @FILL
        0;JMP

    (WHITE)
        @color
        M=0

        @FILL
        0;JMP

    (FILL)
        @pointer
        D=M

        @maxaddress
        D=M-D

        @LOOP
        D;JEQ

        @color
        D=M

        @pointer
        A=M
        M=D

        @pointer
        M=M+1

        @FILL
        0;JMP
    
(END)
0;JMP