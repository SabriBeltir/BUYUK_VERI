import function

import sqlite3
from types import ModuleType
db=sqlite3.connect('Odev.db') #veri tabanı olusturma
#db1=sqlite3.connect('C:/Users/User/Desktop/Büyük Veri Ödev/Odev1.db')

imlec=db.cursor()
kmt="CREATE TABLE IF NOT EXISTS veriler(ad,soyad,numara)"  # tablo olusturma 
imlec.execute(kmt)

"""
# ^EKLEME^

kmt="INSERT INTO veriler VALUES('ali','efe',13)"
imlec.execute(kmt)

#db.commit()

kmt="Select * from veriler"
imlec.execute(kmt)

verilenler=imlec.fetchall()
print(verilenler)

for blg in imlec:
   print(blg)

print(imlec.fetchone())
print(imlec.fetchone())
print(imlec.fetchone())
print(imlec.fetchone())
print(imlec.fetchone())
"""
"""
# ^LİSTELEME^

#kmt="Select * from veriler where ad={}".format('sabri')
#kmt="Select * from veriler where ad='sabri'
#imlec.execute(kmt)
kmt="Select * from veriler where ad=?"
imlec.execute(kmt,('ali,')))
blg=imlec.fetchone()

print ("ad : "+str(blg[0]))
print ("soyad : "+str(blg[1]))
print ("numara : "+str(blg[2]))
"""
"""
#birden fazla kayıt gosterme
kmt="Select * from veriler"
imlec.execute(kmt)
verilenler=imlec.fetchmany(1)
print(verilenler)
"""
"""
kmt="Select * from veriler"
imlec.execute(kmt)

for blg in range(6):
   print(imlec.fetchone())
   """

# ^GÜNCELLEME^

kmt="UPDATE veriler SET numara=? where ad=?" 
imlec.execute(kmt,(100,'sabri'))
db.commit()
"""
kmt="Select * from veriler"
imlec.execute(kmt)
verilenler=imlec.fetchall()
print(verilenler)
"""
kmt="Select * from veriler"
verilenler=function.ekle(db,kmt).fetchall()
print(verilenler)




# ^SİLME^
"""
kmt="Delete from veriler where ad=?"
imlec.execute(kmt,('ali',))
db.commit()

kmt="Select * from veriler"
imlec.execute(kmt)
verilenler=imlec.fetchall()
print(verilenler)


kmt="Select * from veriler"
verilenler=function.sil(db,kmt).fetchall()
print(verilenler)
"""

#fetchall=Bütün verileri çeker
#fetchone=Sadece bir veriyi ceker
#fetchmany=İstediğimiz kadar veri veker

db.close() #veri tabanını kapatmak