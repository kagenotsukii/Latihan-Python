def penjumlahan(angka1, angka2):
    x = angka1 + angka2
    return float(x)

def pengurangan(angka1, angka2):
    x = angka1 - angka2
    return float(x)

def pembagian(angka1, angka2):
    x = angka1 / angka2
    return float(x)

def perkalian(angka1, angka2):
    x = angka1 * angka2
    return  float(x)

def gagen(hasil):
    if int(hasil) % 2 == 0:
        return ("Genap")
    else:
        return ("Ganjil")
    

while True:
    print("======Kalkulator======")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Pembagian")
    print("4. Perkalian")
    print("0. Keluar")
    pilihan = input("Silahkan masukkan pilihan dari 1-4: ")
    if pilihan == "1":
        x1 = int(input("Angka pertama: "))
        x2 = int(input("Angka kedua: "))
        print(f"\nHasil {x1} + {x2} adalah = ", penjumlahan(x1, x2), gagen(penjumlahan(x1, x2)), "\n")
    elif pilihan == "2":
        y1 = int(input("Angka pertama: "))
        y2 = int(input("Angka kedua: "))
        print(f"\nHasil {y1} - {y2} adalah = ", pengurangan(y1, y2),gagen(pengurangan(y1, y2)), "\n")
    elif pilihan == "3":
        t1 = int(input("Angka pertama: "))
        t2 = int(input("Angka kedua: "))
        print(f"\nHasil {t1} : {t2} adalah = ", pembagian(t1, t2),gagen(pembagian(t1, t2)), "\n")
    elif pilihan == "4":
        r1 = int(input("Angka pertama: "))
        r2 = int(input("Angka kedua: "))
        print(f"\nHasil {r1} x {r2} adalah = ", perkalian(r1, r2),gagen(perkalian(r1, r2)), "\n")
    else:
        break
    