.. _docs-meteoinfolab-numeric-stats-pearsonr:


**********
pearsonr
**********

.. currentmodule:: numeric.stats

.. function:: pearsonr(x, y)

    Calculates a Pearson correlation coefficient and the p-value for testing non-correlation.

    The Pearson correlation coefficient measures the linear relationship between two datasets. 
    Strictly speaking, Pearson’s correlation requires that each dataset be normally distributed, 
    and not necessarily zero-mean. Like other correlation coefficients, this one varies between 
    -1 and +1 with 0 implying no correlation. Correlations of -1 or +1 imply an exact linear 
    relationship. Positive correlations imply that as x increases, so does y. Negative 
    correlations imply that as x increases, y decreases.

    The p-value roughly indicates the probability of an uncorrelated system producing datasets 
    that have a Pearson correlation at least as extreme as the one computed from these datasets. 
    The p-values are not entirely reliable but are probably reasonable for datasets larger than 
    500 or so.
    
    :param x: (*array_like*) x data array.
    :param y: (*array_like*) y data array.
    
    :returns: Pearson’s correlation coefficient and 2-tailed p-value.
    
    Examples::
    
        from mipylib.numeric import stats

        y = [29.81,30.04,41.7,43.71,28.75,37.73,52.25,32.41,25.67,28.17,25.71,36.05,37.62,34.28,38.82,40.15,35.69,28.36,39.56,52.56,54.14,50.76,39.35,43.16]
        x = [51.6,46,64.3,83.4,65.9,49.5,88.6,101.4,55.9,41.8,33.4,57.3,66.5,40.5,72.3,70,83.3,65.8,63.1,83.4,102,94,77,77]
        r, p = stats.pearsonr(x, y)
        print r, p

    Result::
    
        >>> run script...
        0.700798023949 0.000136713449709