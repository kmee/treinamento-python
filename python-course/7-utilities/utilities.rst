Python Utilities
================

Python Utilities
----------------
Nesta sessão, vamos dar uma olhada em algumas das muitas funções da biblioteca
padrão do Python, visando resolver problemas comuns.

File System -- os, os.path, shutil
----------------------------------

Os modulos **os** e **os.path** contem muitas funcionalidades para interagir
com o sistema operacional.

O modulo **shutil** pode copiar arquivos

- `os module docs <http://docs.python.org/lib/module-os.html/>`_

- filenames = os.listdir(dir) - lista o nome dos arquivos no diretório (não incluindo path atual . e path pai ..). Os nomes dos arquivos são apenas os nomes dos arquivos e não os seus caminhos absolutos.

- os.path.join(dir, filename) - recupera o nome de arquivo da lista acima, usar isso para colocar o diretório (path) e nome do arquivo em conjunto para fazer um caminho completo

- os.path.abspath(path) - recupera um caminho, retorna a forma absoluta, por exemplo, /home/nick/foo/bar.html

- os.path.dirname(caminho), os.path.basename (path) - recupera o caminho completo dir/foo/bar.html, retorna o diretório "dir/foo" e nome do arquivo "bar.html"

.. nextslide::

- os.path.exists(path) -- true if it exists
- os.mkdir(dir_path) -- makes one dir, os.makedirs(dir_path) makes all the needed dirs in this path
- shutil.copy(source-path, dest-path) -- copy a file (dest path directories should exist)

.. code-block:: python

    ## Example pulls filenames from a dir, prints their relative and absolute paths
    def printdir(dir):
      filenames = os.listdir(dir)
      for filename in filenames:
        print filename  ## foo.txt
        print os.path.join(dir, filename) ## dir/foo.txt (relative to current dir)
        print os.path.abspath(os.path.join(dir, filename)) ## /home/nick/dir/foo.txt


Explorar um modulo funciona muito bem com as funções da **biblioteca
padrão**: help() e dir().

No interpretador execute um import os e use os comandos para avaliar os
modulos: dir(os), help(os.listdir), dir(os.path), help(os.path.dirname).

Running External Processes -- commands
--------------------------------------

O modulo **commands** é uma forma simples de executar um comando externo e
capturar sua saida.

- commands module docs
- (status, output) = commands.getstatusoutput(cmd) -- executa o comando, aguarda a execução para sair, e retorna status int e texto de saída como uma tupla. O comando é executado com sua saída padrão e erro padrão combinado em uma única saída de texto. O status será diferente de zero se o comando falhou. Desde que o standar-err do comando seja capturado, se ele falhar, é preciso imprimir alguma indicação sobre o que aconteceu.
- output = commands.getoutput(cmd) -- como o comando acima, mas sem o status int.
- Há o commands.getstatus(), mas ele faz outra coisa, por isso não utilize.

.. nextslide::

- Se você gostaria de ter mais controle dos sub-processos que estão rodando, veja o módulo "popen2" (http://docs.python.org/lib/module-popen2.html)
- Há também o simples os.system(cmd), que executa o comando e retorna sua saída e retorna seu código de erro. Isso funciona se você deseja executar o comando, mas não precisa capturar a sua saída em suas estruturas de dados python.

.. code-block:: python

    ## Given a dir path, run an external 'ls -l' on it --
    ## shows how to call an external program
    def listdir(dir):
      cmd = 'ls -l ' + dir
      print "Command to run:", cmd   ## good to debug cmd before actually running it
      (status, output) = commands.getstatusoutput(cmd)
      if status:    ## Error case, print the command's output to stderr and exit
        sys.stderr.write(output)
        sys.exit(1)
      print output  ## Otherwise do something with the command's output

Excessões
---------

Uma exceção representa um erro de tempo de execução que suspende a execução normal 
em uma linha particular e transfere o controle para manipulação de erros de código. 
Esta seção apenas introduz os usos mais básicos de exceções. Por exemplo, um erro 
de tempo de execução pode ser que uma variável utilizada no programa não tenha um 
valor (ValueError... você provavelmente já viu este erro algumas vezes), ou um erro 
de operação de abertura de arquivo por causa do arquivo não existir ( IOError). 
(Veja docs http://docs.python.org/tut/node10.html][exception~~number=plural)

.. nextslide::

Sem qualquer código de manipulação de erro (como temos feito até agora), uma 
exceção de tempo de execução apenas interrompe o programa com uma mensagem de erro.
Isso é um bom comportamento padrão, e você já viu isso muitas vezes. Você pode adicionar 
uma estrutura "try/except" no seu código para lidar com exceções, como esta:


.. code-block:: python

  try:
    ## Either of these two lines could throw an IOError, say
    ## if the file does not exist or the read() encounters a low level error.
    f = open(filename, 'rU')
    text = f.read()
    f.close()
  except IOError:
    ## Control jumps directly to here if any of the above lines throws IOError.
    sys.stderr.write('problem reading:' + filename)
  ## In any case, the code then continues with the line after the try/except

.. nextslide::

A tentativa: seção inclui o código que pode lançar uma exceção. 
A exceção: seção contém o código para ser executado se houver uma exceção. 
Se não houver nenhuma exceção, a exceção: a seção é ignorada (isto é, que 
o código é para a manipulação de erro somente, não é o caso "normal" para 
o código). 

Você pode obter um ponteiro para a exceção do próprio objeto com 
a sintaxe ``except IOError, e:`` (e aponta para o objeto de exceção).

HTTP -- urllib and urlparse
---------------------------

O modulo **urllib** permite acessar servidores HTTP por meios de requests GET
e POST de maneira direta -- Tornando as urls acessiveis como um arquivo que
possa ser lido. O **urlparse** permite você trabalhar com partes de url e unir urls.

-urllib module docs
-ufile = urllib.urlopen(url) -- returns a file like object for that url
-text = ufile.read() -- can read from it, like a file (readlines() etc. also work)
-info = ufile.info() -- the meta info for that request. info.gettype() is the  mime time, e.g. 'text/html'
-baseurl = ufile.geturl() -- gets the "base" url for the request, which may be different from the original because of redirects
-urllib.urlretrieve(url, filename) -- downloads the url data to the given file path
-urlparse.urljoin(baseurl, url) -- given a url that may or may not be full, and the baseurl of the page it comes from, return a full url. Use geturl() above to provide the base url.

.. code-block:: python

    ## Given a url, try to retrieve it. If it's text/html,
    ## print its base url and its text.
    def wget(url):
      ufile = urllib.urlopen(url)  ## get file-like object for url
      info = ufile.info()   ## meta-info about the url content
      if info.gettype() == 'text/html':
        print 'base url:' + ufile.geturl()
        text = ufile.read()  ## read all its text
        print text

O codigo acima funciona bem, mas não inclue tratamento de erros caso a url
não exista. Segue uma versão de uma função que adiciona a lógica try/except
exibindo uma mensagem em caso de erro.

.. code-block:: python

    ## Version that uses try/except to print an error message if the
    ## urlopen() fails.
    def wget2(url):
      try:
        ufile = urllib.urlopen(url)
        if ufile.info().gettype() == 'text/html':
          print ufile.read()
      except IOError:
        print 'problem reading url:', url

Exercise
--------

Log Puzzle Exercise.
