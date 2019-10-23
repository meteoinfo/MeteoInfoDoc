.. _examples-miml-cluster-dbscan:

************************************************************
Density-Based Spatial Clustering of Applications with Noise
************************************************************

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) finds a number of clusters 
starting from the estimated density distribution of corresponding nodes.

::

    from miml import datasets
    from miml.cluster import DBSCAN

    fn = os.path.join(datasets.get_data_home(), 'clustering', 'chameleon', 
        't4.8k.txt')
    df = DataFrame.read_table(fn, header=None, names=['x1','x2'], 
        format='%2f')
    x = df.values

    model = DBSCAN(min_pts=20, radius=10)
    y = model.fit_predict(x)

    k = 6
    levs = range(k)
    levs.append(int(y.max()))
    cols = makecolors(k)
    cols.append('gray')
    scatter(x[:,0], x[:,1], c=y, edgecolor=None, s=3, levels=levs, colors=cols)
    title('Density-Based Spatial Clustering of Applications with Noise example')
    
.. image:: ../../../_static/miml/dbscan_1.png