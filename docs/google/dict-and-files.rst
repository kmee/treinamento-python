Dicionários e Arquivos Python
=============================

Dicionários
-----------

Dicionário é uma estrutura de dados que contem uma lista de pares **chave:valor**.

São delimitados por chaves: **{ }** e seus elementos separados por vírgulas.

.. code-block:: python

    ## Dicionario simples
    a = {'nome': 'Amanda', 'idade': 13}


Qualquer programa python em execução tem diversos dicionários simultaneamente
ativos, mesmo que o código do programa do usuário não utilize
explicitamente um dicionário.

O tipo dict não só é amplamente usado em nossos programas como também é parte
fundamental da implementação Python. Namespaces de módulos, atributos de
classes e de instância e argumentos nomeados de funções são algumas das
construções básicas em que os dicionários estão implementados.

.. image:: img/dict.png
    :align: center


Chaves Imutáveis
----------------
As chaves do dicionário devem ser imutáveis (hashable), isto é devem ser Inteiros, strings ou tuplas.
Um objeto é hashable se tiver um valor de hash que nunca muda durante seu
tempo de vida e puder ser comparado com outros objetos.

.. nextslide::

Operações com Dict
------------------

Para construir um dicionário, podemos iniciar com a notação **{}**  criando um dicionario vazio
e em seguida adicionar conjuntos de chaves:valor da seguinte maneira:

.. code-block:: python

    dict = {}
    dict['a'] = 'alpha'
    dict['g'] = 'gamma'
    dict['o'] = 'omega'

    print dict  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

Ou também podemos utilizar outras estratégias como:

.. code-block:: python

    dict(Nome='Zara', Idade=21)
    d = {'Nome': 'Zara', 'Idade': 21, 'Classe': '8/10'}


.. nextslide::
Para acessar as informações do dicionário, devemos utilizar duas chaves.

.. code-block:: python

    mercadinho = {"Banana": 3.00, "Laranja": 5.00, "Uva": 8.00}

    mercadinho['Banana']

Dicionarios são mutáveis. Podemos editar as informações com a mesma notação de chaves:

.. code-block:: python

    mercadinho['Banana'] =  12.00

    print(mercadinho)

.. nextslide::

Use “in” para checar se uma chave existe no dicionário

.. code-block:: python

    mercadinho = { "Banana" : 3.00, "Uva": 8.00 }
    print("Manga" in mercadinho)
    False
    print("Uva" in mercadinho)
    True

Use dict.get(chave) que retorna o valor ou None se a chave não existe.
A expressão get(key, returnvalue) permite a você especificar um valor do retorno
se a chave não for encontrada.

.. code-block:: python

    mercadinho = { "Banana" : 3.00, "Uva": 8.00 }
    print(mercadinho.get('Uva'))
    8.00
    print(mercadinho.get('Manga'))
    None
    print(mercadinho.get('Manga', 10.0))
    10.0

.. nextslide::

Remoção

O operador "del" faz deleções. No caso mais simples, ele pode remover
a definição de uma variável, como se a variável não tivesse sido definida.
Del também pode ser usada em uma lista de elementos ou pedaços para
deletar parte da lista e para deletar entradas de um dicionário.

.. code-block:: python

    var = 6
    del var  # var nunca mais!

    list = ['a', 'b', 'c', 'd']
    del list[0]     ## Deleta primeiro elemento
    del list[-2:]   ## Deleta últimos dois elementos
    print list      ## ['b']

    dict = {'a':1, 'b':2, 'c':3}
    del dict['b']   ## Deleta a entrada 'b'
    print dict      ## {'a':1, 'c':3}


.. nextslide::

Um laço “for” em um dicionário interage sobre suas chaves por padrão.
As chaves aparecerão em uma ordem arbitrária.

Os métodos dict.keys() e dict.values() retornam listas de chaves ou valores explicitamente.


.. code-block:: python

    ## Por padrão, interagindo em um dict interage-se com suas chaves.
    ## Veja que as chaves estão em ordem randômica.
    for key in mercadinho: print key

    ## Exatamente o mesmo resultado de cima
    for key in mercadinho.keys(): print key

    ## Pegue a lista de chaves:
    print mercadinho.keys()

    ## Do mesmo jeito, um .values() lista os valores
    print mercadinho.values()

    ## Uso comum – laço sobre as chaves ordenadas,
    ## acessando cada chave/valor
    for key in sorted(mercadinho.keys()):
    print key, mercadinho[key]


