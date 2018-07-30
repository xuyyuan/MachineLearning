import numpy as np

def train_test_split(X, y, test_ratio=0.2, random_state=None):

    """将数据 X 和 y 按照test_ratio分割成X_train, X_test, y_train, y_test"""
    assert X.shape[0] == y.shape[0], \
        'the size of X must be equal to the size of y'
    assert 0.0 <= test_ratio <= 1.0, \
        'test_ratio must be valid'

    if random_state:
        np.random.seed(random_state)

    shuffle_indexes = np.random.permutation(len(X))  # permutation不改变原来的数组，shuffle则不然
    test_size = int(test_ratio * len(X))

    train_indexes = shuffle_indexes[test_size:]
    test_indexes = shuffle_indexes[:test_size]

    X_train = X[train_indexes]
    y_train = y[train_indexes]

    X_test = X[test_indexes]
    y_test = y[test_indexes]

    return X_train, X_test, y_train, y_test


class GridSearchCV:
    """网格搜索，进行参数参数"""
    pass








