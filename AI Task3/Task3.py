import csv
import math
import random

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import Task2Petter as FileObj
import EdvinHelpCode as FileObj2

import sys
import os

import random
from copy import *
from random import randint


CasesFromDatabaseList=[]
QualityAndPriceFromCasesList=[]
ClusterList=[]
CopyClusterList=[]
counterList=[]

def ReadFile():
   FileObj.Restaurants.CSV_ReadFile(FileObj.case_Db,"testDB")

   for i in FileObj.case_Db:
       CasesFromDatabaseList.append(i) 
   return CasesFromDatabaseList

class Centroid(object):
    CentroidsPosition=[]    #tillför att lagra randomlagrade centroids
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def GetCentroidPosX(self):
        return self.x
    def GetCentroidPosY(self):
        return self.y
    def SetCentroidPosX(self,x):
        self.x=x
    def SetCentroidPosY(self,y):
        self.y=y

# if ObjList is None:
#             ObjList=[]
#         else:
class Cluster(object):
    def __init__(self,clusterid=0,ClusterPosX=deepcopy(Centroid().GetCentroidPosX()),ClusterPosY=deepcopy(Centroid().GetCentroidPosY()),ObjList=[],ActiveFlag=True):
        self.clusterid=clusterid
        self.ObjList=ObjList
        self.PosX=ClusterPosX
        self.PosY=ClusterPosY
        self.Flag=ActiveFlag
    def SetClusterid(self,clusterid):
        self.clusterid=clusterid
    def GetClusterid(self):
        return self.clusterid
    def GetClusterPosX(self):
        return self.PosX
    def GetClusterPosY(self):
        return self.PosY
    def SetClusterPosX(self,ClusterPosX):
        self.PosX=ClusterPosX
    def SetClusterPosY(self,ClusterPosY):
        self.PosY=ClusterPosY            

def InitialCentroidPosition(NumberOfCentroids):

    while(NumberOfCentroids>=0):
        if (NumberOfCentroids == 0):
            print("\n--Centroids initialized at positions--\n")
            for i in Centroid.CentroidsPosition:
                print(i) 
            break
        else:
            Centroid.x=randint(1,5)
            Centroid.y=randint(1,5)

            PositionList=[Centroid.x,Centroid.y]
            Centroid.CentroidsPosition.append(PositionList)

        NumberOfCentroids= NumberOfCentroids - 1
    return Centroid.CentroidsPosition

def ReadFileIntoCaseList():

    ReadFile()
    print("\n--Restaurants--\n")
    for i in CasesFromDatabaseList:
        print(i)
    return CasesFromDatabaseList

def CreateClusters(NumberOfClusters):
    #clusterid=0,ClusterPosX=deepcopy(Centroid().GetCentroidPosX()),ClusterPosY=deepcopy(Centroid().GetCentroidPosY()),ObjList=None,ActiveFlag=True
    for CentroidPos in Centroid.CentroidsPosition:
        CentroidTempList=[]
        CentroidTempList=CentroidPos
        ClusterObject=Cluster(NumberOfClusters,CentroidTempList[0],CentroidTempList[1],[],True)
        ClusterList.append(ClusterObject)
        NumberOfClusters-=1
        CentroidTempList.clear()
        if(NumberOfClusters<1):
            break    
        else:
            continue
    return ClusterList    



def Distance(CentroidPosX=0,CentroidPosY=0,CasePosX=0,CaseposY=0):

    return math.sqrt(math.pow((CentroidPosY-CaseposY),2) + math.pow((CentroidPosX-CasePosX),2))



def AssignCasesToCentroids():
    GuideLineDistance=0
    DistanceList=[]
    distance=0
    Cases_List=[]
    Cases_List=deepcopy(CasesFromDatabaseList)
    for case in reversed(Cases_List):
        obj=[]
        obj=case
        for clust in ClusterList:
            distance=Distance(int(clust.GetClusterPosX()),int(clust.GetClusterPosY()),int(obj.get_price()),int(obj.get_quality()))
            DistanceList.append(distance)
            DistanceList.sort()
            GuideLineDistance=DistanceList[0]
        for clust in ClusterList:
            distance=0
            distance=Distance(int(clust.GetClusterPosX()),int(clust.GetClusterPosY()),int(obj.get_price()),int(obj.get_quality()))
            if(GuideLineDistance==distance and case not in clust.ObjList):
                #If sats som kollar ifall case redan existerar, då kan vi antigen ta bort det case från objList och ta den senaste caset och lägg in det i Listan
                clust.ObjList.append(case)
                Cases_List.remove(case)
                DistanceList.clear()
                GuideLineDistance=0
                distance=0
                del obj
                del case
                break
            else:
                continue    
    return ClusterList            
                
             
            
