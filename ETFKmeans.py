import numpy as np
import torch
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

option = 0
config = []
TotalCented = []
env_tensors = []

epsilon = 1e-6
env_tensor = env_tensors[option]
env_tensor = torch.nan_to_num(env_tensor, nan=0.0, posinf=0.0, neginf=0.0)

# 环境变化率张量: batch, feature, seq, cycle
env_rate = (env_tensor[:, :, 1:, :] - env_tensor[:, :, :-1, :]) / (env_tensor[:, :, :-1, :] + epsilon)
env_mean = env_rate.mean(dim=2, keepdim=True)  # 第3维求均
EnvTotalCented = (env_rate - env_mean) / (env_mean + epsilon)
total_dfs = []
for cycle in range(env_tensor.shape[-1]):
    # 映射中心
    EnvCented = EnvTotalCented[..., cycle]  # select cols in each cycle, by config define
    env_reshaped = EnvCented[:, config[option + 'EnvCluster'], :]  # select cols in each cycle, by config define
    env_total_reshaped = EnvCented.view(EnvCented.shape[0], -1)

    if option == 0:
        if cycle == 0:
            # 轮廓系数
            silhouette_scores = []
            for k in range(2, 11):
                kmeans = KMeans(n_clusters=k, random_state=0)
                labels = kmeans.fit_predict(env_total_reshaped)
                silhouette_scores.append(silhouette_score(env_total_reshaped, labels))
            # 输出最佳聚类
            best_k = np.argmax(silhouette_scores) + 2
        # 使用K-Means聚类算法进行聚类分析，自学习中心点
        kmeans = KMeans(n_clusters=best_k, max_iter=best_k, random_state=0)
        kmeans.fit(env_total_reshaped)
        initial_centers = kmeans.cluster_centers_

    initial_centers = env_reshaped.view(env_reshaped.shape[0], -1)
