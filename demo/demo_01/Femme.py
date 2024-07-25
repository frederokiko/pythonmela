from Personne import Personne
import random;

class Femme(Personne) :
    def __init__(self,nom,prenom,dateNaissance) :
        Personne.__init__(self,nom,prenom,dateNaissance)
        self._isenceinte=False
        # def tombeEnceinte(self,booli):
        #      self._isenceinte = booli

    def Accoucher(self):
        # self.isenceinte=ok
        if not self._isenceinte :
            
             print("elle ne vas pas accoucher elle n'est meme pas enceinte ;)")
 
        else:
            sexe =random.randint(1,2)
            if sexe==1 :
                print("elle à accouché d'un garcon")
                self._isenceinte=False
                print("et n'est plus enceinte bluetooh 🤣")
            else :
                print("elle à accouché d'une fille")
                self._isenceinte=False
                print("et n'est plus enceinte bluetooh 😂" )