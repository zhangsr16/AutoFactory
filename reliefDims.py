from skrebate import ReliefF

X=train_tensor.view(train_tensor.shape[0],-1)
X=pd.DataFrame(X)
y=train_data['appid']

# 使用ReliefF算法进行特征选择
relief = ReliefF(n_neighbors=100)
relief.fit(X.values, y.values)

# 获取每个特征的重要性得分
relief_importances = relief.feature_importances_
relief_topfeatures = relief.top_features_[:10]
# 选择前10个特征

X_train_relief = X_train.iloc[:, relief_topfeatures]
X_test_relief = X_test.iloc[:, relief_topfeatures]
