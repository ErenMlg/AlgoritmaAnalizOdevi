import random
import time

def quicksort(siralanilacakDizi):
    if len(siralanilacakDizi) <= 1:
        return siralanilacakDizi
    pivot = siralanilacakDizi[len(siralanilacakDizi) // 2]
    sol = [x for x in siralanilacakDizi if x < pivot]
    orta = [x for x in siralanilacakDizi if x == pivot]
    sag = [x for x in siralanilacakDizi if x > pivot]
    return quicksort(sol) + orta + quicksort(sag)


# Aynı dizi üzerinde BruteForce algoritmasının çalışma süresini hesaplamak için ise,
# diziyi iki kez döngü kullanarak tüm elemanlarla karşılaştırabiliriz.
# Bu BruteForce algoritmasının çalışma süresi O(n^2) olacaktır.

def brute_force_sort(siralanilacakDizi):
    n = len(siralanilacakDizi)
    for i in range(n):
        for j in range(i+1, n):
            if siralanilacakDizi[i] > siralanilacakDizi[j]:
                siralanilacakDizi[i], siralanilacakDizi[j] = siralanilacakDizi[j], siralanilacakDizi[i]
    return siralanilacakDizi



def secim_islemi(siralanilacakDizi):
    print("\n\nMerhaba hangi algoritmayı kullanmak istersiniz\n1-Quicksort\n2-BruteForce")
    secim = input("Seçiniz: ")
    if secim == "1":
        # Divide and Conquer algoritmasının çalışma süresini hesapladık ve yazdırdık.
        baslangic_zamani = time.time()
        sonuc = quicksort(siralanilacakDizi)
        bitis_zamani = time.time()
        print("Quicksort algoritması ile sıralama:", sonuc)
        print("Quicksort algoritmasının çalışma süresi:", bitis_zamani - baslangic_zamani, "saniye")
        secim2_islemi()
    elif secim == "2":
        baslangic_zamani = time.time()
        sonuc = brute_force_sort(siralanilacakDizi)
        bitis_zamani = time.time()
        print("BruteForce algoritması ile sıralama:", sonuc)
        print("BruteForce algoritması çalışma süresi:", bitis_zamani - baslangic_zamani, "saniye")
        secim2_islemi()
    else:
        print("Hatalı bir giriş yaptınız...")
        secim_islemi(siralanilacakDizi)


def secim2_islemi():
    print("\n1-Aynı dizi ile farklı bir işlem yapmak için\n2-Farklı dizi ile farklı bir işlem yapmak için\n3-Kapatmak "
          "için")
    secim = input("Seçiniz: ")
    if secim == "1":
        secim_islemi(siralanilacakDizi)
    elif secim == "2":
        siralanilacakYeniDizi = [random.randint(-10000, 10000) for _ in range(10000)]
        secim_islemi(siralanilacakYeniDizi)
    elif secim == "3":
        exit()
    else:
        print("Hatalı bir giriş yaptınız...")
        secim2_islemi()

print("\nVeri sıralama algoritmaları, verilerin sayısı, boyutu, dağılımı ve hangi sıralama kriterleri kullanıldığına\n"
      "bağlı olarak farklı şekillerde performans gösterebilir. Ancak, en iyi sıralama algoritması\n"
      "olarak kabul edilen ve genellikle tercih edilen algoritma Quicksort'tur. \n\n"
      "Quicksort, n log n zamanda çalışır ve O(n^2) en kötü durumda çalışma süresine sahip olabilir. \n"
      "Ancak, verilerin çoğunlukla rastgele dağıldığı durumlarda, Quicksort, \n"
      "diğer sıralama algoritmalarından daha iyi performans gösterir.\n")
siralanilacakDizi = [random.randint(-10000, 10000) for _ in range(10000)]
secim_islemi(siralanilacakDizi)

