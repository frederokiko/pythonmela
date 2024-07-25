from Homme import Homme
from datetime import date
phil = Homme("De belgique","Philippe",date(1960, 10, 9))
phil.parler("Bonjour")
print(phil.getage())
# phil.barbe=5
# print(phil.barbe)
phil.seRaser(5)
phil.setPrenom("phil")
print(phil.getPrenom())
