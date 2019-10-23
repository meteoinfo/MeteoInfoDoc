.. _examples-miml-cluster-clarans:

**********************************************************
Clustering Large Applications based upon RANdomized Search
**********************************************************

The K-Medoids algorithm is an adaptation of the k-means algorithm. Rather than calculate the mean of 
the items in each cluster, a representative item, or medoid, is chosen for each cluster at each 
iteration. The K-Medoids algorithm attempts to minimize the distance between points labeled to be in a 
cluster and the medoid of that cluster. So a medoid is a most centrally located point in the cluster. 
K-Medoids works with an arbitrary matrix of distances between data points instead of L2. It is also 
more robust to noise and outliers as compared to K-Means.

The most common realisation of K-Medoids clustering is the Partitioning Around Medoids (PAM) algorithm. 
PAM uses a greedy search which may not find the optimum solution, but it is faster than exhaustive 
search.

CLARANS (Clustering Large Applications based upon RANdomized Search) is a more efficient medoid-based 
clustering algorithm. In CLARANS, the process of finding k medoids from n objects is viewed abstractly 
as searching through a certain graph. In the graph, a node is represented by a set of k objects as 
selected medoids. Two nodes are neighbors if their sets differ by only one object. In each iteration, 
CLARANS considers a set of randomly chosen neighbor nodes as candidate of new medoids. We will move to 
the neighbor node if the neighbor is a better choice for medoids. Otherwise, a local optima is 
discovered. The entire process is repeated multiple time to find better.

::

    from miml.cluster import CLARANS

    fn = os.path.join(datasets.get_data_home(), 'clustering', 'gaussian', 
        'six.txt')
    df = DataFrame.read_table(fn, header=None, names=['x1','x2'], 
        format='%2f')
    x = df.values
    clusters = CLARANS(x, k=6, max_neighbor=10, nlocal=20)
    y = clusters.get_cluster_label()

    scatter(x[:,0], x[:,1], c=y, edgecolor=None, s=3)
    title('Clustering Large Applications based upon RANdomized Search example')
    
.. image:: ../../../_static/miml/clarans_1.png