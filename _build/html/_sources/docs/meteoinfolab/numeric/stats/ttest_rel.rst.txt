.. _docs-meteoinfolab-numeric-stats-ttest_rel:


************
ttest_rel
************

.. currentmodule:: numeric.stats

.. function:: ttest_rel(a, b)

    Calculates the T-test on TWO RELATED samples of scores, a and b.

    This is a two-sided test for the null hypothesis that 2 related or repeated samples 
    have identical average (expected) values.
    
    :param a: (*array_like*) Sample data a.
    :param b: (*array_like*) Sample data b.
    
    :returns: t-statistic and p-value
    
    Examples::
    
        from mipylib.numeric import stats

        a = [3,5,4,6,5,5,4,5,3,6,7,8,7,6,7,8,8,9,9,8,7,7,6,7,8]  
        b = [7,8,6,7,8,9,6,6,7,8,8,7,9,10,9,9,8,8,4,4,5,6,9,8,12]  
        t,p=stats.ttest_rel(a,b)  
        print 't-statistic: %f' % t  
        print 'p-value: %f' % p

    Result::
    
        >>> run script...
        t-statistic: -2.449490
        p-value: 0.021983