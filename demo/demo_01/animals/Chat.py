from Animal import Animal
class Chat(Animal):
    nb_chat=0
    def __init__(self,nom,couleur) :
        Animal.__init__(self,nom,4,couleur,"Miaou")
        Chat.nb_chat+=1
        
        