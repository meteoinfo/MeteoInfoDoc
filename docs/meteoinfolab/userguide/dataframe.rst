.. _docs-meteoinfolab-user_guid-dataframe:


*********************
Series and DataFrame
*********************

Series
=======

Series is a one-dimensional labeled array. The axis labels are collectively referred to as the *index*. 
Creating a Series by passing a list of values, letting pandas create a default integer index:

::

    >>> s = Series([1,3,5,np.nan,6,8])
    >>> s
    0	1.0
    1	3.0
    2	5.0
    3	NaN
    4	6.0
    5	8.0

DataFrame
==========

DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. Creating a 
DataFrame by passing an array, with a datetime index and labeled columns:

::

    >>> dates = date_range('20130101', periods=6)
    >>> dates
    DateTimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04', '2013-01-05', '2013-01-06'])
    
    >>> df = DataFrame(random.randn(6,4), index=dates, columns=list('ABCD'))
    >>> df
                       A         B         C         D
    2013-01-01  0.730520  0.088258  0.488905  0.461837
    2013-01-02  0.448598  0.697712  0.277767  0.759961
    2013-01-03  0.219245  0.920414  0.886056  0.222002
    2013-01-04  0.883879  0.439466  0.392876  0.994732
    2013-01-05  0.881501  0.283149  0.247825  0.593564
    2013-01-06  0.511849  0.077208  0.040160  0.683068

Creating a DataFrame by passing a dict of objects that can be converted to series-like.
    
::

    >>> df = DataFrame({'A' : 1.,
    ...     'C' : [1,2,3,4],
    ...     'D' : array([3] * 4),
    ...     'E' : ['test','train','test','train'],
    ...     'F' : 'foo'})
    >>> df
         A C D     E   F
    0  1.0 1 3  test foo
    1  1.0 2 3 train foo
    2  1.0 3 3  test foo
    3  1.0 4 3 train foo

Viewing Data
=============

Here is how to view the top and bottom rows of the frame:

::

    >>> df.head()
                       A         B         C         D
    2013-01-01  0.730520  0.088258  0.488905  0.461837
    2013-01-02  0.448598  0.697712  0.277767  0.759961
    2013-01-03  0.219245  0.920414  0.886056  0.222002
    2013-01-04  0.883879  0.439466  0.392876  0.994732
    2013-01-05  0.881501  0.283149  0.247825  0.593564
    ...
    >>> df.tail(3)
                       A         B         C         D
    2013-01-04  0.883879  0.439466  0.392876  0.994732
    2013-01-05  0.881501  0.283149  0.247825  0.593564
    2013-01-06  0.511849  0.077208  0.040160  0.683068

Display the index, columns, and the underlying array data:

::

    >>> df.index
    DateTimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04', '2013-01-05', '2013-01-06'])
    >>> df.columns
    Index(['A', 'B', 'C', 'D'])
    >>> df.values
    array([[0.730519863614471, 0.08825840967622589, 0.4889045498516358, 0.461837214623537]
          [0.4485983912283127, 0.6977123432245299, 0.2777673057578094, 0.7599608278137966]
          [0.21924450192488787, 0.9204140116502296, 0.886055787176944, 0.22200160212508913]
          [0.8838785592364334, 0.43946558709097283, 0.3928764411717487, 0.9947320023919717]
          [0.8815007984632135, 0.2831489393823492, 0.24782537013522343, 0.5935642792213479]
          [0.5118487849556497, 0.07720751395148084, 0.04016027357410157, 0.6830675875686567]])


``describe()`` shows a quick statistic summary of the data:

::

    >>> df.describe()
                  A         B         C         D
    count  6.000000  6.000000  6.000000  6.000000
     mean  0.612598  0.417701  0.388932  0.619194
      std  0.265172  0.338873  0.286724  0.263857
      var  0.070316  0.114835  0.082211  0.069621
      max  0.883879  0.920414  0.886056  0.994732
      min  0.219245  0.077208  0.040160  0.222002

Transposing the data:

::

    >>> df.T
      2013-01-01 2013-01-02 2013-01-03 2013-01-04 2013-01-05 2013-01-06
    A   0.730520   0.448598   0.219245   0.883879   0.881501   0.511849
    B   0.088258   0.697712   0.920414   0.439466   0.283149   0.077208
    C   0.488905   0.277767   0.886056   0.392876   0.247825   0.040160
    D   0.461837   0.759961   0.222002   0.994732   0.593564   0.683068

Sorting by index:

::

    >>> df.sort_index(ascending=False)
                       A         B         C         D
    2013-01-06  0.511849  0.077208  0.040160  0.683068
    2013-01-05  0.881501  0.283149  0.247825  0.593564
    2013-01-04  0.883879  0.439466  0.392876  0.994732
    2013-01-03  0.219245  0.920414  0.886056  0.222002
    2013-01-02  0.448598  0.697712  0.277767  0.759961
    2013-01-01  0.730520  0.088258  0.488905  0.461837

Sorting by values:

