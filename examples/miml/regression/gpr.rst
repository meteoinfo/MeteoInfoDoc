.. _examples-miml-regression-gpr:

*************************************
Gaussian Process
*************************************

A Gaussian process is a stochastic process whose realizations consist of random values associated with 
every point in a range of times (or of space) such that each such random variable has a normal 
distribution. Moreover, every finite collection of those random variables has a multivariate normal 
distribution.

A Gaussian process can be used as a prior probability distribution over functions in Bayesian 
inference. Given any set of N points in the desired domain of your functions, take a multivariate 
Gaussian whose covariance matrix parameter is the Gram matrix of N points with some desired kernel, 
and sample from that Gaussian. Inference of continuous values with a Gaussian process prior is known 
as Gaussian process regression.

::

    from miml import datasets
    from miml.regression import GaussianProcessRegression

    fn = os.path.join(datasets.get_data_home(), 'regression', 
        'diabetes.csv')
    df = DataFrame.read_table(fn, delimiter=',', 
        format='%64f', index_col=0)

    x = df.values
    y = array(df.index.data)

    model = GaussianProcessRegression(x, y, sigma=0.06, L=0.01)
    print(model.predict(x[:10,:]))
    
::

    >>> run script...
    array([149.63350796115427, 74.28911292438774, 139.68088364423298, 203.983666653454, 134.05095165718586, 96.03965267973412, 136.64741122676267, 62.37623771726341, 108.97096286320787, 306.95039738967637])
