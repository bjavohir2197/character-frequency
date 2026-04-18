def harflar_soni(s):
    harflar = {}
    for harf in s:
        if harf in harflar:
            harflar[harf] += 1
        else:
            harflar[harf] = 1
    return harflar

def qatnashgan_soni(s):
    harflar = harflar_soni(s)
    qatnashgan_soni = {}
    for harf, son in harflar.items():
        qatnashgan_soni[son] = qatnashgan_soni.get(son, 0) + 1
    return qatnashgan_soni

def main():
    s = input("Istalgan matn kiriting: ")
    qatnashgan_soni = qatnashgan_soni(s)
    for son, qatnashgan_soni in qatnashgan_soni.items():
        print(f"{son} martaga qatnashgan harflar: {', '.join([str(harf) for harf in [k for k, v in harflar_soni(s).items() if v == son]])}")

if __name__ == "__main__":
    main()
```

Kodni ishlatish uchun quyidagicha amal qilishingiz mumkin:

1. Kodni yuklab oling va Python ni o'rnatgan kompyuterda ishlab ko'ring.
2. Kodni yuklab olingan joyga saqlab oling.
3. Kompyuterda terminal yoki command prompt ni ochib, kodni ishlab ko'rish uchun quyidagicha amal qiling:
 * Windowsda: `python kod.py` (kod.py - bu kodni saqlagan joy)
 * Mac yoki Linuxda: `python3 kod.py` (kod.py - bu kodni saqlagan joy)
4. Kompyuterda terminal yoki command promptda quyidagicha amal qiling:
 * Istalgan matnni kiriting (masalan: "Hello, World!")
 * Matnni kiritingdan keyin Enter tugmasini bosib, kod ishlay boshlaydi.
5. Kod ishlay boshlagandan keyin quyidagicha amal qiling:
 * Kod quyidagicha natijani chiqaradi:
 * 1 martaga qatnashgan harflar: harf1, harf2, ...
 * 2 martaga qatnashgan harflar: harf3, harf4, ...
 * 3 martaga qatnashgan harflar: harf5, harf6, ...
 * ...
