.. _examples-miml-model_selection-cross_validate:

*************************************
Get cross validate score
*************************************

The simplest way to use cross-validation is to call the `cross_val_score` helper function on the 
estimator and the dataset.

The following example demonstrates how to estimate the accuracy of a linear kernel support vector 
machine on the iris dataset by splitting the data, fitting a model and computing the score 5 
consecutive times (with different splits each time. The mean score and the 95% confidence interval 
of the score estimate are hence given.

::

    from miml import datasets
    from miml.classification import SVM
    from miml.model_selection import cross_val_score

    iris = datasets.load_iris()
    model = SVM(kernel='linear', C=1)
    scores = cross_val_score(model, iris.data, iris.target, cv=5)
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    
::

    >>> run script...
    Accuracy: 0.94 (+/- 0.15)
