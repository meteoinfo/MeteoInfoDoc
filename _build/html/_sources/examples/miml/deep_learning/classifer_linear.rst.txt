.. _examples-miml-deep_learning-classifer_linear:

*************************************
Classification linear
*************************************

MultiLayerNetwork linear classification example.

::

    from miml import datasets
    from miml.deep_learning import Network, Activation, WeightInit, LossFunction
    from miml.deep_learning import Nesterovs
    from miml.deep_learning import DenseLayer, OutputLayer

    fn = os.path.join(datasets.get_data_home(), 'classification',
        'linear_data_train.csv')
    df = DataFrame.read_table(fn, delimiter=',', header=None, names=['x1','x2'],
        format='%2f', index_col=0)
    tfn = os.path.join(datasets.get_data_home(), 'classification',
        'linear_data_train.csv')
    tdf = DataFrame.read_table(tfn, delimiter=',', header=None, names=['x1','x2'],
        format='%2f', index_col=0)

    X = df.values
    y = array(df.index.data)

    model = Network(seed=123, weight_init=WeightInit.XAVIER,
        updater=Nesterovs(learn_rate=0.01, momentum=0.9))
    model.add(DenseLayer(nin=2, nout=20, activation=Activation.RELU))
    model.add(OutputLayer(loss=LossFunction.NEGATIVELOGLIKELIHOOD, nin=20, nout=2,
        activation=Activation.SOFTMAX))
    model.compile()
    model.fit(X, y, epochs=30, batchsize=50)

    meval = model.eval(tdf.values, array(tdf.index.data), batchsize=50)
    print(meval)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = 0., 1.
    y_min, y_max = -0.2, 0.8
    n = 100  # size in the mesh
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, n),
                         np.linspace(y_min, y_max, n))
    data = np.vstack((xx.flatten(), yy.flatten())).T
    z = model.predict(data)

    # Put the result into a color plot
    Z = z[:,0].reshape(xx.shape)

    #Plot
    # Create color maps
    cmap_light = ['#FFAAAA', '#AAAAFF']
    cmap_bold = ['#FF0000', '#0000FF']
    gg = imshow(xx[0,:], yy[:,0], Z, 40, cmap='MPL_gist_gray', interpolation='None')
    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y,
        edgecolor=None, s=4, levels=[0,1], colors=cmap_bold)
    plt.contour(xx[0,:], yy[:,0], Z, [0.5], color='k', smooth=False)
    colorbar(gg)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("Classifer example")
    
.. image:: ../../../_static/miml/dl_classifer_1.png