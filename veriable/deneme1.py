# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 01:01:52 2022

@author: 90542
"""
print("Merhaba Hoşgeldiniz!\n")
isim= input("isminiz: ")
yas= int(input("yaşınız: "))
egitimdurumu= input("eğitim durumunuz: ")
if (yas>=18):
    if (egitimdurumu == 'lise' or "üniversite"):
        print (isim +' ehliyet alabilirsin.')
    else:
        print (isim + " malesef ehliyet almak için eğitim durumun yetersiz")
else:
    print (isim + " ehliyet almak için yaşın küçük.")
    
    