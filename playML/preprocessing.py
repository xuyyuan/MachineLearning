# 均值方差归一化
class StandardScaler:

    def __init__(self):
        self.mean_ = None
        self.scale_ = None

    def fit(self, X):
        """根据训练数据集 X 来获得数据的均值和方差"""
        assert X.ndim == 2, 'The dimension of X must be 2'

        self.mean_ = [np.mean(X[:, i]) for i in X.shape(1)]
        self.scale_ = [np.std(X[:, i]) for i in X.shape(1)]
        return self

    def transform(self, X):
        """将 X 根据 StandardScale 进行均值方差归一化处理"""
        assert X.ndim == 2, 'The dimension of X must be 2'
        assert self.mean_ is not None and self.scale_ is not None, \
            'must fit before transform'
        assert  X.shape[1] == len(self.mean_), \
            'the feature num of X must be equal to self.mean_ and scale_'

        resX = np.empty(shape=X.shape, dtype=float)
        for col in range(X.shape(1)):
            resX[:, col] = (X[:, col] - self.mean_[col]) / self.scale_[col]
        return resX

# 最值归一化，可以试试
class Minmaxscaler:
    pass

