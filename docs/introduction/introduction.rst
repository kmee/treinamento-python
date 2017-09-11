.. -*- coding: utf-8 -*-

Introdução
==========

Introdução
----------
- Python  2.7
- Não vamos usar Python 3 =(

Como vai ser o curso:
---------------------
1. Mix: Teoria + Exercícios
2. Não se sintam obrigados a anotar tudo!

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

- `Case Studies & Success Stories <http://brochure.getpython.info/media/releases/psf-python-brochure-vol.-i-final-download.pdf/>`_.
- "Porque o Python cabe na sua mente" `Bruce Eckel <https://en.wikipedia.org/wiki/Bruce_Eckel>`_,
    - Autor de livros especializados em Java e C++, `que estava apaixonado pelo Python; <https://pt.slideshare.net/didip/why-i-love-python>`_
- Excelente biblioteca padrão +230 `módulos <https://docs.python.org/2.7/library/>`_ (EN)
- Documentação em `Português <http://turing.com.br/pydoc/2.7/tutorial/index.html>`_
- Resolver problemas e compartilhar esta na essência do Python!
    Python package index: `pypi <https://pypi.python.org/pypi>`_ (repositório de softwares)

.. code-block:: bash

    $ pip install nomedomodulo

Zen python - Tim Peters
-----------------------

Nada mais é do que uma série de filosofias escritas pelo criador da linguagem Python.

**Se seu código é inspirado nessas regras é pythonico.**

`Zen Python <https://en.wikipedia.org/wiki/Zen_of_Python>`_.

`Zen Python pt-BR <https://zenorocha.com/licoes-aprendidas-com-o-mundo-python>`_.

Easter Egg ;)

.. code-block:: python

    >>> import this




.. nextslide::

- Bonito é melhor que feio.
- Explícito é melhor que implícito.
- Simples é melhor que complexo.
- Complexo é melhor que complicado.
- Plano é melhor que aninhado.
- Dispersa é melhor que denso.
- Legibilidade conta.

.. nextslide::

- Casos especiais não são especiais o suficiente para quebrar as regras.
- Embora praticidade vença pureza.
- Erros nunca devem passar silenciosamente.
- A menos que explicitamente silenciados.
- Em face da ambiguidade, recuse a tentação de adivinhar.
- Deve haver uma -- e de preferência apenas uma -- maneira óbvia para fazê-lo.

.. nextslide::

- Apesar dessa maneira poder não ser óbvia à primeira vista, a menos que você seja holandês.
- Agora é melhor do que nunca.
- Embora nunca tenha sido muitas vezes é melhor do que agora mesmo.
- Se a implementação é difícil de explicar, é uma má idéia.
- Se a implementação é fácil de explicar, pode ser uma boa idéia.
- Namespaces são uma grande ideia - vamos fazer mais desses!


Introdução à linguagem
======================

Introdução à linguagem
----------------------

- Python é uma linguagem **interpretada** (bytecode-compiled).
- Tipagem **dinâmica** (não existem declarações de tipos de variáveis, parâmetros, funções)
- Reduzida utilização de **caracteres** especiais (vírgula, dois pontos, ponto e vírgula)
- **Modular** (vasta coleção de módulos que podem ser utilizados como base para sua aplicação, Alguns desses módulos implementam manipulação de arquivos, chamadas do sistema, sockets, e até mesmo acesso a bibliotecas de construção de interfaces gráficas, como Tk)
- **Código compacto, legível e flexível**;

O interpretador Python
----------------------

Melhor forma de se ver como um código funciona é utilizando o interpertador do python

::

    $ python

.. code-block:: python

    >>> a = 6       ## Seta uma variável na sessão do interpretador
    >>> a           ## Entrando com uma expressão o interpretador imprime o resultado
    6
    >>> a + 2
    8
    >>> a = 'hi'    ## 'a' pode ser uma string em seguida
    >>> a
    'hi'
    >>> len(a)      ## chamando a função len() da string
    2
    >>> a + len(a)  ## Tente algo que não funcione
    Traceback (most recent call last):
      File "", line 1, in
    TypeError: cannot concatenate 'str' and 'int' objects
    >>> a + str(len(a))  ## provavelmente o que você queria
    'hi2'
    >>> foo         ## Tente algo que nao esteja definido
    Traceback (most recent call last):
      File "", line 1, in
    NameError: name 'foo' is not defined
    >>> ^D          ## Pressione CTRL-d para sair (CTRL-z em Windows/DOS terminal)



.. nextslide::

- Fácil de experimentar variáveis e operadores;
- O interpretador também exibe as exceções;
- Python é case sensitive;
- O fim da linha marca o fim da declaração;
- Não é preciso colocar ponto e virgula no fim de cada declaração;
- Comentários começam com '#' e se estendem até o fim da linha.

