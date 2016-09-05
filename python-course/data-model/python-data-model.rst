Python Data Model
=================

O modelo de dados python
------------------------

 - Nesses ultimo dias vc pode ter achado estranho escrever len(collection)

**em vez de collection.len()...**

.. nextslide::

A ponta do iceberg...
---------------------

O iceberg é chamado de python data model e descreve a API que você pode usar
para fazer com que seus próprios objetos interajam bem com os recursos mais
"malukos" da linguagem.

- É como se fosse um framework, formalizando a contrução da propria linguagem
- O interpretador python chama metodos especiais para realizar operações básicas.
- Os metodos especiais são sempre descritos com underscores duplos

Metodos especiais
-----------------

obj[key]

obj.__getitem__(key)

Exemplo Um Baralho Pythonico
----------------------------

.. code-block:: python

    import collections

    Card = collections.namedtuple('Card', ['rank', 'suit'])

    class FrenchDeck:
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = 'spades diamonds clubs hearts'.split()

        def __init__(self):
            self._cards = [Card(rank, suit) for suit in self.suits
                                            for rank in self.ranks]

        def __len__(self):
            return len(self._cards)

        def __getitem__(self, position):
            return self._cards[position]


.. nextslide::

.. code-block:: python

    >>> from frenchdeck import FrenchDeck, Card
    >>> beer_card = Card('7', 'diamonds')
    >>> beer_card
    Card(rank='7', suit='diamonds')
    >>> deck = FrenchDeck()
    >>> len(deck)
    52
    >>> deck[:3]
    [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
    >>> deck[12::13]
    [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
    >>> Card('Q', 'hearts') in deck
    True
    >>> Card('Z', 'clubs') in deck
    False
    >>> for card in deck:  # doctest: +ELLIPSIS
    ...   print(card)
    Card(rank='2', suit='spades')
    Card(rank='3', suit='spades')
    Card(rank='4', suit='spades')
    ...
    >>> for card in reversed(deck):  # doctest: +ELLIPSIS
    ...   print(card)
    Card(rank='A', suit='hearts')
    Card(rank='K', suit='hearts')
    Card(rank='Q', suit='hearts')

.. nextslide::

.. code-block:: python

    >>> for n, card in enumerate(deck, 1):  # doctest: +ELLIPSIS
    ...   print(n, card)
    1 Card(rank='2', suit='spades')
    2 Card(rank='3', suit='spades')
    3 Card(rank='4', suit='spades')
    ...
    >>> suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    >>> def spades_high(card):
    ...     rank_value = FrenchDeck.ranks.index(card.rank)
    ...     return rank_value * len(suit_values) + suit_values[card.suit]

    Rank test:

    >>> spades_high(Card('2', 'clubs'))
    0
    >>> spades_high(Card('A', 'spades'))
    51

    >>> for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
    ...      print(card)
    Card(rank='2', suit='clubs')
    Card(rank='2', suit='diamonds')
    Card(rank='2', suit='hearts')
    ...
    Card(rank='A', suit='diamonds')
    Card(rank='A', suit='hearts')
    Card(rank='A', suit='spades')


Como os metodos especiais sao usados
------------------------------------

- Eles foram criados para serem chamados pelo interpretador e não por você.

- Não escrevemos my_object.__len__(), escrevemos len(my_object)

Se my_object for uma instancia de uma classe definida por você, o python chamara
o metodo __len__ que voce implementou.

Para muitos tipos embutidos os interpretador usará um atalho: a implementação de len()
do CPython, retorna o valor do ob_size da Scruct C PyVarObject que representa qualquer
objeto embutido de tamanho váriavel na memoria. Isto é muito mais rapido que chamar um metodo.

Emulando tipos numéricos
------------------------

.. code-block:: python

    from math import hypot

    class Vector:

        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def __repr__(self):
            return 'Vector(%r, %r)' % (self.x, self.y)

        def __abs__(self):
            return hypot(self.x, self.y)

        def __bool__(self):
            return bool(abs(self))

        def __add__(self, other):
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)

        def __mul__(self, scalar):
            return Vector(self.x * scalar, self.y * scalar)


Mecanismo flexivel de parametros
--------------------------------
Um dos melhores recursos das funções python. Usamos os * e ** para explodir:

- "*" faz com que o vetor seja utilizado como argumentos ordenados.
- "**" faz com que o dicionario seja usado como argumentos nomeados.

.. code-block:: python

    >>> tag('br')  # <1>
    '<br />'
    >>> tag('p', 'hello')  # <2>
    '<p>hello</p>'
    >>> print(tag('p', 'hello', 'world'))
    <p>hello</p>
    <p>world</p>
    >>> tag('p', 'hello', id=33)  # <3>
    '<p id="33">hello</p>'
    >>> print(tag('p', 'hello', 'world', cls='sidebar'))  # <4>
    <p class="sidebar">hello</p>
    <p class="sidebar">world</p>
    >>> tag(content='testing', name="img")  # <5>
    '<img content="testing" />'
    >>> my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
    ...           'src': 'sunset.jpg', 'cls': 'framed'}
    >>> tag(**my_tag)


.. nextslide::

.. code-block:: python

    def tag(name, *content, cls=None, **attrs):
        """Generate one or more HTML tags"""
        if cls is not None:
            attrs['class'] = cls
        if attrs:
            attr_str = ''.join(' %s="%s"' % (attr, value)
                               for attr, value
                               in sorted(attrs.items()))
        else:
            attr_str = ''
        if content:
            return '\n'.join('<%s%s>%s</%s>' %
                             (name, attr_str, c, name) for c in content)
        else:
            return '<%s%s />' % (name, attr_str)



