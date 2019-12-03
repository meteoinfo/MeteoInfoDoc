.. _examples-miml-model_selection-kfold:

*************************************
K-Folds cross-validator
*************************************

K-Folds cross-validator provides train/test indices to split data in train/test sets. Split
dataset into k consecutive folds (without shuffling by default).

Each fold is then used once as a validation while the k - 1 remaining
folds form the training set.

::

    from miml.model_selection import KFold

    X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
    y = np.array([1, 2, 3, 4])
    kf = KFold(n_splits=2)
    kf.get_n_splits(X)
        
    print(kf)
    for train_index, test_index in kf.split(X):
        print("TRAIN:", train_index, "TEST:", test_index)
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
    
::

    >>> run script...
    Base cross validation class
    ('TRAIN:', array([2, 3]), 'TEST:', array([0, 1]))
    ('TRAIN:', array([0, 1]), 'TEST:', array([2, 3]))
