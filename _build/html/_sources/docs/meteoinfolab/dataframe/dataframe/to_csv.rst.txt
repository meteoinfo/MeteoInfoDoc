.. _docs-meteoinfolab-dataframe-dataframe-DataFrame-to_csv:


*******************
to_csv
*******************

.. method:: DataFrame.to_csv(filepath, delimiter=',', format=None, date_format=None, \
        float_format=None, index=True)

    Save the data to an csv file.
        
    :param filename: (*string*) The file name.
    :param delimiter: (*string*) Field delimiter character. Default is ``,``.
    :param format: (*string*) Format string.
    :param date_format: (*string*) Date format string. i.e. 'yyyyMMddHH'.
    :param float_format: (*string*) Float format string. i.e. '%.2f'.
    :param index: (*boolean*) Write index or not.

    Examples::

        df = DataFrame({'name': ['Raphael', 'Donatello'],
                   'mask': ['red', 'purple'],
                   'weapon': ['sai', 'bo staff']})
        df.to_csv('D:/Test/out.csv')