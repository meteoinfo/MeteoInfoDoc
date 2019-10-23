.. _examples-miml-regression-ols:

*************************************
Ordinary Least Squares
*************************************

In linear regression, the model specification is that the dependent variable is a linear combination of 
the parameters. The residual is the difference between the value of the dependent variable predicted 
by the model, and the true value of the dependent variable. Ordinary least squares obtains parameter 
estimates that minimize the sum of squared residuals, SSE (also denoted RSS).

The ordinary least squares (OLS) estimator is consistent when the independent variables are exogenous 
and there is no multicollinearity, and optimal in the class of linear unbiased estimators when the 
errors are homoscedastic and serially uncorrelated. Under these conditions, the method of OLS 
provides minimum-variance mean-unbiased estimation when the errors have finite variances.

::

    from miml import datasets
    from miml.regression import OLS

    fn = os.path.join(datasets.get_data_home(), 'weka', 'regression', 
        '2dplanes.arff')
    ds = datasets.load_arff(fn, 10)
    x = ds.x
    y = ds.y

    model = OLS()
    model.fit(x, y)

    r = model.predict(x[:10,:])

    print r
    
::

    >>> run script...
    array([5.073347387304948])
    >>> model
    Linear Model:

    Residuals:
               Min	        1Q	    Median	        3Q	       Max
           -8.5260	   -1.6514	   -0.0049	    1.6755	    7.8116


    Coefficients:
                Estimate        Std. Error        t value        Pr(>|t|)
    Intercept    -0.0148            0.0118        -1.2503          0.2112 

    Var 1	      2.9730            0.0118       251.7998          0.0000 ***

    Var 2	      1.5344            0.0145       105.8468          0.0000 ***

    Var 3	      1.0357            0.0144        71.7815          0.0000 ***

    Var 4	      0.5281            0.0145        36.4827          0.0000 ***

    Var 5	      1.4766            0.0144       102.2472          0.0000 ***

    Var 6	      1.0044            0.0144        69.5380          0.0000 ***

    Var 7	      0.5238            0.0145        36.1696          0.0000 ***

    Var 8	     -0.0011            0.0145        -0.0750          0.9402 

    Var 9	      0.0024            0.0145         0.1649          0.8690 

    Var 10	     -0.0278            0.0145        -1.9239          0.0544 .

    ---------------------------------------------------------------------
    Significance codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 2.3838 on 40757 degrees of freedom

    Multiple R-squared: 0.7056,    Adjusted R-squared: 0.7055

    F-statistic: 9766.9504 on 10 and 40757 DF,  p-value: 0.000