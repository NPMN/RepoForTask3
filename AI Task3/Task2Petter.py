import sys
import os
import csv
case_Db=[]  #Global lista

class Restaurants:

    def __init__(self,name,type,nationality,quality,price):
        self.name=name
        self.type=type
        self.nationality=nationality
        self.quality=quality
        self.price=price

    def set_name(self,name):
        self.name=name

    def get_name(self):
        return self.name

    def set_type(self,type):
        self.type=type

    def get_type(self):
        return self.type

    def set_nationality(self, nationality):
            self.nationality = nationality

    def get_nationality(self):
            return self.nationality

    def set_quality(self,quality):
        self.quality=quality

    def get_quality(self):
        return str(self.quality)

    def set_price(self,price):
        self.price=price

    def get_price(self):
        return str(self.price)

    def __str__(self):
        return self.name + "," + self.type + "," + self.nationality +","+str(self.quality) + "," + str(self.price)

    def __eq__(self, other):
        if (self.name==other.name) and (self.type==other.type) and (self.nationality==other.nationality) and(self.quality==other.quality) and (self.price==other.price):
            return True
        else:
            return False

    def CSV_ReadFile(self,filename):
        with open(filename + ".txt",'r') as csvfile:
            FileReader = csv.reader(csvfile, delimiter=';', quotechar='|')

            for rad in FileReader:
                case_Db.append(Restaurants(rad[0],rad[1],rad[2],rad[3],rad[4]))
                #case_Db.append(rad)


        csvfile.close()

    def addInputCaseToDb(self):

        answer = input("Do you want to add an Restaurant Press(yes(y)): ")
        while 1:
            if answer.lower() == 'yes' or answer.lower() =='y':
                data=input("Restaurant with semicolon betweem them: ")
                line=data.split(';')
                lines=list(line)
                obj=Restaurants(lines[0],lines[1],lines[2],lines[3],lines[4])
                if obj not in case_Db:    #funkar!!!
                   case_Db.append(obj)
                for i in case_Db:
                        print(i)
                answer = input("Do you want to add an Restaurant Press(yes(y)): ")
            else:
                print("No Restaurant added to list")
                break
        return case_Db

    def addRCase_To_Database(self,Restaurantcase):

        if Restaurantcase not in case_Db:
            case_Db.append(Restaurantcase)
        for i in case_Db:
            print(i)
        return case_Db

    def CSV_SaveToFile(self):
        print("Save to file!")
        with open("Db.csv","w") as csvfile:
            csvfile.write("Name,Type,Nationality,Quality,Price\n")
            for rad in case_Db:
                #print(rad)
                csvfile.write(str(rad) + "\n")
            print("Success!")
        csvfile.close()

    def SimPrice(self,obj):
        value = 0
        a = int(self.price)
        b = int(obj.price)

        if (a==0):
            value=1
        elif (a == b):
            value = 1
        elif (a + 1 == b or a - 1 == b):
            value = 0.8
        elif (a + 2 == b or a - 2 == b):
            value = 0.6
        elif (a + 3 == b or a - 3 == b):
            value = 0.4
        elif (a + 4 == b or a - 4 == b):
            value = 0.2

        return value

    def SimQuality(self,obj2):
        value = 0
        a = int(self.quality)
        b = int(obj2.quality)
        if (a==0):
            value =1
        elif (a == b):
            value = 1
        elif (a + 1 == b or a - 1 == b):
            value = 0.8
        elif (a + 2 == b or a - 2 == b):
            value = 0.6
        elif (a + 3 == b or a - 3 == b):
            value = 0.4
        elif (a + 4 == b or a - 4 == b):
            value = 0.2

        return value

    def SimType(self,obj2):
        value = 0
        a = self.type
        b = obj2.type
        if(a==0):
            value=1
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

    def SimNationality(self,obj2):
            value = 0
            a = self.nationality
            b = obj2.nationality
            if (a==0):
                value=1
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

    def Similarity(self,D):
            value = 0
            value = ((1 / 16) * ((2 * self.SimPrice(D)) + 2 * self.SimQuality(D) + 5 * self.SimType(D) + 7 * self.SimNationality(D)))
            return value

    def SimilarityDb(self,case_Db):
        bestValue=0
        bestRest=None
        for i in case_Db:
            obj=i
            if self.Similarity(obj) > bestValue:
                bestRest=obj
                bestValue=self.Similarity(obj)
        return "Best Restaurant: "+str(bestRest) +" and Value: "+str(bestValue)


def main():
 #1.Read the textfile
    Restaurants.CSV_ReadFile(case_Db, "big")
 #2.Create an Restaurant and add case to Database
    R=Restaurants("Soobi","Fastfood","American", 5,5)
    Restaurants.addRCase_To_Database(case_Db,R)
 #3.Similarity
    print("\n")

    for i in case_Db:
        print(i)


    print("similarity: ",case_Db[0].Similarity(case_Db[1]))
    #4.SimilarityDb
    name=input("name: ")
    type=input("type: ")
    nation=input("nationality: ")
    q=input("quality: ")
    p=input("price: ")
    R1=Restaurants(name,type,nation,int(q),int(p))

    print(R1.SimilarityDb(case_Db))

if __name__=='__main__':
    main()
