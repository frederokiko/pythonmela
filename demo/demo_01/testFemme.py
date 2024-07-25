from Femme import Femme
from datetime import date
lulu = Femme("DeMeisje","Mathilde",date(1965, 11, 9))
lulu.parler("Bonjour")
print(lulu.getage(),"ans")
# phil.barbe=5
# print(phil.barbe)
#lulu.seRaser(5)
#lulu.setPrenom("phil")
print(lulu.getPrenom())
lulu._isenceinte=True
print(lulu._isenceinte)
lulu.Accoucher()
print(lulu._isenceinte)