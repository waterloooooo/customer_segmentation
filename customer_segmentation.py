import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Mall_Customers.csv')

# Display first few rows
print(df.head())

# Select features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Scale features for better clustering performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Choose the number of clusters
k = 5  # You can experiment with this

# Fit K-Means
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X_scaled)

# Assign cluster labels to the dataframe
df['Cluster'] = kmeans.labels_

# Show dataframe with clusters
print(df.head())

# Plot the clusters
plt.figure(figsize=(8,6))
plt.scatter(
    X_scaled[:, 0], X_scaled[:, 1], 
    c=df['Cluster'], cmap='viridis', s=50
)
plt.xlabel('Annual Income (scaled)')
plt.ylabel('Spending Score (scaled)')
plt.title('Customer Segmentation with K-Means Clustering')
plt.colorbar(label='Cluster')
plt.show()
