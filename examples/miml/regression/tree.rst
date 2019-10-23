.. _examples-miml-regression-tree:

*************************************
Regression Tree
*************************************

Similar to decision trees, regression trees can be learned by splitting the training set into subsets 
based on an attribute value test. This process is repeated on each derived subset in a recursive manner 
called recursive partitioning. The recursion is completed when the subset at a node all has the same 
value of the target variable, or when splitting no longer adds value to the predictions.

::

    from miml import datasets
    from miml.regression import RegressionTree

    fn = os.path.join(datasets.get_data_home(), 'regression', 
        'diabetes.csv')
    df = DataFrame.read_table(fn, delimiter=',', 
        format='%64f', index_col=0)

    x = df.values
    y = array(df.index.data)

    model = RegressionTree(200)
    model.fit(x, y)

    print(model.predict(x[:10,:]))
    
::

    >>> run script...
    array([201.4, 59.44444444444444, 122.2, 195.42857142857142, 72.8, 88.5, 121.625, 65.83333333333333, 83.5, 267.0])
