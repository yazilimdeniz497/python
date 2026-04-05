cikolatafiyati=0.99
sutfiyati=1.10
ekmekfiyati=1.25
cikolataadet=5
sutadet=1
ekmekadet=3
toplamcikolatafiyati=cikolatafiyati*cikolataadet
toplamsutfiyati=sutfiyati*sutadet
toplamekmekfiyati=ekmekadet*ekmekfiyati
toplamfiyat=toplamcikolatafiyati+toplamekmekfiyati+toplamsutfiyati
kasayaodenen=10
netfiyat=kasayaodenen-toplamfiyat
print("Toplam Fiyat: ",netfiyat)