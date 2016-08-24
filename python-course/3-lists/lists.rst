Listas Python
=============

Listas Python
-------------

O Python tem um otimo tipo embutido de listas chamado **list**. As declarações de listas
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

Atribuições com = em listas não criam cópias. Em ves disso são criadas duas váriáveis apontando para a mesma lista em memória.

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

As decalrações Python **for** e **in** são extremamente uteis. A palavra reservada **for**
 -- for var in list -- é a maneira mais facil de percorrer os elementos de uma lista
 ( ou uma coleção ). **Não adicione ou remova itens de um iterável durante uma iteração.**

.. code-block:: python

    squares = [1, 4, 9, 16]
    sum = 0
    for num in squares:
    sum += num
    print sum  ## 30

Se você sabe o que procurar em uma lista, use o nome da variável no loop para
capturar a informação desejada, como um "num", um "nome" ou uma "url".

O termo 'in" é uma forma simples de testar se um elemento aparecer em uma lista, retornando True/False.

.. code-block:: python

    list = ['larry', 'curly', 'moe']
    if 'curly' in list:
        print 'yay'

Os termos for/in são muito utilizados em Python ao trabalhar com dados que não sejam listas,
então você deve memorizar sua sintaxe. Você pode ter o hábito vindo de outras linguagens
de iniciar manualmente as iterações em uma coleção, em python você deve usar apenas for/in.

Você pode tambem usar for/in para trabalhar com uma string. Um string atua como uma lista
com chars, então:

.. code-block:: python

    for ch in 'treinamento':
        print ch

Range
-----

A função range(n) produz uma lista de números 0, 1, ..., n-1 e range(a,b)
retorna a, a+1, ... b-1 -- até o ultimo número menos um. A combinação de um for-loop e o
metodo range() permite criarmos for numérico tradicional.

.. code-block:: python
    ## print the numbers from 0 through 99
    for i in range(100):
        print i


While Loop
----------

Python also has the standard while-loop, and the *break* and *continue* statements work as in C++ and Java, altering the course of the innermost loop. The above for/in loops solves the common case of iterating over every element in a list, but the while loop gives you total control over the index numbers. Here's a while loop which accesses every 3rd element in a list:

  ## Access every 3rd element in a list
  i = 0
  while i < len(a):
    print a[i]
    i = i + 3
List Methods

Here are some other common list methods.

list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
list.reverse() -- reverses the list in place (does not return it)
list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
Notice that these are *methods* on a list object, while len() is a function that takes the list (or string or whatever) as an argument.

  list = ['larry', 'curly', 'moe']
  list.append('shemp')         ## append elem at end
  list.insert(0, 'xxx')        ## insert elem at index 0
  list.extend(['yyy', 'zzz'])  ## add list of elems at end
  print list  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
  print list.index('curly')    ## 2

  list.remove('curly')         ## search and remove that element
  list.pop(1)                  ## removes and returns 'larry'
  print list  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
Common error: note that the above methods do not *return* the modified list, they just modify the original list.

  list = [1, 2, 3]
  print list.append(4)   ## NO, does not work, append() returns None
  ## Correct pattern:
  list.append(4)
  print list  ## [1, 2, 3, 4]
List Build Up

One common pattern is to start a list a the empty list [], then use append() or extend() to add elements to it:

  list = []          ## Start as the empty list
  list.append('a')   ## Use append() to add elements
  list.append('b')
List Slices

Slices work on lists just as with strings, and can also be used to change sub-parts of the list.

  list = ['a', 'b', 'c', 'd']
  print list[1:-1]   ## ['b', 'c']
  list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
  print list         ## ['z', 'c', 'd']
Exercise: list1.py

To practice the material in this section, try the problems in list1.py that do not use sorting (in the Basic Exercises).