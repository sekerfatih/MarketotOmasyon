
#Muhammet Fatih ŞEKER   18010011038

ürünn = ["Marka", "Ad", "Çeşit", "TETT", "Adet", "Fiyat", "Stok Numara"]
toplamürün = {}
liste = list
stok = [0]*100
satılan = [0]*100
iadeedilen = [0]*100
k = j = a = toplam = satış = 0



def ürünekle():

    print("Lütfen ")
    with open("dosya.txt", "a", encoding ="utf-8") as dosya:

        global liste
        global stok
        global ürünn
        global toplamürün

        ürün = input("Ürün Markası: ")
        dosya.write(ürün + ' ')

        ürün = input("Ürün Adı:  ")
        dosya.write(ürün + ' ')

        ürün = input("Ürün Çeşidi ")
        dosya.write(ürün + ' ')

        ürün = input("Ürün Tavsiye Edilen Tüketim Tarihi: ")
        dosya.write(ürün + ' ')

        ürün = input("Ürün Adedi: ")
        dosya.write(ürün + ' ')

        ürün = input("Ürün Fiyatı: ")
        dosya.write(ürün + ' ')

        ürün = input("Ürün Stok Numarası: ")
        dosya.write(ürün)
        dosya.write("\n")
        dosya.write = sözlük()
        print("\n")

def sözlük(): #dosyadaki verileri nested sözlüğe dönüştüryor

    with open("dosya.txt","r+", encoding = "utf-8") as dosya:

        global liste
        global ürünn
        global toplamürün
        global stok
        global j

        liste = dosya.read().splitlines()

        for line in liste:

            value = line.split(" ")
            ürünler = {}
            stok[j] = value[6]
            j += 1
            for i in range (0,7):
                ürünler[ürünn[i]] = value[i]

            toplamürün[value[6]] = ürünler



def dos(): #sözlükteki bilgileri dosyaya aktarıyor.
    with open("dosya.txt", "w", encoding="utf-8") as dosya:

        global stok
        global toplamürün

        for i in range (0,100):

            if (stok[i] != 0):
                dosya.write(str(toplamürün[stok[i]]['Marka']) + ' ')
                dosya.write(str(toplamürün[stok[i]]['Ad']) + ' ')
                dosya.write(str(toplamürün[stok[i]]['Çeşit']) + ' ')
                dosya.write(str(toplamürün[stok[i]]['TETT']) + ' ')
                dosya.write(str(toplamürün[stok[i]]['Adet']) + ' ')
                dosya.write(str(toplamürün[stok[i]]['Fiyat']) + ' ')
                dosya.write(str(toplamürün[stok[i]]['Stok Numara']))
                dosya.write("\n")

            else:
                continue




def ürünçıkar(x):

    global toplamürün
    global stok

    del toplamürün[x]

    for i in range (0,100):
        if (stok[i] == x):
            stok[i] = 0
            dosya.write = dos()
            break

def ürüngüncelle():

    global toplamürün
    global stok

    x = input("Lütfen güncellemek istediğiniz ürünün stok numarasını giriniz: ")
    y = int(input("[1] Ürün markasını değiştir\n"
              "[2] Ürün adını değiştir\n"
              "[3] Ürün çeşidini\n"
              "[4] Ürün TETT değiştir\n"
              "[5] Ürün adedini değiştir\n"
              "[6] Ürün fiyatını değiştir\n"
              "[7] Ürün stok numarasını değiştir\n"))


    if y == 1:
        toplamürün[x]['Marka'] = input("Lütfen yeni bilgiyi giriniz: ")

    if y==2:
        toplamürün[x]['Ad'] = input("Lütfen yeni bilgiyi giriniz: ")

    if y==3:
        toplamürün[x]['Çeşit'] = input("Lütfen yeni bilgiyi giriniz: ")

    if y==4:
        toplamürün[x]['TETT'] = input("Lütfen yeni bilgiyi giriniz: ")

    if y==5:
        toplamürün[x]['Adet'] = input("Lütfen yeni bilgiyi giriniz: ")

    if y==6:
        toplamürün[x]['Fiyat'] = input("Lütfen yeni bilgiyi giriniz: ")

    if y==7:
        toplamürün[x]["Stok Numara"] = input("Lütfen yeni bilgiyi giriniz: ")

    dosya.write = dos()

def ürünara():

    global toplamürün
    global stok
    x = input("Lütfen aramak istediğiniz ürünün stok numarasını giriniz: ")
    print("\n")

    for y in range(0,100):

        if stok[y] == x:
            for i, j in toplamürün[x].items():
                print(i, j, sep=': ')
            break


        elif y == 100:
            print("Girdiğiniz stok numarası bulanamadı. Tekrar deneyiniz.")
            ürünara()
            break


