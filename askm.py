#!/usr/bin/python
import math
import random
import time
def askm():
    red = '\033[1;31m'
    black = '\033[1;0m'
    print "\n",'*'*50
    print "Hi, Ready to practise your multiplication tables?"
    print "Type", red, "999", black, "to stop"
    print "*"*50
    wrong = 0
    right = 0
    f= open('child_name.txt','a')
    while True:
        first = int(math.floor(11*random.random()))+1
        second = int(math.floor(11*random.random()))+1
        result = first*second
        print "{0:1d}x{1:1d} =".format(first,second)
	try:
            inp = raw_input('Answer ')
	    int(inp)
	    if inp == '999'.strip(''):
                print "*"*50
	        line = "{0:2d} questions, {1:2d} right and \033[1;31m{2:2d}\033[0;0m wrong".format(right+wrong,right,wrong)
	        print "You answered ",line
	        fintime = time.strftime("%X %x ")
	        f.write(fintime)
	        f.write(line)
	        f.write("\n")
	       	f.close()
		print "Bye and come back soon.","\n", "*"*50, "\n"
	        break
	    elif int(inp) == first*second:
	        right+=1
	        print "correct\n"
	    else:
	        print "The answer is {0:1d}. Have another go!".format(first*second)
	        wrong+=1
	except ValueError:
		print "Type a whole number like ", red,"4", black, "or", red, "12", black

askm()


    
