#!/usr/bin/python
"""
    - Interactive CLI program to practise multiplication tables
    - Records number of questions, right and wrong in child_name.txt 
    - Type 999 to quit
    
"""
from random import randint
import time

def askm():

    red = '\033[1;31m'
    black = '\033[1;0m'
    print "\n",'*' * 50
    print "Hi, Ready to practise your multiplication tables?"
    print "Type", red, "999", black, "to stop"
    print "*" * 50
    wrong = 0
    right = 0
    f = open('child_name.txt', 'a')
    while True:
        try:
            first = randint(2, 12)
            second = randint(2, 12)
            result = first * second
            print "{0:1d}x{1:1d} =".format(first, second)
            inp = int(raw_input('Answer ').strip())
            if inp  == 999:
                print "*" * 50
                line = "{0:2d} questions, {1:2d} right and {2}{3:2d}{4} wrong".format(right + wrong, right, red, wrong, black)
                print "You answered ", line
                fintime = time.strftime("%X %x ")
                f.write(fintime)
                f.write(line)
                f.write("\n")
                f.close()
                print "Bye and come back soon.","\n", "*" * 50, "\n"
                break
            elif int(inp) == first * second:
                right += 1
                print "correct\n"
            else:
                print "The answer is {0:1d}. Have another go!".format(first * second)
                wrong += 1
        except ValueError:
            print "Type a whole number like ", red, "4", black, "or", red, "12", black
        
if __name__ == "__main__":
    askm()


    
