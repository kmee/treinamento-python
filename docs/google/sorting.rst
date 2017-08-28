Sorting
=======

Python Sorting
--------------

A maneira mais fácil de classificar um resultado é com a função sorted(list),
que recebe uma lista e retorna uma nova lista com os elementos na ordem de
classificação. A lista original não é alterada.

.. code-block:: python

	a = [5, 1, 4, 3]
	print sorted(a)  ## [1, 3, 4, 5]
	print a  ## [5, 1, 4, 3]

.. nextslide::

É mais comum passar uma lista para a função sorted(), mas na verdade ele pode
tomar como entrada qualquer tipo de coleção iterável. O antigo método
list.sort() é uma alternativa detalhada abaixo. A função sorted() parece
mais fácil de usar em comparação com sort(), então eu recomendo o uso da
função sorted().

A função sorted() pode ser personalizada com argumentos opcionais. O argumento
opcional reverse=True do sorted(), por exemplo, sorted(list, reverse=True),
retorna os valores ao contrário.

.. code-block:: python

  strs = ['aa', 'BB', 'zz', 'CC']
  print sorted(strs)  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
  print sorted(strs, reverse=True)   ## ['zz', 'aa', 'CC', 'BB']

Custom Sorting With key=
------------------------

Para classificação personalizada mais complexa, a função sorted() recebe um
"key=" opcional que especifica uma função "key" que transforma cada elemento
antes de comparação. A função key recebe 1 valor por parâmetro e retorna 1 outro valor valor, sendo este o "proxy", utilizado para as comparações com o sorted.

Por exemplo, com uma lista de strings, especificando key=len (construído com
a função len()) classifica as strings pelo comprimento, do mais curto para o
mais longo. O sorted chama len() para cada string para obter a lista de valores
de comprimento proxy, e os tipos com esses valores de proxy.

.. code-block:: python

  strs = ['ccc', 'aaaa', 'd', 'bb']
  #calling sorted with key=len
  print sorted(strs, key=len)  ## ['d', 'bb', 'ccc', 'aaaa']

.. nextslide::

.. image:: img/sorted-key.png
    :align: center

.. nextslide::

Outro exemplo, especificar "str.lower" como a função chave é uma maneira de forçar a triagem para o mesmo tratamento de letras maiúsculas e minúsculas:

.. code-block:: python

  ## "key" argument specifying str.lower function to use for sorting
  print sorted(strs, key=str.lower)  ## ['aa', 'BB', 'CC', 'zz']

Você também pode passar em sua própria MyFn como a função chave, como:

.. code-block:: python

  ## Say we have a list of strings we want to sort by the last letter of the string.
  strs = ['xc', 'zb', 'yd' ,'wa']

  ## Write a little function that takes a string, and returns its last letter.
  ## This will be the key function (takes in 1 value, returns 1 value).
  def MyFn(s):
    return s[-1]

  ## Now pass key=MyFn to sorted() to sort by the last letter:
  print sorted(strs, key=MyFn)  ## ['wa', 'zb', 'xc', 'yd']

.. nextslide::

Para usar key= custom sorting, lembre-se de que você deve fornecer uma função que
receba um valor e retorne o valor proxy para orientar a classificação.
Há também um argumento opcional "cmp=cmpFn" para o sorted() que especifica
uma função de comparação de dois argumentos que leva dois valores da lista
e retorna negativo/0/positiva para indicar a sua ordenação. A função de
comparação default para strings, inits, ... é cmp(a, b), então, você pode
chamar quantas vezes quiser a função cmp() no seu comparador personalizado.
O mais recente um argumento key= é geralmente preferível.

sort() method
-------------
Como uma alternativa para o método sorted(), o metódo sort() em uma lista
classifica seus dados em ordem crescente, por exemplo, list.sort().
O método sort() altera a lista subjacente e retorna None, use-o desta maneira:

.. code-block:: python

    alist.sort () ## correta
    alist = blist.sort () ## NO incorreto, sort () retorna None

A descrição acima é um equívoco muito comum com sort() - que *não retorna* a
lista ordenada. O método sort() deve ser chamado em uma lista; ele não funciona
em qualquer coleção enumerada (mas a função sorted() acima funciona em
qualquer condição). O método sort() antecede a função sorted(), então
você provavelmente vai vê-lo em códigos antigos. O método sort() não precisa
criar uma nova lista, por isso pode ser um pouco mais rápido no caso em que
os elementos a serem classificados já estão em uma lista.