def ReCalculateCentroids():
    helpercounter=0
    List=[]

    for clust in ClusterList:
        TotalX=0
        TotalY=0
        TotalInCluster=0

        for case in clust.ObjList:
            for diffcase in CasesFromDatabaseList:
                if(case==diffcase):
                    TotalX+=int(diffcase.get_price())
                    TotalY+=int(diffcase.get_quality())
                    TotalInCluster+=1
        if(TotalInCluster>0):
            clust.SetClusterPosX(TotalX/TotalInCluster)
            clust.SetClusterPosY(TotalY/TotalInCluster)       
            
    List=deepcopy(ClusterList)   #Kanske tänka om här
    for i in List:
        CopyClusterList.append(i)
    for clust in ClusterList:   #Gör alla clusters listor tomma
        clust.ObjList.clear()
        helpercounter+=1
    counterList.append(helpercounter)    
    return ClusterList,CopyClusterList,counterList



            
'''
# def Reassign_Cluster(NumberOfCentroids):
#     counter=0
#     checkIfIn=0

#     ListToStoreClusterId=[]
#     CopyClusterList=[]
#     CopyClusterList=deepcopy(ClusterList)
    
#     for clust in ClusterList:   #Gör alla clusters listor tomma
#         clust.ObjList.clear()
#         counter+=1              #Hela denna sektionen är till för att ta bort alla cases från cluster interna listor
#     if(counter>=NumberOfCentroids): #Kollar ifall alla centroids/clusters gått igenom 
#         del clust
#         AssignCasesToCentroids()    #Assignar jag nya cases till dem nya centroids som är skapade
#         for clust in ClusterList:
#             for copy_clust in CopyClusterList:
#                 if((clust.clusterid==copy_clust.clusterid) and (clust.ObjList==copy_clust.ObjList)):
#                       ListToStoreClusterId.append(int(clust.clusterid))
#     for clust in ClusterList:  #Här är det meningen att den ska kolla och jämföra upprepningar, vilket kommer leta till att en ny centroid skapas och sen cases som läggs till, tänker göra det till funktioner för blir mycket upprepning i kod.  
        
#         if clust.clusterid in ListToStoreClusterId:
#             checkIfIn+=1
#             if(checkIfIn==len(ListToStoreClusterId)):
#                 checkIfIn=0
#                 return ClusterList
#         elif clust.clusterid not in ListToStoreClusterId:
#               ReCalculateCentroids()
#               Reassign_Cluster(NumberOfCentroids)  
'''         

def Reassign_Cluster(NumberOfCentroids):
    CentroidActiveMovement=1
    var=0
    var=int(counterList[0])
    counterList.clear()
    ListToStoreClusterId=[] 
    if(var>=NumberOfCentroids):
        AssignCasesToCentroids()
        for copyclust in CopyClusterList:
            for clust in ClusterList:
                if((copyclust.clusterid == clust.clusterid) and (copyclust.ObjList==clust.ObjList)):
                    ListToStoreClusterId.append(clust.clusterid)
    #if(len(ListToStoreClusterId)==NumberOfCentroids):
    #inte klart här, men här ska den iallafall kolla efter ändringar mellan kopierade cluterlist oh clusterlist interna listor, kan ta hjälp med att lägga in clusterid i en lista och sen kolla om alla id som finns i clusterlist  existerar      
        
        # for ID in ListToStoreClusterId:
        #     for clust in ClusterList: 
    
    
    return CentroidActiveMovement

def Tostring():
    for clust in ClusterList:
        print("\nClusterId: " + str(clust.clusterid) + "\tPositions " + "X=" + str(clust.PosX)+ " Y="+ str(clust.PosY)+"\n")
        for obj in clust.ObjList:
            print("[ " +  str(obj) + " ]")
        print("\n")
    print("\n")        

def K_means(K):
    CentroidActiveMovement=1
    ReadFileIntoCaseList()
    InitialCentroidPosition(K)  #Genereates random X and Y Position of Centroid
    CreateClusters(K)   #Creates Clusters with the position of Centroids
    AssignCasesToCentroids()
    while(CentroidActiveMovement != 0):
          Tostring()
          ReCalculateCentroids()
          CentroidActiveMovement=Reassign_Cluster(K) #denna del inte klar
    
    return Tostring()
    
            
                
            
            
                              
  


   
    
                    

    
    

#Reassign cases

def main():
    
    K_means(3)
    
if __name__=='__main__':
    main()
