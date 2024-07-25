from abc import ABC,abstractmethod
class Animal(ABC) :
    nb_animal=0
    @abstractmethod
   
    def __init__(self,nom,nbPattes,couleur,son) :
       self.nom=nom
       self.nbPattes=nbPattes
       self.couleur=couleur
       self.son=son
       Animal.nb_animal+=1
       
    nom =""
   
    #nbPattes=4
    couleur =""
    def crier(self):
            print("Je m'appele :",self.nom,"j'ai :",self.nbPattes
                  ,"papattes et mon cri est:",self.son)
    

    