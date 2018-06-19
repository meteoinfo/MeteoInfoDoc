.. _docs-meteoinfolab-user_guid-arrays:


*******************
Arrays
*******************

MeteoInfoLab's main object is the homogeneous multidimensional array. It is a table of elements (usually
numbers), all of the same type, indexed by a tuple of positive intergers. Dimensions are also called axes.
The number of axes is *rank*.

**Array Creation**

To create an array with three elements in a single row, separate the elements with a comma.

::

    >>> array([1,2,3])
    array([1, 2, 3])
    >>> array(25.6)
    array([25.6])
    
array transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences
into three-dimensional arrays, and so on.

::

    >>> array([[1,2], [3,4]])
    array([[1.0, 2.0]
          [3.0, 4.0]])

Another way to create an anrray is to use a function, such as ``ones``, ``zeros``, or ``rand``. For example, 
create a 5 element vector of zeros.

::

    >>> zeros(5)
    array([0.0, 0.0, 0.0, 0.0, 0.0])
    >>> zeros(5, dtype='int')
    array([0, 0, 0, 0, 0])
    >>> zeros((2, 1))
    array([[0.0]
          [0.0]])
          
To create sequences of numbers, MeteoInfoLab provides a function analogous to range that returns arrays.

::

    >>> arange( 10, 30, 5 )
    array([10, 15, 20, 25])
    >>> arange( 0, 2, 0.3 )                 # it accepts float arguments
    array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])
    
The function ``linspace`` that receives as an argument the number of elements that we want, instead of the 
step:

::

    >>> linspace( 0, 2, 9 )                 # 9 numbers from 0 to 2
    array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])
    >>> x = linspace( 0, 2*pi, 100 )        # useful to evaluate function at lots of points
    >>> f = sin(x)
    
**Array Operations**

Arithmetic operators on arrays apply *elementwise*. A new array is created and filled with the result.

::

    >>> a = array( [20,30,40,50] )
    >>> b = arange( 4 )
    >>> b
    array([0, 1, 2, 3])
    >>> c = a-b
    >>> c
    array([20, 29, 38, 47])
    >>> b**2
    array([0, 1, 4, 9])
    >>> 10*sin(a)
    array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
    
Unlike in many matrix languages such as MATLAB, the product operator * operates elementwise in MeteoInfoLab
arrays. The matrix product can be performed using the dot function or method:

::
    
    >>> A = array( [[1,1],
    ...             [0,1]] )
    >>> B = array( [[2,0],
    ...             [3,4]] )
    >>> A*B                         # elementwise product
    array([[2, 0],
           [0, 4]])
    >>> A.dot(B)                    # matrix product
    array([[5, 4],
           [3, 4]])
    >>> dot(A, B)                   # another matrix product
    array([[5, 4],
           [3, 4]])
           
**Array Indexing, Slicing and Iterating**

*One-dimensional* arrays can be indexed, sliced and iterated over, much like lists and other Python 
sequences.

::

    >>> a = arange(10)**3
    >>> a
    array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
    >>> a[2]
    8
    >>> a[2:5]
    array([ 8, 27, 64])
    >>> a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
    >>> a
    array([-1000,     1, -1000,    27, -1000,   125,   216,   343,   512,   729])
    >>> a[ : :-1]                                 # reversed a
    array([  729,   512,   343,   216,   125, -1000,    27, -1000,     1, -1000])
    >>> for i in a:
    ...     print(i**(1/3.))
    ...
    nan
    1.0
    nan
    3.0
    nan
    5.0
    6.0
    7.0
    8.0
    9.0
    
*Multidimensional* arrays can have one index per axis. These indices are given in a tuple separated by 
commas:

::

    >>> b = array([[0,1,2,3],[10,11,12,13],[20,21,22,23],[30,31,32,33],[40,41,42,43]])
    >>> b[2,3]
    23
    >>> b[0:5, 1]                       # each row in the second column of b
    array([ 1, 11, 21, 31, 41])
    >>> b[ : ,1]                        # equivalent to the previous example
    array([ 1, 11, 21, 31, 41])
    >>> b[1:3, : ]                      # each column in the second and third row of b
    array([[10, 11, 12, 13],
           [20, 21, 22, 23]])