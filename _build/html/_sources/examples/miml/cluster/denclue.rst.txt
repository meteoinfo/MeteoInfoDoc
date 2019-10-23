.. _examples-miml-cluster-denclue:

************************
DENsity CLUstering
************************

DENCLUE (DENsity CLUstering) employs a cluster model based on kernel density estimation. A cluster is 
defined by a local maximum of the estimated density function. Data points going to the same local 
maximum are put into the same cluster. DENCLUE works efficiently for high-dimensional data sets and 
allows arbitrary noise levels while still guaranteeing to find the clustering.

::

    from miml.cluster import DENCLUE

    fn = os.path.join(datasets.get_data_home(), 'clustering', 'gaussian', 
        'six.txt')
    df = DataFrame.read_table(fn, header=None, names=['x1','x2'], 
        format='%2f')
    x = df.values

    model = DENCLUE(1.0, 50)
    y = model.fit_predict(x)

    scatter(x[:,0], x[:,1], c=y, edgecolor=None, s=3)
    title('DENsity CLUstering example')
    
.. image:: ../../../_static/miml/denclue_1.png