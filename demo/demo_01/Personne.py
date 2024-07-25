from datetime import datetime
from abc import ABC,abstractmethod

class Personne(ABC):
    @abstractmethod
    def __init__(self,nom,prenom,dateNaissance) :
        self.__nom=nom
        self._prenom=prenom
        self.__dateNaissance=dateNaissance
        pass
    #setter
    def setPrenom(self,newPrenom):
        self._prenom=newPrenom
    #getter
    def getPrenom(self):
        return self._prenom
    # procedure
    def parler(self,phrase):
        print(phrase)
    #fonction self = this
    def getage(self): 
        dateNow=datetime.now()
       
        return dateNow.year - self.__dateNaissance.year   
    def sePresenter(self):
        print("je m'appelle",self.__prenom,self.__nom)