.. nextslide::
Também existe um método items() que retorna a lista de tuplas (chave, valor),
que é o método mais eficiente de examinar todos os dados em um dicionário.
Todas estas listas podem ser passadas pela função sorted().

.. nextslide::

.. code-block:: python

    ## .items() é o dicionário expresso como tuplas (chave, valor)
    print mercadinho.items()


**Nota de Estratégia**: do ponto de vista de **velocidade**, o dicionário é uma das
melhores ferramentas e você deve usá-la sempre que puder com um método simples
de **organizar dados**. Por exemplo, você pode ler um arquivo de log onde cada
linha começa com um endereço IP, e guardar os dados usando o endereço IP
como chave, e a lista de linhas onde ele aparece como valor. Assim que você
ler todo o arquivos, você pode buscar por qualquer endereço IP e
instantaneamente ver a sua lista de linhas. O dicionário pega dados
dispersos e os torna algo coerente.

Formatando Dicionários
----------------------

O operador % funciona convenientemente para substituir valores de um dicionário
em uma string pelo nome:

.. code-block:: python

    hash = {}
    hash['word'] = 'garfield'
    hash['count'] = 42
    s = 'Eu quero %(count)d cópias de %(word)s' % hash  # %d for int, %s for string
    # 'Eu quero 42 cópias de garfield'

Arquivos
--------

A função open() abre e retorna um identificador de arquivo que pode ser usado
para ler ou escrever um arquivo da maneira usual.

.. code-block:: python

  # Mostra o conteúdo de um arquivo
  f = open('foo.txt', 'rU')
  f.close()


O código f = open(‘name’, ‘r’) abre o arquivo na variável f, pronto para operações de leitura, e
use o método f.close(), quando terminar. Ao invés de ‘r’, use ‘w’ para
escrita, e ‘a’ para adicionar (append). O modo especial ‘rU’ é a opção
universal para arquivos de texto onde o Python usa inteligência para
converter diferentes tipos de fim-de-linha (line-endings) para que eles
sempre venham como um simples ‘\n’.


.. nextslide::

O laço de repetição padrão “for-loop”
funciona para arquivos de texto, interagindo pelas linhas do arquivo
(isso só funciona para arquivos texto, não para arquivos binários).

A técnica do for-loop é um simples e eficiente método para olhar todas as
linhas em um arquivo de texto:


.. code-block:: python

  # Mostra o conteúdo de um arquivo
  f = open('foo.txt', 'rU')
  for line in f:   ## interage pelas linhas do arquivo
    print line,    ## print não adicionar um character de fim-de-linha
                   ## já que ‘line’ já tem um no fim de cada linha.
  f.close()

.. nextslide::

Ler uma linha de cada vez tem a boa qualidade de **não precisar carregar todo
o arquivo na memória** de uma única vez – vem a calhar se você precisa olhar
em todas as linhas de um arquivo de 10 gigabytes sem usar 10 gigabytes de
memória.

O método **f.readlines()** carrega todo o arquivo para a memória e
retorna seu conteúdo como uma lista de suas linhas.

O método **f.read()** carrega todo o arquivo em uma única string,
que é um método que vem a calhar se você precisa lidar com o texto todo de uma vez,
como em uma expressão regular que veremos mais tarde.

o método **f.write(sring)** é a maneira mais fácil de gravar
dados em um arquivo aberto. Ou você pode usar “print” com um arquivo aberto,
mas a sintaxe é feia: “print >> f, string”.

.. nextslide::

Exercitando

.. code-block:: python

    arquivo = open('arquivo.txt', 'r') # Abra o arquivo (leitura)
    conteudo = arquivo.readlines()
    conteudo.append('Nova linha')   # insira seu conteúdo

    arquivo = open('arquivo.txt', 'w') # Abre novamente o arquivo (escrita)
    arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

    arquivo.close()

Escrever em um arquivo

Se o arquivo já existir ele irá sobrescrever todo o conteúdo.

.. code-block:: python

    arquivo = open('arquivo.txt', 'w')
    arquivo.write('Felipe\nEder\nLuciano')
    arquivo.close()

.. nextslide::

Ler todas as linhas em um única string

.. code-block:: python

  arquivo = open('arquivo.txt', 'r')
  unica_string = arquivo.read()
  arquivo.close()


