data_santri = []

def tambah_santri():
    id = input("Masukkan ID: ")
    nama = input("Masukkan Nama: ")
    umur = input("Masukkan Umur: ")

    santri = {
        "id": id,
        "nama": nama,
        "umur": umur
    }

    data_santri.append(santri)
    print("✅ Data berhasil ditambahkan")

def lihat_santri():
    if len(data_santri) == 0:
        print("❌ Data kosong")
    else:
        for santri in data_santri:
            print(f"ID: {santri['id']}, Nama: {santri['nama']}, Umur: {santri['umur']}")

def ubah_santri():
    id_cari = input("Masukkan ID yang mau diubah: ")

    for santri in data_santri:
        if santri["id"] == id_cari:
            santri["nama"] = input("Nama baru: ")
            santri["umur"] = input("Umur baru: ")
            print("✅ Data berhasil diubah")
            return

    print("❌ ID tidak ditemukan")

def hapus_santri():
    id_cari = input("Masukkan ID yang mau dihapus: ")

    for santri in data_santri:
        if santri["id"] == id_cari:
            data_santri.remove(santri)
            print("✅ Data berhasil dihapus")
            return

    print("❌ ID tidak ditemukan")

while True:
    print("\n=== MENU CRUD SANTRI ===")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_santri()
    elif pilihan == "2":
        lihat_santri()
    elif pilihan == "3":
        ubah_santri()
    elif pilihan == "4":
        hapus_santri()
    elif pilihan == "5":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak valid")
