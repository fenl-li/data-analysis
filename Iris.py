# 导入库
import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
iris_data = pd.read_csv('Iris.csv')

# 查看数据前5行
print(iris_data.head())

# 数据分析：计算不同种类鸢尾花的平均特征值
mean_values_by_species = iris_data.groupby('Species').mean()

# 打印分析结果
print(mean_values_by_species)

# 可视化：绘制不同鸢尾花种类的特征平均值
mean_values_by_species.plot(kind='bar', figsize=(10, 6), color=['blue', 'green', 'red', 'purple'])
plt.title('Mean Feature Values by Iris Species')
plt.ylabel('Mean Value')
plt.xlabel('Species')
plt.xticks(rotation=0)
plt.legend(loc='upper right')
plt.show()