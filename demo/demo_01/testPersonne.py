
# importer la classe Personne
from Personne import Personne
from datetime import date
phil = Personne("De belgique","Philippe",date(1960, 10, 9))
phil.parler("Bonjour")
print(phil.getage())
phil.setPrenom("phil")
print(phil.getPrenom())
