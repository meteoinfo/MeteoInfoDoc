.. _docs-meteoinfolab-numeric-stats-chisquare:


************
chisquare
************

.. currentmodule:: numeric.stats

.. function:: chisquare(f_obs, f_exp=None)

    Calculates a one-way chi square test.

    The chi square test tests the null hypothesis that the categorical data has the 
    given frequencies.
    
    :param f_obs: (*array_like*) Observed frequencies in each category.
    :param f_exp: (*array_like*) Expected frequencies in each category. By default the categories 
        are assumed to be equally likely.
    
    :returns: Chi-square statistic and p-value
    
    Examples::
    
        from mipylib.numeric import stats

        r = stats.chisquare([16, 18, 16, 14, 12, 12], [16, 16, 16, 16, 16, 8])
        print r

    Result::
    
        >>> run script...
        (3.5, 0.623387627749582)