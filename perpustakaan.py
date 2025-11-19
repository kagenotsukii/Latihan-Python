import json, csv, os

filePath_json = "database.json" # daftar buku, status peminjaman, daftar user
filePath_csvBuku = "dataBuku.csv"
filePath_csvUser = "dataUser.csv"
filePath_csvRiwayat = "dataiwayat.csv"

class RLPages:
    def __init__(self):
        pass
    
    def register(self):
        with open(filePath_json, "r") as jr:
            data = json.load(jr)
        username = input("Masukkan username: ")
        if username in data["Users"]:
            print("Username sudah ada")
            return
        password = input("Masukkan password: ")
        data["Users"][username] = {"password": password, "role": "Member"}
        with open(filePath_json, "w") as jw:
            json.dump(data, jw, indent=4)

    def login(self): # Sistem Login
        with open(filePath_json, "r") as js:
            data = json.load(js)
        print("====== Login ======")
        userInput = input("Masukkan username: ")
        passInput = input("Masukkan password: ")
        if userInput in data["Users"] and data["Users"][userInput]["password"] == passInput:
            return { "role": data["Users"][userInput]["role"],
                    "username": userInput}

def menuSistemAdmin(): # Interface Menu Untuk Admin
    menu = """=== SISTEM PERPUSTAKAAN ===
1. Lihat semua buku
2. Pinjam buku
3. Kembalikan buku
4. Riwayat semua user
5. Tambah buku
6. Hapus buku
7. Edit data buku
8. Hapus user
9. Edit role user
10. Ekspor -> CSV
11. Save data JSON
12. Muat data JSON
0. Keluar"""
    print(menu)

def menuSistemMember():  # Interface Menu Untuk Member
    menu = """=== SISTEM PERPUSTAKAAN ===
1. Lihat semua buku
2. Lihat buku tersedia
3. Pinjam buku
4. Kembalikan buku
5. Riwayat saya
0. Keluar"""
    print(menu)   

class User: # Class untuk User
    def __init__(self):
        pass

    def pinjamBuku(self, user):
        with open(filePath_json, "r") as jr:
            data = json.load(jr)
        cariBuku = input("Masukkan judul buku: ")
        if cariBuku in data["Books"]:
            if data["Books"][cariBuku]["status"] == "Dipinjam":
                if data["Books"][cariBuku]["dipinjamOleh"] == user:
                    print("Buku telah kamu pinjam! ")
                else:
                    print("Buku sedang dipinjam orang lain")
            else:
                for judul, info in data["Books"].items():
                    data["Books"][cariBuku]["status"] = "Dipinjam"
                    data["Books"][cariBuku]["dipinjamOleh"] = user
                    data["Riwayat"][user].append(f"Meminjam buku {cariBuku}")
                    with open(filePath_json, "w") as jw:
                        json.dump(data, jw, indent=4)
                    print(f"Buku dengan judul {judul} berhasil dipinjam")
        else:
            print("Buku tidak ada.")

    def kembalikanBuku(self, user):
        with open(filePath_json, "r") as jr:
            data = json.load(jr)
        cariBuku = input("Masukkan judul buku: ")
        if cariBuku in data["Books"]:
            if data["Books"][cariBuku]["status"] == "Dipinjam":
                if data["Books"][cariBuku]["dipinjamOleh"] == user:
                    data["Books"][cariBuku]["status"] = "Tersedia"
                    data["Books"][cariBuku].pop("dipinjamOleh")
                    with open(filePath_json, "w") as jw:
                        json.dump(data, jw, indent=4)
                    print(f"Buku dengan judul {cariBuku} berhasil dikembalikan")
                else:
                    print("Buku sedang dipinjam orang lain")
            elif data["Books"][cariBuku]["status"] != "Dipinjam":
                print("Buku tersedia")
        else:
            print("Buku tidak ada")

    def lihatRiwayat(self, user):
        with open(filePath_json, "r") as jr:
            data = json.load(jr)
        for index, riwayat in enumerate(data["Riwayat"][user]):
            print(f"{index + 1}. {riwayat}")            

