import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import MaxAbsScaler
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

dataset = pd.read_csv('data.csv')
data = dataset.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8]].values
print(data)

# Feature Scaling
scaler=MaxAbsScaler()
data_final=scaler.fit_transform(data)
print(data_final)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=0)
    y_kmeans = kmeans.fit(data_final)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.show()

# Perform k-means clustering
kmeans = KMeans(n_clusters = 5, init='k-means++', random_state=0)
y_kmeans = kmeans.fit_predict(data_final)
print(y_kmeans)
print(len(y_kmeans))

# Visualizing the clusters with PCA Plotting (Visualizing Multidimensional Data)
pca=PCA(n_components=2)
transformed=pd.DataFrame(pca.fit_transform(data_final))

plt.scatter(transformed[y_kmeans==0][0], transformed[y_kmeans==0][1], s=200, label='Cluster 1', c='red')
plt.scatter(transformed[y_kmeans==1][0], transformed[y_kmeans==1][1], s=200, label='Cluster 2', c='blue')
plt.scatter(transformed[y_kmeans==2][0], transformed[y_kmeans==2][1], s=200, label='Cluster 3', c='lightgreen')
plt.scatter(transformed[y_kmeans==3][0], transformed[y_kmeans==3][1], s=200, label='Cluster 4', c='magenta')
plt.scatter(transformed[y_kmeans==4][0], transformed[y_kmeans==4][1], s=200, label='Cluster 5', c='orange')
#plt.scatter(transformed[y_kmeans==5][0], transformed[y_kmeans==5][1], s=200, label='Cluster 6', c='yellow')
#plt.scatter(transformed[y_kmeans==6][0], transformed[y_kmeans==6][1], s=200, label='Cluster 7', c='purple')
plt.title('Clusters of Overseas Traveling Destination \n(K-Means Clustering Model)')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.legend()
plt.show()




# Create a dendrogram
plt.figure(figsize=(10, 7))
z=sch.linkage(data_final, method='ward')
dendrogram=sch.dendrogram(z)
plt.title('Dendrogram')
#plt.axhline(y=1, color='r', linestyle='--')
plt.show()

# Perform the actual clustering
hc=AgglomerativeClustering(n_clusters=6, affinity='euclidean', linkage='ward')
y_hc=hc.fit_predict(data_final)
print(y_hc)

# Visualizing the clusters with PCA Plotting (Visualizing Multidimensional Data)
pca=PCA(n_components=2)
transformed=pd.DataFrame(pca.fit_transform(data_final))

plt.scatter(transformed[y_hc==0][0], transformed[y_hc==0][1], s=200, label='Cluster 1', c='red')
plt.scatter(transformed[y_hc==1][0], transformed[y_hc==1][1], s=200, label='Cluster 2', c='blue')
plt.scatter(transformed[y_hc==2][0], transformed[y_hc==2][1], s=200, label='Cluster 3', c='lightgreen')
plt.scatter(transformed[y_hc==3][0], transformed[y_hc==3][1], s=200, label='Cluster 4', c='magenta')
plt.scatter(transformed[y_hc==4][0], transformed[y_hc==4][1], s=200, label='Cluster 5', c='orange')
plt.scatter(transformed[y_hc==5][0], transformed[y_hc==5][1], s=200, label='Cluster 6', c='yellow')
plt.title('Clusters of Overseas Traveling Destination \n(Hierarchical Clustering Model)')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.legend()
plt.show()





