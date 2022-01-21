from random import *
from turtle import *
from time import  *
speed(0)
getscreen()
hideturtle()
function_output = []
#x = int(input())


#preperation
# Rysowanie wykresu

goto_pos = (-650, -325)
pu()
goto(goto_pos)
pd()

goto(-650, 325)
goto(goto_pos)
goto(650, -325)
goto(goto_pos)




def draw():


    #drawing line
    for i in range(len(function_output)):
        goto(-650+i*11,(function_output[i])/15+-325)
    pu()
    goto(goto_pos)
    pd()


def function(x):
    while True:

        if x % 2 != 0:
            x = 3 * x + 1
        else:
            x = x / 2

        function_output.append(int(x))

        if len(function_output) >= 3:
            if function_output[len(function_output) - 1] == 1:
                function_output.clear()
                break

for x in range(1000):

    x=x+1
    print(x)
    function_output.append(x)
    function(x)
sleep(5)