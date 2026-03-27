K-Means is an unsupervised learning algorithm used to group similar data points into K clusters.

k == numbers of cluster you want
means = center or average 

## how k -mean cluster work 
- step 1 : choosen k(numbers of cluster )
example: k =3

- Step 2: Initialize centroids randomly

Pick K random points as centers

- Step 3: Assign points to nearest centroid

Use distance (usually Euclidean distance)
- Step 4: Update centroids

Take mean of points in each cluster

- Step 5: Repeat

Repeat step 3 & 4 until centroids stop changin



Mathematical Idea

https://www.tutorialspoint.com/machine_learning/machine_learning_k_means_clustering.htm

Distance between points and their cluster center should be minimum

# sualization Idea

Think like:

Points move toward nearest center
Centers adjust until stable