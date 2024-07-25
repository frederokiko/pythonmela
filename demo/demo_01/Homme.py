from Personne import Personne
class Homme(Personne) :
    def __init__(self,nom,prenom,dateNaissance) :
        Personne.__init__(self,nom,prenom,dateNaissance)
        self.__barbe=0
        def changerNom(self,newNom):
            self.__nom=newNom
        def changerPrenom(self,newPrenom):
            self._prenom=newPrenom

    def seRaser(self,cm):
        self.__barbe +=cm
        print(self.__barbe)