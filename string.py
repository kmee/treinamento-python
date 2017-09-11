
# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
    if len(sys.argv) > 1:
        print 'Hello there', sys.argv[1]

    nome = 'Ana Beatriz'
    print (nome)

    stringa = " Foi por uma gota d'agua. "

    stringb = ' Ele disse: "Foi por pouco!" .'

    stringc = 'Ele disse: "Foi por pouco,' \
        'quase deu ruim.'

    stringd = """
        Strings literais entre aspas triplas,
        podem se estender por varias linhas de texto.

        """

    print (stringa)
    print (stringb)
    print (stringc)
    print (stringd)

###############################################################

    nome = 'Ana Beatriz'
    print (nome)
    print (nome.join('!!'))
    print (nome)

    nome = '!' + nome + '!'
    print (nome)

###############################################################





# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()





