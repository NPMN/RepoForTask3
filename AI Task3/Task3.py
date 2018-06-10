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

def ReadFile():
   FileObj.Restaurants.CSV_ReadFile(FileObj.case_Db,"small")

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

def InitialCentroidPosition(NumberOfCentroids):

    while(NumberOfCentroids>=0):
        if (NumberOfCentroids == 0):
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

def InitialPositionsFromCase_Db():

    ReadFile()
    for obj in CasesFromDatabaseList:   #Denna listan har alla cases
        TempList=[]
        TempList=obj
        
        X=int(TempList.get_price())
        Y=int(TempList.get_quality())

        PositionList=[X,Y]
        QualityAndPriceFromCasesList.append(PositionList)   #Denna listan innehåller price och quality från alla cases, till för kalkylationen med distance

    for i in QualityAndPriceFromCasesList:
        print(i)  
    return QualityAndPriceFromCasesList


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
            distance=Distance(int(clust.GetClusterPosX()),int(clust.GetClusterPosY()),int(obj.get_price()),int(obj.get_quality()))
            if(GuideLineDistance==distance):
                clust.ObjList.append(case)
                Cases_List.remove(case)
                DistanceList.clear()
                GuideLineDistance=0
                distance=0
                del obj
                del case
                break
               
    return ClusterList            
                
             
            
def ReassignClusters():
    
#Reassign
#Perform K-means
#Results





def main():
    N=3
    InitialCentroidPosition(N) #Klar
    print()
    InitialPositionsFromCase_Db()   #Klar
    print()
    CreateClusters(N)
    AssignCasesToCentroids()
if __name__=='__main__':
    main()
