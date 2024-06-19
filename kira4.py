def Kira ():
    """Mendapatkan nilai darab,bahagi dan kuasa dua bagi nombor dimasukkan"""
    #Memasukkan nombor
    x = int(input("Masukkan nombor pertama :"))
    y = int(input("Masukkan nombor kedua :"))

    if x > y :
        #Mengira Hasil Bahagi Bagi Nombor Yang Dimasukkan
        HasilBahagi = y/x
        print("Hasil bahagi nombor adalah :", HasilBahagi)
    elif x < y :
        #Mengira Hasil Darab Bagi Nombor Yang Dimasukkan
        HasilDarab = x * y
        print("Hasil darab nombor adalah :", HasilDarab)
    elif x == y :
        #Mengira Kuasa dua Bagi Nombor Yang Dimasukkan
        HasilKuasa = x **2
        print("Hasil Kuasa nombor adalah :", HasilKuasa)

Kira ()