from Animal import Animal
class Chien(Animal):
    nb_chien=0
    def __init__(self,nom,couleur,) :
        Animal.__init__(self,nom,4,couleur,"Waf")
        Chien.nb_chien+=1
        
      
       