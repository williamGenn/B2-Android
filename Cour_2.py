class terrestre():
    
    def __init__(self,nombre, genre, domestique, regime, nb_pattes, quantite,mar):
        self.domestique=0
        self.regime=regime
        self.quantite=quantite
        self.nb_pattes = nb_pattes
        self.genre=genre
        self.nombre=nombre
        self.mar=0
                        
    def __str__(self):
        if (self.genre<1):
            if (self.domestique==1):
                return "\t  " + str(self.nombre)+ "\t   oui\t\t   oui\t\t   non\t  "+self.regime+" \t  "+str(self.nb_pattes)+" \t  "+str(self.quantite)
            if (self.domestique==0):
                return "\t  " + str(self.nombre)+ "\t   oui\t\t   non\t\t   non\t  "+self.regime+" \t  "+str(self.nb_pattes)+" \t  "+str(self.quantite)
        else:
            if (self.domestique==1):
                return "\t  " + str(self.nombre)+ "\t   non\t\t   oui\t\t   non\t  "+self.regime+" \t  "+str(self.nb_pattes)+" \t  "+str(self.quantite)
            if (self.domestique==0):
                return "\t  " + str(self.nombre)+ "\t   non\t\t   non\t\t   non\t  "+self.regime+" \t  "+str(self.nb_pattes)+" \t  "+str(self.quantite)
            
class aquatique():
    
    def __init__(self,nombre,regime,nb_pattes,quantite,mar):
        self.regime=regime
        self.quantite=quantite
        self.nb_pattes = 0
        self.nombre=nombre
        self.mar=1
        
        
        
        
    def __str__(self):
        
        return "\t  " + str(self.nombre)+ " \t   non \t\t   non  \t   oui\t  "+self.regime+" \t  "+str(self.nb_pattes)+" \t  "+str(self.quantite)


      
if __name__ == "__main__":
    total_nourriture=0.0
    nb_marin=0
    nb_omnivore=0
    nb_pattesf=0
    #on crée notre table
    mon_zoo={}
    mon_zoo["humain"]= terrestre(2,0,0,"omnivore",2,0.6,0)
    mon_zoo["Lion"]= terrestre(1,0,0,"carnivore",4,3,0)
    mon_zoo["Lapin"]= terrestre(7,0,1,"vegetarien",4,0.1,0)
    mon_zoo["Mouton"]= terrestre(5,0,0,"vegetarien",4,0.5,0)
    mon_zoo["Chien"]= terrestre(2,0,1,"omnivore",2,0.5,0)
    mon_zoo["Serpent"]= terrestre(2,1,0,"carnivore",0,0.2,0)
    mon_zoo["Autruch"]= terrestre(4,1,0,"omnivore",2,1,0)
    mon_zoo["Poule"]= terrestre(4,1,0,"omnivore",2,0.2,0)
    mon_zoo["Pieuvre"]= aquatique(1,"carnivore",0,0.2,1)
     
    
    print("\n\nAnimal   Nombre   Mammifère   Domestique   Animal marin    Régime      pattes   Quantité(Kg)")
    
    for my_key in mon_zoo:
        if ((mon_zoo[my_key].regime)=="omnivore"):
            nb_omnivore=nb_omnivore+1
        nb_marin = nb_marin+int(mon_zoo[my_key].mar)
        nb_pattesf=nb_pattesf+int(mon_zoo[my_key].nb_pattes)
        total_nourriture=total_nourriture+float(mon_zoo[my_key].quantite)
        #on affiche notre table avec en premier l'ID
        print(my_key+str(mon_zoo[my_key]))
    #on multiplie par 7 pour le nb de jours    
    total_nourriture=total_nourriture*7
    print("nourriture="+str(total_nourriture))
    print("marins="+str(nb_marin))
    print("omnivores="+ str(nb_omnivore))
    print("nombre pattes="+str(nb_pattesf))
     
    