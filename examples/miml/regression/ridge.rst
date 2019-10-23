.. _examples-miml-regression-ridge:

*************************************
Ridge Regression
*************************************

Coefficient estimates for multiple linear regression models rely on the independence of the model 
terms. When terms are correlated and the columns of the design matrix X have an approximate linear 
dependence, the matrix X'X becomes close to singular. As a result, the least-squares estimate becomes 
highly sensitive to random errors in the observed response Y, producing a large variance.

Ridge regression is one method to address these issues. In ridge regression, the matrix X'X is 
perturbed so as to make its determinant appreciably different from 0.

Ridge regression is a kind of Tikhonov regularization, which is the most commonly used method of 
regularization of ill-posed problems. Ridge regression shrinks the regression coefficients by 
imposing a penalty on their size. By allowing a small amount of bias in the estimates, more 
reasonable coefficients may often be obtained. Often, small amounts of bias lead to dramatic 
reductions in the variance of the estimated model coefficients.

Another interpretation of ridge regression is available through Bayesian estimation. In this setting 
the belief that weight should be small is coded into a prior distribution.

::

    from miml import datasets
    from miml.regression import RidgeRegression

    x = array([[234.289,      235.6,        159.0,    107.608, 1947,   60.323],
            [259.426,      232.5,        145.6,    108.632, 1948,   61.122],
            [258.054,      368.2,        161.6,    109.773, 1949,   60.171],
            [284.599,      335.1,        165.0,    110.929, 1950,   61.187],
            [328.975,      209.9,        309.9,    112.075, 1951,   63.221],
            [346.999,      193.2,        359.4,    113.270, 1952,   63.639],
            [365.385,      187.0,        354.7,    115.094, 1953,   64.989],
            [363.112,      357.8,        335.0,    116.219, 1954,   63.761],
            [397.469,      290.4,        304.8,    117.388, 1955,   66.019],
            [419.180,      282.2,        285.7,    118.734, 1956,   67.857],
            [442.769,      293.6,        279.8,    120.445, 1957,   68.169],
            [444.546,      468.1,        263.7,    121.950, 1958,   66.513],
            [482.704,      381.3,        255.2,    123.366, 1959,   68.655],
            [502.601,      393.1,        251.4,    125.368, 1960,   69.564],
            [518.173,      480.6,        257.2,    127.852, 1961,   69.331],
            [554.894,      400.7,        282.7,    130.081, 1962,   70.551]])
    y = array([83.0,  88.5,  88.2,  89.5,  96.2,  98.1,  99.0, 100.0, 101.2,
               104.6, 108.4, 110.8, 112.6, 114.2, 115.7, 116.9])
    model = RidgeRegression(0.0057)
    model.fit(x, y)

    print(model.predict(x[:10,:]))
    
::

    >>> run script...
    array([83.71913397911655])
    >>> model
    Ridge Regression:

    Residuals:
               Min	        1Q	    Median	        3Q	       Max
           -2.0691	   -0.5736	    0.2619	    0.4844	    1.6328


    Coefficients:
                Estimate        Std. Error        t value        Pr(>|t|)
    Intercept  -247.2810                NA             NA              NA

    Var 1	      0.1789            7.8561         0.0228          0.9823 

    Var 2	      0.0197            2.0319         0.0097          0.9925 

    Var 3	      0.0066            0.8647         0.0076          0.9941 

    Var 4	     -1.3433            4.2777        -0.3140          0.7607 

    Var 5	      0.2216            9.7525         0.0227          0.9824 

    Var 6	     -0.0575            3.7635        -0.0153          0.9881 

    ---------------------------------------------------------------------
    Significance codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 1.2361 on 9 degrees of freedom

    Multiple R-squared: 0.9921,    Adjusted R-squared: 0.9869

    F-statistic: 189.0534 on 6 and 9 DF,  p-value: 6.011e-09