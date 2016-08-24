Introdução
==========

Introduçao
----------
- Python 2.7
- Não vamos usar Python 3 =(
-

Como vai ser o curso:
---------------------

1. Mix: Teoria + Exercicios
2. Qualquer coisa, curiosidade ligada ao curso;
3. Se possível tragam algum problema do trabalho de vcs para que possamos resolver com Python.
4. Não se sintam obrigados a anotar tudo!


Material
--------
1. Como baixar
2. Como compilar o material

Origem
------

- Criada por Guido Van Rossum, Holandez;
- Em 1991 o autor publicou o codigo fonte na internet;
- Construido colaborativamente por pessoas;
- Sem nenhuma empresa por trás, sem restrições econômicas;

Python é tão especial?
----------------------

- `Brochura <http://brochure.getpython.info/media/releases/psf-python-brochure-vol.-i-final-download.pdf/>`_.
- 'Pq o python cabe na sua mente' Bruce Eckel;
- Os programadores que usam linguagens dinamicas são mais felizes;
- Excelente biblioteca padrão +230 módulos: `EN <https://docs.python.org/2.7/library/>`_
- Documentação em `Português <http://turing.com.br/pydoc/2.7/tutorial/index.html>`_
- Python package index: `pypi <https://pypi.python.org/pypi>`_
- Resolver os problemas e compartilhar esta na essência do python;

Zen python
----------
- Tim peters

::

    import this


Se seu codigo é inspirado nessas regras é pythonico
---------------------------------------------------

- Bonito é melhor que feio.
- Explícito é melhor que implícito.
- Simples é melhor que complexo.
- Complexo é melhor que complicado.
- Plano é melhor que aninhado.
- Dispersa é melhor que denso.
- Legibilidade conta.
- Casos especiais não são especiais o suficiente para quebrar as regras.
- Embora praticidade vença pureza.

.. nextslide::

- Erros nunca devem passar silenciosamente.
- A menos que explicitamente silenciados.
- Em face da ambiguidade, recuse a tentação de adivinhar.
- Deve haver um-- e de preferência apenas uma maneira --obvious para fazê-lo.
- Apesar dessa maneira pode não ser óbvio à primeira vista, a menos que você seja holandês.
- Agora é melhor do que nunca.
- Embora nunca tenha sido muitas vezes é melhor do que agora mesmo.

.. nextslide::

- Se a implementação é difícil de explicar, é uma má idéia.
- Se a implementação é fácil de explicar, pode ser uma boa idéia.
- Namespaces são uma grande idéia - vamos fazer mais desses!

Ponto de vista
--------------

Ano 2000, nos EUA, em um treinamento nos EUA, Guido apareceu na sala de aula ( ele não era professor ).
Na sessão de perguntas e respostas, alguem perguntou quais recursos de Python foram emprestados de outras linguagens.¹

Sua resposta: **"TUDO que há de bom em Python foi roubado de outras linguagens".**

O Artigo "Ensinando liniguagens de programaçao em uma era pós-Lineu":

Os "paradigmas" das linguagens de programação são um legado moribundo e tedioso da uma era que já se foi. Os designers das linguagens modernas não têm respeito por esses paradigmas, [...] eles emprestam recursos como querem.

1 - Python Fluente: Luciano Ramalho pg. 201
2 - http://cs.brown.edu/~sk/Publications/Papers/Published/sk-teach-pl-post-linnaean/

Introdução a linguagem
======================

Introdução a linguagem
----------------------

- Python é uma linguagem dinâmica e interpretada(bytecode-compiled).
- Não existem declaraçoes de tipos de variaveis, parametros, funçoes ou metodos no codigo fonte.
- Isto mantem o codigo compacto e flexivel;
- Você não precisa perder tempo esperando o codigo compilar;

O interpretador Python
----------------------

Melhor forma de se ver como um código funciona e utilizando o interpertador do python

::

    $ python

.. code-block:: python

    >>> a = 6       ## set a variable in this interpreter session
    >>> a           ## entering an expression prints its value
    6
    >>> a + 2
    8
    >>> a = 'hi'    ## 'a' can hold a string just as well
    >>> a
    'hi'
    >>> len(a)      ## call the len() function on a string
    2
    >>> a + len(a)  ## try something that doesn't work
    Traceback (most recent call last):
      File "", line 1, in
    TypeError: cannot concatenate 'str' and 'int' objects
    >>> a + str(len(a))  ## probably what you really wanted
    'hi2'
    >>> foo         ## try something else that doesn't work
    Traceback (most recent call last):
      File "", line 1, in
    NameError: name 'foo' is not defined
    >>> ^D          ## type CTRL-d to exit (CTRL-z in Windows/DOS terminal)

.. nextslide::

- Facil de experimentar variáveis e operadores;
- O interpretador também exibe as exceções;
- Python é case sensitive;
- O fim da linha marca o fim da declaração;
- Não é preciso colocar ponto e virgula no fim de cada declaração;
- Comentários começam com '#' e se extendem até o fim da linha.

Código fonte python
-------------------
O código fonte python utiliza a extensão ".py" e as extensões são chamadas de "modulos".
Por exemplo para executar o modulo python hello.py, a maneira mais facil de executa-lo é ir no sheel e digitar.

::

     $ python hello.py Kmee

O comando chama o interpretador Python para executar o código na hello.py,
passando o argumento de linha de comando "Kmee". Veja a página da `Documentação oficial <http://docs.python.org/using/cmdline/>`_
oficial sobre todas as diferentes opções que você tem ao executar Python a
partir da linha de comando.

hello.py
-----------------

.. code-block:: bash

    #!/usr/bin/env python

    # import modules used here -- sys is a very standard one
    import sys

    # Gather our code in a main() function
    def main():
        print 'Hello there', sys.argv[1]
        # Command line args are in sys.argv[1], sys.argv[2] ...
        # sys.argv[0] is the script name itself and can be ignored

    # Standard boilerplate to call the main() function to begin
    # the program.
    if __name__ == '__main__':
        main()

.. nextslide::

Executando o programa através da linha de comando:

::

    $ python hello.py Guido
    Hello there Guido
    $ ./hello.py Kmee  ## without needing 'python' first (Unix)
    Hello there Kmee

Imports, len() e argumentos de linha de comando
-----------------------------------------------

As declarações em um arquivo ou modulo python são processadas uma unica vez
durante a primeira importação do modulo em algum lugar, iniciando suas variáveis e funções.

Um modulo python pode ser executado diretamente - como fizemos acima "python hello.py Mileo" - ou pode ser
importado e utilizado em outro modulo. Quando um arquivo python é executado diretamente, uma variável especial "__name__" é atribuida ao "__main__".

É muito comum vermos o trecho de código:

.. code-block:: python

    if __name__ ==...

Para chamar a função main(), mas não quando este módulo é importado por outro modulo.

Argumentos
----------
Em em um programa Python padrão, a lista *sys.argv* contém os argumetos da linha de comando na forma padrão:

- sys.argv[0] sendo o próprio programa;
- sys.argv[1] o primeiro argumento,
- e assim vai.


len()
-----
Se você estiver na duvida com o numero de argumentos de um programa, você pode simplesmente consulta-los através da função len(sys.argv)
como fizemos ao verificar o tamanho da string.

Em geral, **len()** pode te dizer:

- Tamanho de uma string;
- Numero de elementos em uma lista, dicionário, tupla ou qualquer estrutura de dados;


Funções definidas pelo usuário
------------------------------

Funções em Python são definidas desta forma:

::

    # Defines a "repeat" function that takes 2 arguments.
    def repeat(s, exclaim):
        """
        Returns the string 's' repeated 3 times.
        If exclaim is true, add exclamation marks.
        """

        result = s + s + s # can also use "s * 3" which is faster (Why?)
        if exclaim:
            result = result + '!!!'
        return result

::

Note que todas as linhas que compoem a função ou instrução if, são agrupados pelo mesmo nível de identação.

.. nextslide::

- Também apresentamos duas maneira diferentes de se repetir strings:
    - utilizando o operador "+"
    - utilizando o operador "*" (De forma que "-" * 10 = "----------");

*OBS: Utilizar o "*" é mais rápido "+", por que * calcula o tamanho da string somente uma vez, enquanto "+" calcula a cada operação de "+"

- Ambos + e * são chamados de operadores sobrecarregados pois tem significados diferentes para numeros, strings e outros tipos de dados.

.. nextslide::

- A palavra reservada *def* definie a função com seus parametros entre parenteses e seu código identado. A primeria linha de uma função pode ser sua documentação string ("docstring") que deve descrever o que a função faz.
- O docstring pode ser uma unica linha, ou multiplas linhas como no exemplo anterior. (Com aspas triplas).
- Váriáveis definidas dentro de uma função são locais para para esta função, então o result da função anterior é separado de uma mesma váriavel result em outra função.
- Se a declaração de retorno receber um argumento, este será retornado a quem chamou a função.

.. nextslide::

Exemplo:

::

    def main():
        print repeat('Yay', False)      ## YayYayYay
        print repeat('Woo Hoo', True)   ## Woo HooWoo HooWoo Hoo!!!


Indentação
-----------
Uma caractéristica do Python é que um espaço em branco pode alterar o significado
 de um trecho de código. Um bloco lógico de declarações que compoem uma função devem
 ter todos a mesma identação, em relaçao ao identação da função ou do bloco if ou
 qualquer outro tipo de bloco. Se uma das linhas em um grupo tem uma identação
 diferente, temos um erro de sintaxe.

O uso de espaços em branco parece ser bem estranho de inicio, mas é lógico e você
acaba se acostumando muito rapido.

.. nextslide::

Evite usar TABs pois eles detonam o esquema de recuo. (Tabs significam coisas diferentes em diferentes plataformas).
Configure o seu editor para inserir espaços em vez de tabs.

Uma questão comum: "Com quantos espaços eu devo identar?

De acordo com o a PEP8, deve-se identar com 4 espaços.

PEPs
-------

O desenvolvimento de Python é conduzido amplamente através do processo Python Enhancement Proposal ("PEP"), em português Proposta de Melhoria do Python. Os PEPs são documentos de projeto padronizados que fornecem informações gerais relacionadas ao Python, incluindo propostas, descrições, justificativas de projeto (design rationales) e explicações para características da linguagem.

https://www.python.org/dev/peps/


O Código é checado em tempo de execução
---------------------------------------

O Python realiza pouca checagem ao compilar, adiando as checagens de nomes, tipos e etc. para quando a linha for executada.

Exemplo:

.. code-block:: python

    def main():
        if name == 'Guido':
            print repeeeet(name) + '!!!'
        else:
            print repeat(name)


Este codigo compila e funciona muito bem desde que o nome não seja 'Guido'. Somente
quando a aplicação tenta executar o metodo com o nome errado que um erro será exibido.

Esta é uma área em que linguagens como Java podem ter vantagens... Pois podem detectar erros deste tipo durante a compilação. Por isso é muito importante
que os testes percorram todo o trecho do codigo.

Nomes de Variáveis
------------------

Como as variáveis em Python não têm seus tipos de especificados no código-fonte,
É importante darmos nomes com significado as variáveis para lembrarmos o do que ela se trata.

Muitos erros básicos ocorrem ao esquecermos o tipo de uma variável.



As far as actual naming goes, some languages prefer underscored_parts for
 variable names made up of "more than one word," but other languages prefer
 camelCasing. In general, Python prefers the underscore method but guides
 developers to defer to camelCasing if integrating into existing Python code
 that already uses that style. Readability counts. Read more in the section on
  naming conventions in PEP 8.

As you can guess, keywords like 'print' and 'while' cannot be used as variable
 names — you'll get a syntax error if you do. However, be careful not to use
  built-ins as variable names. For example, while 'str' and 'list' may seem
  like good names, you'd be overriding those system variables. Built-ins are
  not keywords and thus, are susceptible to inadvertent use by new Python developers.

More on Modules and their Namespaces
------------------------------------

Suppose you've got a module "binky.py" which contains a "def foo()". The fully
qualified name of that foo function is "binky.foo". In this way, various Python
 modules can name their functions and variables whatever they want, and the
  variable names won't conflict — module1.foo is different from module2.foo.
  In the Python vocabulary, we'd say that binky, module1, and module2 each have
  their own "namespaces," which as you can guess are variable name-to-object bindings.

For example, we have the standard "sys" module that contains some standard
system facilities, like the argv list, and exit() function. With the statement
 "import sys" you can then access the definitions in the sys module and make
 them available by their fully-qualified name, e.g. sys.exit(). (Yes, 'sys' has a namespace too!)

::

  import sys

  # Now can refer to sys.xxx facilities
  sys.exit(0)

There is another import form that looks like this: "from sys import argv, exit".
 That makes argv and exit() available by their short names; however, we recommend
 the original form with the fully-qualified names because it's a lot easier
 to determine where a function or attribute came from.

There are many modules and packages which are bundled with a standard installation
of the Python interpreter, so you don't have to do anything extra to use them.
These are collectively known as the "Python Standard Library." Commonly used
modules/packages include:

- sys — access to exit(), argv, stdin, stdout, ...
- re — regular expressions
- os — operating system interface, file system
You can find the documentation of all the Standard Library modules and packages
at http://docs.python.org/library.

Online help, help(), and dir()
------------------------------

There are a variety of ways to get help for Python.

Do a Google search, starting with the word "python", like "python list" or "python
 string lowercase". The first hit is often the answer. This technique seems to
  work better for Python than it does for other languages for some reason.
The official Python docs site — docs.python.org — has high quality docs. Nonetheless,
 I often find a Google search of a couple words to be quicker.
There is also an official Tutor mailing list specifically designed for those
 who are new to Python and/or programming!
Many questions (and answers) can be found on StackOverflow and Quora.
Use the help() and dir() functions (see below).
Inside the Python interpreter, the help() function pulls up documentation
strings for various modules, functions, and methods. These doc strings are
 similar to Java's javadoc. The dir() function tells you what the attributes
  of an object are. Below are some ways to call help() and dir() from the
   interpreter:

help(len) — help string for the built-in len() function; note that it's "len"
not "len()", which is a call to the function, which we don't want
help(sys) — help string for the sys module (must do an import sys first)
dir(sys) — dir() is like help() but just gives a quick list of its defined
symbols, or "attributes"
help(sys.exit) — help string for the exit() function in the sys module
help('xyz'.split) — help string for the split() method for string objects.
 You can call help() with that object itself or an example of that object,
 plus its attribute. For example, calling help('xyz'.split) is the same as
 calling help(str.split).
help(list) — help string for list objects
dir(list) — displays list object attributes, including its methods
help(list.append) — help string for the append() method for list objects