::

    >>> df.sort_values(by='B')
                       A         B         C         D
    2013-01-06  0.511849  0.077208  0.040160  0.683068
    2013-01-01  0.730520  0.088258  0.488905  0.461837
    2013-01-05  0.881501  0.283149  0.247825  0.593564
    2013-01-04  0.883879  0.439466  0.392876  0.994732
    2013-01-02  0.448598  0.697712  0.277767  0.759961
    2013-01-03  0.219245  0.920414  0.886056  0.222002

Selection
==========

**Getting**

Selecting a single column, which yields a Series, equivalent to df.A:

::

    >>> df['A']
    2013-01-01  0.730519863614471
    2013-01-02  0.4485983912283127
    2013-01-03  0.21924450192488787
    2013-01-04  0.8838785592364334
    2013-01-05  0.8815007984632135
    2013-01-06  0.5118487849556497

Selecting via [], which slices the rows.

::

    >>> df[0:3]
                       A         B         C         D
    2013-01-01  0.730520  0.088258  0.488905  0.461837
    2013-01-02  0.448598  0.697712  0.277767  0.759961
    2013-01-03  0.219245  0.920414  0.886056  0.222002

    >>> df['20130102':'20130104']
                       A         B         C         D
    2013-01-02  0.448598  0.697712  0.277767  0.759961
    2013-01-03  0.219245  0.920414  0.886056  0.222002
    2013-01-04  0.883879  0.439466  0.392876  0.994732

**Selection by Label**

For getting a cross section using a label:

::

    >>> df.loc[dates[0]]
    A  0.730519863614471
    B  0.08825840967622589
    C  0.4889045498516358
    D  0.461837214623537

Selecting on a multi-axis by label:

::

    >>> df.loc[:,['A','B']]
                       A         B
    2013-01-01  0.730520  0.088258
    2013-01-02  0.448598  0.697712
    2013-01-03  0.219245  0.920414
    2013-01-04  0.883879  0.439466
    2013-01-05  0.881501  0.283149
    2013-01-06  0.511849  0.077208

Showing label slicing, both endpoints are included:

::

    >>> df.loc['20130102':'20130104',['A','B']]
                       A         B
    2013-01-02  0.448598  0.697712
    2013-01-03  0.219245  0.920414
    2013-01-04  0.883879  0.439466

Reduction in the dimensions of the returned object:

::

    >>> df.loc['20130102',['A','B']]
    A  0.4485983912283127
    B  0.6977123432245299
 
For getting a scalar value:

::

    >>> df.at[dates[0],'A']
    0.730519863614471

**Selection by Position**

Select via the position of the passed integers:

::

    >>> df.iloc[3]
    A  0.8838785592364334
    B  0.43946558709097283
    C  0.3928764411717487
    D  0.9947320023919717

By integer slices:
    
::

    >>> df.iloc[3:5,0:2]
                       A         B
    2013-01-04  0.883879  0.439466
    2013-01-05  0.881501  0.283149
    
By lists of integer position locations:

::

    >>> df.iloc[[1,2,4],[0,2]]
                       A         C
    2013-01-02  0.448598  0.277767
    2013-01-03  0.219245  0.886056
    2013-01-05  0.881501  0.247825

For getting a value explicitly:

::

    >>> df.iloc[1,1]
    0.6977123432245299

For getting fast access to a scalar (equivalent to the prior method):

::

    >>> df.iat[1,1]
    0.6977123432245299

Grouping
==========

::

    >>> df = DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
    ...                        'foo', 'bar', 'foo', 'foo'],
    ...                 'B' : ['one', 'one', 'two', 'three',
    ...                        'two', 'two', 'one', 'three'],
    ...                 'C' : random.randn(8),
    ...                 'D' : random.randn(8)})
    >>> df
        A     B         C         D
    0 foo   one  0.235064  0.235064
    1 bar   one -0.419857 -0.419857
    2 foo   two -0.888507 -0.888507
    3 bar three -3.056019 -3.056019
    4 foo   two -0.476107 -0.476107
    5 bar   two  1.831309  1.831309
    6 foo   one -0.800894 -0.800894
    7 foo three  0.936860  0.936860

Grouping and then applying the sum() function to the resulting groups.

::

    >>> df.groupby('A').sum()
                 C          D
    foo  -0.993584  -0.993584
    bar  -1.644567  -1.644567
    
Grouping by multiple columns forms a hierarchical index, and again we can apply the sum function.

::

    >>> df.groupby(['A','B']).sum()
                 C         D
    [foo, one] -0.565830 -0.565830
    [bar, one] -0.419857 -0.419857
    [foo, two] -1.364614 -1.364614
    [bar, three] -3.056019 -3.056019
    [bar, two]  1.831309  1.831309
    [foo, three]  0.936860  0.936860

Time resample
==============

To performing resampling operations during frequency conversion (e.g., converting secondly data into 
5-minutely data):

::

    >>> rng = date_range('1/1/2012', periods=100, freq='S')
    >>> ts = Series(np.random.randint(0, 500, len(rng)), index=rng)
    >>> ts.resample('5Min').sum()
    2012-01-01 00:00  22561.0
    