Estudo de caso: Refatorando Strategy
------------------------------------

O Padrão Strategy: Define uma familia de algoritimos, encapsula cada um e torna-os
intercambiábeis.

Exemplo:

Aplicação de descontos em pedidos com atributos diferentes ou da inpeção dos
itens comprados.

Considere:

- Clientes com mil ou mais pontos no program de fidelidade obtêm um desconto global de 5% sobre o pedido.
- Um desconto de 10% é aplicado a cada item com 20 ou mais unidades no mesmo pedido.
- Pedidos com pelo menos dez itens diferentes recebem um desconto global de 7%.

.. nextslide::

.. code-block:: python

    Customer = namedtuple('Customer', 'name fidelity')

    class LineItem:

        def __init__(self, product, quantity, price):
            self.product = product
            self.quantity = quantity
            self.price = price

        def total(self):
            return self.price * self.quantity

    class Order:  # the Context

        def __init__(self, customer, cart, promotion=None):
            self.customer = customer
            self.cart = list(cart)
            self.promotion = promotion

        def total(self):
            if not hasattr(self, '__total'):
                self.__total = sum(item.total() for item in self.cart)
            return self.__total

.. nextslide::

.. code-block:: python

        def due(self):
            if self.promotion is None:
                discount = 0
            else:
                discount = self.promotion.discount(self)
            return self.total() - discount

        def __repr__(self):
            fmt = '<Order total: {:.2f} due: {:.2f}>'
            return fmt.format(self.total(), self.due())

    class Promotion(ABC):  # the Strategy: an Abstract Base Class
        @abstractmethod
        def discount(self, order):
            """Return discount as a positive dollar amount"""

    class FidelityPromo(Promotion):  # first Concrete Strategy
        """5% discount for customers with 1000 or more fidelity points"""
        def discount(self, order):
            return order.total() * .05 if order.customer.fidelity >= 1000 else 0

    class BulkItemPromo(Promotion):  # second Concrete Strategy
        """10% discount for each LineItem with 20 or more units"""
        def discount(self, order):
            discount = 0
            for item in order.cart:
                if item.quantity >= 20:
                    discount += item.total() * .1
            return discount

    class LargeOrderPromo(Promotion):  # third Concrete Strategy
        """7% discount for orders with 10 or more distinct items"""

        def discount(self, order):
            distinct_items = {item.product for item in order.cart}
            if len(distinct_items) >= 10:
                return order.total() * .07
            return 0

.. nextslide::

.. code-block:: python

    >>> joe = Customer('John Doe', 0)  # <1>
    >>> ann = Customer('Ann Smith', 1100)
    >>> cart = [LineItem('banana', 4, .5),  # <2>
    ...         LineItem('apple', 10, 1.5),
    ...         LineItem('watermellon', 5, 5.0)]
    >>> Order(joe, cart, FidelityPromo())  # <3>
    <Order total: 42.00 due: 42.00>
    >>> Order(ann, cart, FidelityPromo())  # <4>
    <Order total: 42.00 due: 39.90>
    >>> banana_cart = [LineItem('banana', 30, .5),  # <5>
    ...                LineItem('apple', 10, 1.5)]
    >>> Order(joe, banana_cart, BulkItemPromo())  # <6>
    <Order total: 30.00 due: 28.50>
    >>> long_order = [LineItem(str(item_code), 1, 1.0) # <7>
    ...               for item_code in range(10)]
    >>> Order(joe, long_order, LargeOrderPromo())  # <8>
    <Order total: 10.00 due: 9.30>
    >>> Order(joe, cart, LargeOrderPromo())
    <Order total: 42.00 due: 42.00>

Com funções
-----------

.. code-block:: python

    class LineItem:
        ...
    class Order:  # the Context
        ...

    def fidelity_promo(order):
        """5% discount for customers with 1000 or more fidelity points"""
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0

    def bulk_item_promo(order):
        """10% discount for each LineItem with 20 or more units"""
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount

    def large_order_promo(order):
        """7% discount for orders with 10 or more distinct items"""
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0

    promos = [fidelity_promo, bulk_item_promo, large_order_promo]  # <1>

    def best_promo(order):  # <2>
        """Select best discount available        """
        return max(promo(order) for promo in promos)  # <3>


Decorators
----------
.. code-block:: python

    promos = []  # <1>
    def promotion(promo_func):  # <2>
        promos.append(promo_func)
        return promo_func

    @promotion  # <3>
    def fidelity(order):
        """5% discount for customers with 1000 or more fidelity points"""
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0

    @promotion
    def bulk_item(order):
        """10% discount for each LineItem with 20 or more units"""
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount

    @promotion
    def large_order(order):
        """7% discount for orders with 10 or more distinct items"""
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0

    def best_promo(order):  # <4>
        return max(promo(order) for promo in promos)


Closure
-------

.. code-block:: python

    def make_averager():
    series = []

        def averager(new_value):
            series.append(new_value)
            total = sum(series)
            return total/len(series)

    return averager
    >>> avg = make_averager()
    >>> avg(10)
    10.0
    >>> avg(11)
    10.5
    >>> avg(12)
    11.0

Herança
-------

.. code-block:: python

    class Parent(object):

    def override(self):
        print "PARENT override()"

    class Child(Parent):

        def override(self):
            print "CHILD override()"

    dad = Parent()
    son = Child()

    dad.override()
    son.override()

    >>> PARENT override()
    >>> CHILD override()