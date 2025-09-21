import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample data: (SAT Score, GPA, Extracurricular Score out of 10)
students = np.array([
    [1550, 4.0, 9],  # Top applicant
    [1480, 3.9, 8],
    [1200, 3.2, 6],  # Average applicant
    [1250, 3.3, 5],
    [980, 2.5, 3],  # At-risk applicant
    [1020, 2.8, 2],
])

# Apply K-Means Clustering (3 groups)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(students)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Plot results
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(students[:, 0], students[:, 1], students[:, 2], c=labels, cmap='coolwarm', edgecolors='black', s=100)
ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], c='yellow', marker='X', s=200, label="Centers")
ax.set_xlabel("SAT Score")
ax.set_ylabel("GPA")
ax.set_zlabel("Extracurricular Score")
ax.set_title("College Admissions Clustering")
ax.legend()
plt.show()