class Admin(User):
    def __init__(self):
        super().__init__()
        
    def lihatRiwayat(self, user=None):
        with open(filePath_json, "r") as jr:
            data = json.load(jr)
        for u, riwayat in data["Riwayat"].items():
            print(f"{u} : {riwayat}")           

    def tambahBuku(self):
        with open(filePath_json, "r") as jr:
            data = json.load(jr)
        judulBuku = input("Masukkan judul buku: ")
        penulisBuku = input("Masukkan penulis buku: ")
        tahunBuku = input("Masukkan tahun buku dibuat: ")
        statusAwal = "Tersedia"
        data["Books"][judulBuku] = {"id": len(data["Books"])+1,"tahun": tahunBuku, "penulis": penulisBuku, "status": statusAwal}
        with open(filePath_json, "w") as jw:
            json.dump(data, jw, indent=4)

    def hapusBuku(self):
        with open(filePath_json, "r") as jr:
            data = json.load(jr)
        bukuYangDihapus = input("Masukkan buku yang mau dihapus: ")
        data["Books"].pop(bukuYangDihapus)
        with open(filePath_json, "w") as jw:
            json.dump(data, jw, indent=4)
    
    def editDataBuku(self):
        with open(filePath_json, "r") as jr:
            data = json.load(jr)
        namaBuku = input("Masukkan judul buku yang mau diedit: ")
        if namaBuku not in data["Books"]:
            print("Buku tidak ada!")
            return
        yangMaudiEdit = input("Masukkan part yang mau diedit: ")
        if yangMaudiEdit.lower() not in data["Books"][namaBuku]:
            print("Part hanya ada |Judul|Penulis|Tahun|")
            return
        perubahan = input("Masukkan perubahan: ")
        data["Books"][namaBuku][yangMaudiEdit.lower()] = perubahan
        with open(filePath_json, "w") as jw:
            json.dump(data, jw, indent=4)

    def hapusUser(self):
        with open(filePath_json, "r") as jr:
            data = json.load(jr)
        username = input("Masukkan username yang mau dihapus: ")
        data["Users"].pop(username)
        with open(filePath_json, "w") as jw:
            json.dump(data, jw, indent=4)
    
    def editRole(self):
        with open(filePath_json, "r") as jr:
            data = json.load(jr)
        username = input("Masukkan username yang mau diubah role-nya: ")
        menu = f"""==== Ubah Role {username} ====
        1. Admin
        2. Member"""
        print(menu)
        pilihanRole = input("Pilih role: ")
        if pilihanRole == "1": 
            roleUser = "Admin"
            data["Users"][username]["role"] = roleUser
        elif pilihanRole == "2":
            roleUser = "Member"
            data["Users"][username]["role"] = roleUser
        else:
            print("Role tidak ada")
        with open(filePath_json, "w") as jw:
            json.dump(data, jw, indent=4)

    def muatData(self):
        with open(filePath_json, "r") as jr:
            return json.load(jr)

    def saveData(self, data):
        with open(filePath_json, "w") as jw:
            json.dump(data, jw, indent=4)

    def importCSV(self):
        with open(filePath_json, "r") as jr:
            data = json.load(jr)
        dataBuku = data["Books"]
        dataUser = data["Users"]
        dataRiwayat = data["Riwayat"]
        data_csvBuku = []
        data_csvUser = []
        data_csvRiwayat = []
        for judul, infoBuku in dataBuku.items():
            data_csvBuku.append({"id": infoBuku["id"], "judul": judul, "penulis": infoBuku["penulis"], "tahun": infoBuku["tahun"], "status": infoBuku["status"]})
        for nama, infoUser in dataUser.items():
            data_csvUser.append({"username": nama, "password": infoUser["password"], "role": infoUser["role"]})
        for nama, infoRiw in dataRiwayat.items():
            data_csvRiwayat.append({"nama": nama, "riwayat": infoRiw})
        with open(filePath_csvBuku, "w", newline="") as cwb:
            kolomBuku = ["id", "judul", "penulis", "tahun", "status"]
            writerBuku = csv.DictWriter(cwb, fieldnames=kolomBuku)
            writerBuku.writeheader()
            writerBuku.writerows(data_csvBuku)
        with open(filePath_csvUser, "w", newline="") as cwu:
            kolomUser = ["username", "password", "role"]
            writerUser = csv.DictWriter(cwu, fieldnames=kolomUser)
            writerUser.writeheader()
            writerUser.writerows(data_csvUser)
        with open(filePath_csvRiwayat, "w", newline="") as cwr:
            kolomRiwayat = ["nama", "riwayat"]
            writerRiwayat = csv.DictWriter(cwr, fieldnames=kolomRiwayat)
            writerRiwayat.writeheader()
            writerRiwayat.writerows(data_csvRiwayat)

