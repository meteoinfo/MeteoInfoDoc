.. _examples-miml-regression-lasso:

*************************************
Lasso Regression
*************************************

Lasso (least absolute shrinkage and selection operator) regression is a shrinkage and selection 
method for linear regression. It minimizes the usual sum of squared errors, with a bound on the 
sum of the absolute values of the coefficients (i.e. L1-regularized). It has connections to 
soft-thresholding of wavelet coefficients, forward stage-wise regression, and boosting methods.

The Lasso typically yields a sparse solution, of which the parameter vector β has relatively few 
nonzero coefficients. In contrast, the solution of L2-regularized least squares (i.e. ridge 
regression) typically has all coefficients nonzero. Because it effectively reduces the number 
of variables, the Lasso is useful in some contexts.

There is no analytic formula or expression for the optimal solution to the L1-regularized least 
squares problems. Therefore, its solution must be computed numerically. The objective function in 
the L1-regularized least squares is convex but not differentiable, so solving it is more of a 
computational challenge than solving the L2-regularized least squares. The Lasso may be solved 
using quadratic programming or more general convex optimization methods, as well as by specific 
algorithms such as the least angle regression algorithm.

::

    from miml import datasets
    from miml.regression import LASSO

    fn = os.path.join(datasets.get_data_home(), 'regression', 
        'diabetes.csv')
    df = DataFrame.read_table(fn, delimiter=',', 
        format='%64f', index_col=0)

    x = df.values
    y = array(df.index.data)

    model = LASSO(10)
    model.fit(x, y)

    print model
    
::

    >>> run script...
    LASSO:

    Residuals:
               Min	        1Q	    Median	        3Q	       Max
         -156.0745	  -30.4014	   -3.1887	   31.4334	  149.7378


    Coefficients:
                Estimate
    Intercept   152.1335

    Var 1	     42.2524

    Var 2	   -257.7338

    Var 3	    449.3283

    Var 4	    341.2134

    Var 5	   -185.8292

    Var 6	     -1.3917

    Var 7	   -158.5119

    Var 8	    121.4534

    Var 9	    677.1183

    Var 10	     68.3447

    Var 11	     70.5993

    Var 12	     50.9044

    Var 13	     -7.6045

    Var 14	    560.1727

    Var 15	     -1.9227

    Var 16	    262.6268

    Var 17	    556.6405

    Var 18	    480.8531

    Var 19	    116.6087

    Var 20	    165.4373

    Var 21	     -8.5606

    Var 22	     15.5317

    Var 23	   -169.8404

    Var 24	    -63.1208

    Var 25	    222.9773

    Var 26	    185.1293

    Var 27	    114.1537

    Var 28	     60.7931

    Var 29	     70.9789

    Var 30	     86.5622

    Var 31	    345.4959

    Var 32	   -289.2375

    Var 33	    -77.4019

    Var 34	   -100.5561

    Var 35	   -115.9185

    Var 36	     48.2530

    Var 37	    158.0210

    Var 38	   -539.1530

    Var 39	    441.9235

    Var 40	    197.2877

    Var 41	    -28.1507

    Var 42	    156.7630

    Var 43	     28.3774

    Var 44	    345.3906

    Var 45	   -210.9563

    Var 46	   -127.9888

    Var 47	    -54.1669

    Var 48	   -105.2098

    Var 49	   -143.7805

    Var 50	   -185.4770

    Var 51	   -362.4059

    Var 52	   -697.8575

    Var 53	   -974.6574

    Var 54	    -59.0982

    Var 55	    -88.6933

    Var 56	    -68.7470

    Var 57	    782.8276

    Var 58	    -25.0998

    Var 59	    508.6851

    Var 60	    286.4917

    Var 61	    177.2804

    Var 62	    -70.9310

    Var 63	    241.0674

    Var 64	     39.9994


    Residual standard error: 53.3841 on 377 degrees of freedom

    Multiple R-squared: 0.5901,    Adjusted R-squared: 0.5205

    F-statistic: 8.4796 on 64 and 377 DF,  p-value: 4.440e-43
