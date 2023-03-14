import time


def divide_conquer_max(aranilanDizi):
    n = len(aranilanDizi)
    # Dizi boyutu 1 ise, tek eleman da en büyük sayıdır
    if n == 1:
        return aranilanDizi[0]
    # Dizi boyutu 2 ise, iki elemanın en büyüğü en büyük sayıdır
    elif n == 2:
        if aranilanDizi[0] > aranilanDizi[1]:
            return aranilanDizi[0]
        else:
            return aranilanDizi[1]
    else:
        # Dizi ortası belirlenir
        ortaEleman = n // 2
        # Sol ve sağ alt diziler oluşturulur
        solDizi = aranilanDizi[:ortaEleman]
        sagDizi = aranilanDizi[ortaEleman:]
        # Her bir alt dizi içindeki en büyük sayıları bulduk
        sol_max_eleman = divide_conquer_max(solDizi)
        sag_max_eleman = divide_conquer_max(sagDizi)
        # Her iki alt dizi içindeki en büyük sayıları karşılaştırdık
        if sol_max_eleman > sag_max_eleman:
            return sol_max_eleman
        else:
            return sag_max_eleman
        # Bu algoritma ortalama olarak O(n log n) zamanda çalışır. Yukarıdaki kodda 10,000 elemanlı bir dizide
        # çalıştırıldığında, işlem süresi yaklaşık 0.001 saniye civarındadır.


def brute_force_max(aranilanDizi):
    en_buyuk_sayi = aranilanDizi[0]
    for sayi in aranilanDizi:
        if sayi > en_buyuk_sayi:
            en_buyuk_sayi = sayi
    return en_buyuk_sayi


def secim_islemi(aranilanDizi):
    print("Merhaba hangi algoritmayı kullanmak istersiniz\n1-Divide and Conquer\n2-BruteForce")
    secim = input("Seçiniz: ")
    if secim == "1":
        # Divide and Conquer algoritmasının çalışma süresini hesapladık ve yazdırdık.
        baslangic_zamani = time.time()
        sonuc = divide_conquer_max(aranilanDizi)
        bitis_zamani = time.time()
        print("Divide and Conquer algoritması ile en büyük sayı:", sonuc)
        print("Divide and Conquer algoritmasının çalışma süresi:", bitis_zamani - baslangic_zamani, "saniye")
        secim2_islemi()
    elif secim == "2":
        baslangic_zamani = time.time()
        sonuc = brute_force_max(aranilanDizi)
        bitis_zamani = time.time()
        print("BruteForce algoritması ile en büyük sayı:", sonuc)
        print("BruteForce algoritması çalışma süresi:", bitis_zamani - baslangic_zamani, "saniye")
        secim2_islemi()
    else:
        print("Hatalı bir giriş yaptınız...")
        secim_islemi(aranilanDizi)


def secim2_islemi():
    print("\n1-Aynı dizi ile farklı bir işlem yapmak için\n2-Farklı dizi ile farklı bir işlem yapmak için\n3-Kapatmak "
          "için")
    secim = input("Seçiniz: ")
    if secim == "1":
        secim_islemi(aranilanDizi)
    elif secim == "2":
        aranilacakYeniDizi = [random.randint(0, 1000000) for _ in range(10000)]
        secim_islemi(aranilacakYeniDizi)
    elif secim == "3":
        exit()
    else:
        print("Hatalı bir giriş yaptınız...")
        secim2_islemi()


# 10,000 elemanlık bir dizi oluşturduk
import random

aranilanDizi = [random.randint(0, 1000000) for _ in range(10000)]

print('\nEn hızlı yöntem olarak Divide and Conquer (Böl ve Fethet) algoritması kullanılabilir.\n'
      'Bu algoritma, dizi içindeki en büyük sayıyı hızlı bir şekilde bulmak için verimli bir yöntemdir.\n'
      'İlk önce dizinin ortasındaki elemanı seçerek, bu elemandan önceki ve sonraki alt diziler oluşturulur.\n'
      'Bu alt diziler içinde en büyük sayı aranır ve bu sayı, ana dizideki en büyük sayı ile karşılaştırılır.\n'
      'Eğer alt dizideki en büyük sayı daha büyükse, bu sayı yeni en büyük sayı olarak seçilir ve işlem alt diziler\n'
      'için tekrarlanır.\n')

secim_islemi(aranilanDizi)
