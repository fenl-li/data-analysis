import pandas as pd
import matplotlib.pyplot as plt

iris_data = pd.read_csv('Iris.csv')


print(iris_data.head())

mean_values_by_species = iris_data.groupby('Species').mean()

print(mean_values_by_species)

mean_values_by_species.plot(kind='bar', figsize=(10, 6), color=['blue', 'green', 'red', 'purple'])
plt.title('Mean Feature Values by Iris Species')
plt.ylabel('Mean Value')
plt.xlabel('Species')
plt.xticks(rotation=0)
plt.legend(loc='upper right')
plt.show()