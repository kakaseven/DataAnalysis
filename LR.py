import numpy as np
###定义模型主体部分
###包括线性回归模型公式、均方损失函数和参数求偏导
def linear_loss(X, y, w, b):
    '''
    输入：
    :param X:输入变量矩阵
    :param y: 输出标签向量
    :param w: 变量参数权重矩阵
    :param b: 偏置
    输出：
    y_hat:线性回归模型预测值
    loss:均方损失
    dw:权重系数一阶偏导
    db:偏置一阶偏导
    '''
    # 训练样本量
    num_train = X.shape[0]
    # 训练特征数
    num_feature = X.shape[1]
    # 线性回归预测值
    y_hat = np.dot(X, w) + b
    # 计算预测值与实际标签之间的均方损失
    test