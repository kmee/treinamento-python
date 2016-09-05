Dicionários e Arquivos Python
=============================

Dicionários
-----------
Qualquer programa python em execução tem diversos dicionários simultaneamente
ativos, mesmo que o código do programa do usuário não utilize
explicitamente um dicionário.

- Beaultiful Code (O'Reilly 2007), Cap 18, Python's Dictonary Implementation

O tipo dict não só é amplamente usado em nossos programas como também é parte
fundamental da implementação Python. Namespaces de módulos, atributos de
classes e de instância e argumentos nomeados de funções são algumas das
construções básicas em que os dicionários estão implementados. As próprias
funções embutidas ficam em um dicionário:

__builtins__.__dict__.

Por causa desse papel essencial, os dicts são extremamente otimizados.
As tabelas hash são o mecanismo responsável pelo seu auto desempenho.

Hashable?
---------
Um objeto é hashable se tiver um valor de hash que nunca muda durante seu
tempo de vida e puder ser comparado com outros objetos.

A estrutura de hash chave/valor (key/value) é chamada de “dict”. O conteúdo
de um dict pode ser escrito como uma série de pares chave: valor (key:value)
dentro de chave {}, ex: dict = {chave1:valor1, chave2:valor2, ... }. Um
“dicionário vazio” é simplesmente um par de chaves {}.

.. nextslide::

Para usar ou definir um valor em um dicionário use o formato com colchete,
ex: dict[‘foo’] busca pelo valor dentro da chave ‘foo’. Strings, números e
até tuplas (tuples) funcionam como chaves, e qualquer tipo pode ser um valor.
Outros tipos podem ou não funcionar corretamente com chaves (strings e tuplas
funcionam lindamente desde que sejam imutáveis). Buscar por um valor que não
está no dicionário retorna um KeyError – use “in” para checar se uma chave
existe no dicionário, ou use dict.get(chave) que retorna o valor ou None se
a chave não existe (ou get(chave, nao-encontrado) permite a você especificar
o valor do retorno se a chave não for encontrada).

.. code-block:: python

    ## Pode construir um dicionário iniciando um vazio {}
    ## e guardando pares de chave/valor no dicionário neste formato:
    ## dict[chave] = valor-para-esta-chave
    dict = {}
    dict['a'] = 'alpha'
    dict['g'] = 'gamma'
    dict['o'] = 'omega'

    print dict  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

    print dict['a']     ## Busca simples, retorna 'alpha'
    dict['a'] = 6       ## Altera chave/valor no dicionário
    'a' in dict         ## True
    ## print dict['z']                  ## Retorna KeyError
    if 'z' in dict: print dict['z']     ## Evita KeyError
    print dict.get('z')  ## None (ao invés de KeyError)


.. image:: img/dict.png
    :align: center

.. nextslide::

Um laço “for” em um dicionário interage sobre suas chaves por padrão.
As chaves aparecerão em uma ordem arbitrária. Os métodos dict.keys() e
dict.values() retornam listas de chaves ou valores explicitamente.
Também existe um método items() que retorna a lista de tuplas (chave, valor),
que é o método mais eficiente de examinar todos os dados em um dicionário.
Todas estas listas podem ser passadas pela função sorted().

.. code-block:: python

    ## Por padrão, interagindo em um dict interage-se com suas chaves.
    ## Veja que as chaves estão em ordem randômica.
    for key in dict: print key
    ## prints a g o

    ## Exatamente o mesmo resultado de cima
    for key in dict.keys(): print key

    ## Pegue a lista de chaves:
    print dict.keys()  ## ['a', 'o', 'g']

    ## Do mesmo jeito, um .values() lista os valores
    print dict.values()  ## ['alpha', 'omega', 'gamma']

    ## Uso comum – laço sobre as chaves ordenadas,
    ## acessando cada chave/valor
    for key in sorted(dict.keys()):
    print key, dict[key]

    ## .items() é o dicionário expresso como tuplas (chave, valor)
    print dict.items()  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

    ## Esta sintaxe de laço acessa toda a lista repetindo
    ## pela lista de tuplas .items(), acessando um par (chave, valor)
    ## em cada interação.
    for k, v in dict.items(): print k, '>', v
    ## a > alpha    o > omega     g > gamma

.. nextslide::

Existem “iter” variações destes métodos chamados itereys(), intervalues() e
iteritems() que evitam o custo de contrus a lista inteira – traz um ganho
de velocidade se os dados forem muitos. No entanto eu normalmente prefiro
os métodos padrões keys() e values() com os nomes sensíveis. Na revisão
Python 3 a necessidade de usar as variants iterkeys() foi descartada.

.. nextslide::

Nota de Estratégia: do ponto de vista de velocidade, o dicionário é uma das
melhores ferramentas e você deve usá-la sempre que puder com um método simples
de organizar dados. Por exemplo, você pode ler um arquivo de log onde cada
linha começa com um endereço IP, e guardar os dados usando o endereço IP
como chave, e a lista de linhas onde ele aparece como valor. Assim que você
ler todo o arquivos, você pode buscar por qualquer endereço IP e
instantaneamente ver a sua lista de linhas. O dicionário pega dados
disperses e os torna algo coerente.

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

Del
----

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

Arquivos
--------

A função open() abre e retorna um identificador de arquivo que pode ser usado
para ler ou escrever um arquivo da maneira usual. O código f = open(‘name’,
‘r’) abre o arquivo na variável f, pronto para operações de leitura, e
use o método f.close(), quando terminar. Ao invés de ‘r’, use ‘w’ para
escrita, e ‘a’ para adicionar (append). O modo especial ‘rU’ é a opção
universal para arquivos de texto onde o Python usa inteligência para
converter diferentes tipos de fim-de-linha (line-endings) para que eles
sempre venham como um simples ‘\n’. O laço de repetição padrão “for-loop”
funciona para arquivos de texto, interagindo pelas linhas do arquivo
(isso só funciona para arquivos texto, não para arquivos binários).

A técnica do for-loop é um simples e eficiente método para olhar todas as
linhas em um arquivo de texto:


.. nextslide::

.. code-block:: python

  # Mostra o conteúdo de um arquivo
  f = open('foo.txt', 'rU')
  for line in f:   ## interage pelas linhas do arquivo
    print line,    ## print não adicionar um character de fim-de-linha
                   ## já que ‘line’ já tem um no fim de cada linha.
  f.close()

.. nextslide::

Ler uma linha de cada vez tem a boa qualidade de não precisar carregar todo
o arquivo na memória de uma única vez – vem a calhar se você precisa olhar
em todas as linhas de um arquivo de 10 gigabytes sem usar 10 gigabytes de
memória. O método f.readlines() carrega todo o arquivo para a memória e
retorna seu conteúdo como uma lista de suas linhas. O método f.read()
carrega todo o arquivo em uma única string, que é um método que vem a
calhar se você precisa lidar com o texto todo de uma vez, como em uma
expressão regular que veremos mais tarde.

Para escrever, usar o método f.write(sring) é a maneira mais fácil de gravar
dados em um arquivo aberto. Ou você pode usar “print” com um arquivo aberto,
mas a sintaxe é feia: “print >> f, string”. Em python 3000, a sintaxe do
comando print será fixada como uma expressão regular com um arquivo como
argumento:

"print(string, file=f)".

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


Criando um programa Python, não escreva tudo em um único passo. Ao invés disso
identifique apenas a primeira parte, ex: “o primeiro passo é extrair a lista
de palavras.”. Escreva o código para cumprir esta parte, e apenas imprima
sua estrutura de dados neste ponto, então você pode fazer um sys.exit(0)
para que o programa não rode mais nada que ainda não esteja pronto. Assim
que a parte do código estiver funcionando, você pode continuar trabalhando
no código para a próxima parte. Ser capaz de olhar o printout (resultado)
de suas variáveis em um estado pode ajudá-lo a pensar sobre como você
precisa transformar as variáveis para chegar ao próximo estado.
Python é muito rápido com estes padrões, permitindo a você fazer
pequenas alterações e rodar o programa para ver o resultado.
Aproveite esta característica para criar seu programa em pequenos passos.


Exercício: wordcount.py
-----------------------

Combinando todo o material do Python básico – strings, listas, dicionários,
tuplas e arquivos. ---- Tente fazer o exercício wordcount.py dos exercícios básicos.