def satışyap():

    b = 0
    while b == 0:

        global toplamürün
        global satış

        x = input("Lütfen satışını gerçekleştirdiğiniz ürünün stok numarasını giriniz: ")
        y = input("{} {} ürününden {} adet bulunmaktadır.\n"
                "Satılacak ürün adedi: ".format(toplamürün[x]['Marka'], toplamürün[x]['Ad'], toplamürün[x]['Adet']))
        print("\n")

        def detay(x, y, satış):  # satışı yapılan ürün bilgilerini günlük rapor için listeye aktarır

            global toplamürün
            global k
            global satılan

            satılan[k] = ('Ürün: ' + toplamürün[x]['Marka'] + ' ' + toplamürün[x]['Ad'] + '\n' + 'Birim Fiyatı: '
                          + toplamürün[x]['Fiyat'] + '\n' + 'Satılan Adet: ' + str(
                        y) + '\n' + 'Kasaya Giren Para: ' + str(satış))
            k += 1


        if int(toplamürün[x]["Adet"]) - int(y) == 0:
            satış += (float(toplamürün[x]['Fiyat'])) * int(y)
            toplamürün[x]["Adet"] = int(toplamürün[x]['Adet']) - int(y)
            print("Üründen başarıyla {} adet sattınız.\nBirim fiyatı: {}\nKasaya eklenen para: {}\nKalan ürün: Ürün tükendi"
                  .format(y,toplamürün[x]['Fiyat'],(float(toplamürün[x]['Fiyat'])) * int(y)))
            detay(x,y,satış)
            ürünçıkar(x)
            b=1

        elif int(toplamürün[x]["Adet"]) - int(y) < 0:
            print("Bu üründen elinizde {} adet bulunmaktadır. Lütfen tekrar deneyiniz.".format(toplamürün[x]["Adet"]))

        elif int(toplamürün[x]['Adet']) - int(y) > 0:

            toplamürün[x]["Adet"] = int(toplamürün[x]['Adet']) - int(y)

            print("Üründen başarıyla {} adet sattınız.\nBirim fiyatı: {}\nKasaya eklenen para: {}"
                  .format(y, toplamürün[x]['Fiyat'], (float(toplamürün[x]['Fiyat'])) * int(y)))

            print("Kalan ürün adedi: {}\n".format(toplamürün[x]['Adet']))

            satış = (float(toplamürün[x]['Fiyat'])) * int(y)
            detay(x, y, satış)
            b=1

        dosya.write = dos()


def iadeal():

    global toplamürün
    global stok
    global satış
    global toplam
    a = 0

    x = input("Lütfen iade edilen ürünün stok numarasını giriniz: ")
    y = input("Lütfen iade edilen ürün adedini giriniz: ")

    def iade(x, y, satış):  # iadesi yapılan ürün bilgilerini günlük rapor için listeye aktarır

        global toplamürün
        global j
        global iadeedilen

        iadeedilen[j] = ('Ürün: ' + toplamürün[x]['Marka'] + ' ' + toplamürün[x]['Ad'] + '\n' + 'Birim Fiyatı: '
                      + toplamürün[x]['Fiyat'] + '\n' + 'İade Edilen Adet: ' + str(
                    y) + '\n' + 'Kasadan Çıkan Para: ' + str(satış))
        j += 1

    for i in range (0,100):
        if stok[i] == x:
            toplamürün[x]['Adet'] = int(toplamürün[x]['Adet']) + int(y)
            print("{} {} ürününe {} adet iade edilmiştir.".format(toplamürün[x]['Marka'], toplamürün[x]['Ad'], y))
            satış = float(toplamürün[x]['Fiyat']) * int(y)
            toplam -=satış
            print("Kasadan çıkarılan para: {}".format(float(toplamürün[x]['Fiyat']) * int(y)))
            iade(x, y, satış)
            dosya = dos()
            a = 1

    if a == 0:
        print("Bu ürün tükenmiştir. Lütfen ürünü yeniden ekleyiniz.")
        dosya = ürünekle()
        satış = float(toplamürün[x]['Fiyat']) * int(y)
        toplam -= satış
        print("Kasaya eklenen para: {}".format(float(toplamürün[x]['Fiyat']) * int(y)))
        iade(x, y, satış)



def rapor():

    global toplamürün
    print("Kasaya Giren Toplam Para: {}\n".format(toplam))

    for i in range (0,100):
        if satılan[i] != 0:
            print(satılan[i])
            print("\n")

    print("İade Edilen Ürünler")

    for i in range (0,100):
        if iadeedilen[i] != 0:
            print(iadeedilen[i])
            print("\n")




while a < 8:

    with open("dosya.txt", "a", encoding="utf-8") as dosya:

        dosya.write=sözlük()

    a = int(input("[1] Ürün Ekle\n"
              "[2] Ürün Çıkar\n"
              "[3] Ürün Güncelle\n"
              "[4] Ürün Ara\n"
              "[5] Satış Yap\n"
              "[6] İade Al\n"
              "[7] Günlük Rapor Çıkar\n"
              "[8] Çıkış\n"))


    if a == 1:
        dosya = ürünekle()
        print("Ürün başarıyla eklenmiştir.")
        print("\n")

    if a == 2:
        x = input("Lütfen silmek istediğiniz ürünün stok numarasını giriniz: ")
        dosya = ürünçıkar(x)
        print("Ürün başarıyla çıkarılmıştir.")
        print("\n")

    if a == 3:
        dosya = ürüngüncelle()
        print("Ürün başarıyla güncellenmiştir.")
        print("\n")

    if a == 4:
        ürünara()
        print("\n")

    if a == 5:
        dosya = satışyap()
        print("\n")

    if a == 6:
        dosya = iadeal()
        print("\n")

    if a == 7:
        rapor()
        print("\n")

    if a == 8:
        break
