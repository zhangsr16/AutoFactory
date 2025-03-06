# 加载必要的包
library(ggplot2)
library(scales)
# Python
epsilon = 1e-6
rate_of_change = (tensor[..., 1:] - tensor[..., :-1]) / (tensor[..., :-1] + epsilon)
seqmean=rate_of_change.mean(dim=-1, keepdim=True)
seq_cented=rate_of_change-seqmean
seq_cented=(tensor_data-seqmean)/seqmean

# R
# 生成一些随机数据
data <- matrix(runif(200), ncol = 2)

# 对数据进行中心化和标准化
data_scaled <- scale(data)

# 人工设定聚类中心点
centroids <- matrix(c(0.2, 0.2, 0.8, 0.8, 0.2, 0.8), ncol = 2)
centroids_scaled <- scale(centroids, center = attr(data_scaled, "scaled:center"), scale = attr(data_scaled, "scaled:scale"))

# 使用K-Means聚类算法，传入人工设定的中心点
kmeans_result <- kmeans(data_scaled, centers = centroids_scaled, nstart = 1)

# 计算每个点到各个聚类中心的距离
distances <- as.matrix(dist(rbind(data_scaled, centroids_scaled)))[1:nrow(data_scaled), (nrow(data_scaled) + 1):(nrow(data_scaled) + nrow(centroids_scaled))]


# 聚类结果的标签
labels <- kmeans_result$cluster

# 可视化聚类结果
data_plot <- as.data.frame(data_scaled)
data_plot$cluster <- as.factor(labels)
centroids_plot <- as.data.frame(centroids_scaled)
centroids_plot$cluster <- as.factor(1:nrow(centroids_scaled))

ggplot(data_plot, aes(x = V1, y = V2, color = cluster)) +
  geom_point() +
  geom_point(data = centroids_plot, aes(x = V1, y = V2), color = "red", size = 4, shape = 4) +
  theme_minimal() +
  labs(title = "K-Means Clustering with Standardized Data",
       x = "Standardized X",
       y = "Standardized Y")



# 示例代码
result <- try({
  # 这里放可能会出错的代码
 a=3
  stop("这是一个错误")
}, silent = T)

# 检查是否发生错误
if (inherits(result, "try-error")) {
  message("捕获到错误，但继续执行后续代码")
}

# 后续代码
message("继续执行后续代码")
