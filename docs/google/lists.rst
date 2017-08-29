Listas Python
=============

Listas Python
-------------

O Python tem um ótimo tipo embutido de listas chamado **list**. As declarações de listas
são escritas entre colchetes []. Listas funcionam de maneira similar aos strings, podemos usar a função len()
e acessar informações através de []. Com o primeiro elemento iniciado por 0. `(Veja a documentação oficial) <https://docs.python.org/2.7/tutorial/>`_



.. code-block:: python

      colors = ['red', 'blue', 'green']
      print colors[0]    ## red
      print colors[2]    ## green
      print len(colors)  ## 3

.. image:: img/list1.png
    :align: center

.. nextslide::

Atribuições com = em listas não criam cópias. Ao invés disso são criadas duas váriáveis apontando para a mesma lista em memória.

.. code-block:: python

    >>> colors = ['red', 'blue', 'green']
    >>> b=colors
    >>> b[0]= 'black'
    >>> colors
    ['black', 'blue', 'green']

.. image:: img/list2.png
    :align: center

.. nextslide::

- Uma lista vazia é apenas uma par de colchetes [].
- O '+' funciona ao adicionar duas listas:

.. code-block:: python

    >>> a = []
    >>> a
    []
    >>> a = ['red']
    >>> z = ['blue', 'black']
    >>> a + z
    ['red', 'blue', 'black']


FOR e IN
--------

As declarações Python **for** e **in** são extremamente úteis. A palavra reservada **for**
 -- for var in list -- é a maneira mais fácil de percorrer os elementos de uma lista
 ( ou uma coleção ). **Não adicione ou remova itens de um iterável durante uma iteração.**

.. code-block:: python

    squares = [1, 4, 9, 16]
    sum = 0
    for num in squares:
        sum += num
    print sum  ## 30

Se você sabe o que procurar em uma lista, use o nome da variável no loop para
capturar a informação desejada, como um "num", um "nome" ou uma "url".

.. nextslide::

O termo 'in" é uma forma simples de testar se um elemento aparece em uma lista, retornando True/False.

.. code-block:: python

    list = ['larry', 'curly', 'moe']
    if 'curly' in list:
        print 'yay'

Os termos for/in são muito utilizados em Python ao trabalhar com dados que não sejam listas,
então você deve memorizar sua sintaxe. Você pode ter o hábito vindo de outras linguagens
de iniciar manualmente as iterações em uma coleção, em python você deve usar apenas for/in.

Você pode também usar for/in para trabalhar com uma string. Uma string atua como uma lista
com chars, então:

.. code-block:: python

    for ch in 'treinamento':
        print ch

Range
-----

A função range(n) produz uma lista de números 0, 1, ..., n-1 e range(a,b)
retorna a, a+1, ... b-1 -- até o último número menos um. A combinação de um for-loop e o
método range() permitem criarmos o for numérico tradicional.

.. code-block:: python

    ## print the numbers from 0 through 99
    for i in range(100):
        print i


While Loop
----------
O Python também tem um laço while, e declarações de *break* and *continue* como em C++ e Java,
que alteram o curso do laço mais próximo.

Os laços anteriores com laços for/int resolvem os casos mais comuns de iteração
através de cada elemento de uma lista, já o loop while permite controle total dos índices.

Segue um loop while que acessa cada 3º elemento de uma lista:

.. code-block:: python

  ## Access every 3rd element in a list
  i = 0
  while i < len(a):
    print a[i]
    i = i + 3

List Methods
------------
Alguns métodos comuns de listas:

.. code-block:: python

    list.append(elem) # adiciona um único elemento no final de uma lista
    # Erro comum: não retorna a nova lista, apenas modifica a original
    list.insert(index, elem) # insere um elemento em um determinado index
    # movendo elementos para a direita.
    list.extend(list2) # adiciona os elementos da lista2 no final da lista
    # Usar + ou += em um lista temos um comportamento similiar ao extend().
    list.index(elem) # Procura por um elemento a partir do início da lista
    # retornando seu índice; Lança uma exceção do tipo ValueError se o
    # elemento não existir (utilize "in" para realizar a verificação s/ um ValueError).
    list.remove(elem) # Busta pelo primeiro elemento dado e o remove
    # (throws ValueError if not present)
    list.sort() # ordena uma lista in place (não retorna a mesma).
    # (A função sorted() é preferível;)
    list.reverse() # reverte a lista in place (não retorna a mesma)
    list.pop(index) # remove e retorna um elemento de um determinado index.
    # Se o index for omitido retorna o elemento mais a direita.

Existem métodos que recebem uma lista como argumento, como por exemplo o len()

.. nextslide::

.. code-block:: python

  list = ['larry', 'curly', 'moe']
  list.append('shemp')         ## append elem at end
  list.insert(0, 'xxx')        ## insert elem at index 0
  list.extend(['yyy', 'zzz'])  ## add list of elems at end
  print list  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
  print list.index('curly')    ## 2

  list.remove('curly')         ## search and remove that element
  list.pop(1)                  ## removes and returns 'larry'
  print list  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

Erro comum: Note que os métodos acima não retornam a lista modificada, eles apenas modificam a lista original.

.. code-block:: python

    list = [1, 2, 3]
    print list.append(4)   ## NO, does not work, append() returns None
    ## Correct pattern:
    list.append(4)
    print list  ## [1, 2, 3, 4]

Criação de listas
-----------------

Um padrão comum é iniciar uma lista com um par de colchetes vazios [], então usar append() ou extend() para adicionar elementos:

.. code-block:: python

  list = []          ## Start as the empty list
  list.append('a')   ## Use append() to add elements
  list.append('b')

Fatiamento de Listas
--------------------

Fatiamentos funcionam com listas da mesma forma que strings, e podem ser usados para modificar sub-partes de uma lista.

.. code-block:: python

  list = ['a', 'b', 'c', 'd']
  print list[1:-1]   ## ['b', 'c']
  list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
  print list         ## ['z', 'c', 'd']


Exercício: list1.py
-------------------
Para praticarmos o material desta sessão, tente os problemas do arquivo list1.py que não usam ordenação (nos exercícios básicos).

Download do Arquivo: :download:`list1.py <../code/basic/list1.py>`

Exercício A: match-ends

.. code-block:: python

    # Dada uma lista de strings, retorne a quantidade de strings
    # cujo tamanho seja 2 ou maior e seu primeiro e último
    # caracter sejam iguais.
    # Obs: Python não possui o operador ++,  mas  += funciona
