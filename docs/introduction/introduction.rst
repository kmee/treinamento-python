Introdução
==========

Introdução
----------
- Python 2.7
- Não vamos usar Python 3 =(

Como vai ser o curso:
---------------------

1. Mix: Teoria + Exercícios
2. Qualquer coisa, curiosidade ligada ao curso;
3. Se possível tragam algum problema do trabalho de vocês para que possamos resolver com Python.
4. Não se sintam obrigados a anotar tudo!


Material
--------
1. Como baixar
2. Como compilar o material

Origem
------

- Criada por Guido Van Rossum, Holandez;
- Em 1991 o autor publicou o código fonte na internet;
- Construído colaborativamente por pessoas;
- Sem nenhuma empresa por trás, sem restrições econômicas;

Python é tão especial?
----------------------

- `Brochura <http://brochure.getpython.info/media/releases/psf-python-brochure-vol.-i-final-download.pdf/>`_.
- 'Porque o Python cabe na sua mente' Bruce Eckel;
- Os programadores que usam linguagens dinâmicas são mais felizes;
- Excelente biblioteca padrão +230 módulos: `EN <https://docs.python.org/2.7/library/>`_
- Documentação em `Português <http://turing.com.br/pydoc/2.7/tutorial/index.html>`_
- Python package index: `pypi <https://pypi.python.org/pypi>`_
- Resolver os problemas e compartilhar esta na essência do Python;
d
Zen python
----------
- Tim peters

::

    import this


Se seu código é inspirado nessas regras é pythonico
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
- Deve haver uma -- e de preferência apenas uma -- maneira óbvia para fazê-lo.
- Apesar dessa maneira poder não ser óbvia à primeira vista, a menos que você seja holandês.
- Agora é melhor do que nunca.
- Embora nunca tenha sido muitas vezes é melhor do que agora mesmo.

.. nextslide::

- Se a implementação é difícil de explicar, é uma má idéia.
- Se a implementação é fácil de explicar, pode ser uma boa idéia.
- Namespaces são uma grande ideia - vamos fazer mais desses!

Ponto de vista
--------------

Ano 2000, nos EUA, em um treinamento nos EUA, Guido apareceu na sala de aula ( ele não era professor ).
Na sessão de perguntas e respostas, alguém perguntou quais recursos de Python foram emprestados de outras linguagens.¹

Sua resposta: **"TUDO que há de bom em Python foi roubado de outras linguagens".**

O Artigo "Ensinando linguagens de programação em uma era pós-Lineu":

Os "paradigmas" das linguagens de programação são um legado moribundo e tedioso de uma era que já se foi. Os designers das linguagens modernas não têm respeito por esses paradigmas, [...] eles emprestam recursos como querem.

1 - Python Fluente: Luciano Ramalho pg. 201
2 - http://cs.brown.edu/~sk/Publications/Papers/Published/sk-teach-pl-post-linnaean/

Introdução à linguagem
======================

Introdução à linguagem
----------------------

- Python é uma linguagem dinâmica e interpretada (bytecode-compiled).
- Não existem declarações de tipos de variáveis, parâmetros, funções ou métodos no código fonte.
- Isto mantém o código compacto e flexível;
- Você não precisa perder tempo esperando o código compilar;

O interpretador Python
----------------------

Melhor forma de se ver como um código funciona é utilizando o interpertador do python

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

- Fácil de experimentar variáveis e operadores;
- O interpretador também exibe as exceções;
- Python é case sensitive;
- O fim da linha marca o fim da declaração;
- Não é preciso colocar ponto e virgula no fim de cada declaração;
- Comentários começam com '#' e se estendem até o fim da linha.

Código fonte python
-------------------
O código fonte python utiliza a extensão ".py" e as extensões são chamadas de "módulos".
Por exemplo para executar o módulo python hello.py, a maneira mais fácil de executá-lo é ir no shell e digitar.

::

     $ python hello.py Kmee

O comando chama o interpretador Python para executar o código na hello.py,
passando o argumento de linha de comando "Kmee". Veja a página da `Documentação oficial <http://docs.python.org/using/cmdline/>`_
sobre todas as diferentes opções que você tem ao executar Python a
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

As declarações em um arquivo ou módulo python são processadas uma única vez
durante a primeira importação do módulo em algum lugar, iniciando suas variáveis e funções.

Um módulo python pode ser executado diretamente - como fizemos acima "python hello.py Mileo" - ou pode ser
importado e utilizado em outro módulo. Quando um arquivo python é executado diretamente, uma variável especial "__name__" é atribuída ao "__main__".

É muito comum vermos o trecho de código:

.. code-block:: python

    if __name__ ==...

para chamar a função main(), mas não quando este módulo é importado por outro módulo.

Argumentos
----------
Em em um programa Python padrão, a lista *sys.argv* contém os argumentos da linha de comando na forma padrão:

- sys.argv[0] sendo o próprio programa;
- sys.argv[1] o primeiro argumento,
- e assim vai.


len()
-----
Se você estiver na dúvida com o número de argumentos de um programa, você pode simplesmente consultá-los através da função len(sys.argv)
como fizemos ao verificar o tamanho da string.

Em geral, **len()** pode te dizer:

- Tamanho de uma string;
- Número de elementos em uma lista, dicionário, tupla ou qualquer estrutura de dados;


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

Note que todas as linhas que compõem a função ou instrução if, são agrupadas
pelo mesmo nível de identação.

.. nextslide::

- Também apresentamos duas maneira diferentes de se repetir strings:
    - utilizando o operador "+"
    - utilizando o operador "*" (De forma que "-" * 10 = "----------");

*OBS: Utilizar o "*" é mais rápido "+", porque * calcula o tamanho da string somente uma vez, enquanto "+" calcula a cada operação de "+"

- Ambos + e * são chamados de operadores sobrecarregados pois têm significados diferentes para números, strings e outros tipos de dados.

.. nextslide::

- A palavra reservada *def* define a função com seus parâmetros entre parênteses e seu código identado. A primeira linha de uma função pode ser sua documentação string ("docstring") que deve descrever o que a função faz.
- O docstring pode ser uma única linha, ou múltiplas linhas como no exemplo anterior. (Com aspas triplas).
- Váriáveis definidas dentro de uma função são locais para esta função, então o result da função anterior é separado de uma mesma váriavel result em outra função.
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
de um trecho de código. Um bloco lógico de declarações que compõem uma função devem
ter todos a mesma indentação, em relaçao à indentação da função ou do bloco if ou
qualquer outro tipo de bloco. Se uma das linhas em um grupo tem uma indentação
diferente, temos um erro de sintaxe.

O uso de espaços em branco parece ser bem estranho de início, mas é lógico e você
acaba se acostumando muito rápido.

.. nextslide::

Evite usar TABs pois eles detonam o esquema de recuo. (Tabs significam coisas diferentes em diferentes plataformas).
Configure o seu editor para inserir espaços em vez de tabs.

Uma questão comum: "Com quantos espaços eu devo indentar meu código?"

**De acordo com o a PEP8, deve-se indentar com 4 espaços.**

PEPs
-------

O desenvolvimento de Python é conduzido amplamente através do processo **Python Enhancement Proposal ("PEP")**, em português Proposta de Melhoria do Python.

Os PEPs são documentos de projeto padronizados que fornecem informações gerais relacionadas ao Python, incluindo propostas, descrições, justificativas de projeto (design rationales) e explicações para características da linguagem.

https://www.python.org/dev/peps/


O Código é checado em tempo de execução
---------------------------------------

O Python realiza pouca checagem ao compilar, adiando as checagens de nomes, tipos e etc. para quando a linha for executada.

Exemplo:'

.. code-block:: python

    def main():
        if name == 'Guido':
            print repeeeet(name) + '!!!'
        else:
            print repeat(name)


Este código compila e funciona muito bem desde que o nome não seja 'Guido'. Somente
quando a aplicação tenta executar o método com o nome errado que um erro será exibido.

.. nextslide::

Esta é uma área em que linguagens como Java podem ter vantagens... Pois podem detectar erros deste tipo durante a compilação. Por isso é muito importante
que os testes percorram todo o trecho do código.

Nomes de Variáveis
------------------

Como as variáveis em Python não têm seus tipos especificados no código-fonte,
é importante nomearmos as variáveis com significados que nos auxiliem a lembrar
do que se trata. Muitos erros básicos ocorrem ao esquecermos o tipo de uma variável.

Para nomes de variáveis a PEP8 recomenda o uso de variáveis de **"mais_de_uma_palavra"**
com underscore mas recomenda aos desenvolvedores a adiar alterar códigos que
utilizem a notação **camelCase.**

Como toda linguagem palavras como 'print' e 'while' não podem ser usadas como nomes de variáveis. Enquanto 'str' e 'list' podem parecer bons nomes, você estaria substituindo essas variáveis ​​do sistema. Built-ins não são palavras-chave e, portanto, são suscetíveis ao uso inadvertido por novos desenvolvedores Python.


Mais um pouco de módulos e seus Namespaces
------------------------------------------

Suponha que você criou um módulo chamado "blink.py" que contem um método "def foo()".
O nome completo desta função é "blink.foo". Desta forma, vários módulos podem ter
suas funções e variáveis da maneira que eles quiserem, e suas variáveis não
entrarão em conflito.

- module1.foo é diferente de module2.foo.

No vocabulário Python dizemos que cada módulo tem seu próprio namespace.


Que são vínculos entre nome de objetos e variáveis.

.. nextslide::

Por exemplo, se o modulo padrão "sys". Que contem algumas ferramentas como argv, exit().
Com o trecho "import sys" você então pode acessar as definições do modulo sys no seu namespace.

.. code-block:: python

  import sys

  # Now can refer to sys.xxx facilities
  sys.exit(0)

Outra forma de realizarmos importações:

.. code-block:: python

    from sys import argv, exit

Isto torna o argv e exit() disponíveis através dos seus nomes curtos.
Mas é recomendada a forma original com nomes completos (fully-qualified) pois é
muito mais simples determinar à que função pertence certo atributo.

.. nextslide::

Existem vários módulos e pacotes que são empacotados em conjunto com a instalação
do interpretador padrão do Python, de forma que você não precisa fazer mais nada
para usá-los.

Eles são conhecidos como a Biblioteca Padrão do Python ("Python Standard Library."). Módulos e pacotes inclusos:

- sys — exit(), argv, stdin, stdout, ...
- re — regular expressions
- os — interface com o sistema operacional, sistema de arquivos.

Standard Library Link: http://docs.python.org/library.

Ajuda Online, help(), and dir()
-------------------------------

Existe uma grande variedade de opções para se obter ajuda em Python!

1. Pesquisa no google inciando com python;
    1.1 Geralmente o primeiro resultado da pesquisa será a documentação oficial — docs.python.org
2. StackOverflow and Quora;
3. help()
4. dir()

Quando você estiver dentro do interpretador python, a função help() imprime o docstring
do objeto enviado com o parâmetro.

Já a função dir() imprime quais são os atributos do objeto.

.. nextslide::

Abaixo alguns exemplos:

.. code-block:: python

    help(len) # Ajuda para a função embutida len() function
    # Note que é "len", não "len()". que é uma chamada da função, algo que não queremos.
    help(sys) # help string do modulo sys (você deve antes importar o sys)
    dir(sys) # dir() é como um help() mas retorna uma pequna lista dos atributos do objeto.
    help(sys.exit) # help string para o exit(), função do modulo sys.
    help('xyz'.split) # help string do metodo split() de um objeto string 'xyz';

Você pode invocar o help() de uma instância de um objeto ou mesmo do objeto.

.. code-block:: python

    help('kmee'.split)
    a = 'abcd'
    help(a.split)
    help(str.split)
    help(list) # help string para listas;
    dir(list) # exibe os atributos das listas, incluindo os seus métodos.
    help(list.append) # help string para o método append() de uma lista.

