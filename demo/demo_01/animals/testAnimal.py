from Chien import Chien
from Chat import Chat
from Animal import Animal

print(Animal.nb_animal)
chien1 =Chien ("Medor","vert")
chat1=Chat("Minou","bleu")
chien1.crier()
chat1.crier()
print("nbr animaux :",Animal.nb_animal)
print("nbr chat :",Chat.nb_chat)
print("nbr chien :",Chien.nb_chien)