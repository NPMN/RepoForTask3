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
CheckList=[]
OldClusterList=[]

def ReadFile():
   FileObj.Restaurants.CSV_ReadFile(FileObj.case_Db,"big")

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
            #Centroid.x=randint(0.0,5.0)
            Centroid.x=random.uniform(0,5)
            Centroid.y=random.uniform(0,5)
            #Centroid.y=randint(0.0,5.0)

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
            distance=Distance(float(clust.GetClusterPosX()),float(clust.GetClusterPosY()),float(obj.get_price()),float(obj.get_quality()))
            DistanceList.append(distance)
            DistanceList.sort()
            GuideLineDistance=DistanceList[0]
        for clust in ClusterList:
            distance=0
            distance=Distance(float(clust.GetClusterPosX()),float(clust.GetClusterPosY()),float(obj.get_price()),float(obj.get_quality()))
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
    List=deepcopy(ClusterList)
    for cluster in List:
       OldClusterList.append(cluster)

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
            
  
    for clust in ClusterList:   #Gör alla clusters listor tomma
        clust.ObjList.clear()
        helpercounter+=1
    counterList.append(helpercounter)    
    return ClusterList,counterList,OldClusterList




def Reassign_Cluster(NumberOfCentroids):
    CentroidActiveMovement=1
    check=0
    Flag=False
    counter=0
    var=0
    var=int(counterList[0])
    counterList.clear()
    CopyClusterList=[] 
    if(var>=NumberOfCentroids):
        if(len(CheckList)>0):
            counter=CheckList[0]
            CheckList.clear()
        else:
            counter=0    
        AssignCasesToCentroids()    #Här får ClusterList nya cases
        
        CopyClusterList=deepcopy(ClusterList)
        for ex1 in OldClusterList:
            for ex2 in CopyClusterList:
                if(ex1.clusterid == ex2.clusterid and ex1.ObjList==ex2.ObjList):
                    Flag=True
        if(counter>=1 and Flag==True):
            for i in CopyClusterList:
                for j in OldClusterList:
                    if(i.clusterid==j.clusterid and i.ObjList == j.ObjList):
                        check+=1         
        counter+=1
        if(check>=len(CopyClusterList)):
            CentroidActiveMovement=0
     
        CopyClusterList.clear()
        OldClusterList.clear()
        Flag=False
        CheckList.append(counter)
        #På något sätt när clusterna inte ändras, skicka CentroidActiveMovement=0 och uppgiften klart      
    return CentroidActiveMovement

def Tostring():
    for clust in ClusterList:
        print("\nClusterId: " + str(clust.clusterid) + "\tPositions " + "X=" + str(clust.PosX)+ " Y="+ str(clust.PosY)+"\tCount: " + str(len(clust.ObjList))+"\n" )
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
    Tostring()
    while(CentroidActiveMovement != 0):
         
          ReCalculateCentroids()
          CentroidActiveMovement=Reassign_Cluster(K) #denna del inte klar
          print("--New cycle--\n")
          Tostring()
          
    print("Clusters Finished")        
    return Tostring()
    
            
                
            
            
                              
  


   
    
                    

    
    

#Reassign cases

def main():
    
    K_means(2)
    
if __name__=='__main__':
    main()
