.. _examples-miml-regression-rforest:

*************************************
Random Forest
*************************************

Random forest is an ensemble classifier that consists of many decision trees and outputs the majority 
vote of individual trees. The method combines bagging idea and the random selection of features.

Each tree is constructed using the following algorithm:

- If the number of cases in the training set is N, randomly sample N cases with replacement from the original data. This sample will be the training set for growing the tree.

- If there are M input variables, a number m << M is specified such that at each node, m variables are selected at random out of the M and the best split on these m is used to split the node. The value of m is held constant during the forest growing.

- Each tree is grown to the largest extent possible. There is no pruning.

::

    from miml import datasets
    from miml.regression import RandomForest

    fn = os.path.join(datasets.get_data_home(), 'regression', 
        'diabetes.csv')
    df = DataFrame.read_table(fn, delimiter=',', 
        format='%64f', index_col=0)

    x = df.values
    y = array(df.index.data)

    model = RandomForest(max_nodes=200)
    model.fit(x, y)

    print(model.predict(x[:10,:]))
    
::

    >>> run script...
    array([181.82626507936502, 82.71104862914865, 160.33670873015865, 183.59972301587305, 121.25169920634929, 109.46714523809518, 103.04361904761905, 115.80702063492069, 134.72605714285723, 222.78942936507926])
