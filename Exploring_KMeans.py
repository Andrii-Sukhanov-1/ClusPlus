import matplotlib
matplotlib.use("TkAgg") 

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import clusplus 
import time 

print('Welcome to Exploring K-means!\nThere you can do K-means for different datasets and K-values')
time.sleep(0.4)
sset_name, sset = clusplus.userdialogue.choose_dataset()
points, labels = sset

time.sleep(0.4)
max_K = clusplus.userdialogue.get_integer_hyperparameter(parameter_name='maximum K for elbow method')
#Exploring what K is better        
inertias = {}
K_values = range(1, max_K + 1)
for K in K_values:
    model = KMeans(n_clusters=K)
    model.fit(points)
    inertias[K] = model.inertia_
    
fig1, ax1 = plt.subplots()
ax1.plot(K_values, inertias.values(), 'o-')
ax1.set_xlabel('K')
ax1.set_ylabel('Inertia')
ax1.set_title('Elbow method for K Means')

time.sleep(0.4)
plt.show(block=False)

x, y = clusplus.utils.get_x_y(points)
while True:
    time.sleep(0.4)
    #Selecting K
    K_choice = clusplus.userdialogue.get_integer_hyperparameter(parameter_name='K')

    #Visualising clusters   
    chosen_model = KMeans(n_clusters=K_choice)
    chosen_model.fit(points)

    fig2, ax2 = plt.subplots()
    ax2.scatter(x, y, c = chosen_model.labels_)
    ax2.set_title('K-Means')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    
    time.sleep(0.4)
    plt.show(block=False)
    
    time.sleep(0.4)
    if clusplus.userdialogue.get_yes_or_no('Do you want to try another number of clusters?') == 'no':
        break
    time.sleep(0.1)
    plt.close(fig2)
time.sleep(0.4)
print('Hope you enjoyed experimenting!')