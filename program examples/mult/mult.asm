// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
@i
M = 0;  // Set iterator to i

@R2
M = 0;  // Set output register to 0

(LOOP)
@i
D = M;

@R1
D = D-M;

@END
D;JEQ   // If i==R1 end the loop

@R0
D=M

@R2
M = D+M;  // Add R0 to R2

@i
M = M+1;  // Increment iterator

@LOOP
D;JMP     // Next iteration

(END)
@END      // End loop
0;JMP