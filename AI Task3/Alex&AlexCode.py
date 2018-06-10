# from task2cbr import *
# from random import *
# import random
# from copy import *
# import matplotlib.pyplot as plt     #plot function
# from math import sqrt
# import itertools    #endless loop

# class centroid(object):
#     def _init_ (self, x = 0, y = 0):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return "%f,%f\n" % (self.x,self.y) 

# class cluster(object):
#     def _init_ (self, id = 0, List = [], croid = deepcopy(centroid()), flag = True):
#         self.id = id
#         self.croid = croid
#         self.List = List
#         self.flag = flag

#     def __repr__(self):
#         return "%s,%s" % (self.id, self.List) 

    
# clusterList = []
# def cluster_func(cases, k):
#     numberOfCases = len(cases)
   
#     for x in range(k):    #create given amount k clusters
    
#         clust = deepcopy(cluster(x))
#         clusterList.append(clust)

#     while(1):
#         for i in range(len(cases)):
#             for clust in clusterList:
#                 if(len(cases)):     #itera te as long cases is not empty
#                     iRand = randrange(0, k)     #generates random index
#                     randomCase = random.choice(cases)   #chooses random case from cases
#                     clusterList[iRand].List.append(randomCase)  #append randomCase to random clust object in clusterList
#                     cases.remove(randomCase) 
#         return clusterList        
    
# def centroid_calc():

#     for clust in clusterList:
#         meanQuality = 0
#         meanPrice = 0   
#         counter = 0
        
#         for case in clust.List:
#             meanQuality += int(case.quality)
#             meanPrice += int(case.price)
#             counter+=1

#         clust.croid.x = (meanQuality / counter)     #calculate new value for centroid
#         clust.croid.y = (meanPrice / counter)
        
#         #print("cluster",clust.id,"centroid:", clust.croid)     #print every new centroid



# def reassign():
#     minDistance = 100   #arbitrary "high" value
#     minClusterId = ""
#     centroid_calc()

#     for cluster1 in itertools.cycle(clusterList):   #infinite loop until break
#         check = 0
#         for c in clusterList:   #loop to check if there are changes in the clusters. If not, break
#             if c.flag:
#                 continue
#             else:
#                 check+=1
#         if check == len(clusterList):
#             break
                
#         for case in cluster1.List:  #iterate through all cases and compare them one by one with all centroids.
#             centroid_calc()     #calculate new centroid
#             minDistance = 100   #reset minDistance

#             for cluster2 in clusterList:
#                 euclidean_distance = sqrt( (int(case.quality)-cluster2.croid.x)**2 + (int(case.price)-cluster2.croid.y)**2 )    #calculate euclidean distance between case and centroid
#                 if euclidean_distance < minDistance:
#                     minDistance = euclidean_distance
#                     minClusterId = cluster2.id
#             if case not in clusterList[minClusterId].List:  #move case to new cluster if it is not already in the one with shortest distance to centroid
#                 cluster1.flag = True
#                 clusterList[minClusterId].List.append(case)
#                 if case in cluster1.List:
#                     cluster1.List.remove(case)
#             else:
#                 cluster1.flag = False   #if no changes been made, set flag to False
#     return clusterList



# def main():
#     n = 5   #number of clusters
#     read_file() 

#     cluster_func(cases,n)

#     print("--------------Number of clusters:",n,"----------------------------------\n")
#     reassign()

#     for x in range(n):
#         print("\nCluster",x,":",len(clusterList[x].List), "cases")    
#         print("------------Cluster",x,"-----------------------")
#         for c in clusterList[x].List:
#             print(c)


#     #Uncomment for plotted graph
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     for clust in clusterList:
#         plt.plot(clust.croid.x, clust.croid.y,'bo')     #plot centroids

#     ax.set_xlabel('Price')
#     ax.set_ylabel('Quality')
#     plt.show()


# if _name_ == '_main_':
#     main()