"""
def sorgu(db,sorgu):
   imlec=db.cursor()
   kmt=sorgu
   imlec.execute(kmt)
   return imlec
"""
def ekle(db,ekle):
    imlec=db.cursor()
    kmt=ekle
    imlec.execute(kmt)
    return imlec
