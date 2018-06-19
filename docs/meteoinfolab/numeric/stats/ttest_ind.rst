.. _docs-meteoinfolab-numeric-stats-ttest_ind:


************
ttest_ind
************

.. currentmodule:: numeric.stats

.. function:: ttest_ind(a, b)

    Calculates the T-test for the means of TWO INDEPENDENT samples of scores.

    This is a two-sided test for the null hypothesis that 2 independent samples have 
    identical average (expected) values. This test assumes that the populations have 
    identical variances.
    
    :param a: (*array_like*) Sample data a.
    :param b: (*array_like*) Sample data b.
    
    :returns: t-statistic and p-value
    
    Examples::
    
        from mipylib.numeric import stats

        random.seed(1)
        # Create sample data.
        a = random.randn(40)
        b = 4 * random.randn(50)

        r = stats.ttest_ind(a, b)
        print r

    Result::
    
        >>> run script...
        (1.4947945927091304, 0.14061883167278577)