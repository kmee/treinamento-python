#-*- coding: utf-8 -*-

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def funcao():

    print (type(sys.argv))

    if len(sys.argv) > 1:
        print u'Hello there é', sys.argv[1]
    else:
        print 'Faltando Parametro'
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.


nome = 'Eder'

if __name__ == '__main__':
    funcao()