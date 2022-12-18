# Toy-car-paints-the-map
Imagine a toy car with a brush in front of it circulating in a room. The car is controlled by
python application using control flows, loops and functions. Brush in the car can be in two
different positions: above or below. When the brush is down, it paints the places where the
vehicle goes and does nothing when the brush is up.

Command Task
1 Brush down
2 Brush up
3 Turn right
4 Turn left
5 Move up to x (except the square where it is located.)
6 Jump (Jump as 3 square except the square where it is located. After jumping, the brush comes up)
7 Reverse direction ( rotates 180 degrees)
8 View the matris
0 End program (if it sees 0, it will ignore subsequent commands.)

Commands will be separated with each other by ” + ”. An exemplary command is as follows.
Commands: N (board size) +5 5+3+5 1+3+1+5 4+4+5 7+4+5 4+4+5 3+4+5 2+7+6+8+0