O IPython
---------

Interpretador com recursos embutidos que facilitam o dia-a-dia.

.. code-block:: bash

    $ sudo pip install ipython
    $ ipython
    $ In [1]:

- Auto-Complete
- Execução de comandos de sistema (ls -l)
- Autoindentação
- Interface Web:  (notebook)
- Histórico
- Ex.: '_' (underline) resultado do último comando.
- Execução de programas Python: com apenas um comando, é possível executar um arquivo Python dentro do iPython.
- Ex.: %run arquivo.py



hello.py
-----------------

.. code-block:: bash

    #!/usr/bin/env python

    # import dos modulos são feitos aqui -- sys é um modulo muito comum
    import sys

    # Reúna o nosso código em uma função main()
    def main():
        print 'Hello there', sys.argv[1]
        # Os argumentos da linha de comando estão em sys.argv[1], sys.argv[2] ...
        # sys.argv[0] é o próprio nome do script

    # Definindo uma variavel simples
    nome = 'Ana Beatriz'

    # Forma padrão para chamar a função main para iniciar o programa
    if __name__ == '__main__':
        main()


Código fonte python
-------------------
O código fonte python utiliza a extensão ".py" e as extensões são chamadas de "módulos".

Por exemplo para executar o módulo python hello.py, a maneira mais fácil de executá-lo é ir no shell e digitar.

::

     $ python hello.py Kmee

O comando citado, inicializa o interpretador Python para executar o módulo/arquivo hello.py,

A string "Kmee" funciona como argumento de linha de comando.

Veja a página da `Documentação oficial <http://docs.python.org/using/cmdline/>`_
sobre todas as diferentes opções que você tem ao executar Python a partir da linha de comando.


.. nextslide::

|

Executando o programa através da linha de comando:

|

::

    $ python hello.py Guido
    Hello there Guido
    $ ./hello.py Kmee  ## without needing 'python' first (Unix)
    Hello there Kmee


Argumentos de linha de comando
-----------------------------------------------

As declarações em um arquivo ou módulo python são processadas uma única vez
durante a primeira importação do módulo em algum lugar, iniciando suas variáveis e funções.

Um módulo python pode ser executado diretamente - como fizemos acima "python hello.py Carol" - ou pode ser
importado e utilizado em outro módulo. Quando um arquivo python é executado diretamente, uma variável especial "__name__" é atribuída ao "__main__".

É muito comum vermos o trecho de código:

.. code-block:: python

    if __name__ == '__main__':
        pass

para chamar a função main(), mas não quando este módulo é importado por outro módulo.

Argumentos
----------
Em em um programa Python padrão, a lista *sys.argv* contém os argumentos da linha de comando na forma padrão:

- sys.argv[0] sendo o próprio nome do arquivo programa;
- sys.argv[1] o primeiro argumento,
- sys.argv[2] o segundo argumento,
- e assim por diante.


len()
-----
Se você estiver na dúvida com o número de argumentos de um programa, você pode simplesmente consultá-los através da função len(sys.argv)
como fizemos ao verificar o tamanho da string.

Em geral, **len()** pode te dizer:

- Tamanho de uma string;
- Número de elementos em uma lista, dicionário, tupla ou qualquer estrutura de dados;


Interpretador Python Interativo
--------------------------------

Chama o interpretador python processando o modulo do parâmetro, e continua com
a sessão do interpretador aberta.

.. code-block:: shell

    $ ipython -i hello.py
    $ python -i hello.py

- Variáveis que foram definidas no arquivo hello.py continuam disponíveis na sessão
- É possível interagir com a sessão

.. code-block:: python

    >>> nome
    'Ana Beatriz'


Funções definidas pelo usuário
------------------------------

Funções em Python são definidas desta forma:

::

    # Define a função 'repetidor' que espera 2 argumentos.
    def repetidor(s, exclamacao):
        """
        Retorna a string 's' repetida 3 vezes.
        Se 'exclamacao' for true, adiciona o marcador de exclamacao.
        """

        result = s + s + s # você pode também usar a notação "s * 3"
        if exclaim:
            result = result + '!!!'
        return result

Note que todas as linhas que compõem a função ou instrução if, são agrupadas
pelo mesmo nível de identação.

.. nextslide::

- Também apresentamos duas maneira diferentes de se repetir strings:
    - utilizando o operador "+"
    - utilizando o operador "*" (De forma que "-" * 10 = "----------");

\*OBS: Utilizar o "\*" é mais rápido do que o "+", porque * calcula o tamanho da string somente uma vez, enquanto "+" calcula a cada operação de "+"

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
do objeto enviado como parâmetro.

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

