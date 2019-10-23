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

    print(LASSO(x, y, 10))
    print(LASSO(x, y, 100))
    print(LASSO(x, y, 500))
    
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


    LASSO:

    Residuals:
               Min	        1Q	    Median	        3Q	       Max
         -150.8634	  -30.2993	   -0.9237	   31.4198	  150.6769


    Coefficients:
                Estimate
    Intercept   152.1335

    Var 1	     36.6525

    Var 2	   -245.5668

    Var 3	    463.0968

    Var 4	    335.7204

    Var 5	   -158.2084

    Var 6	     -0.5220

    Var 7	   -191.6142

    Var 8	     78.5352

    Var 9	    646.8603

    Var 10	     67.2958

    Var 11	     76.0344

    Var 12	     51.5637

    Var 13	    -14.2055

    Var 14	      0.1245

    Var 15	      0.0952

    Var 16	     -4.1430

    Var 17	    109.8307

    Var 18	    305.8216

    Var 19	    109.5986

    Var 20	    169.0939

    Var 21	     -7.1909

    Var 22	     21.3213

    Var 23	     -0.2355

    Var 24	   -164.5738

    Var 25	    125.8486

    Var 26	    127.8888

    Var 27	     56.0188

    Var 28	     41.7694

    Var 29	     72.5458

    Var 30	     81.4176

    Var 31	     73.8387

    Var 32	    -89.7767

    Var 33	     46.0889

    Var 34	    -51.4487

    Var 35	    -24.2738

    Var 36	     35.8418

    Var 37	    159.7508

    Var 38	   -128.9617

    Var 39	     65.6612

    Var 40	     51.4690

    Var 41	     -1.9807

    Var 42	     -0.0582

    Var 43	     30.0582

    Var 44	     73.7347

    Var 45	      6.2924

    Var 46	      1.3435

    Var 47	    -35.8823

    Var 48	     -1.5986

    Var 49	   -128.8626

    Var 50	    124.5337

    Var 51	     -0.2666

    Var 52	   -304.1846

    Var 53	   -539.6028

    Var 54	    -40.2991

    Var 55	    -74.2158

    Var 56	     -0.4553

    Var 57	    545.3053

    Var 58	     -0.7582

    Var 59	      0.2111

    Var 60	    177.0759

    Var 61	    134.8773

    Var 62	    -62.3075

    Var 63	    192.0340

    Var 64	     21.6115


    Residual standard error: 53.6649 on 377 degrees of freedom

    Multiple R-squared: 0.5858,    Adjusted R-squared: 0.5154

    F-statistic: 8.3296 on 64 and 377 DF,  p-value: 2.561e-42


    LASSO:

    Residuals:
               Min	        1Q	    Median	        3Q	       Max
         -145.6406	  -34.9690	   -1.6296	   31.7290	  150.4327


    Coefficients:
                Estimate
    Intercept   152.1335

    Var 1	     19.7381

    Var 2	   -215.2641

    Var 3	    491.3508

    Var 4	    318.3337

    Var 5	    -73.9669

    Var 6	     -0.1219

    Var 7	   -271.3485

    Var 8	      0.3327

    Var 9	    536.7865

    Var 10	     56.9666

    Var 11	     62.4591

    Var 12	     39.6532

    Var 13	     -0.0997

    Var 14	      0.0402

    Var 15	      0.0367

    Var 16	      0.0299

    Var 17	      5.1949

    Var 18	      0.0054

    Var 19	    109.8448

    Var 20	    161.9601

    Var 21	     -0.0513

    Var 22	     20.8245

    Var 23	     -0.0211

    Var 24	    -74.1101

    Var 25	     52.2148

    Var 26	      0.0487

    Var 27	     76.2901

    Var 28	     35.3560

    Var 29	     52.1337

    Var 30	     67.5079

    Var 31	     -0.0170

    Var 32	    -33.3879

    Var 33	     77.8882

    Var 34	     -5.6083

    Var 35	     -0.0811

    Var 36	      4.2298

    Var 37	    142.5695

    Var 38	    -13.2135

    Var 39	     -0.0544

    Var 40	      0.0154

    Var 41	     -0.0150

    Var 42	      0.0723

    Var 43	      0.3325

    Var 44	     25.7653

    Var 45	      0.2970

    Var 46	     38.7466

    Var 47	     -0.0526

    Var 48	      0.0269

    Var 49	    -77.7430

    Var 50	      0.2351

    Var 51	     11.5565

    Var 52	    -92.0404

    Var 53	    -41.8455

    Var 54	      0.3094

    Var 55	     -0.0218

    Var 56	      0.0278

    Var 57	    163.1993

    Var 58	      2.8986

    Var 59	    -94.6948

    Var 60	      0.0827

    Var 61	     23.1071

    Var 62	   -114.8251

    Var 63	     66.9084

    Var 64	      0.1338


    Residual standard error: 54.5366 on 377 degrees of freedom

    Multiple R-squared: 0.5722,    Adjusted R-squared: 0.4996

    F-statistic: 7.8787 on 64 and 377 DF,  p-value: 5.422e-40