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
M = 0;  // Initialise color with white


@SCREEN
D = A;
@address
M = D;

@24575
D = A
@limit
M = D

(DRAW)  // Draw loop fills the screen with the value store in @color
@color
D = M
@address
A = M
M = D

@address
M = M+1
D = M

@limit
D = M-D

@DRAW
D;JGE

@LOOP
0;JMP   // Loop the whole program