class Perpustakaan:
    def __init__(self):
        self.__status = "Tersedia"
        pass
        
    def infoBukuTersedia(self):
        with open(filePath_json, "r") as jr:
            data = json.load(jr)
        ketersedian = {judul for judul, info in data["Books"].items() if info["status"] == self.__status}
        print(f"Buku yang tersedia: {ketersedian}")

    def tampilkanInfo(self):
        try:
            with open(filePath_json, "r") as jr:
                data = json.load(jr)
                for judul, informasi in data["Books"].items():
                    print(f"ID Buku: {informasi["id"]} | Judul Buku: {judul} | Penulis Buku: {informasi["penulis"]} | Tahun Buku: {informasi["tahun"]}")
        except:
            print("Tidak dapat menemukan info")

class Book:
    def __init__(self):
        pass

    def dataBuku(self):
        with open(filePath_json, "r") as jr:
            data = json.load(jr)
        dataBuku = data["Books"]
        return dataBuku

    @staticmethod
    def isAvailable(info):
        return info["status"] == "Tersedia"


halamanPertama = RLPages()
library = Perpustakaan()
buku = Book()
pengguna = User()
administrator = Admin()

while True:
    try:
        print("===== R|L Pages =====")
        print("1. Login.")
        print("2. Register.")
        print("0. Keluar")
        pilihanRlpages = input("Masukkan pilihan: ")
        if pilihanRlpages == "1":
            authentifikasi = halamanPertama.login()
            role = authentifikasi["role"]
            currentUser = authentifikasi["username"]
        elif pilihanRlpages == "2":
            halamanPertama.register()
        elif pilihanRlpages == "0":
            break
        ####################################
        if role == "Admin":
            print("Selamat datang Admin!")
            while True:
                menuSistemAdmin()
                pilihanAdmin = input("Masukkan pilihan anda: ")
                if pilihanAdmin == "1":
                    library.tampilkanInfo()
                elif pilihanAdmin == "2":
                    administrator.pinjamBuku(currentUser)
                elif pilihanAdmin == "3":
                    administrator.kembalikanBuku(currentUser)
                elif pilihanAdmin == "4":
                    administrator.lihatRiwayat()
                elif pilihanAdmin == "5":
                    administrator.tambahBuku()
                elif pilihanAdmin == "6":
                    administrator.hapusBuku()
                elif pilihanAdmin == "7":
                    administrator.editDataBuku()
                elif pilihanAdmin == "8":
                    administrator.hapusUser()
                elif pilihanAdmin == "9":
                    administrator.editRole()
                elif pilihanAdmin == "10":
                    administrator.importCSV()
                elif pilihanAdmin == "11":
                    administrator.saveData(administrator.muatData())
                elif pilihanAdmin == "12":
                    administrator.muatData()
                elif pilihanAdmin == "0":
                    break
        
        elif role == "Member":
            print("Selamat datang Member!")
            while True:
                menuSistemMember()
                pilihanMember = input("Masukkan pilihan anda: ")
                if pilihanMember == "1":
                    library.tampilkanInfo()
                elif pilihanMember == "2":
                    library.infoBukuTersedia()
                elif pilihanMember == "3":
                    pengguna.pinjamBuku(currentUser)
                elif pilihanMember == "4":
                    pengguna.kembalikanBuku(currentUser)
                elif pilihanMember == "5":
                    pengguna.lihatRiwayat(currentUser)
                elif pilihanMember == "0":
                    break
    except Exception as e:
        print(f"Error: {e}")