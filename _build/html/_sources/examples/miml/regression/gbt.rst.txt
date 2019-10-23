.. _examples-miml-regression-gbt:

*************************************
Gradient Boosting
*************************************

Gradient boosting is typically used with decision trees (especially CART regression trees) of a fixed 
size as base learners. For this special case Friedman proposes a modification to gradient boosting 
method which improves the quality of fit of each base learner.

::

    from miml import datasets
    from miml.regression import GradientTreeBoost

    fn = os.path.join(datasets.get_data_home(), 'regression', 
        'diabetes.csv')
    df = DataFrame.read_table(fn, delimiter=',', 
        format='%64f', index_col=0)

    x = df.values
    y = array(df.index.data)

    model = GradientTreeBoost()
    model.fit(x, y)

    print(model.predict(x[:10,:]))
    
::

    >>> run script...
    array([194.7389360248372, 75.38935152901469, 167.1564225597021, 192.1702512661937, 99.397482512624, 100.2975566989432, 82.72846455873852, 91.96946209282093, 114.3010663633844, 219.91127834377713])
