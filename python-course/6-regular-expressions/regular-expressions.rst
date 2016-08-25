Expressões Regulares
====================

Expressões Regulares
--------------------

As expressões regulares são uma linguagem poderosa para a buscas de padrões de texto. Esta página dá uma introdução básica à expressões regulares suficientes para os nossos exercícios Python e mostra como expressões regulares trabalham em Python. 

O módulo Python "re" oferece suporte a expressões regulares.

Em Python uma pesquisa de expressões regulares são tipicamente escritas como:

.. code-block:: python

  match = re.search(pat, str)

.. nextslide::

O método re.search() busca um padrão de expressões regulares e strings e realiza a busca dentro da string. Se a pesquisa for bem sucedida, search() retorna um objeto com dados ou None caso contrário. Portanto, a busca é geralmente seguida imediatamente por uma instrução if para testar se a busca bem-sucedida, como mostrado no exemplo a seguir que procura o padrão 'word:' seguido por 3 letras (detalhes abaixo):

.. code-block:: python

	str = 'an example word:cat!!'
	match = re.search(r'word:\\w\\w\\w', str)
	# If-statement after search() tests if it succeeded
  	if match:                      
    	print 'found', match.group() ## 'found word:cat'
  		else:
    	print 'did not find'

.. nextslide::

O código match = re.search(pat, str) armazena o resultado da pesquisa em uma variável chamada "match". Em seguida, a instrução if testa o match -- Se for verdadeiro o resultado da busca e match.group() será o texto correspondente (por exemplo, 'word:cat'). Caso contrário, se a resultado é falso (Nada para ser mais específico), então não houve sucesso na busca, e não há nenhum texto correspondente.

O 'r' no início da string padrão designa uma string python "row" que passa por barras invertidas sem mudança que é muito útil para expressões regulares (Java precisa deste recurso). 

Eu recomendo que você sempre escrever strings com o 'r'.

Padrões básicos
---------------

O poder das expressões regulares é que eles podem especificar padrões, não apenas caracteres fixos. Aqui estão os padrões mais básicos que correspondem a caracteres individuais:

