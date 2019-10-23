.. _examples-miml-regression-svr:

*************************************
Support Vector Regression
*************************************

Support vector machine can be used as a regression method, maintaining all the main features of the 
algorithm. In the case of regression, a margin of tolerance ε is set in approximation. The goal of SVR 
is to find a function that has at most ε deviation from the response variable for all the training 
data, and at the same time is as flat as possible. In other words, we do not care about errors as long 
as they are less than ε, but will not accept any deviation larger than this.

Like SVM for classification, nonlinear SVR employs kernel trick for implict mapping. And the model 
produced by SVR depends only on a subset of the training data, because the cost function ignores any 
training data close to the model prediction (within the ε threshold).

::

    from miml import datasets
    from miml.regression import SVR

    fn = os.path.join(datasets.get_data_home(), 'regression', 
        'diabetes.csv')
    df = DataFrame.read_table(fn, delimiter=',', 
        format='%64f', index_col=0)

    x = df.values
    y = array(df.index.data)

    model = SVR(x, y, eps=20, C=10, sigma=0.06)
    print(model.predict(x[:10,:]))
    
::

    >>> run script...
    array([142.2071541042286, 131.17336799586252, 141.9969343397669, 151.74854896190865, 136.68999031380795, 131.67378007748619, 141.41197536235626, 131.67378321314663, 131.49468762528412, 151.24965587158746])
