# Fill code

The general purpose of this program is read the keyboard. When any key is pressed, the screen must turn black. When the same key is released, the screen returns to white.

The pseudo-code is:

```
//Start with white screen
cor = white //0

// Set screen memory address pixels (start and end)
screen_address = SCREEN
pointer = screen_address
max_address = screen_address + 8192 //here 8162 it's the number of 16 bits words needed. (256*512/16)

// LOOP:
Do:
    //reset the pointer to start of screen
    pointer = screen_address

    //Read the keyboard input
    keyboard_input = KBD

    //define color based on keyboard input
    if keyboard_input > 0:
        color = -1 (black)
    else
        color = 0

     //FILL LOOP:

     while (pointer != max_address):
     //fill with black or white
     scheen[pointer] = color

     //next pixel
     pointer = pointer + 1
while(true)
```
