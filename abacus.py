# Define a procedure my_abacus(integer) that takes a positive integer and prints a visual representation of an abacus.

def my_abacus(value):
    x= str(value)
    i = (10 - len(str(value))) 
    while i > 0:
        x = '0' + x  # Appending 0 in front of the str to make it a 10 digit value i.e.  1234 becomes 0000001234
        i = i - 1
    while i < 10:
        out = '|'
        j = 0
        while j < 10:
            if j < 5:
                out = out + '0'
            else:
                out = out + '*'
            j = j + 1
            if j == (10 - int(x[i])):
                out = out + '   '        #When count value equal to 10- integer value, print seperation. this is because reverse counting is implimented. i.e. strating counter from 10
        i = i + 1
        print out + '|'    #print 1 line. repeat 10 times for each value in the 10 digit abacus
