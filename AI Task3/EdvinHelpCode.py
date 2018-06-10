import sys
import os
import csv
import matplotlib.pyplot as plt
# import pandas as pd
import numpy as np
import random

case_Db=[]

class Restaurants():
    def __init__(self,name,type,nationality,quality,price):
        self.name=name
        self.type=type
        self.nationality=nationality
        self.quality=quality
        self.price=price
    def __str__(self):
        return self.name + "," + self.type + "," + self.nationality +","+str(self.quality) + "," + str(self.price)
    def __repr__(self):
        return self.name + "," + self.type + "," + self.nationality +","+str(self.quality) + "," + str(self.price)
    def __eq__(self, other):
        if (self.name==other.Name) and (self.type==other.Type) and (self.nationality==other.nationality) and(self.quality==other.quality) and (self.price==other.price):
            return True
        else:
            return False
    def addRCase_To_Database(self,Restaurantcase):
        if Restaurantcase not in case_Db:
            case_Db.append(Restaurantcase)
        for i in case_Db:
            print(i)
        return case_Db
    def CSV_ReadFile(self,filename):

        with open(filename + ".txt",'r') as csvfile:
            FileReader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for rad in FileReader:
                case_Db.append(rad)   
        csvfile.close()
def CSV_SaveToFile(case_Db):
        print("Save to file!")
        with open("hej.csv","w") as csvfile:
            for rad in case_Db:
                csvfile.write(str(rad) + "\n")
            print("Success!")
        csvfile.close()
def SimPrice(obj, obj2):
        value = 0
        a = int(obj[4])
        b = int(obj2[4])
        
        if (a==0):
            value =1
        elif (a == b):
            value = 1
        elif (a +1 == b or a -1 == b):
            value = 0.8
        elif (a +2 == b or a -2 == b):
            value = 0.6
        elif (a +3 == b or a -3 == b):
            value = 0.4
        elif (a +4 == b or a -4 == b):
            value = 0.2

        return value
def SimQuality(obj, obj2):
        value =0
        a = int(obj[3])
        b = int(obj2[3])
        if (a==0):
            value = 1
        elif (a == b):
            value = 1
        elif (a +1 == b or a -1 == b):
            value = 0.8
        elif (a +2 == b or a -2 == b):
            value = 0.6
        elif (a +3 == b or a -3 == b):
            value = 0.4
        elif (a +4 == b or a -4 == b):
            value = 0.2

        return value
def SimType(obj, obj2):
    value = 0
    a = obj[1]
    b = obj2[1]
    if (a=="0"):
        value =1
    elif a == b:
        value = 1
    elif (a == 'Fastfood'):
        if (b == 'Café'):
            value = 0.7
        elif (b == 'Gourmet'):
            value = 0.1
        elif (b == 'Traditional'):
            value = 0.4
    elif (a == 'Café'):
        if (b == 'Fastfood'):
            value = 0.7
        elif (b == 'Gourmet'):
            value = 0.3
        elif (b == 'Traditional'):
            value = 0.4
    elif (a == 'Gourmet'):
        if (b == 'Fastfood'):
            value = 0.1
        elif (b == 'Café'):
            value = 0.3
        elif (b == 'Traditional'):
            value = 0.7
    elif (a == 'Traditional'):
        if (b == 'Fastfood'):
            value = 0.4
        elif (b == 'Café'):
            value = 0.4
        elif (b == 'Gourmet'):
            value = 0.7
    return value
def SimNationality(obj, obj2):
    value = 0
    a = obj[2]
    b = obj2[2]
    if (a==0):
        value =1
    elif a == b:
        value = 1
    elif (a == 'Swedish'):
        if (b == 'Asian'):
            value = 0.2
        elif (b == 'Italian'):
            value = 0.6
        elif (b == 'American'):
            value = 0.6
    elif (a == 'Asian'):
        if (b == 'Swedish'):
            value = 0.2
        elif (b == 'Italian'):
            value = 0.4
        elif (b == 'American'):
            value = 0.2
    elif (a == 'Italian'):
        if (b == 'Swedish'):
            value = 0.6
        elif (b == 'Asian'):
            value = 0.4
        elif (b == 'American'):
            value = 0.3
    elif (a == 'American'):
        if (b == 'Swedish'):
            value = 0.6
        elif (b == 'Asian'):
            value = 0.2
        elif (b == 'Italian'):
            value = 0.3
    return value
def Similarity(W,D):
    value = 0
    value = ((1/18)*((2*SimPrice(W,D))+4*SimQuality(W,D)+5*SimType(W,D)+7*SimNationality(W,D)))
    return round(value, 3)
def SimilarityDb(W, case_Db):
    a = 0
    b = []
    for i in case_Db:
        if a < Similarity(W, i):
            a = Similarity(W, i)
            b = i
           
    print("This Resturante match you're suggestens with",a*100,"%:",b)

#-------------------------main--------------------------
# Restaurants.CSV_ReadFile(case_Db, "big")
# #CSV_SaveToFile(case_Db)
# print(Similarity(case_Db[2],case_Db[5]))
# obj = ("NAme","Gourmet","Swedish",5,5)
# SimilarityDb(obj, case_Db)
