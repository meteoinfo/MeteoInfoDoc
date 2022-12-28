.. _dos-meteoinfolab-milab_cn-numeric-random:


***************************
随机数生成（numeric.random）
***************************

numeric.random包中包含一些生成随机数的函数：random(size)函数生成指定size的[0, 1)范围的随机数或数组；
rand(d0, d1, …, dn)函数生成n维随机数组，randn函数生成正态分布的随机数组；randint(low, [high, size])
函数生成[low, high)范围的整数。

::

    >>> random.random(5)
    array([0.7120722502780094, 0.7285606928111786, 0.9501585619503155, 0.9665260911436336, 0.23553147325993318])
    >>> random.rand(2,3)
    array([[0.4658542538619157, 0.2759412614799148, 0.5274271669862279]
          [0.8195906996167274, 0.9739781724332607, 0.44585042150460574]])
    >>> random.randint(1, 10, size=10)
    array([1, 5, 5, 5, 8, 7, 2, 5, 1, 5])

seed函数用于指定随机数生成时所用算法开始的整数值，如果使用相同的seed值，则每次生成的随即数都相同，如果不设置这个值，
则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。seed(None)相当于取消seed值设置。

::

    >>> random.rand()
    0.28557379561026175
    >>> random.rand()
    0.2235382498062879
    >>> random.seed(10)
    >>> random.rand()
    0.7304302967434272
    >>> random.rand()
    0.7304302967434272
    >>> random.seed(None)
    >>> random.rand()
    0.26737134272585183

shuffle和permutation函数对数组进行随机洗牌，shuffle是在数组内部洗牌，permutation是生成一个新的洗牌后的数组，
不改变原数组的元素顺序。

::

    >>> a = arange(10)
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> random.shuffle(a)
    >>> a
    array([7, 2, 9, 5, 1, 4, 3, 8, 6, 0])
    >>> a = arange(10)
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> b = random.permutation(a)
    >>> b
    array([6, 3, 5, 0, 1, 8, 9, 4, 7, 2])
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

random包中还有一些函数来生成特定分布的随机数，如f、exponential、gamma、gumbel、laplace、logistic、lognormal、
normal、pareto、poisson、standard_t、triangular、uniform、weibull等。