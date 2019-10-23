.. _examples-miml-regression-rbfnet:

*************************************
Radial Basis Function Networks
*************************************

A radial basis function network is an artificial neural network that uses radial basis functions as 
activation functions. It is a linear combination of radial basis functions. They are used in 
function approximation, time series prediction, and control.

::

    from miml import datasets
    from miml.regression import RBFNetwork

    fn = os.path.join(datasets.get_data_home(), 'regression', 
        'diabetes.csv')
    df = DataFrame.read_table(fn, delimiter=',', 
        format='%64f', index_col=0)

    x = df.values
    y = array(df.index.data)

    model = RBFNetwork(ncenters=10)
    model.fit(x, y)

    print(model.predict(x[:10,:]))
    
::

    >>> run script...
    array([184.24810109990693, 56.45535138916093, 84.27105955131076, 263.694752740725, 89.74377301427681, 120.98329139858919, 150.4263763674829, 79.06152761584222, 108.62840807898104, 94.94832854058508])
