# -*- coding: utf-8 -*-
import datetime
import time
import math

class animal():
    def __init__(self,genre, age, sexe):
        self.genre=genre
        self.age=age
        self.sexe=sexe
        
        
    def __str__(self):  
        return self.genre + str(self.age) + self.sexe
        
        
        

class farm():
    def __init__(self,name):
        self.name=name
        self.list=[]
        
        
        
    def add(self,genre,age,sexe):
        global number
        self.list.append(animal(genre,age,sexe))
        print("nom= "+self.list[number].genre+ "  age="+str(self.list[number].age)+"  sexe="+self.list[number].sexe)
        number=number+1
        
    def aff(self,idx):
        print("nom= "+self.list[idx].genre+ "  age="+str(self.list[idx].age)+"  sexe="+self.list[idx].sexe)
        
        
    
    def __str__(self):  
        return self.name
    

        
if __name__ == "__main__": 
    
    number=0
    datetime_today = datetime.datetime.now() 
    my_delta = datetime.timedelta(days = 30) 
    new_date = datetime_today + my_delta
    print (new_date)
    
    
    
    
    
    Farm_list=[]
    Farm_list.append(farm("Première ferme"))
    print(Farm_list[0])
    Farm_list[0].add("vache",1,"F")
    Farm_list[0].add("vache",1,"M")
    timer=True
    count=0
    while timer is True:
        global list
        time.sleep (3)
        count=count+1
        new_date = new_date + my_delta
        if count % 12==0:
            for ix in number:
                Farm_list.age=Farm_list.age+1
        print (new_date)
        for idx in number:
            aff(idx)
            
        
        
    
        
    