.. _examples-miml-deep_learning-convolution_mnist:

*************************************
Convolution mnist
*************************************

Convolution neuron network mnist example.

::

    from miml import datasets
    from miml.preprocessing import MinMaxScaler
    from miml.model_selection import train_test_split
    from miml.deep_learning import Network, InputType, Optimizer, Adam
    from miml.deep_learning import Activation, LossFunction, WeightInit
    from miml.deep_learning import DenseLayer, OutputLayer, ConvolutionLayer,\
        SubsamplingLayer

    print('Read data...')
    fn = 'D:/Temp/machine_learning/mnist_784.arff'
    mnist = datasets.load_arff(fn, ridx=784)
    X = mnist.x
    y = mnist.y

    print('Train/Test split...')
    X_train, X_test, y_train, y_test = train_test_split(X,
        y, test_size=0.4, random_state=0)

    print(X_train.shape, y_train.shape)
    print(X_test.shape, y_test.shape)

    print('MinMax scaling...')
    scaler = MinMaxScaler(feature_range=(0, 1))
    X_train = scaler.fit_transform(X_train.flatten()).reshape(X_train.shape)
    X_test = scaler.fit_transform(X_test.flatten()).reshape(X_test.shape)

    print('Build neural network...')
    model = Network(seed=123, l2=0.0005, weight_init=WeightInit.XAVIER,
        updater=Adam(1e-3), input_type=InputType.convolutionalFlat(28,28,1))
    model.add(ConvolutionLayer(kernel_size=(5,5), nin=1, stride=(1,1), nout=20,
        activation=Activation.IDENTITY))
    model.add(SubsamplingLayer(pooling_type='max', kernel_size=(2,2), stride=(2,2)))
    model.add(ConvolutionLayer(kernel_size=(5,5), stride=(1,1), nout=50,
        activation=Activation.IDENTITY))
    model.add(SubsamplingLayer(pooling_type='max', kernel_size=(2,2), stride=(2,2)))
    model.add(DenseLayer(nout=500, activation=Activation.RELU))
    model.add(OutputLayer(loss=LossFunction.NEGATIVELOGLIKELIHOOD, nin=500, nout=10,
        activation=Activation.SOFTMAX))
    model.compile()

    print('Fit model...')
    nepochs = 1
    model.fit(X_train, y_train, epochs=nepochs, batchsize=64)

    print('Model evaluation...')
    meval = model.eval(X_test, y_test, batchsize=64)
    print(meval)