Python Strings
==============

Python Strings
--------------
Python tem uma classe string default chamada "str" com muitos recursos úteis

.. code-block:: python

    nome = 'Ana Beatriz'


Uma string com **aspas duplas** pode conter **aspas simples** sem qualquer problema
e o inverso também é verdade.
Por exemplo:

.. code-block:: python

    a = " Foi por uma gota d'agua. "

    b = ' Ele disse: "Foi por pouco!"  .'

.. nextslide::

A declaração da string pode ocupar várias linhas, mas deve haver uma **barra
invertida** no final de cada linha para indicar a continuidade da nova linha.

.. code-block:: python

    c = 'Ele disse: "Foi por pouco,' \
        'quase deu ruim.'


Strings literais entre aspas triplas, """ ou ''', podem se estender por várias linhas de texto.

.. code-block:: python

    d  = """
        Strings literais entre aspas triplas,
        podem se estender por várias linhas de texto.

        """

.. nextslide::

Strings python são **"imutáveis"**, o que significa que elas não podem ser
alteradas depois de serem criadas (strings em Java também utilizam este
estilo imutável).

.. code-block:: python

    nome = 'Ana Beatriz'
    print (nome)            # 'Ana Beatriz'
    nome.join('!!')         # '!Ana Beatriz!'
    print (nome)            # 'Ana Beatriz'

Sabendo que as strings não podem ser alteradas, podemos construir novas
strings como **valores concatenados**.

.. code-block:: python

    nome = '!' nome + '!'
    print (nome)            # '!Ana Beatriz!'


.. nextslide::

Os caracteres de uma string são acessados pela sintaxe padrão **[ ]**
Como em Java e C++, Python utiliza indexação baseada em zero.

.. code-block:: python

    print (nome[0])         # A
    print (nome[1])         # n
    print (nome[2])         # a
    print (nome[3])         #


Se o índice estiver **fora** dos limites da string, o Python **gerará um erro**.

.. code-block:: python

    print (nome[11])
    IndexError: string index out of range

O estilo Python (ao contrário do Perl) **interrompe** se não pode dizer o que
fazer, **em vez de** apenas retornar um valor padrão.


.. nextslide::

O **"slice"** é uma sintaxe útil que trabalha para extrair qualquer substring de uma string.

.. code-block:: python

    nome[0:3]               # 'Ana'

A função **len** (string) devolve o comprimento de uma string.

.. code-block:: python

    len(nome)               # 11

A sintaxe **[ ]** e a função **len()** trabalham em qualquer tipo de sequência - strings, lists, etc...



.. nextslide::

O Python tenta fazer suas operações funcionarem de forma consistente em
diferentes tipos.

Pegadinha para o novato em Python: não use **"len"** como um nome
de variável para evitar o bloqueio a função **len()**.

O operador **'+'** pode concatenar duas strings.

Observe no código abaixo que diferente de outras LP's as
variáveis não são pré-declaradas - apenas para atribuir.

.. code-block:: python

	s = 'hi'
	print s[1]          ## i
	print len(s)        ## 2
	print s + ' there'  ## hi there


.. nextslide::

Ao contrário do Java, o '+' não converte automaticamente números ou outros tipos em string.

A função str() converte valores a uma forma de string para
que possam ser combinados com outras strings.

.. code-block:: python

	pi = 3.14
	##text = 'Valor de pi: ' + pi               ## Erro, não funciona
	text = 'Valor de pi: '  + str(pi)           ## concatenando duas strings
    print (text)                                ## Valor de pi: 3.14

Para números, os operadores **+**,  **-**,  **/**,  **\*** trabalham da maneira usual.



.. nextslide::

Em python não há operador **++**, porém, **+=**, **-=**, e outros funcionarão.

.. code-block:: python

    x = 12
    x += 1
    print (x)                                   ## 13


Se você quiser uma divisão inteira, o correto é utilizar 2 barras - por exemplo:

.. code-block:: python

    # python 2.7
    >>> 6/5
    1
    >>> 6.0/5.0
    1.2

.. code-block:: python

    # python 3.4
    >>> 6/5
    1.2
    >>> 6//5
    1


String Methods
--------------
Um **método** é como uma função, mas é executado "em um objeto".

Se a variável **s** é uma string (objeto da classe String), então o código **s.lower()**
executa método lower() no objeto **'s'** e retorna o resultado
(esta ideia de um método de execução em um objeto é uma das ideias básicas
que compõem a Programação Orientada a Objetos, POO). Aqui estão alguns dos
métodos mais comuns:

* **s.lower()**, **s.upper()** -- retorna a string em minúscula ou maiúscula
* **s.strip()** -- retorna a string sem espaços no início e no fim
* **s.isalpha() s.isdigit() s.isspace()**... -- verifica se todas os caracteres da string correspondem ao teste

.. nextslide::

* **s.startswith('other'), s.endswith('other')** -- testa se a string inicia ou termina com dados de outra string

* **s.find('other')** -- procura dados em uma string (não procura expressão regular) e retorna o valor do primeiro caractere. Se retornar -1 o dado não foi encontrado

* **s.replace('old', 'new')** -- retorna uma string quando todas as ocorrências de 'old' forem subistituidas por 'new'

.. nextslide::

* **s.split('delim')** -- retorna uma lista de substrings separadas por um delimitador. O delimitador não é uma expressão regular, é texto puro. Exemplo: 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. Caso não seja definido um delimitador, será utilizado por padrão os espaços entre os caracteres

* **s.join(list)** -- oposto do split (), junta os elementos de uma lista de dados, utilizando a string como o delimitador. Exemplo.: '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

* Uma busca no Google por "python str" deverá levar você ao site oficial do Python, `python.org <http://docs.python.org/library/stdtypes.html#string-methods>`_ , que contém uma lista com todos os metódos que podem ser utilizados.


.. nextslide::

Python não tem um tipo de caractere separado. Em vez disso uma expressão como
s[8] retorna uma string de tamanho 1 contendo o caractere.

Com essa string de tamanho 1, os operadores ==, <=, ... farão todo o trabalho
como seria de se esperar, portanto, na maior parte das vezes, você não precisa saber
que o Python não tem uma variável do tipo "char" separado.

String Slices
-------------
A sintaxe "slice" é uma maneira prática para se referir a sub-partes
de sequências - tipicamente strings e lists. Os slices s [start:end] são
os elementos que começam no início e que se estendem até, mas não incluindo
o fim. Suponha que temos s = "Hello"

.. image:: img/hello.png
    :align: center

.. nextslide::

A string 'hello' com índice de letras 0 1 2 3 4 

* s[1:4] is 'ell' -- caractere começando com 1 e não exibindo o 4
* s[1:] is 'ello' -- omite o primeiro caracter (0)
* s[:] is 'Hello' -- uma cópia da string (é o jeito pythonico de copiar uma sequência como uma string ou lista)
* s[1:100] is 'ello' -- Um index que é muito grande e será truncado até o comprimento real da string

.. nextslide::

Números de índice negativos são contados para trás a partir do final da string:

* s[-1] == 'o' -> último caractere (1º a partir do fim)
* s[-4] == 'e' -> 4º a partir do fim
* s[:-3] == 'He' -> indo até o início mas não incluindo os últimos 3 caracteres.
* s[-3:] == 'llo' -> iniciando com o 3º caractere a partir do final e extendendo até o fim da string.

.. nextslide::

É óbvio que slices que para qualquer índice n, s[:n] + s[n:] == s.

Isso funciona mesmo para n negativos ou fora dos limites.

Ou dito de outra forma s[:n] e s[n:] sempre dividirão a string em duas partes,
conservando todos os caracteres.

Como veremos na seção lists mais tarde, slices também trabalham com listas.

Composição de Strings
---------------------

O símbolo % é usado para indicar composição de strings com variáveis.
O '%' é chamado de marcador de posição, e indica que na posição em que foi colocado,
conterá um valor. Veja os principais tipos de marcadores suportador pelo Python:

======== ================
Marcador Tipo
======== ================
%d       Números inteiros
%s	     Strings
%f	     Números decimais
======== ================

.. code-block:: python

  # % operator
  text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')
  print (text)
  "3 little pigs come out or I'll huff and puff and blow down"


.. nextslide::

A linha acima é um metódo comprido - suponha que você quer dividi-lo em linhas
separadas. Você não pode simplesmente dividir a linha após o '%' como é possível
em outras linguagens, já que por padrão o Python trata cada linha como
uma declaração separada (no lado positivo, é por isso que não precisa
digitar ponto e vírgula em cada linha). Para corrigir isso, coloque toda
a expressão em um conjunto externo de parênteses - então a expressão é
permitida a abranger várias linhas. Esta técnica de códigos através de
linhas trabalha com vários construtores agrupados detalhados abaixo: (),[],{}.

.. code-block:: python

	# add parens to make the long-line work:
	text = ("%d little pigs come out or I'll %s and %s and %s" %
	(3, 'huff', 'puff', 'blow down'))

If Statement
------------

Python não  utiliza {} para incluir blocos de código para if/strings/funções etc ..
Em vez disso, Python usa dois pontos (:) e recuo/espaço em branco com declarações
do grupo. O teste booleano para um if não precisa estar em parênteses (grande
diferença do C++/Java), e pode ter as cláusulas *elif* e *else* (mnemonic:
a palavra "elif" tem o mesmo comprimento que a palavra "else").

.. nextslide::

Qualquer valor pode ser usado como um if-test.

Todos os valores "zero" contam como falso: None, 0, string vazia, lista vazia, dicionário vazio.

Há também um tipo booleano com dois valores: verdadeiro e falso (convertido
para um int, estes são 1 e 0).

Python tem as operações de comparação habituais: ==, !=, <, <=,>,>=.

Ao contrário de Java e C, == está preparado para funcionar corretamente com
strings.

Os operadores booleanos são identificados pelas palavras *and*, *or*, *not*

**(Python não usa o estilo C, && ||!)**.

Observe como cada bloco declarado de then/else é seguido de um":"
e as demonstrações são agrupadas por sua identação:

.. nextslide::

.. code-block:: python

  if speed >= 80:
    print 'License and registration please'
    if mood == 'terrible' or speed >= 100:
      print 'You have the right to remain silent.'
    elif mood == 'bad' or speed >= 90:
      print "I'm going to have to write you a ticket."
      write_ticket()
    else:
      print "Let's try to keep it under 80 ok?"

.. nextslide::

Omitir o ":" é o um erro comum sintaxe mais comum quando se digita o tipo de código acima,
provavelmente já que é uma coisa adicional para digitar vs. meus hábitos C ++ / Java.

Além disso, não colocar o teste booleano em parênteses - que é um hábito C / Java.

Se o código é curto, você pode colocar o código na mesma linha após ":",

Como o exemplo abaixo (isso se aplica a funções, loops, etc. também), embora algumas pessoas
achem que é mais legível para o espaço as coisas em linhas separadas.

.. code-block:: python

	if speed >= 80: print 'You are so busted'
	else: print 'Have a nice day'


Exercício: string1.py
---------------------

Download do Arquivo: :download:`string1.py <../code/basic/string1.py>`

Exercício A: Donuts

.. code-block:: python

    # Dado um número de donuts, retorne um string
    # contendo 'Number of donuts: <count>', onde <count> é o número recebido.
    # Entretanto, se o número for 10 ou mais, use a palavra 'many'
    # ao invés do contador.
    # Então donuts(5) returns 'Number of donuts: 5'
    # e donuts(23) returns 'Number of donuts: many'

Exercício B: both-ends

.. code-block:: python

    # Dada uma string s, retorne uma string constituída pelos 2 primeiros
    # e pelos dois últimos caracteres da string original,
    # então 'sprint' resulta 'spng'. Entretando, se a string tem
    # comprimento menor que 2, retorna uma string vazia.

.. nextslide::

Exercicio C: fix-start

.. code-block:: python

    # Dada uma string s, retorne uma string
    # onde todas as ocorrências do seu primeiro caracter tenha
    # sido mudada para '*', exceto o primeiro caracter propriamente.
    # Por exemplo: 'babble' resulta 'ba**le'
    # Assuma que a string tem comprimento 1 ou maior.
    # Dica: s.replace(stra, strb) retorna uma versão da string s
    # onde todas instâncias de 'stra' foram mudadas para 'strb'

Exercício D: MixUp

.. code-block:: python

    # Dadas as strings 'a' e 'b', retorne uma única string com 'a' e 'b' separados
    # por um espaço '<a> <b>', substituindo os 2 primeiros caracteres de cada string.
    # Exemplo:
    #    'mix', 'pod' -> 'pox mid'
    #    'dog', 'dinner' -> 'dig donner'
    # Assuma que 'a' e 'b' tenham comprimento 2 ou mais. 




