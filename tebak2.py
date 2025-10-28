import random

jawaban = random.randrange(1,10)
attemp = 0
while True:
    print("\nPilih Game: \n1.Tebak Angka \n0.Keluar")
    pilihan = input("Silahkan Pilih: ")
    if pilihan == "1":
        while True:
            print("\nGame Mulai ")
            tebak = input("Tebak Angka: ")
            if tebak == str(jawaban):
                print("Selamat kamu menang!")
                print("Jawabannya: ", jawaban, "\n")
                break
            else:
                attemp += 1
                print("Salah, Coba lagi! (Percobaan ke-" + str(attemp) + ")" )
                if attemp > 5:
                    print("Percobaan habis, jawabannya: ", jawaban)
                    break
    else :
        break