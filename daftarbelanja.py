daftarBelanja = [
    "Sayur",
    "Minyak",
    "Beras",
    "Minyak",
    "Gula",
    "Garam",
    "Telur",
    "Bawang Merah", 
    "Bawang Putih",
    "Mie Instan"
]

def listCantik():
    for index, daftar in enumerate(daftarBelanja):
        print(f"{index}. {daftar}")

def tambahDaftar(nama):
    daftarBelanja.append(nama)

def hapusDaftar(nomor):
    daftarBelanja.pop(nomor)

while True:
    print("======Menu List Belanjaan======")
    print("1. Lihat barang belanjaan")
    print("2. Tambah barang belanjaan")
    print("3. Hapus barang belanjaan")
    print("0. Keluar")
    pilihan = input("Pilih Menu: ")
    if pilihan == "1":
        print("=======Daftar Belanja======")
        listCantik()
        print("\n")
    elif pilihan == "2":
        barang = input("Masukkan nama barang: ")
        tambahDaftar(barang)
        print("Barang berhasil ditambahkan! \n")
    elif pilihan == "3":
        number = int(input("Masukkan nomor barang: "))
        hapusDaftar(number)
        print("Barang berhasil dihapus! \n")
    else:
        break