* a,X,9, <- caracteres ordinários apenas correspondem a eles mesmos. Os meta-caracteres que não correspondem a sí próprio, porque eles têm significados especiais são eles: . ^ $ * +? {[] \\ | () (detalhes abaixo)
* . . (a period) - corresponde a qualquer caractere único exceto nova linha '\\n'
* \\w - (w minúsculo) corresponde a um único caractere de texto: uma letra ou dígito ou underline [a-zA-Z0-9_]. \\W (W maiúsculo) corresponde a qualquer caractere sem letras, dígitos ou underline.

.. nextslide::

* \\b - limite entre palavra e não-palavra
* \\s - (s minúsculo) corresponde a um único espaço em branco - espaço, nova linha, retorno/return, tab, form [\\n\\r\\t\\f]. \\S (S maíusculo) corresponde a qualquer caractere sem espaço em branco.
* \\t,\\n,\\r - tab, nova linha, retorno/return
* \\d - dígitos decimais [0-9] (alguns utilitários regex mais velhos não suportam mais \\d, mas todos suportam \\w e \\s)

.. nextslide::

* ^ = Começar, $ = end - coincidir com o início ou o fim da string
* \\ - Inibir a "excepcionalidade" de um caracter. Assim, por exemplo, usar \\. para coincidir com um período ou \\ para coincidir com uma barra. Se você não tem certeza se um caracter tem um significado especial, como '@', você pode colocar uma barra na frente dele, \\@, para ter certeza que é tratada apenas como um caracter.

Exemplos Básicos
----------------
Piada: what do you call a pig with three eyes? piiig!

As regras básicas de pesquisa de expressão regular dentro de uma string são:

* A busca prossegue através da string do início ao fim, parando na primeira correspondência encontrada
* Todo o padrão deve ser correspondido, mas não toda a string
* Se ``match = re.search(pat, str)`` for bem sucedida, o resultado é Nenhum e em particular match.group() é o texto correspondente

.. nextslide::

.. code-block:: python

  ## Search for pattern 'iii' in string 'piiig'.
  ## All of the pattern must match, but it may appear anywhere.
  ## On success, match.group() is matched text.
  match = re.search(r'iii', 'piiig') =>  found, match.group() == "iii"
  match = re.search(r'igs', 'piiig') =>  not found, match == None

  ## . = any char but \\n
  match = re.search(r'..g', 'piiig') =>  found, match.group() == "iig"

  ## \\d = digit char, \\w = word char
  match = re.search(r'\\d\\d\\d', 'p123g') =>  found, match.group() == "123"
  match = re.search(r'\\w\\w\\w', '@@abcd!!') =>  found, match.group() == "abc"

.. nextslide::

Repetição
---------
As coisas ficam mais interessantes quando você usa + e * para especificar a repetição do padrão

* \\+ : 1 ou mais ocorrências do padrão à sua esquerda, por exemplo, 'i+' = um ou mais 'i'
* \\* : 0 ou mais ocorrências do padrão à sua esquerda
* \\? : jogo 0 ou 1 ocorrências do padrão à sua esquerda

Leftmost & Largest
------------------

Em primeiro lugar a procura encontra regra leftmost por padrão e, segundo ele tenta usar o máximo da cadeia possível - Exemplo: + e * vão tão longe quanto possível (a + e * são conhecidos como "gananciosos").

Exemplos de repetições

.. code-block:: python

  ## i+ = one or more i's, as many as possible.
  match = re.search(r'pi+', 'piiig') =>  found, match.group() == "piii"

  ## Finds the first/leftmost solution, and within it drives the +
  ## as far as possible (aka 'leftmost and largest').
  ## In this example, note that it does not get to the second set of i's.
  match = re.search(r'i+', 'piigiiii') =>  found, match.group() == "ii"

  ## \\s* = zero or more whitespace chars
  ## Here look for 3 digits, possibly separated by whitespace.
  match = re.search(r'\\d\\s*\\d\\s*\\d', 'xx1 2   3xx') =>  found, match.group() == "1 2   3"
  match = re.search(r'\\d\\s*\\d\\s*\\d', 'xx12  3xx') =>  found, match.group() == "12  3"
  match = re.search(r'\\d\\s*\\d\\s*\\d', 'xx123xx') =>  found, match.group() == "123"

  ## ^ = matches the start of string, so this fails:
  match = re.search(r'^b\\w+', 'foobar') =>  not found, match == None
  ## but without the ^ it succeeds:
  match = re.search(r'b\\w+', 'foobar') =>  found, match.group() == "bar"


Exemplos de emails
------------------
Suponha que você queira encontrar o endereço de e-mail dentro do string 'xyz alice-b@google.com purple monkey' . Iremos utilizar essa string como um exemplo de execução para demonstrar mais recursos de expressões regulares. Aqui está uma tentativa usando o padrão de r'\\w+@\\w+':

.. code-block:: python

  str = 'purple alice-b@google.com monkey dishwasher'
  match = re.search(r'\\w+@\\w+', str)
  if match:
    print match.group()  ## 'b@google'


A pesquisa não obteu todo o endereço de e-mail, neste caso, porque o \\w não corresponde ao '-' ou '.' no endereço. Vamos corrigir isso usando a expressão regular apresenta abaixo.

Square Brackets
---------------
Square brackets (colchetes) pode ser usado para indicar um conjunto de caracteres, então [abc] combina 'a' ou 'b' ou 'c'. Os códigos \\w, \\s etc trabalham dentro de colchetes também com a única exceção que ponto (.) significa apenas um ponto literalmente. Para o problema de e-mails, os colchetes são uma maneira fácil de adicionar '.' e '-' para o conjunto de caracteres que podem aparecer ao redor do @ com a expressão r'[\\w.-]+@[\\w.-]+' para obter todo a e-mail:

.. code-block:: python

  match = re.search(r'[\\w.-]+@[\\w.-]+', str)
  if match:
    print match.group()  ## 'alice-b@google.com'

(Mais recursos de colchetes) - Você também pode usar um traço para indicar um intervalo, para isso [a-z] corresponde a todas as letras minúsculas. Para usar um hífen sem indicar um intervalo, basta colocar um hífen no final da string, por exemplo, [abc-]. Um chapéu (^) no início de um conjunto de colchetes inverte a operação, então [^ab] significa qualquer caractere exceto 'a' ou 'b'.

Group Extraction
----------------

O recurso de "grupo" de uma expressão regular permite escolher partes do texto correspondente. Suponha que para o problema de e-mails que queremos extrair o nome do usuário e o domínio separadamente. Para fazer isso, adicionar parênteses () em torno do nome de usuário e do domínio, como este: r'([\\w.-]+)@([\\w.-]+)'. 

Neste caso, o parêntese não muda o que a busca irá buscar, em vez disso, estabelecerá "grupos" lógicos dentro do texto a ser buscado. Em uma busca com sucesso, match.group(1) é o texto de partida correspondente ao primeiro parêntese esquerdo, e match.group(2) é o texto correspondente ao segundo parêntese esquerdo. O match.group() puro retornará o texto completo.

.. code-block:: python

  str = 'purple alice-b@google.com monkey dishwasher'
  match = re.search('([\\w.-]+)@([\\w.-]+)', str)
  if match:
    print match.group()   ## 'alice-b@google.com' (the whole match)
    print match.group(1)  ## 'alice-b' (the username, group 1)
    print match.group(2)  ## 'google.com' (the host, group 2)


.. nextslide::

Um fluxo de trabalho comum com expressões regulares é que você escreve um padrão para as coisas que você está procurando, adicionando grupos de parênteses para extrair as partes que deseja.

findall
-------

findall() é provavelmente a função mais poderosa do módulo de re. Acima usamos re.search() para encontrar o primeiro dado de uma busca. findall() localiza *todos* os dados e retorna como uma lista de strings, com cada string representando um dado.

.. code-block:: python

  ## Suppose we have a text with many email addresses
  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

  ## Here re.findall() returns a list of all the found email strings
  emails = re.findall(r'[\\w\\.-]+@[\\w\\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
  for email in emails:
    # do something with each found email string
    print email

findall com arquivos
--------------------
Para arquivos, você deve ter o hábito de escrever um loop para iteragir sobre as linhas do arquivo, e você poderá chamar a função findall() em cada linha. Ao invéz disso, vamos deixar a função findall() fazer a iteração por você -- muito melhor! Apenas alimente todo o arquivo de texto em findall() e deixe-o retornar uma lista de todos os dados da busca em uma única etapa (lembre que f.read () retorna o texto inteiro de um arquivo em uma única string):

.. code-block:: python

  # Open file
  f = open('test.txt', 'r')
  # Feed the file text into findall(); it returns a list of all the found strings
  strings = re.findall(r'some pattern', f.read())

findall e Groups
----------------
O mecanismo grupo de parêntesis ( ) pode ser combinado com findall(). Se o padrão inclui 2 ou mais grupos de parênteses, em seguida, em vez de retornar uma lista de strings, findall() retorna uma lista de tuples. Cada tuple representa um busca padrão, e dentro das dados das tuples, group(1), o group(2) ... Então, se 2 grupos de parênteses são adicionados ao padrão de e-mail, em seguida, findall() retorna uma lista de tuples, cada length 2 contém o nome de usuário e do domínio, por exemplo, ('Alice', 'google.com').

.. code-block:: python

  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
  tuples = re.findall(r'([\\w\\.-]+)@([\\w\\.-]+)', str)
  print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]
  for tuple in tuples:
    print tuple[0]  ## username
    print tuple[1]  ## host

.. nextslide::

Depois de ter a lista de tuples, você pode executar um loop sobre ele para fazer alguma computação para cada tuple. Se o padrão não inclui parênteses, então findAll() retornará uma lista de strings encontrados como nos exemplos anteriores. Se o padrão inclui um único conjunto de parênteses, então findAll() retornará uma lista de strings correspondentes a esse grupo único. (Recurso opcional Obscuro: Às vezes você tem grupos de parênteses (), mas que você não deseja extrair. 

Nesse caso, escrever os parênteses com ?: no início, por exemplo, (?: ) e que o parêntese da esquerda não vai contar como resultado do grupo.

RE Workflow and Debug
---------------------

O Pacote de expressões regulares padrão contém um monte de significados em apenas alguns caracteres, mas eles são muito densos, você pode gastar um monte de tempo depurando seu código. Configure o tempo de execução para que você possa executar um padrão e imprimir o que corresponde facilmente, por exemplo, executando em um pequeno texto de teste e imprimir o resultado com findall(). Se o padrão corresponde a nada, tente desabilitar os padrões, remover partes dele para que você obtenha mais acertos. 

Quando não econtrar nada, você não poderá fazer qualquer progresso já que não há nada de concreto para olhar. Uma vez que ele está retornando resultados, você pode trabalhar em melhorar o código de forma incremental para atingir apenas o que você quer.

Opções
------
As funções re tem opções para modificar o comportamento da busca. A opção é adicionada como um argumento extra para a search() ou findAll(), etc., por exemplo, re.search (pat, str, re.IGNORECASE).

* IgnoreCase - ignorar as diferenças maiúsculas/minúsculas, de modo 'a' corresponde tanto 'a' e 'A'.
* Dotall - Permite ponto (.) para coincidir como uma nova linha - normalmente ele corresponde a qualquer coisa, mas uma nova linha. Isso pode te enganar - você pensa que .* corresponde a tudo, mas por padrão ele não vai além do fim de uma linha. Note que \\s (espaços em branco) inclui novas linhas, por isso, se você quer combinar uma série de espaços em branco que podem incluir uma nova linha, você pode apenas usar \\s*
* MULTILINE - Dentro de uma string feita de muitas linhas, permitem ^ e $ para coincidir com o início e o fim de cada linha. Normalmente ^/$ seria apenas coincidir com o início e o fim de toda a string.

Greedy vs. Non-Greedy (opcional)
--------------------------------
Esta é uma seção opcional que mostra uma técnica mais avançada de expressão regular.

Supondo que você tem texto com tags: <b>foo</b> e <i>assim por diante</i>

Supondo que você está tentando encontrar cada tag com o padrão '(<*.>)' -- O que isso corresponde em primeiro lugar?

O resultado é um pouco surpreendente, mas o aspecto ganancioso do .* Faz com que a busca coincida todo '<b>foo</b> e <i>assim por diante</i>' como um grande resultado. O problema é que o .* vai tão longe quanto puder, em vez de parar na primeira > (por isso é chamado de ganancioso - Greedy).

.. nextslide::

Existe uma extensão para a expressão regular, onde você adicionar um ? no final, tais como .*? ou .+?, que irá alterá-lo para não ser tão ganancioso. Agora eles param assim que puder. Assim, o padrão '(<.*?>)' vai ficar apenas '<b>' como o primeiro resultado, e '</b>' como o segundo resultado, e assim por diante para cada par de tags <..>. O recomendado é que normalmente você use um .*?, e logo em seguida encontre o marcador correto (>, neste caso) que força o final da chamada .*?.

O *? extensão originada do Perl, e expressões regulares que incluem extensões do Perl são conhecidos como Perl Compatible Regular Expressions - pcre. O Python inclui suporte a pcre. Muito Útil EM linha de comando e tem uma flag onde se aceita utilizar padrões pcre.

.. nextslide::

Uma técnica mais velha, porém, amplamente usado para codificar esta ideia de "todos estes caracteres, exceto parando em X" usa o estilo de colchetes. Pelo exposto, você pode escrever da forma padrão, mas em vez de .* para obter todos os caracteres, use [^>] *, que ignora todos os caracteres que não são > (o ^ "inverte" o conjunto de colchetes, de modo que corresponda qualquer caractere que não esteja presente nos colchetes).


Substituição (Opcional)
-----------------------

A função re.sub(pat, replacement, str) pesquisa por todas os dados na string, e as substitui. O texto de substituição pode incluir '\\1', '\\2', que se referem ao texto do group(1), o group(2), e assim por diante a partir do texto encontrado original.

Aqui está um exemplo que procura todos os endereços de e-mail, e modifica-os para manter o usuário (\\1), mas tem yo-yo-dyne.com como o domínio.

.. code-block:: python

  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
  ## re.sub(pat, replacement, str) -- returns new string with all replacements,
  ## \\1 is group(1), \\2 group(2) in the replacement
  print re.sub(r'([\\w\\.-]+)@([\\w\\.-]+)', r'\\1@yo-yo-dyne.com', str)
  ## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher

Exercícios
----------

Execícios de Expressões Regulares
