.. _examples-miml-deep_learning-classifer_iris:

*************************************
Classification iris
*************************************

MultiLayerNetwork iris classification example.

::

    from miml import datasets
    from miml.model_selection import train_test_split
    from miml.preprocessing import MinMaxScaler
    from miml.deep_learning import Network, LossFunction, Activation, WeightInit
    from miml.deep_learning import Sgd
    from miml.deep_learning import DenseLayer, OutputLayer

    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X,
        y, test_size=0.35, random_state=0)

    print(X_train.shape, y_train.shape)
    print(X_test.shape, y_test.shape)

    scaler = MinMaxScaler(feature_range=(0, 1))
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    model = Network(seed=6, activation=Activation.TANH, weight_init=WeightInit.XAVIER,
        updater=Sgd(learn_rate=0.1), l2=1e-4)
    model.add(DenseLayer(nin=4, nout=3))
    model.add(DenseLayer(nin=3, nout=3))
    model.add(OutputLayer(loss=LossFunction.NEGATIVELOGLIKELIHOOD, nin=3, nout=3,
        activation=Activation.SOFTMAX))
    model.compile()

    nepochs = 1000
    model.fit(X_train, y_train, epochs=nepochs, batchsize=150, print_stride=100)

    meval = model.eval(X_test, y_test, batchsize=150)
    print(meval)