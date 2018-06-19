.. _docs-meteoinfolab-numeric-stats-spearmanr:


**********
spearmanr
**********

.. currentmodule:: numeric.stats

.. function:: spearmanr(m, y=None, axis=0)

    Calculates a Spearman rank-order correlation coefficient.
    
    The Spearman correlation is a nonparametric measure of the monotonicity of the relationship 
    between two datasets. Unlike the Pearson correlation, the Spearman correlation does not 
    assume that both datasets are normally distributed. Like other correlation coefficients, 
    this one varies between -1 and +1 with 0 implying no correlation. Correlations of -1 or +1 
    imply an exact monotonic relationship. Positive correlations imply that as x increases, so 
    does y. Negative correlations imply that as x increases, y decreases.
    
    :param m: (*array_like*) A 1-D or 2-D array containing multiple variables and observations.
    :param y: (*array_like*) Optional. An additional set of variables and observations. y has the same form as 
        that of m.
    :param axis: (*int*) If axis=0 (default), then each column represents a variable, with 
        observations in the rows. If axis=1, the relationship is transposed: each row represents 
        a variable, while the columns contain observations..
    
    :returns: Spearman correlation matrix.
    
    Examples::
    
        from mipylib.numeric import stats

        y = [1,2,3,4,5]
        x = [5,6,7,8,7]
        r = stats.spearmanr(x, y)
        print r

    Result::
    
        >>> run script...
        array([[1.0, 0.8207826816681233]
              [0.8207826816681233, 1.0]])