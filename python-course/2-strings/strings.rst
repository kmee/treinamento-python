Python Strings
==============

Python Strings
--------------
Python tem uma classe string default chamada "str" com muitos recursos úteis (há um módulo mais antigo chamado "string" que você não deve usar). Declarações de Strings podem ser delimitadas por aspas duplas ou simples, embora aspas simples são mais comumente usadas. Barra invertida para quebras de linhas trabalham da forma habitual tanto com aspas simples e aspas duplas citadas anteriormente - por exemplo, n '". Uma string com aspas duplas pode conter aspas simples sem qualquer problema (por exemplo," I didn't do it ") e da mesma forma uma string com aspas simples pode conter aspas duplas. A delcaração da string pode ocupar várias linhas, mas deve haver um barra invertida no final de cada linha de escape da nova linha. Strings literais entre aspas triplas, """ ou ''', pode se estender por várias linhas de texto.


.. nextslide::

Strings python são "imutáveis", o que significa que elas não podem ser alteradas depois de serem criadas (strings em Java também utilizam este estilo imutável). Sabendo que as strings não podem ser alteradas, podemos construir novas strings como  valores concatenados. Assim, por exemplo a expressão ('Hello' + 'There') concatena as strings "Hello" e "There" resultando em uma nova string "Hello There".


.. nextslide::

Caracteres em uma seqüência podem ser acessados usando a sintaxe padrão [] e, como em Java e C++, Python utiliza indexação baseada em zero, por isso, se str é 'Hello' str[1] é a letra 'e'. Se o índice estiver fora dos limites da string, o Python gerará um erro. O estilo Python (ao contrário do Perl) é parar se ele não pode dizer o que fazer, em vez de apenas retornar um valor padrão. A sintaxe útil "slice" (abaixo) também trabalha para extrair qualquer substring de uma string. A função len (string) devolve o comprimento de uma string. A sintaxe [] e a função len() trabalham em qualquer tipo de sequência - strings, lists, etc...


.. nextslide::

O Python tenta fazer suas operações funcionarem de forma consistente em diferentes tipos.
Pegadinha para o novato em Python: não use "len" como um nome de variável para evitar o bloqueio a função len(). O operador '+' pode concatenar duas strings. Observe no código abaixo que as variáveis não são pré-declarados - apenas para atribuir.

.. code-block:: python

	s = 'hi'
	print s[1]          ## i
	print len(s)        ## 2
	print s + ' there'  ## hi there


.. nextslide::

Ao contrário do Java, o '+' não converte automaticamente números ou outros tipos de forma de string. A função str() converte valores a uma forma de string para que possam ser combinados com outras strings.

.. code-block:: python

	pi = 3.14
	##text = 'The value of pi is ' + pi      ## NO, does not work
	text = 'The value of pi is '  + str(pi)  ## yes


Para números, os operadores padrão, +,/,* trabalham da maneira usual. Não há operador ++, porém, +=, -=, e outros funcionarão. Se você quiser uma divisão inteira, o correto é utilizar 2 barras - por exemplo, 6 // 5 é 1 (anterior para python 3000, uma / simples faz uma divisão int única com ints de qualquer maneira, mas a utilizar // é a melhor forma para indicar que você deseja divisão int.)

.. nextslide::
opposite of split(), joins the elements in the given list together using the string as the delimiter. 
O operador "print" imprime um ou mais itens python seguido por uma nova linha (deixe uma vírgula à direita no final dos itens para inibir a nova linha). Uma string "raw" é prefixado por um 'r' e passa todos os caracteres sem tratamento especial de barras invertidas, então r'x\nx' avalia a string length-4 'x\nx'. O prefixo 'u' permite que você escreva uma string unicode (Python tem muitos outros recursos de suporte unicode - veja a documentação abaixo).

.. code-block:: python

  raw = r'this\t\n and that'
  print raw     ## this\t\n and that
    
  multi = """It was the best of times.
  It was the worst of times."""


String Methods
--------------
Aqui estão alguns dos métodos mais comuns de strings. Um método é como uma função, mas é executada "em um objeto". Se a variável s é uma string, então o código s.lower() executa método lower() nesse objeto e retorna o resultado (esta ideia de um método de execução em um objeto é uma das ideias básicas que compõem a Programação Orientada a Objetos, POO). Aqui estão alguns dos métodos mais comuns:

* s.lower(), s.upper() -- retorna a string em minúscula ou maiúscula
* s.strip() -- retorna a string sem espaços no início e no fim
* s.isalpha()/s.isdigit()/s.isspace()... -- verifica se todas os caracteres da string correspondem ao teste

.. nextslide::

* s.startswith('other'), s.endswith('other') -- testa se a string inicia ou termina com dados de outra string
* s.find('other') -- procura dados em uma string (não procura expressão regular) e retorna o valor do primeiro caracter. Se retornar -1 o dado não foi encontrado
* s.replace('old', 'new') -- retorna uma string quando todas as ocorrências de 'old' forem subistituidas por 'new'

.. nextslide::

* s.split('delim') -- retorna uma lista de substrings separadas por um delimitador. O delimitador não é uma expressão regular, é texto puro. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. Caso não seja definido um delimitador, será utilizado por padrão os espaços entre os caracteres
* s.join(list) -- oposto do split (), junta os elementos de uma lista de dado, utilizando a string como o delimitador. Exemplo '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
* Uma busca no google por "python str" deverá levar você ao site oficial do Python, `python.org <http://docs.python.org/library/stdtypes.html#string-methods>`_ , que contém uma lista com todos os metódos que podem ser utilizados.

.. nextslide::

Python não tem um tipo de caracter separado. Em vez disso uma expressão como s[8] retorna uma string-length-1 contendo o caracter. Com essa string-length-1, os operadores ==, <=, ... fará todo o trabalho como seria de se esperar, portanto, na maior parte você não precisa saber que o Python não tem uma escala do tipo "char" separado.

String Slices
-------------
A sintaxe "slice" é uma maneira prática para se referir a sub-partes de sequências - tipicamente strings e lists. O slice s [start:end] são os elementos que começam no início e que se estende até, mas não incluindo o fim. Suponha que temos s = "Hello"

.. nextslide::

A string 'hello' com indice de letras 0 1 2 3 4 

* s[1:4] is 'ell' -- caracter começando com 1 e não exibindo o 4
* s[1:] is 'ello' -- omite o primeiro caracter (0)
* s[:] is 'Hello' -- uma cópia da string (é o jeito pythonico de copiar uma sequência como uma string ou lista)
* s[1:100] is 'ello' -- Um index que é muito grande e será truncado até o comprimento real da string

.. nextslide::

Os números de índice baseado em zero padrão dão acesso fácil a caracteres perto do início da string. Como alternativa, o Python usa números negativos para dar fácil acesso aos caracteres no final da string: s[-1] é o último caractere 'o', s[-2] é 'l' o próximo ao último caracter, e assim por diante. Números de índice negativos são contados para trás a partir do final da string:

.. nextslide::

* s[-1] is 'o' -- último caracter (1º a partir do fim)
* s[-4] is 'e' -- 4º a partir do fim
* s[:-3] is 'He' -- indo até o início mas não incluindo os últimos 3 caracteres.
* s[-3:] is 'llo' -- iniciando com o 3º caracter a partir do final e extendendo até o fim da string.

.. nextslide::

É óbvio que slices que para qualquer índice n, s[:n] + s[n:] == s. Isso funciona mesmo para n negativos ou fora dos limites. Ou dito de outra forma s[:n] e s[n:] sempre dividirão a string em duas partes, conservando todos os caracteres. Como veremos na seção lists mais tarde, slices também trabalham com listas.

String %
-------
Python tem um printf() - como facilitador para montar um string. O operador % assume um formato de string printf-type do lado esquerdo (%d int, %s string, %f/%g floating point), e os valores correspondentes em uma tupla à direita (uma tupla é feita de valores separados por vírgulas, geralmente agrupadas dentro de parênteses):

.. code-block:: python

  # % operator
  text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')

.. nextslide::

A linha acima é um metódo comprido - suponha que você quer dividi-lo em linhas separadas. Você não pode simplesmente dividir a linha após o '%' como você pode em outras linguagens, já que por padrão o Python trata cada linha como uma declaração separada (no lado positivo, é por isso que não precisa digitar ponto e vírgula em cada linha). Para corrigir isso, coloque toda a expressão em um conjunto externo de parênteses - então a expressão é permitida a abranger várias linhas. Esta técnica de códigos através de linhas trabalha com vários construtores agrupados detalhados abaixo: (),[],{}.

.. code-block:: python

	# add parens to make the long-line work:
	text = ("%d little pigs come out or I'll %s and %s and %s" %
	(3, 'huff', 'puff', 'blow down'))

i18n Strings (Unicode)
----------------------

Strings regulares do Python *não* são unicode, elas são simplesmente bytes. Para criar uma string unicode, use o prefixo 'u' na string:

.. code-block:: python

	> ustring = u'A unicode \u018e string \xf1'
	> ustring
	u'A unicode \u018e string \xf1'


A sequência de caracteres Unicode é um tipo diferente de objeto de string regular "str", mas a seqüência de caracteres Unicode é compatível (que compartilham a superclasse comum "basestring"), e as várias bibliotecas como expressões regulares funcionam corretamente se passarmos uma seqüência de caracteres Unicode em vez de uma sequência regular.

.. nextslide::

Para converter uma sequência de caracteres Unicode para bytes com uma codificação como 'utf-8', chame o método ('utf-8') na string Unicode. Indo na outra direção, a função unicode(s, encoding) converte bytes codificados para uma string unicode:

.. code-block:: python

	## (ustring from above contains a unicode string)
	> s = ustring.encode('utf-8')
	> s
	'A unicode \xc6\x8e string \xc3\xb1'  ## bytes of utf-8 encoding
	> t = unicode(s, 'utf-8')             ## Convert bytes back to a unicode string
	> t == ustring                      ## It's the same as the original, yay!
	True

.. nextslide::

O print default não funciona plenamente com strings unicode. Você pode utilizar encode() primeiro para imprimir em utf-8 ou qualquer outra. Na seção de leitura de arquivo, há um exemplo que mostra como abrir um arquivo de texto com alguns codificação e ler as strings unicode. Observe que o manuseio unicode é uma área onde Python 3000 é significativamente limpo vs. o comportamento do Python 2.x descrito aqui.

If Statement
------------

Python não  utiliza {} para incluir blocos de código para if/strings/funções etc .. Em vez disso, Python usa dois pontos (:) e recuo/espaço em branco com declarações do grupo. O teste booleano para um if não precisa estar em parênteses (grande diferença do C++/Java), e pode ter as cláusulas *elif* e *else* (mnemonic: a palavra "elif" tem o mesmo comprimento que a palavra "else").

.. nextslide::

Qualquer valor pode ser usado como um if-test. Todos os valores "zero" contam como falso: None, 0, string vazia, lista vazia, dicionário vazio. Há também um tipo booleano com dois valores: verdadeiro e falso (convertido para um int, estes são 1 e 0). Python tem as operações de comparação habituais: ==, !=, <, <=,>,>=. Ao contrário de Java e C, == está preparado para funcionar corretamente com strings. Os operadores booleanos são identificados pelas palavras *and*, *or*, *not* (Python não usa o estilo C, && ||!). Observe como cada bloco declarado de then/else começa com um : e as demonstrações são agrupados por sua identação:

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

Acho que omitindo o ":" é o meu erro de sintaxe mais comum quando se digita no tipo de código acima, provavelmente já que é uma coisa adicional para digitar vs. meus hábitos C ++ / Java. Além disso, não colocar o teste booleano em parênteses - que é um hábito C / Java. Se o código é curto, você pode colocar o código na mesma linha após ":", como este (isso se aplica a funções, loops, etc. também), embora algumas pessoas acham que é mais legível para o espaço as coisas em linhas separadas.

.. code-block:: python

	if speed >= 80: print 'You are so busted'
	else: print 'Have a nice day'


Exercício: string1.py
--------------------