Ler todas as linhas em uma lista

.. code-block:: python

  arquivo = open('arquivo.txt', 'r')
  lista = arquivo.readlines() # readlinesssssss
  arquivo.close()

Ler linha a linha do arquivo

.. code-block:: python

  arquivo = open('arquivo.txt', 'r')
  primeira_linha = arquivo.readline()
  segunda_linha  = arquivo.readline()
  terceira_linha = arquivo.readline()
  # etc...
  arquivo.close()


Arquivos Unicode
----------------

Os módulos "codecs" proveem suporte para ler arquivos em formato Unicode.

.. code-block:: python

    import codecs

    f = codecs.open('foo.txt', 'rU', 'utf-8')
    for line in f:
      # esta linha é uma string *Unicode*


Para gravar, use f.write() já que print não suporta integralmente formatos unicode.


Exercício de Desenvolvimento Incremental
----------------------------------------

Criando um programa Python, **não escreva tudo em um único passo**. Ao invés disso
identifique apenas a primeira parte, ex: “o primeiro passo é extrair a lista
de palavras.”. Escreva o código para cumprir esta parte, e apenas imprima
sua estrutura de dados neste ponto, então você pode fazer um sys.exit(0)
para que o programa não rode mais nada que ainda não esteja pronto.

**Passo-por-passo** Assim que a parte do código estiver funcionando,
você pode continuar trabalhando
no código para o próxima passo. Ser capaz de olhar o printout (resultado)
de suas variáveis em um estado pode ajudá-lo a pensar sobre como você
precisa transformar as variáveis para chegar ao próximo estado.

Python é muito rápido com estes padrões, permitindo a você fazer
pequenas alterações e rodar o programa para ver o resultado.
Aproveite esta característica para criar seu programa em pequenos passos.


Exercício: wordcount.py
-----------------------

0 - Escreva uma função para substituir os valores de um dicionario pelo seu quadrado.

d = { 'boleto1': 9, 'boleto2': 3, 'boleto3': 0, 'boleto4': 5, 'boleto5': 1 }

-------------------------------------------------------------------------------

1 - Crie um dicionário e armazene nele os seus dados:
nome, idade, telefone, endereço.
Imprima todos os dados usando o padrão chave: valor.

1.1 - Crie um novo dicionario com os mesmos campos mas com novas informações.

1.2 - Refaça a 1.1

1.3 - Crie um dicionario contendo os dicionarios criados anteriormente

1.4 - Imprima sua idade.


-------------------------------------------------------------------------------

2- Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve construir um dicionario e fazer um programa que informe o nome, os saltos e a média dos saltos.
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

- Salto: 6.5 m
- Salto: 6.1 m
- Salto: 6.2 m
- Salto: 5.4 m
- Salto: 5.3 m


.. code-block:: python

  print (rodrigo['media']) == '5.9 m'


-------------------------------------------------------------------------------

**3** - Contruir um dicionario com informações baseada na tabela abaixo:

Comparativo de Consumo de Combustível

======= =========
Veiculo Autonomia
======= =========
Fusca   7
Gol     10
Uno     12.5
Vectra  9
Corsa   14.5
======= =========

Quantos litros de combustível cada um dos carros cadastrados consome para
percorrer uma distância de 1000 quilômetros e quanto isto custará,
considerando um que a gasolina custe R$ 2,25 o litro.

Construir um dicionario com todas essas informações, de modo que

.. code-block:: python

  print (dicionario['gol']['custo']) == 'R$ 225.00'
  print (dicionario['gol']['consumo']) == '100.0 litros'

..
.. Relatório Final:
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   14.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   10.5 -   69.0 litros - R$ 155.17

.. O menor consumo é do gol. ..


-------------------------------------------------------------------------------

4 - Write a Python program to sort Counter by value. Go to the editor
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]


--------------------------------------------------------------------------------

Given the following dictionary:

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
Try to do the followings:

Add a key to inventory called 'pocket'.
Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
.sort()the items in the list stored under the 'backpack' key.
Then .remove('dagger') from the list of items stored under the 'backpack' key.
Add 50 to the number stored under the 'gold' key.

________________________________________________________________________________

Combinando todo o material do Python básico – strings, listas, dicionários,
tuplas e arquivos. ---- Tente fazer o exercício wordcount.py dos exercícios básicos.

Download do Arquivo: :download:`wordcount.py <../code/basic/wordcount.py>`
