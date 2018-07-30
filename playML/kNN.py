import numpy as np
from math import sqrt
from collections import Counter
from .metrics import accuracy_score

class kNNclassfier:

    """初始化kNN分类器"""
    def __init__(self, k):
        assert k >= 1, 'k must be valid'
        self.k = k
        self._X_train = None
        self._y_train = None

    def fit(self, X_train, y_train):

        """根据训练集X_train,y_train训练kNN分类器"""
        assert X_train.shape[0] == y_train.shape[0], \
            'the size of X_train must be equal to the size to y_train'
        assert self.k <= X_train.shape[0], \
            'the size of X_train must be at least k'

        self._X_train = X_train
        self._y_train = y_train
        return self

    def predict(self, X_predict):

        """给定待预测的X_predict， 返回表示X_predict的结果向量"""
        assert self._X_train is not None and self._y_train is not None, \
            'must fit before predict'
        assert X_predict.shape[1]  == self._X_train.shape[1], \
            'the feature num of X_predict must be equal to X_train'
        y_predict = [self._predict(x) for x in X_predict]
        return np.array(y_predict) # 规定返回结果应该是一个数组

    def _predict(self, x):

        """给定单个的待预测数据x, 返回x的预测结果值"""
        assert x.shape[0] == self._X_train.shape[1], \
            'the feature num of X_predict must be equal to X_train'   # 注意这里的x.shape[0]可别写成了x.shape[1],因为这里x是向量
        distances = [sqrt(np.sum((x_train-x)**2)) for x_train in self._X_train]
        nearest = np.argsort(distances)
        topK_y = [self._y_train[i] for i in nearest[:self.k]]
        votes = Counter(topK_y)
        return votes.most_common(1)[0][0]

    def score(self, X_test, y_test):
        """根据测试数据集 X_train 和 y_train 确定模型的准确度"""
        y_predict = self.predict(X_test)
        return accuracy_score(y_test, y_predict)  # 不用再添加assert语句了，因为predict和accuracy_score函数内已经有了相应的判断
          
    def __repr__(self):
        return 'kNN(%d)' % self.k

# 其实呢还应该考虑到距离的权重（weights='distance'/'uniform'），这里再自己写的kNN算法里面没有写，以后再写吧