Tuples
------
Uma tuple é um agrupamento de elementos de tamanho fixo, tais como um (x, y) de
coordenadas. Tuples são como listas, exceto que elas são imutáveis e não mudam de tamanho (tuples não são estritamente imutáveis desde que um dos elementos contidos possa ser mutável). Tuples desempenham um tipo de papel "struct" em Python - uma maneira conveniente para passar em torno de uma pequena lógica, tamanhos fixos de valores. Uma função que precisa retornar vários valores pode simplesmente retornar uma tuple dos valores. Por exemplo, se eu quisesse ter uma lista de coordenadas 3-D, a representação python natural seria uma lista de tuples, onde cada tuple é tamanho 3 segurando um (x,y,z) do grupo.

.. nextslide::

Para criar uma tuple, basta listar os valores entre parênteses separados por vírgulas. Uma tuple "vazio" é apenas um par vazio de parênteses. Acessar os elementos de uma tuple é como uma lista - len(),[], for, in, etc. Todos funcionam da mesma forma.

.. code-block:: python

  tuple = (1, 2, 'hi')
  print len(tuple)  ## 3
  print tuple[2]    ## hi
  tuple[2] = 'bye'  ## NO, tuples cannot be changed
  tuple = (1, 2, 'bye')  ## this works


Para criar um tamanho tuple size-1, o único elemento da tuple deve ser seguido por uma vírgula.

.. code-block:: python

  tuple = ('hi',)   ## size-1 tuple

.. nextslide::

É um caso engraçado na sintaxe, mas a vírgula é necessária para distinguir a tuple do caso de colocar uma expressão entre parênteses. Em alguns casos, você pode omitir o parêntese e o Python vai ver a partir das vírgulas que você pretende criar uma tuple.

Atribuindo uma tuple a uma tuple de tamanho idêntico de nomes de variáveis atribui todos os valores correspondentes. Se as tuples não são do mesmo tamanho, ele lança um erro. Este recurso funciona para listas também.

.. code-block:: python

  (x, y, z) = (42, 13, "hike")
  print z  ## hike
  (err_string, err_code) = Foo()  ## Foo() returns a length-2 tuple


List Comprehensions (optional)
------------------------------

List comprehensions (Compreensão de listas) é um recurso mais avançado que é bom para alguns casos, mas não é necessário para os exercícios e não é algo que você precisa saber em primeiro lugar. A compreensão de lista é uma forma compacta de escrever uma expressão que se expande para uma lista inteira. Suponha que temos uma lista nums [1, 2, 3], aqui é mostrada como a compreensão de listas para computar uma lista de seus quadrados [1, 4, 9]:

.. code-block:: python

  nums = [1, 2, 3, 4]

  squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]


.. nextslide::

A sintaxe é [ expr for var in list ] - o "for var in list" parece um for-loop regular, mas sem os dois pontos (:). O expr à sua esquerda é avaliada uma vez para cada elemento para dar os valores para a nova lista. Aqui está um exemplo com strings, em que cada string é alterada para maiúsculas com '!!!':

.. code-block:: python

  strs = ['hello', 'and', 'goodbye']

  shouting = [ s.upper() + '!!!' for s in strs ]
  ## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']


Você pode adicionar um caso de teste para a direita do for-loop para estreitar o resultado. O caso de teste é calculado para cada elemento, incluindo apenas os elementos em que o teste é verdadeiro.

.. code-block:: python

  ## Select values <= 2
  nums = [2, 8, 1, 6]
  small = [ n for n in nums if n <= 2 ]  ## [2, 1]

  ## Select fruits containing 'a', change to upper case
  fruits = ['apple', 'cherry', 'bannana', 'lemon']
  afruits = [ s.upper() for s in fruits if 'a' in s ]
  ## ['APPLE', 'BANNANA']

Exercício: list1.py
------------------
Para praticarmos o material desta sessão, tente agora os problemas do arquivo list1.py que utilizam ordenação.

Exercício B: front-x

.. code-block:: python

    # Dada uma lista de strings, retorne uma lista com as strings
    # ordenadas, agrupando todas as strings que começam com 'x' primeiro.
    # Exemplo: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] resulta em
    # ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
    # Dica: isso pode ser feito criando-se 2 listas e ordenando-as antes
    # de combiná-las

Exercício C: sort-last

.. code-block:: python

    # Dada uma lista de tuples não-vazias, retorne uma lista ordenada crescente
    # pelo último elemento da tuple.
    # Exemplo: [(1, 7), (1, 3), (3, 4, 5), (2, 2)] resulta em
    # [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    # Dica: use um método key= para extrair o último elemento de cada tupla.


