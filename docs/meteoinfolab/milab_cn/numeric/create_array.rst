.. _dos-meteoinfolab-milab_cn-numeric-create_array:


***************************
创建数组
***************************

可以用array函数将Jython列表（list）转换为一个NDArray数组对象，需要注意的是多维数组中的元素的数据类型必须是一致的。
多层嵌套的列表可以创建多维数组。数组有几个重要的属性：ndim属性是数组维（或轴）的个数；shape属性是数组的纬度，即每个
维的大小；size属性是数组元素的总数，等于shape元素的乘积；dtype属性表示数组中元素的数据类型。

::

    >>> a = array([1,2,3,4])
    >>> b = array([5,6,7,8])
    >>> c = array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
    >>> b
    array([5, 6, 7, 8])
    >>> c
    array([[1, 2, 3, 4]
          [4, 5, 6, 7]
          [7, 8, 9, 10]])
    >>> c.ndim
    2
    >>> c.shape
    (3, 4)
    >>> c.size
    12
    >>> c.dtype
    int

a是一维数组，其shape只有一个元素。而c是二维数组，其shape有两个元素，其中第0维（或轴，axis）的长度为3，第1维的
长度为4。在保持数组元素个数不变的情况下，可以改变shape中每个维的大小。下面的例子将数组C的shape从(3,4)改为(4,3)，
只是改变了每个维的大小，数组元素在内存中的位置并没有改变。

::

    >>> c.shape = 4, 3
    >>> c
    array([[1, 2, 3]
          [4, 4, 5]
          [6, 7, 7]
          [8, 9, 10]])
    >>> c.shape
    (4, 3)

使用数组的reshape方法，可以创建一个改变了shape的新数组，原数组的shape保持不变，注意新数组和原数据的元素个数保持不变。

::

    >>> d = a.reshape(2,2)
    >>> d
    array([[1, 2]
          [3, 4]])
    >>> a
    array([1, 2, 3, 4])

也可以用numeric包中包含的一些数组创建函数来创建数组。创建一维数组的函数包括arange、arange1、linespace、logspace。
arange函数通过指定起始值、终值和步长来创建一维函数，arange1函数通过指定起始值、元素个数和步长来创建一维函数。

::

    >>> arange(10, 30, 5)
    array([10, 15, 20, 25])
    >>> arange(0, 2, 0.3)
    array([0.0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
    >>> arange1(2, 5)
    array([2, 3, 4, 5, 6])
    >>> arange1(2, 5, 0.1)
    array([2.0, 2.1, 2.2, 2.3, 2.4])

linespace函数通过指定起始值、终值和元素个数来创建一维数组，logspace和linespace参数类似，但创建的是等比数列。

::

    >>> linspace(2, 3, 5)
    array([2.0, 2.25, 2.5, 2.75, 3.0])
    >>> logspace(2, 3, 5)
    array([100.0, 177.82794100389228, 316.22776601683796, 562.341325190349, 1000.0])

创建固定填充值数组的函数包括：zeros、ones、full。zeros和ones函数分别用0和1来填充数组，参数是数组的shape。full
函数可以指定填充值。

::

    >>> zeros(5)
    array([0.0, 0.0, 0.0, 0.0, 0.0])
    >>> zeros((2,2), dtype=dtype.int)
    array([[0, 0]
          [0, 0]])
    >>> ones((2,3))
    array([[1.0, 1.0, 1.0]
          [1.0, 1.0, 1.0]])
    >>> full((2,3), 0.5)
    array([[0.5, 0.5, 0.5]
          [0.5, 0.5, 0.5]])

此外还可以用一些特殊的库函数（例如random）生成随机或特定的数组。