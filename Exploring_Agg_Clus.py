import matplotlib
matplotlib.use('TkAgg')

import time
from clusplus import userdialogue, utils
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt



print('Welcome to Exploring Agglomerative Clustering!\nThere you can do Agglomerative Clustering for different datasets and number of clusters')
time.sleep(1)

sset_name, sset = userdialogue.choose_dataset()
points, labels = sset
print(f'Your dataset has {len(points)} points.')
time.sleep(0.5)
print("Let's make a dendrogram first!")

time.sleep(0.4)


default_dist_metr, default_linkage_method = 'euclidean', 'ward'
if userdialogue.get_yes_or_no('Do you want to select linkage method or distance metrics?') == 'yes':

    time.sleep(0.4)
    print('You can skip selecting a parameter by leaving the field empty')
    print(f'Then default values {default_linkage_method, default_dist_metr} will be used.')
    time.sleep(0.4)

    linkage_methods = ['single', 'average','complete', 'ward', '' ] #compatible with sklearn.AgglomerativeClustering + '' for skipping
    distance_metrics = ['euclidean', 'manhattan', 'cosine', '']
    
    linkage_method = userdialogue.get_discrete_parameter(parameter_name='linkage method', possible_values=linkage_methods)
    time.sleep(0.4)
    print('-'*100)

    distance_metric = userdialogue.get_discrete_parameter(parameter_name='distance metric', possible_values=distance_metrics)
    print('-'*100)

    if not linkage_method:
        linkage_method = default_linkage_method
    if not distance_metrics:
        distance_metrics = default_dist_metr
else:
    time.sleep(0.4)
    print(f'Then default values {default_linkage_method, default_dist_metr} will be used.')
    linkage_method = default_linkage_method
    distance_metric = default_dist_metr



linkage_data = linkage(points, method=linkage_method, metric=distance_metric)
fig1, ax1 = plt.subplots()
dendrogram(linkage_data, ax = ax1)
ax1.set_title('Dendrogram')
ax1.set_ylabel('Distance')
ax1.set_xlabel('Points')
plt.show(block=False)

time.sleep(0.4)
print("Now it's time to visualise clusters!")
time.sleep(0.4)
x, y = utils.get_x_y(points)

while True:
    n_clusters = userdialogue.get_integer_hyperparameter(parameter_name='number of clusters')
    labels = fcluster(linkage_data, t=n_clusters, criterion='maxclust')
    

    fig2, ax2 = plt.subplots()
    ax2.set_title('Clusters')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.scatter(x, y, c=labels)

    time.sleep(0.4)
    plt.show(block=False)
    if userdialogue.get_yes_or_no('Do you want to try another number of clusters?') == 'no':
        break
    plt.close(fig2)
    time.sleep(0.4)

time.sleep(0.4)
print('Hope you enjoyed experimenting!') 