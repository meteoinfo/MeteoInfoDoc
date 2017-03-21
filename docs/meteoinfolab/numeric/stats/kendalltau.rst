.. _docs-meteoinfolab-numeric-stats-kendalltau:


**********
kendalltau
**********

.. currentmodule:: numeric.stats

.. function:: kendalltau(x, y)

    Calculates Kendall's tau, a correlation measure for ordinal data.
    
    Kendall's tau is a measure of the correspondence between two rankings.
    Values close to 1 indicate strong agreement, values close to -1 indicate
    strong disagreement.  This is the 1945 "tau-b" version of Kendall's
    tau [2]_, which can account for ties and which reduces to the 1938 "tau-a"
    version [1]_ in absence of ties.
    
    :param x: (*array_like*) x data array.
    :param y: (*array_like*) y data array.
    
    :returns: Correlation.
    
    Notes
    -----
    The definition of Kendall's tau that is used is [2]_::
      tau = (P - Q) / sqrt((P + Q + T) * (P + Q + U))
    where P is the number of concordant pairs, Q the number of discordant
    pairs, T the number of ties only in `x`, and U the number of ties only in
    `y`.  If a tie occurs for the same pair in both `x` and `y`, it is not
    added to either T or U.
    References
    ----------
    .. [1] Maurice G. Kendall, "A New Measure of Rank Correlation", Biometrika
           Vol. 30, No. 1/2, pp. 81-93, 1938.
    .. [2] Maurice G. Kendall, "The treatment of ties in ranking problems",
           Biometrika Vol. 33, No. 3, pp. 239-251. 1945.
    .. [3] Gottfried E. Noether, "Elements of Nonparametric Statistics", John
           Wiley & Sons, 1967.
    .. [4] Peter M. Fenwick, "A new data structure for cumulative frequency
           tables", Software: Practice and Experience, Vol. 24, No. 3,
           pp. 327-336, 1994.
    
    Examples::
    
        from mipylib.numeric import stats

        x1 = [12, 2, 1, 12, 2]
        x2 = [1, 4, 7, 1, 0]
        tau = stats.kendalltau(x1, x2)
        print tau

    Result::
    
        >>> run script...
        -0.471404520791